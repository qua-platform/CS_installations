import time
from qm.qua import *
from qm import QuantumMachinesManager
from configuration_with_octave import *
from qualang_tools.loops import from_array

###################
# The QUA program #
###################
n_avg = 1000  # The number of averages
# Adjust the pulse duration and amplitude to drive the qubit into a mixed state
saturation_len = 10 * u.us  # In ns
saturation_amp = (
    0.5  # pre-factor to the value defined in the config - restricted to [-2; 2)
)
# Qubit detuning sweep
center = 0 * u.MHz
span = 10 * u.MHz
df = 100 * u.kHz
dfs = np.arange(-span, +span + 0.1, df)

with program() as qubit_spec:
    n = declare(int)  # QUA variable for the averaging loop
    df = declare(int)  # QUA variable for the qubit frequency
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(df, dfs)):
            # Update the frequency of the digital oscillator linked to the qubit element
            update_frequency("qubit", df + center)
            # Play the saturation pulse to put the qubit in a mixed state - Can adjust the amplitude on the fly [-2; 2)
            play(
                "saturation" * amp(saturation_amp),
                "qubit",
                duration=saturation_len * u.ns,
            )
            # Align the two elements to measure after playing the qubit pulse.
            # One can also measure the resonator while driving the qubit by commenting the 'align'
            align("qubit", "resonator")
            # Measure the state of the resonator
            measure(
                "readout",
                "resonator",
                None,
                dual_demod.full("cos", "out1", "sin", "out2", I),
                dual_demod.full("minus_sin", "out1", "cos", "out2", Q),
            )
            # Wait for the qubit to decay to the ground state
            wait(thermalization_time * u.ns, "resonator")
            # Save the 'I' & 'Q' quadratures to their respective streams
            save(I, I_st)
            save(Q, Q_st)
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        I_st.buffer(len(dfs)).average().save("I")
        Q_st.buffer(len(dfs)).average().save("Q")
        n_st.save("iteration")


times = [time.time()]
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)
times.append(time.time())
# Open the quantum machine
qm = qmm.open_qm(config)
times.append(time.time())
# Send the QUA program to the OPX, which compiles and executes it
job = qm.execute(qubit_spec)
times.append(time.time())
job.result_handles.wait_for_all_values()
times.append(time.time())
job.result_handles.get("I").fetch_all()
times.append(time.time())

times = np.diff(times)

print(f"Time for opening qmm - {times[0]}")
print(f"Time for opening qm - {times[1]}")
print(f"Time to execute - {times[2]}")
print(f"Time of program runtime + stream processing - {times[3]}")
print(f"Time to fetch data - {times[4]}")
