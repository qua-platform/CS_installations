# %%
"""
        QUBIT SPECTROSCOPY

Prerequisites:
    -Identification of the resonator's resonance frequency when coupled to the qubit being studied (referred to as "resonator_spectroscopy").
    -Calibration of the IQ mixer connected to the qubit drive line (be it an external mixer or an Octave port).
    -Configuration of the saturation pulse amplitude and duration to transition the qubit into a mixed state.

Before proceeding to the next node:
    -Adjust the qubit frequency settings, labeled as "qubit_IF" and "qubit_LO", in the configuration.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from configuration import *
from qualang_tools.results import progress_counter, wait_until_job_is_paused
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from scipy import signal
import matplotlib.pyplot as plt
from time import sleep
from qualang_tools.results.data_handler import DataHandler

##################
#   Parameters   #
##################
# Parameters Definition
n_avg = 100  # The number of averages
# Adjust the pulse duration and amplitude to drive the qubit into a mixed state
saturation_len = 0.1 * u.us  # In ns
a_min = 0.1
a_max = 1.0
amplitudes = np.geomspace(a_min, a_max, 20)
# The intermediate frequency sweep parameters
f_min = 50 * u.MHz
f_max = 301 * u.MHz
df = 2000 * u.kHz
IFs = np.arange(
    f_min, f_max + 0.1, df
)  # The intermediate frequency vector (+ 0.1 to add f_max to IFs)

# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "amplitudes": amplitudes,
    "IF_frequencies": IFs,
    "config": config,
}

###################
# The QUA program #
###################
with program() as qubit_spec:
    n = declare(int)  # QUA variable for the averaging loop
    i = declare(int)  # QUA variable for the LO frequency sweep
    f = declare(int)  # QUA variable for the qubit frequency
    a = declare(fixed)  # QUA variable for the readout amplitude pre-factor
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(f, IFs)):
            # Update the frequency of the digital oscillator linked to the qubit element
            update_frequency("qubit", f)
            with for_each_(a, amplitudes):
                # Play the saturation pulse to put the qubit in a mixed state - Can adjust the amplitude on the fly [-2; 2)
                play(
                    "saturation" * amp(a),
                    "qubit",
                    duration=saturation_len * u.ns,
                )
                # Align the two elements to measure after playing the qubit pulse.
                # One can also measure the resonator while driving the qubit (2-tone spectroscopy) by commenting the 'align'
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
    # Save the LO iteration to get the progress bar
    save(i, n_st)

    with stream_processing():
        # Cast the data into a 2D matrix, average the matrix along its second dimension (of size 'n_avg') and store the results
        # (1D vector) on the OPX processor
        I_st.buffer(len(amplitudes)).buffer(len(IFs)).buffer(n_avg).map(
            FUNCTIONS.average()
        ).save_all("I")
        Q_st.buffer(len(amplitudes)).buffer(len(IFs)).buffer(n_avg).map(
            FUNCTIONS.average()
        ).save_all("Q")
        n_st.save_all("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip,
    port=qop_port,
    cluster_name=cluster_name,
)


###############
# Run Program #
###############
# Open the quantum machine
qm = qmm.open_qm(config)

# Send the QUA program to the OPX, which compiles and executes it. It will stop at the 'pause' statement.
job = qm.execute(qubit_spec)
# Creates results handles to fetch the data
res_handles = job.result_handles
# Initialize empty vectors to store the global 'I' & 'Q' results
I_tot = []
Q_tot = []
# Live plotting
fig = plt.figure()
interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

# Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
wait_until_job_is_paused(job, timeout=300)
# Fetch the data from the last OPX run corresponding to the current LO frequency
res_handles.get("I").wait_for_values(i + 1)
I = res_handles.get("I").fetch_all()["value"][i]
Q = res_handles.get("Q").fetch_all()["value"][i]
# Update the list of global results
I_tot.append(I)
Q_tot.append(Q)
# Progress bar
progress_counter(i, len(LOs))
# Convert results into Volts
S = u.demod2volts(I + 1j * Q, readout_len)
R = np.abs(S)  # Amplitude
phase = np.angle(S)  # Phase
# Normalize data
row_sums = R.sum(axis=0)
R /= row_sums[np.newaxis, :]

# 2D spectroscopy plot
plt.subplot(211)
plt.suptitle(f"Qubit spectroscopy - LO = {LO / u.GHz} GHz")
plt.cla()
plt.title(r"$R=\sqrt{I^2 + Q^2}$ (normalized)")
plt.pcolor(amplitudes * saturation_amp, IFs / u.MHz, R)
plt.xscale("log")
plt.xlim(amplitudes[0] * saturation_amp, amplitudes[-1] * saturation_amp)
plt.ylabel("Qubit IF [MHz]")
plt.subplot(212)
plt.cla()
plt.title("Phase")
plt.pcolor(amplitudes * saturation_amp, IFs / u.MHz, signal.detrend(np.unwrap(phase)))
plt.ylabel("Qubit IF [MHz]")
plt.xlabel("Qubit amplitude [V]")
plt.xscale("log")
plt.xlim(amplitudes[0] * saturation_amp, amplitudes[-1] * readout_amp)
plt.pause(0.1)
plt.tight_layout()

# Interrupt the FPGA program
job.halt()

# Save results
script_name = Path(__file__).name
data_handler = DataHandler(root_data_folder=save_dir)
save_data_dict.update({"I_data": I})
save_data_dict.update({"Q_data": Q})
save_data_dict.update({"fig_live": fig})
data_handler.additional_files = {script_name: script_name, **default_additional_files}
data_handler.save_data(
    data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0]
)
