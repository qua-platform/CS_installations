# %%
"""
                                 CR_calib_cr_driven_Ramsey

The CR_calib scripts are designed for calibrating cross-resonance (CR) gates involving a system
with a control qubit and a target qubit. These scripts help estimate the parameters of a Hamiltonian,
which is represented as:
    H = I ⊗ (a_X X + a_Y Y + a_Z Z) + Z ⊗ (b_I I + b_X X + b_Y Y + b_Z Z)

This script is to calibrate the AC Stark shift of the control qubit due to CR drive via driven Ramsey.
The difference from the ordinary Ramsey is that we apply CR drive in between the pi pulses. 
This is to induce the AC Stark shift on the control qubit, which has the same effect as detuning.
In principle, this term should not require an extra case if you employ the echoed-CR.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.

Next steps before going to the next node:
    - Estimate the detuning (delta_f) and can apply a frame rotation on the control qubit to cancel the phase shift of
      2 * pi * delta_f * cr_duration.

Reference: Sarah Sheldon, Easwar Magesan, Jerry M. Chow, and Jay M. Gambetta Phys. Rev. A 93, 060302(R) (2016)
"""

from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig

# from configuration import *
from configuration_with_octave import *
import matplotlib.pyplot as plt
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.plot import interrupt_on_close
from macros import qua_declaration, multiplexed_readout
from qualang_tools.plot.fitting import Fit
import warnings
import matplotlib
from qualang_tools.results.data_handler import DataHandler
import time

matplotlib.use("TKAgg")
warnings.filterwarnings("ignore")


###################
# The QUA program #
###################
n_avg = 1000  # Number of averages
t_vec = np.arange(4, 300, 1)  # Idle time sweep in clock cycles (Needs to be a list of integers)

with program() as ramsey:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(nb_of_qubits=2)
    t = declare(int)  # QUA variable for the idle time
    phi = declare(fixed)  # Phase to apply the virtual Z-rotation

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(t, t_vec)):
            # Qubit 1
            play("x90", "q1_xy")  # 1st x90 gate
            wait(pi_len >> 2, "cr_c1t2")
            play("square_positive", "cr_c1t2", duration=t)
            wait(t, "q1_xy")  # Wait a varying idle time
            play("x90", "q1_xy")  # 2nd x90 gate

            # Qubit 2
            play("x90", "q2_xy")  # 1st x90 gate
            wait(pi_len >> 2, "cr_c2t1")
            play("square_positive", "cr_c2t1", duration=t)
            wait(t, "q2_xy")  # Wait a varying idle time
            play("x90", "q2_xy")  # 2nd x90 gate

            # Align the elements to measure after having waited a time "tau" after the qubit pulses.
            align()
            # Measure the state of the resonators
            multiplexed_readout(I, I_st, Q, Q_st, resonators=[1, 2], weights="rotated_")
            # Wait for the qubit to decay to the ground state
            wait(thermalization_time * u.ns)
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

    with stream_processing():
        n_st.save("n")
        # resonator 1
        I_st[0].buffer(len(t_vec)).average().save("Ic")
        Q_st[0].buffer(len(t_vec)).average().save("Qc")
        # resonator 2
        I_st[1].buffer(len(t_vec)).average().save("It")
        Q_st[1].buffer(len(t_vec)).average().save("Qt")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip,
    port=qop_port,
    cluster_name=cluster_name,
    octave=octave_config,
)

###########################
# Run or Simulate Program #
###########################

simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, ramsey, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(ramsey)
    # Prepare the figure for live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)
    # Tool to easily fetch results from the OPX (results_handle used in it)
    results = fetching_tool(job, ["n", "Ic", "Qc", "It", "Qt"], mode="live")
    # Live plotting
    while results.is_processing():
        start_time = results.get_start_time()
        # Fetch results
        n, Ic, Qc, It, Qt = results.fetch_all()
        # Convert the results into Volts
        Ic, Qc = u.demod2volts(Ic, readout_len), u.demod2volts(Qc, readout_len)
        It, Qt = u.demod2volts(It, readout_len), u.demod2volts(Qt, readout_len)
        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)
        # calculate the elapsed time
        elapsed_time = time.time() - start_time
        # Plot
        plt.subplot(221)
        plt.cla()
        plt.plot(4 * t_vec, Ic)
        plt.ylabel("I quadrature [V]")
        plt.title("Qubit 1")
        plt.subplot(223)
        plt.cla()
        plt.plot(4 * t_vec, Qc)
        plt.ylabel("Q quadrature [V]")
        plt.xlabel("Idle times [ns]")
        plt.subplot(222)
        plt.cla()
        plt.plot(4 * t_vec, It)
        plt.title("Qubit 2")
        plt.subplot(224)
        plt.cla()
        plt.plot(4 * t_vec, Qt)
        plt.title("Qt")
        plt.xlabel("Idle times [ns]")
        plt.tight_layout()
        plt.pause(0.1)

    try:
        fit = Fit()
        fig_analysis = plt.figure()
        plt.suptitle(f"Ramsey measurement with CR drive")
        plt.subplot(221)
        fit.ramsey(4 * t_vec, Ic, plot=True)
        plt.xlabel("Idle times [ns]")
        plt.ylabel("I quadrature [V]")
        plt.title("Qubit 1")
        plt.subplot(223)
        fit.ramsey(4 * t_vec, Qc, plot=True)
        plt.xlabel("Idle times [ns]")
        plt.ylabel("I quadrature [V]")
        plt.title("Qubit 2")
        plt.subplot(222)
        fit.ramsey(4 * t_vec, It, plot=True)
        plt.xlabel("Idle times [ns]")
        plt.ylabel("I quadrature [V]")
        plt.subplot(224)
        fit.ramsey(4 * t_vec, Qt, plot=True)
        plt.xlabel("Idle times [ns]")
        plt.ylabel("I quadrature [V]")
        plt.tight_layout()
    except (Exception,):
        pass

    # Close the quantum machines at the end
    qm.close()

    if save_data:
        # Arrange data to save
        data = {
            "fig_live": fig,
            "fig_analysis": fig_analysis,
            "t_vec": t_vec,
            "Ic": Ic,
            "Ic": Ic,
            "Qc": Qc,
            "Qt": Qt,
            "iteration": np.array([n]),  # convert int to np.array of int
            "elapsed_time": np.array([elapsed_time]),  # convert float to np.array of float
        }

        # Initialize the DataHandler
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        data_handler.create_data_folder(name=Path(__file__).stem)
        data_handler.additional_files = {
            script_name: script_name,
            "configuration_with_octave.py": "configuration_with_octave.py",
            "calibration_db.json": "calibration_db.json",
            "optimal_weights.npz": "optimal_weights.npz",
        }
        # Save results
        data_folder = data_handler.save_data(data=data)


# %%
