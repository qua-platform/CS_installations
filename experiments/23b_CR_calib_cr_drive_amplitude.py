# %%
"""
                                 CR_calib_cr_drive_amplitude
TBW
                             

Prerequisites:
    - 
    -
    -

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

def arrange_data_for_crht(state_data):
    return {
        st: {
            bss: state_data[:, j, i]
            for j, bss in enumerate(TARGET_BASES)
        }
        for i, st in enumerate(CONTROL_STATES)
    }


def plot_cr_duration_vs_amplitude(state_c, state_t, t_vec, a_vec, axss):
    data = 2 * [state_c] + 2 * [state_t]
    for i, (axs, bss) in enumerate(zip(axss, TARGET_BASES)):
        for j, (ax, dt, st) in enumerate(zip(axs, data, 2 * CONTROL_STATES)):
            ax.cla()
            ax.pcolor(4 * t_vec, a_vec, dt[:, :, i, j % 2].T)
            if i == 0 and j < 2:
                ax.set_title(f"Q_C w/ Q_C={st}")
            if i == 0 and j >= 2:
                ax.set_title(f"Q_T w/ Q_C={st}")
            if j == 0:
                ax.set_ylabel(f"<{bss}(t)>\namplitude", fontsize=14)
            if i == 2:
                ax.set_xlabel(f"time [ns]", fontsize=14)
    plt.tight_layout()


# Parameters
play_echo = False # True if play echo for CR drive
nb_of_qubits = 2
qubit_suffixes = ["c", "t"] # control and target
resonators = [1, 2] # rr1, rr2
thresholds = [ge_threshold_q1, ge_threshold_q2]
t_vec = np.arange(8, 200, 4) # in clock cylcle = 4ns
a_vec = np.arange(0.1, 2, 0.1) # scaling factor for amplitude
n_avg = 100 # num of iterations

assert len(qubit_suffixes) == nb_of_qubits
assert len(resonators) == nb_of_qubits
assert len(thresholds) == nb_of_qubits
assert (play_echo and np.all(t_vec % 2 == 0) and (t_vec.min() >= 8)) \
    or (not play_echo and (np.min(t_vec) >= 4)), \
    "t_vec should only have even numbers if play echoes"


with program() as cr_calib:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(nb_of_qubits=2)
    state = [declare(bool) for _ in range(nb_of_qubits)]
    state_st = [declare_stream() for _ in range(nb_of_qubits)]
    a = declare(fixed)
    t = declare(int)
    t_half = declare(int)
    c = declare(int)
    s = declare(int)
    
    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)
        with for_(*from_array(t, t_vec)):
            # t/2 for main and echo
            assign(t_half, t >> 1)
            with for_(*from_array(a, a_vec)):
                for bss in TARGET_BASES:
                    for st in CONTROL_STATES:
                        # Align all elements (as no implicit align)
                        align()
                        # Start from the same phase
                        reset_phase("cr_c1t2")

                        # Prepare control state in 1  
                        if st == "1":
                            play("x180", "q1_xy")

                        # Play CR + QST
                        # q1_xy=0, q2_xy=0, cr_c1t2=0, rr1=0, rr2=0
                        align()
                        if play_echo:
                            #                        ____      ____ 
                            # Control(fC): _________| pi |____| pi |________________
                            #                  ____                     
                            #      CR(fT): ___| CR |_____      _____________________
                            #                            |____|     _____
                            #  Target(fT): ________________________| QST |__________
                            #                                              ______
                            # Readout(fR): _____________________ _________|  RR  |__
                            #
                            # q1_xy=0, q2_xy=0, cr_c1t2=t/2, rr1=0, rr2=0
                            play("square_positive" * amp(a), "cr_c1t2", duration=t_half)
                            # q1_xy=t/2, q2_xy=0, cr_c1t2=t/2, rr1=0, rr2=0
                            wait(t_half, "q1_xy")
                            # q1_xy=t/2+p/4, q2_xy=0, cr_c1t2=t/2, rr1=0, rr2=0
                            play("x180", "q1_xy")
                            # q1_xy=t/2+p/4, q2_xy=0, cr_c1t2=t/2+p/4, rr1=0, rr2=0
                            wait(pi_len >> 2, "cr_c1t2")
                            # q1_xy=t/2+p/4, q2_xy=0, cr_c1t2=t+p/4, rr1=0, rr2=0
                            play("square_negative" * amp(a), "cr_c1t2", duration=t_half)
                            # q1_xy=t+p/4, q2_xy=0, cr_c1t2=t+p/4, rr1=0, rr2=0
                            wait(t_half, "q1_xy")
                            # q1_xy=t+p/2, q2_xy=0, cr_c1t2=t+p/4, rr1=0, rr2=0
                            play("x180", "q1_xy")
                            # q1_xy=t+p/2, q2_xy=t+p/2, cr_c1t2=t+p/4, rr1=t+p/2, rr2=t+p/2
                            wait(t + (pi_len >> 1), "q2_xy", "rr1", "rr2")
                        else:
                            #
                            # # Control(fC): _____________________________
                            #                  ________                      
                            #      CR(fT): ___|   CR   |________________
                            #                           _____
                            #  Target(fT): ____________| QST |__________          
                            #                                  ______
                            # Readout(fR): ___________________|  RR  |__
                            #
                            # q1_xy=0, q2_xy=0, cr_c1t2=t, rr1=0, rr2=0 
                            play("square_positive" * amp(a), "cr_c1t2", duration=t)
                            # q1_xy=0, q2_xy=t, cr_c1t2=t, rr1=t, rr2=t
                            wait(t, "q2_xy", "rr1", "rr2")
                        
                        # if play_echo: q1_xy=t+3*p/4, q2_xy=t+p/2, cr_c1t2=t+p/4, rr1=t+p/2, rr2=t+p/2
                        # else: q1_xy=0, q2_xy=t+p/4, cr_c1t2=t, rr1=t, rr2=t
                        if bss == "x":
                            play("-y90", "q2_xy")
                        elif bss == "y":
                            play("x90", "q2_xy")
                        else:
                            wait(pi_len >> 2, "q2_xy")

                        # if play_echo: q1_xy=t+3*p/4, q2_xy=t+3*p/4, cr_c1t2=t+p/4, rr1=t+3*p/4, rr2=t+3*p/4
                        # else: q1_xy=0, q2_xy=t+p/4, cr_c1t2=t, rr1=t+p/4, rr2=t+p/4
                        wait(pi_len >> 2, "rr1", "rr2")

                        # Measure the state of the resonators
                        # Make sure you updated the ge_threshold and angle if you want to use state discrimination
                        multiplexed_readout(I, I_st, Q, Q_st, resonators=[1, 2], weights="rotated_")
                        # multiplexed_readout(I, I_st, Q, Q_st, resonators=[1, 2], weights="optimized_")

                        wait(400 * u.ns)
                        # wait(thermalization_time * u.ns)
                        # Make sure you updated the ge_threshold
                        for q in range(nb_of_qubits):
                            assign(state[q], I[q] > thresholds[q])
                            save(state[q], state_st[q])

    with stream_processing():
        n_st.save("n")
        for q in range(nb_of_qubits):
            state_st[q]\
                .boolean_to_int()\
                .buffer(len(CONTROL_STATES))\
                .buffer(len(TARGET_BASES))\
                .buffer(len(a_vec))\
                .buffer(len(t_vec))\
                .average()\
                .save(f"state_{qubit_suffixes[q]}")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)


###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, cr_calib, simulation_config)
    job.get_simulated_samples().con1.plot(analog_ports=['1', '2', '3', '4', '5', '6'])
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(cr_calib)
    # Prepare the figure for live plotting
    fig, axss = plt.subplots(3, 4, figsize=(12, 9), sharex=True, sharey=True)
    interrupt_on_close(fig, job)
    # Tool to easily fetch results from the OPX (results_handle used in it)
    results = fetching_tool(job, ["n", "state_c", "state_t"], mode="live")
    # Live plotting
    while results.is_processing():
        # Fetch results
        n, state_c, state_t = results.fetch_all()
        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)
        # Plot cr_duration vs amplitude for Qc/Qt x Qc state x bases 
        plot_cr_duration_vs_amplitude(state_c, state_t, t_vec, a_vec, axss)

    # TODO: Delete (loading dummy data for test)
    data = np.load("./crht_test_data/data.npz")
    t_vec = data["t_vec"]
    state_c = data["state_c"] # len(t_vec) x 3 x 2
    state_t = data["state_t"] # len(t_vec) x 3 x 2
    state_c = np.tile(state_c[:, None, ...], reps=[1, len(a_vec), 1, 1]) # len(a_vec) x len(t_vec) x 3 x 2
    state_t = np.tile(state_t[:, None, ...], reps=[1, len(a_vec), 1, 1]) # len(a_vec) x len(t_vec) x 3 x 2
    
    # Perform CR Hamiltonian tomography
    SEED = 0
    coeffs = []
    for a in range(len(a_vec)):
        crht = CRHamiltonianTomographyAnalysis(
            ts=4*t_vec, # 4: clock
            xyz=arrange_data_for_crht(state_t[:, a, ...]), # target data
        )
        crht.fit_params(random_state=SEED, do_print=False)
        coeffs.append(crht.interaction_coeffs)

    # Plot the estimated interaction coefficients
    fig_analysis, ax = plt.subplots(1, 1, figsize=(6, 5))
    arrs_coeff = {p: np.array([coeff[p] for coeff in coeffs]) for p in PAULI_2Q}
    for p in PAULI_2Q:
        ax.plot(a_vec, arrs_coeff[p])
    ax.set_xlabel("amplitude")
    ax.set_ylabel("interaction coefficients [MHz]")
    ax.legend(PAULI_2Q)
    plt.tight_layout()
    plt.show()

    qm.close()

    # Arrange data to save
    data = {
        "fig_live": fig,
        "fig_analysis": fig_analysis,
        "t_vec_ns": 4 * t_vec, # 4: clock
        "a_vec": a_vec,
        "data_c": state_c,
        "data_t": state_t,
        "random_state": SEED,
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
