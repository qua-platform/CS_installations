from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *
from scipy.optimize import curve_fit
from qualang_tools.bakery.randomized_benchmark_c1 import c1_table
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.plot import interrupt_on_close
import matplotlib.pyplot as plt
import numpy as np
import plotly.io as pio
pio.renderers.default='browser'


# get the config
config = get_config(sampling_rate=1e9)

element = "lf_element_1"
x180_amp = 0.2
x180_len = 40
gates = ["x180", "x90", "-x90", "y180", "y90", "-y90"]
amps = [x180_amp, x180_amp/2, -x180_amp/2, x180_amp, x180_amp/2, -x180_amp/2]

for i in range(len(gates)):
    config["elements"][element]["operations"][gates[i]] = f"{gates[i]}_pulse"
    config["pulses"][f"{gates[i]}_pulse"] = {
                "operation": "control",
                "length": x180_len,
                "waveforms": {
                    "single": f"{gates[i]}_wf",
                },
            }
    config["waveforms"][f"{gates[i]}_wf"] = {
        "type": "arbitrary",
        "samples": drag_gaussian_pulse_waveforms(amps[i], x180_len, x180_len//5, 0.0, 50e6, 0)[0]}
##############################
# Program-specific variables #
##############################
num_of_sequences = 50  # Number of random sequences
n_avg = 1  # Number of averaging loops for each random sequence
max_circuit_depth = 10  # Maximum circuit depth
delta_clifford = 2  #  Play each sequence with a depth step equals to 'delta_clifford - Must be > 1
assert (max_circuit_depth / delta_clifford).is_integer(), "max_circuit_depth / delta_clifford must be an integer."
seed = 345324  # Pseudo-random number generator seed
# List of recovery gates from the lookup table
inv_gates = [int(np.where(c1_table[i, :] == 0)[0][0]) for i in range(24)]


###################################
# Helper functions and QUA macros #
###################################
def power_law(power, a, b, p):
    return a * (p**power) + b


def generate_sequence():
    cayley = declare(int, value=c1_table.flatten().tolist())
    inv_list = declare(int, value=inv_gates)
    current_state = declare(int)
    step = declare(int)
    sequence = declare(int, size=max_circuit_depth + 1)
    inv_gate = declare(int, size=max_circuit_depth + 1)
    i = declare(int)
    rand = Random(seed=seed)

    assign(current_state, 0)
    with for_(i, 0, i < max_circuit_depth, i + 1):
        assign(step, rand.rand_int(24))
        assign(current_state, cayley[current_state * 24 + step])
        assign(sequence[i], step)
        assign(inv_gate[i], inv_list[current_state])

    return sequence, inv_gate


def play_sequence(sequence_list, depth, element):
    i = declare(int)
    with for_(i, 0, i <= depth, i + 1):
        with switch_(sequence_list[i], unsafe=True):
            with case_(0):
                wait(x180_len // 4, element)
            with case_(1):
                play("x180", element)
            with case_(2):
                play("y180", element)
            with case_(3):
                play("y180", element)
                play("x180", element)
            with case_(4):
                play("x90", element)
                play("y90", element)
            with case_(5):
                play("x90", element)
                play("-y90", element)
            with case_(6):
                play("-x90", element)
                play("y90", element)
            with case_(7):
                play("-x90", element)
                play("-y90", element)
            with case_(8):
                play("y90", element)
                play("x90", element)
            with case_(9):
                play("y90", element)
                play("-x90", element)
            with case_(10):
                play("-y90", element)
                play("x90", element)
            with case_(11):
                play("-y90", element)
                play("-x90", element)
            with case_(12):
                play("x90", element)
            with case_(13):
                play("-x90", element)
            with case_(14):
                play("y90", element)
            with case_(15):
                play("-y90", element)
            with case_(16):
                play("-x90", element)
                play("y90", element)
                play("x90", element)
            with case_(17):
                play("-x90", element)
                play("-y90", element)
                play("x90", element)
            with case_(18):
                play("x180", element)
                play("y90", element)
            with case_(19):
                play("x180", element)
                play("-y90", element)
            with case_(20):
                play("y180", element)
                play("x90", element)
            with case_(21):
                play("y180", element)
                play("-x90", element)
            with case_(22):
                play("x90", element)
                play("y90", element)
                play("x90", element)
            with case_(23):
                play("-x90", element)
                play("y90", element)
                play("-x90", element)


###################
# The QUA program #
###################
with program() as rb:
    depth = declare(int)  # QUA variable for the varying depth
    depth_target = declare(int)  # QUA variable for the current depth (changes in steps of delta_clifford)
    # QUA variable to store the last Clifford gate of the current sequence which is replaced by the recovery gate
    saved_gate = declare(int)
    m = declare(int)  # QUA variable for the loop over random sequences
    n = declare(int)  # QUA variable for the averaging loop
    I = declare(fixed)  # QUA variable for the 'I' quadrature
    Q = declare(fixed)  # QUA variable for the 'Q' quadrature
    state = declare(bool)  # QUA variable for state discrimination
    # The relevant streams
    m_st = declare_stream()
    I_st = declare_stream()
    Q_st = declare_stream()

    update_frequency(element, 0)
    with for_(m, 0, m < num_of_sequences, m + 1):  # QUA for_ loop over the random sequences
        sequence_list, inv_gate_list = generate_sequence()  # Generate the random sequence of length max_circuit_depth

        assign(depth_target, 0)  # Initialize the current depth to 0

        with for_(depth, 1, depth <= max_circuit_depth, depth + 1):  # Loop over the depths
            # Replacing the last gate in the sequence with the sequence's inverse gate
            # The original gate is saved in 'saved_gate' and is being restored at the end
            assign(saved_gate, sequence_list[depth])
            assign(sequence_list[depth], inv_gate_list[depth - 1])
            # Only played the depth corresponding to target_depth
            with if_((depth == 1) | (depth == depth_target)):
                with for_(n, 0, n < n_avg, n + 1):
                    # Can replace by active reset
                    wait(1000 * u.ns, f"lf_readout_element")
                    # Align the two elements to play the sequence after qubit initialization
                    align()
                    # The strict_timing ensures that the sequence will be played without gaps
                    with strict_timing_():
                        # Play the random sequence of desired depth
                        play_sequence(sequence_list, depth, element)
                    # Align the two elements to measure after playing the circuit.
                    align()
                    # Make sure you updated the ge_threshold and angle if you want to use state discrimination
                    measure("readout", "lf_readout_element", None, demod.full("cos", I, "out1"),
                            demod.full("sin", Q, "out1"))
                    save(I, I_st)
                    save(Q, Q_st)

                # Go to the next depth
                assign(depth_target, depth_target + delta_clifford)
            # Reset the last gate of the sequence back to the original Clifford gate
            # (that was replaced by the recovery gate at the beginning)
            assign(sequence_list[depth], saved_gate)
        # Save the counter for the progress bar
        save(m, m_st)

    with stream_processing():
        m_st.save("iteration")
        I_st.buffer(n_avg).map(FUNCTIONS.average()).buffer(max_circuit_depth / delta_clifford + 1).buffer(
            num_of_sequences
        ).save("I")
        Q_st.buffer(n_avg).map(FUNCTIONS.average()).buffer(max_circuit_depth / delta_clifford + 1).buffer(
            num_of_sequences
        ).save("Q")
        I_st.buffer(n_avg).map(FUNCTIONS.average()).buffer(max_circuit_depth / delta_clifford + 1).average().save(
            "I_avg"
        )
        Q_st.buffer(n_avg).map(FUNCTIONS.average()).buffer(max_circuit_depth / delta_clifford + 1).average().save(
            "Q_avg"
        )

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=100_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, rb, simulation_config)
    job.get_simulated_samples().con1.plot()
    # Get the waveform report
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(rb)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I_avg", "Q_avg", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    # data analysis
    x = np.arange(0, max_circuit_depth + 0.1, delta_clifford)
    x[0] = 1  # to set the first value of 'x' to be depth = 1 as in the experiment
    while results.is_processing():
        # data analysis
        I, Q, iteration = results.fetch_all()
        value_avg = I
        # Progress bar
        progress_counter(iteration, num_of_sequences, start_time=results.get_start_time())
        # Plot averaged values
        plt.cla()
        plt.plot(x, value_avg, marker=".")
        plt.xlabel("Number of Clifford gates")
        plt.ylabel("Sequence Fidelity")
        plt.title("Single qubit RB")
        plt.pause(0.1)

    # At the end of the program, fetch the non-averaged results to get the error-bars
    results = fetching_tool(job, data_list=["I", "Q"])
    I, Q = results.fetch_all()
    value_avg = np.mean(I, axis=0)
    error_avg = np.std(I, axis=0)
    # data analysis
    pars, cov = curve_fit(
        f=power_law,
        xdata=x,
        ydata=value_avg,
        p0=[0.5, 0.5, 0.9],
        bounds=(-np.inf, np.inf),
        maxfev=2000,
    )
    stdevs = np.sqrt(np.diag(cov))

    print("#########################")
    print("### Fitted Parameters ###")
    print("#########################")
    print(f"A = {pars[0]:.3} ({stdevs[0]:.1}), B = {pars[1]:.3} ({stdevs[1]:.1}), p = {pars[2]:.3} ({stdevs[2]:.1})")
    print("Covariance Matrix")
    print(cov)

    one_minus_p = 1 - pars[2]
    r_c = one_minus_p * (1 - 1 / 2**1)
    r_g = r_c / 1.875  # 1.875 is the average number of gates in clifford operation
    r_c_std = stdevs[2] * (1 - 1 / 2**1)
    r_g_std = r_c_std / 1.875

    print("#########################")
    print("### Useful Parameters ###")
    print("#########################")
    print(
        f"Error rate: 1-p = {np.format_float_scientific(one_minus_p, precision=2)} ({stdevs[2]:.1})\n"
        f"Clifford set infidelity: r_c = {np.format_float_scientific(r_c, precision=2)} ({r_c_std:.1})\n"
        f"Gate infidelity: r_g = {np.format_float_scientific(r_g, precision=2)}  ({r_g_std:.1})"
    )

    # Plots
    plt.figure()
    plt.errorbar(x, value_avg, yerr=error_avg, marker=".")
    plt.plot(x, power_law(x, *pars), linestyle="--", linewidth=2)
    plt.xlabel("Number of Clifford gates")
    plt.ylabel("Sequence Fidelity")
    plt.title("Single qubit RB")

    # np.savez("rb_values", value)

    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()
print("Experiment QM is now closed")


