# %%
"""
        SNR optimization
"""

from qm.qua import *
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
from qualang_tools.results import progress_counter, fetching_tool, wait_until_job_is_paused
from qualang_tools.plot import interrupt_on_close
from qualang_tools.addons.variables import assign_variables_to_element
from macros import lock_in_macro
import matplotlib.pyplot as plt
from qualang_tools.loops.loops import from_array
from qm import generate_qua_script

####################
# Helper functions #
####################
def update_readout_length(new_readout_length):

    config["pulses"]["lock_in_readout_pulse"]["length"] = new_readout_length
    config["integration_weights"]["cosine_weights"] = {
        "cosine": [(1.0, new_readout_length)],
        "sine": [(0.0, new_readout_length)],
    }
    config["integration_weights"]["sine_weights"] = {
        "cosine": [(0.0, new_readout_length)],
        "sine": [(1.0, new_readout_length)],
    }
    config["integration_weights"]["minus_sine_weights"] = {
        "cosine": [(0.0, new_readout_length)],
        "sine": [(-1.0, new_readout_length)],
    }

###################
# The QUA program #
###################

readout_len = 5 * u.us  # Readout pulse duration
update_readout_length(readout_len)
# Set the accumulated demod parameters
division_length = 250  # Size of each demodulation slice in clock cycles
number_of_divisions = int((readout_len) / (4 * division_length))
print("Integration weights chunk-size length in clock cycles:", division_length)
print("The readout has been sliced in the following number of divisions", number_of_divisions)

# Time axis for the plots at the end
x_plot = np.arange(division_length * 4, readout_len + 1, division_length * 4)

p5_voltages = np.arange(-0.1, 0.1, 0.01)
p6_voltages = np.arange(-0.1, 0.1, 0.01)

detuning_voltages = p5_voltages + p6_voltages

buffer_len = len(p5_voltages)

# Points in the charge stability map [V1, V2]
level_dephasing = [-0.2, -0.1]
duration_dephasing = 2000  # nanoseconds

seq = OPX_virtual_gate_sequence(config, ["P5_sticky", "P6_sticky"])
seq.add_points("dephasing", level_dephasing, duration_dephasing)
seq.add_points("readout", level_readout, duration_readout)

n_shots = 100
amps = np.arange(0, 1, 0.1)

with program() as snr_opt:
    n = declare(int)  # QUA integer used as an index for the averaging loop
    counter = declare(int)  # QUA integer used as an index for the Coulomb pulse
    n_st = declare_stream()  # Stream for the iteration number (progress bar)

    I = declare(fixed, size=number_of_divisions)
    Q = declare(fixed, size=number_of_divisions)
    I_st = declare_stream()
    Q_st = declare_stream()

    dc_signal = declare(fixed)
    x = declare(fixed)
    y = declare(fixed)
    dur_len = declare(int, value=1000)
    ind = declare(int)
    a = declare(fixed)

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("QDS", I, Q)

    with for_(n, 0, n < n_shots, n + 1):

        save(n, n_st)

        with for_(*from_array(a, amps)):

            # Play fast pulse
            seq.add_step(voltage_point_name="dephasing")
            seq.add_step(voltage_point_name="readout")  # duration in nanoseconds
            seq.add_compensation_pulse(duration=duration_compensation_pulse)

            # Measure the dot right after the qubit manipulation
            wait((duration_dephasing) * u.ns, "QDS")

            measure(
                "readout"*amp(a),
                "QDS",
                None,
                demod.accumulated("cos", I, division_length, "out2"),
                demod.accumulated("sin", Q, division_length, "out2"),
            )

            # Save the QUA vectors to their corresponding streams
            with for_(ind, 0, ind < number_of_divisions, ind + 1):
                save(I[ind], I_st)
                save(Q[ind], Q_st)

            # Wait at each iteration in order to ensure that the data will not be transferred faster than 1 sample
            # per µs to the stream processing. Otherwise, the processor will receive the samples faster than it can
            # process them which can cause the OPX to crash.
            wait(1_000 * u.ns)  # in ns
            # Ramp the voltage down to zero at the end of the triangle (needed with sticky elements)
            align()

            ramp_to_zero("P5_sticky")
            ramp_to_zero("P6_sticky")

    # Stream processing section used to process the data before saving it
    with stream_processing():
        n_st.save("iteration")
        I_st.buffer(number_of_divisions).buffer(len(amps)).save_all("Ig")
        Q_st.buffer(number_of_divisions).buffer(len(amps)).save_all("Qg")

from pprint import pprint

pprint(generate_qua_script(snr_opt))

# %%
#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, snr_opt, simulation_config)
    job.get_simulated_samples().con1.plot()
    plt.show(block=False)
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(snr_opt)
    # Get results from QUA program and initialize live plotting
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch the data from the last OPX run corresponding to the current slow axis iteration
        I, Q, iteration = results.fetch_all()
        # Convert results into Volts
        S = u.demod2volts(I + 1j * Q, lock_in_readout_length)
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        # Progress bar
        progress_counter(iteration, n_shots, start_time=results.start_time)