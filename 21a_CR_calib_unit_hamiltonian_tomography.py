# %%
"""
                                 CR_calib_unit_hamiltonian_tomography

    The CR_calib scripts are designed for calibrating cross-resonance (CR) gates involving a system
with a control qubit and a target qubit. These scripts help estimate the parameters of a Hamiltonian,
which is represented as:
        H = I ⊗ (a_X X + a_Y Y + a_Z Z) + Z ⊗ (b_X X + b_Y Y + b_Z Z)

For the calibration sequences, we employ echoed CR drive.
                                   ____      ____ 
            Control(fC): _________| pi |____| pi |________________
                             ____                     
                 CR(fT): ___| CR |_____      _____________________
                                       |____|     _____
             Target(fT): ________________________| QST |__________
                                                         ______
            Readout(fR): _______________________________|  RR  |__

Each sequence, which varies in the duration of the CR drive, ends with state tomography of the target state
(across X, Y, and Z bases). This process is repeated with the control state in both |0> and |1> states.
We fit the two sets of CR duration versus tomography data to a theoretical model,
yielding two sets of three parameters: delta, omega_x, and omega_y.
Using these parameters, we estimate the interaction coefficients of the Hamiltonian.
We consider this method a form of unit Hamiltonian tomography.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.

Next steps before going to the next node:
    - This is only to test that you can obtain the data and fit to it successfully.

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
from qualang_tools.results.data_handler import DataHandler
import warnings
import matplotlib
from macros import (
    qua_declaration, multiplexed_readout,
    prepare_control_state, play_cr_pulse, perform_QST_target,
)
from cr_hamiltonian_tomography import (
    CRHamiltonianTomographyAnalysis, plot_cr_duration_vs_scan_param, 
    plot_interaction_coeffs, plot_crqst_result_2D, plot_crqst_result_3D,
    TARGET_BASES, CONTROL_STATES,
)

matplotlib.use("TKAgg")
warnings.filterwarnings("ignore")


######################################
#          The QUA program           #
######################################

############
# Parameters
############
nb_of_qubits = 2
qubit_suffixes = ["c", "t"] # control and target
resonators = [1, 2] # rr1, rr2
t_vec_clock = np.arange(8, 8000, 256) # for simulate_dynamics
t_vec_ns = 4 * t_vec_clock
n_avg = 1 # num of iterations
cr_pulse_kind = "direct" # "direct+echo", "direct+cancel", "direct+cancel+echo"

assert len(qubit_suffixes) == nb_of_qubits
assert len(resonators) == nb_of_qubits
assert np.all(t_vec_clock % 2 == 0) and (t_vec_clock.min() >= 8), "t_vec_clock should only have even numbers if play echoes"


with program() as cr_calib:
    
    I, I_st, Q, Q_st, n, n_st = qua_declaration(nb_of_qubits=2)
    t = declare(int)
    c = declare(int)
    s = declare(int)
    t_half = declare(int)
    
    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)
        with for_(*from_array(t, t_vec_clock)):
            # t/2 for main and echo
            assign(t_half, t >> 1)
            # to allow time to save the data
            wait(400 * u.ns)
            for bss in TARGET_BASES:
                for st in CONTROL_STATES:
                    # Align all elements (as no implicit align)
                    align()

                    # Prepare control state in 1
                    prepare_control_state(st=st, elem="q1_xy")

                    # Play CR
                    play_cr_pulse(kind=cr_pulse_kind, t=t, t_half=t_half)

                    # QST on target
                    perform_QST_target(bss=bss, elem="q2_xy")

                    # Measure the state of the resonators
                    # Make sure you updated the ge_threshold and angle if you want to use state discrimination
                    multiplexed_readout(I, I_st, Q, Q_st, resonators=[1, 2], weights="rotated_")

                    # Wait for the qubit to decay to the ground state
                    wait(thermalization_time * u.ns)

    with stream_processing():
        n_st.save("n")
        for q in range(nb_of_qubits):
            I_st[q]\
                .buffer(len(CONTROL_STATES))\
                .buffer(len(TARGET_BASES))\
                .buffer(len(t_vec_clock))\
                .average()\
                .save(f"I_{qubit_suffixes[q]}")
            Q_st[q]\
                .buffer(len(CONTROL_STATES))\
                .buffer(len(TARGET_BASES))\
                .buffer(len(t_vec_clock))\
                .average()\
                .save(f"Q_{qubit_suffixes[q]}")


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
    job = qmm.simulate(config, cr_calib, simulation_config)
    job.get_simulated_samples().con1.plot(analog_ports=['1', '2', '3', '4', '5', '6'])
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(cr_calib)
    # Prepare the figure for live plotting
    fig, axss = plt.subplots(4, 2, figsize=(10, 10))
    interrupt_on_close(fig, job)
    # Tool to easily fetch results from the OPX (results_handle used in it)
    results = fetching_tool(job, ["n", "I_c", "Q_c", "I_t", "Q_t"], mode="live")
    # Live plotting
    while results.is_processing():
        # Fetch results
        n, I_c, Q_c, I_t, Q_t = results.fetch_all()
        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)
        # plotting data
        # control qubit
        fig = plot_crqst_result_2D(t_vec_ns, I_c, I_t, fig, axss)
        plt.tight_layout()
        plt.pause(0.1)

    # cross resonance Hamiltonian tomography analysis
    crht = CRHamiltonianTomographyAnalysis(
        ts=t_vec_ns,
        crqst_data=I_t, # target data
    )
    crht.fit_params()
    fig_analysis = crht.plot_fit_result()
    
    # plot 3D
    fig_3d = plot_crqst_result_3D(t_vec_ns, I_t)

    plt.show()

    # Close the quantum machines at the end
    qm.close()

    if save_data:
        # Arrange data to save
        data = {
            "fig_live": fig,
            "fig_analysis": fig_analysis,
            "t_vec_ns": t_vec_ns,
            "crqst_data_c": I_c,
            "crqst_data_t": I_t,
            "I_c": I_c,
            "Q_c": Q_c,
            "I_t": I_t,
            "Q_t": Q_t,
        }
        data.update(crht.params_fitted_dict)
        data.update(crht.interaction_coeffs)

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
