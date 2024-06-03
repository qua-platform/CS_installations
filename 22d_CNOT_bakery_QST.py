# %%
"""
                                 CNOT_bakery

Prerequisites:
    - 

Next steps before going to the next node:
    - 

Reference: Sarah Sheldon, Easwar Magesan, Jerry M. Chow, and Jay M. Gambetta Phys. Rev. A 93, 060302(R) (2016)
"""

from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig

# from configuration import *
from configuration_with_octave import *
import matplotlib.pyplot as plt
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.plot import interrupt_on_close
from qualang_tools.bakery import baking
from macros import qua_declaration, multiplexed_readout, one_qb_QST, plot_1qb_tomography_results
import warnings
import matplotlib
from qualang_tools.results.data_handler import DataHandler
from cr_hamiltonian_tomography import CRHamiltonianTomographyAnalysis, TARGET_BASES, CONTROL_STATES, PAULI_2Q

matplotlib.use("TKAgg")
warnings.filterwarnings("ignore")


###################
# The QUA program #
###################

# baking
def bake_cross_resonance():
    with baking(config, padding_method="right") as b:
        # Prepare control state in 1
        if st_c == "1":
            b.play("x180", "q1_xy")
        # Prepare target state in 1  
        if st_t == "1":
            b.play("x180", "q2_xy")

        # Play ZI(-pi/2) and IX(-pi/2)
        b.align("q1_xy", "q2_xy")
        b.frame_rotation_2pi(+0.25, "q1_xy") # +0.25 for Z(-pi/2)
        b.play("-x90", "q2_xy")

        # Shift frames to the calibrated phases
        b.frame_rotation_2pi(cr_c1t2_drive_phase, "cr_c1t2")
        b.frame_rotation_2pi(cr_cancel_c1t2_drive_phase, "cr_cancel_c1t2")

        # Play CR
        b.align("q1_xy", "q2_xy", "cr_c1t2", "cr_cancel_c1t2")
        # main
        b.play("square_positive_half", "cr_c1t2")
        b.play("square_positive_half", "cr_cancel_c1t2")
        # echo
        b.align("q1_xy", "cr_c1t2", "cr_cancel_c1t2")
        b.play("x180", "q1_xy")
        b.align("q1_xy", "cr_c1t2", "cr_cancel_c1t2")
        b.play("square_negative_half", "cr_c1t2")
        b.play("square_negative_half", "cr_cancel_c1t2")
        b.align("q1_xy", "cr_c1t2", "cr_cancel_c1t2")
        b.play("x180", "q1_xy")
        b.align("q1_xy", "cr_c1t2", "cr_cancel_c1t2", "rr1", "rr2")

        # Shift back the phase of cr and cr cancel pulse so they won't be accumulated
        b.frame_rotation_2pi(-cr_c1t2_drive_phase, "cr_c1t2")
        b.frame_rotation_2pi(-cr_cancel_c1t2_drive_phase, "cr_cancel_c1t2")

    return b


# Parameters
nb_of_qubits = 2
qubit_suffixes = ["c", "t"] # control and target
thresholds = [ge_threshold_q1, ge_threshold_q2]
resonators = [1, 2] # rr1, rr2
state_ct_pairs = [["0", "0"], ["0", "1"], ["1", "0"], ["1", "1"]]
n_avg = 100 # num of iterations

assert len(qubit_suffixes) == nb_of_qubits
assert len(thresholds) == nb_of_qubits
assert len(resonators) == nb_of_qubits

# back cr for combinations of state_c and state_t
baked_cr = bake_cross_resonance()

with program() as cnot_calib:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(nb_of_qubits=2)
    state = [declare(bool) for _ in range(nb_of_qubits)]
    state_st = [declare_stream() for _ in range(nb_of_qubits)]
    proj_idx = declare(int)
    st_c = declare(int)
    st_t = declare(int)
    
    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)
        # to allow time to save the data
        wait(400 * u.ns)
        with for_(st_c, 0, st_c < 2, st_c + 1):
            with for_(st_t, 0, st_t < 2, st_t + 1):
                with for_(proj_idx, 0, proj_idx < 9, proj_idx + 1):
                    # Prepare control state in 1
                    with if_(st_c == 1):
                        play("x180", "q1_xy")
                    # Prepare target state in 1 
                    with if_(st_t == 1):
                        play("x180", "q2_xy")
            
                    # Play baked CR
                    baked_cr.run()
                    
                    # Measure the state of the resonators
                    # Make sure you updated the ge_threshold and angle if you want to use state discrimination
                    multiplexed_readout(I, I_st, Q, Q_st, resonators=[1, 2], weights="rotated_")
                    # multiplexed_readout(I, I_st, Q, Q_st, resonators=[1, 2], weights="optimized_")

                    # Wait for the qubit to decay to the ground state
                    wait(thermalization_time * u.ns)
                    # Make sure you updated the ge_threshold
                    for q in range(nb_of_qubits):
                        assign(state[q], I[q] > thresholds[q])
                        save(state[q], state_st[q])

    with stream_processing():
        n_st.save("n")
        for q in range(nb_of_qubits):
            state_st[q]\
                .boolean_to_int()\
                .buffer(len(state_ct_pairs))\
                .average()\
                .save(f"state_{qubit_suffixes[q]}")


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

simulate = True
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=4_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, cnot_calib, simulation_config)
    job.get_simulated_samples().con1.plot(analog_ports=['1', '2', '3', '4', '5', '6'])
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(cnot_calib)
    # Prepare the figure for live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)
    # Tool to easily fetch results from the OPX (results_handle used in it)
    results = fetching_tool(job, ["n", "state_c", "state_t"], mode="live")
    # Live plotting
    while results.is_processing():
        # Fetch results
        n, state_c, state_t = results.fetch_all()
        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)
        # Plot
        plt.cla()
        plt.scatter([f"({c},{t})" for c, t in state_ct_pairs], state_c)
        plt.scatter([f"({c},{t})" for c, t in state_ct_pairs], state_t)
        plt.xlabel("initial state of control and target")
        plt.ylabel("State probability <z>")
        plt.title("Control and target qubit after CNOT")
        plt.pause(0.1)

    plt.ylim([-0.05, 1.05])
    xlim = plt.xlim()
    plt.hlines(y=[0.0, 0.5, 1.0], xmin=xlim[0], xmax=xlim[1], color='k', alpha=0.3, linestyle="--")
    plt.legend(["control", "target"])
    plt.xlim(xlim)
    plt.tight_layout()
    plt.show()

    qm.close()

    if save_data:
        # Arrange data to save
        data = {
            "fig_live": fig,
            "state_c": state_c,
            "state_t": state_t,
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
