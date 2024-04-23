# %%
"""
        Cross-Resonance Time Rabi with single-qubit Quantum State Tomography
The sequence consists two consecutive pulse sequences with the qubit's thermal decay in between.
In the first sequence, we set the control qubit in |g> and play a rectangular cross-resonance pulse to
the target qubit; the cross-resonance pulse has a variable duration. In the second sequence, we initialize the control
qubit in |e> and play the variable duration cross-resonance pulse to the target qubit. Note that in
the second sequence after the cross-resonance pulse we send a x180_c pulse. With it, the target qubit starts
in |g> in both sequences when CR lenght -> zero. At the end of both sequences we perform single-qubit Quantum
 State Tomography on the target qubit.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.

Reference: A. D. Corcoles et al., Phys. Rev. A 87, 030301 (2013)

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

matplotlib.use("TKAgg")
warnings.filterwarnings("ignore")

###################
# The QUA program #
###################
t_vec = np.arange(4, 200, 2) # in clock cylcle = 4ns
n_avg = 1000 # num of iterations
resonators = [1, 2] # rr1, rr2

with program() as cr_time_rabi_one_qst:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(nb_of_qubits=2)
    t = declare(int)
    c = declare(int)
    s = declare(int)
    
    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)
        with for_(*from_array(t, t_vec)):
            with for_(c, 0, c < 3, c + 1):
                with for_(s, 0, s < 2, s + 1): # states
                    with if_(s == 1):
                        play("x180", "q1_xy")
                        align()

                    # Control
                    reset_phase("cr_c1t2")
                    play("square_positive", "cr_c1t2", duration=t)
                    align()
                    # Target
                    one_qb_QST("q2_xy", pi_len, c)
                    align()
                    # Measure the state of the resonators
                    multiplexed_readout(I, I_st, Q, Q_st, resonators=resonators, weights="")
                    # multiplexed_readout(I, I_st, Q, Q_st, resonators=[1, 2], weights="rotated_")
                    # Wait for the qubit to decay to the ground state
                    # wait(thermalization_time * u.ns)
                    wait(200 * u.ns)
    
    with stream_processing():
        n_st.save("n")
        for r, rr in enumerate(resonators):
            I_st[r].buffer(2).buffer(3).buffer(len(t_vec)).average().save(f"I{rr}")
            Q_st[r].buffer(2).buffer(3).buffer(len(t_vec)).average().save(f"Q{rr}")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)


###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=3_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, cr_time_rabi_one_qst, simulation_config)
    job.get_simulated_samples().con1.plot(analog_ports=['1', '2', '3', '4', '5', '6'])
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(cr_time_rabi_one_qst)
    # Prepare the figure for live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)
    # Tool to easily fetch results from the OPX (results_handle used in it)
    results = fetching_tool(job, ["n", "I1", "Q1", "I2", "Q2"], mode="live")
    # Live plotting
    while results.is_processing():
        # Fetch results
        n, I1, Q1, I2, Q2 = results.fetch_all()
        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)
        # Plot tomography
        plot_1qb_tomography_results(I2, times * 4)
    # Close the quantum machines at the end
    qm.close()

# %%
