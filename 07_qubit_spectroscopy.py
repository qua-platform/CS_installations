# %%
"""
        QUBIT SPECTROSCOPY
This sequence involves sending a saturation pulse to the qubit, placing it in a mixed state,
and then measuring the state of the resonator across various qubit drive intermediate f_vec.
In order to facilitate the qubit search, the qubit pulse duration and amplitude can be changed manually in the QUA
program directly without having to modify the configuration.

The data is post-processed to determine the qubit resonance frequency, which can then be used to adjust
the qubit intermediate frequency in the configuration under "qubit_IF".

Note that it can happen that the qubit is excited by the image sideband or LO leakage instead of the desired sideband.
This is why calibrating the qubit mixer is highly recommended.

This step can be repeated using the "x180" operation to adjust the pulse parameters (amplitude, duration, frequency)
before performing the next calibration steps.

Prerequisites:
    - Identification of the resonator's resonance frequency when coupled to the qubit in question (referred to as "resonator_spectroscopy_multiplexed").
    - Calibration of the IQ mixer connected to the qubit drive line (whether it's an external mixer or an Octave port).
    - Set the flux bias to the maximum frequency point, labeled as "max_frequency_point", in the configuration.
    - Configuration of the cw pulse amplitude (const_amp) and duration (const_len) to transition the qubit into a mixed state.
    - Specification of the expected qubits T1 in the configuration.

Before proceeding to the next node:
    - Update the qubit frequency, labeled as "qubit_IF_q", in the configuration.
"""

from qm.qua import *
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm import SimulationConfig

# from configuration import *
from configuration_with_octave import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from macros import qua_declaration, multiplexed_readout
import matplotlib.pyplot as plt
import warnings
import matplotlib
from qualang_tools.results.data_handler import DataHandler
import time

matplotlib.use("TKAgg")
warnings.filterwarnings("ignore")


###################
# The QUA program #
###################
n_avg = 1000  # The number of averages
# Adjust the pulse duration and amplitude to drive the qubit into a mixed state
saturation_len = 10 * u.us  # In ns
saturation_amp = 0.5  # pre-factor to the value defined in the config - restricted to [-2; 2)
# Qubit detuning sweep with respect to qubit_IF
span = 10 * u.MHz
df = 100 * u.kHz
f_vec = np.arange(-span, +span + 0.1, df)


with program() as multi_qubit_spec:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(nb_of_qubits=2)
    df = declare(int)  # QUA variable for the readout frequency

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(df, f_vec)):
            # Update the frequency of the two qubit elements
            update_frequency("q1_xy", df + qubit_IF_q1)
            update_frequency("q2_xy", df + qubit_IF_q2)
            # Play the saturation pulse to put the qubit in a mixed state - Can adjust the amplitude on the fly [-2; 2)
            # qubit 1
            play("saturation" * amp(saturation_amp), "q1_xy", duration=saturation_len * u.ns)
            align("q1_xy", "rr1")
            # qubit 2
            play("saturation" * amp(saturation_amp), "q2_xy", duration=saturation_len * u.ns)
            align("q2_xy", "rr2")

            # Multiplexed readout, also saves the measurement outcomes
            multiplexed_readout(I, I_st, Q, Q_st, resonators=[1, 2])
            # Wait for the qubit to decay to the ground state
            wait(thermalization_time * u.ns)
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

    with stream_processing():
        n_st.save("n")
        # resonator 1
        I_st[0].buffer(len(f_vec)).average().save("I1")
        Q_st[0].buffer(len(f_vec)).average().save("Q1")
        # resonator 2
        I_st[1].buffer(len(f_vec)).average().save("I2")
        Q_st[1].buffer(len(f_vec)).average().save("Q2")

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
    job = qmm.simulate(config, multi_qubit_spec, simulation_config)
    job.get_simulated_samples().con1.plot()
    plt.show()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(multi_qubit_spec)
    # Prepare the figure for live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)
    # Tool to easily fetch results from the OPX (results_handle used in it)
    results = fetching_tool(job, ["n", "I1", "Q1", "I2", "Q2"], mode="live")
    # Live plotting
    while results.is_processing():
        start_time = results.get_start_time()
        # Fetch results
        n, I1, Q1, I2, Q2 = results.fetch_all()
        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)
        # calculate the elapsed time
        elapsed_time = time.time() - start_time
        # Data analysis
        S1 = u.demod2volts(I1 + 1j * Q1, readout_len)
        S2 = u.demod2volts(I2 + 1j * Q2, readout_len)
        R1 = np.abs(S1)
        phase1 = np.angle(S1)
        R2 = np.abs(S2)
        phase2 = np.angle(S2)
        # Plots
        plt.suptitle("Qubit spectroscopy")
        plt.subplot(221)
        plt.cla()
        plt.plot((f_vec + qubit_IF_q1) / u.MHz, R1)
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.title(f"Qubit 1 - LO = {qubit_LO_q1 / u.GHz} GHz)")
        plt.subplot(223)
        plt.cla()
        plt.plot((f_vec + qubit_IF_q1) / u.MHz, np.unwrap(phase1))
        plt.ylabel("Phase [rad]")
        plt.xlabel("Qubit intermediate frequency [MHz]")
        plt.subplot(222)
        plt.cla()
        plt.plot((f_vec + qubit_IF_q2) / u.MHz, np.abs(R2))
        plt.title(f"Qubit 2 - LO = {qubit_LO_q2 / u.GHz} GHz)")
        plt.subplot(224)
        plt.cla()
        plt.plot((f_vec + qubit_IF_q2) / u.MHz, np.unwrap(phase2))
        plt.xlabel("Qubit intermediate frequency [MHz]")
        plt.tight_layout()
        plt.pause(0.1)

    plt.show()

    # Close the quantum machines at the end
    qm.close()

    if save_data:
        # Arrange data to save
        data = {
            "fig_live": fig,
            "f_vec": f_vec,
            "I1": I1,
            "I1": I1,
            "Q1": Q1,
            "Q2": Q2,
            "S1": S1,
            "S2": S2,
            "R1": R1,
            "R2": R2,
            "phase1": phase1,
            "phase2": phase2,
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
