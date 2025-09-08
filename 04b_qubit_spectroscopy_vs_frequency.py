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
from qualang_tools.results import (
    progress_counter,
    wait_until_job_is_paused,
    fetching_tool,
)
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
# The intermediate frequency sweep parameters
f_min = 50 * u.MHz
f_max = 301 * u.MHz
df = 2000 * u.kHz
IFs = np.arange(
    f_min, f_max + 0.1, df
)  # The intermediate frequency vector (+ 0.1 to add f_max to IFs)

# Resonator
# The frequency sweep parameters
resontor_f_min = 120 * u.MHz
resontor_f_max = 140 * u.MHz
resontor_df = 50 * u.kHz
resontor_frequencies = np.arange(
    resontor_f_min, resontor_f_max + 0.1, resontor_df
)  # The frequency vector (+ 0.1 to add f_max to frequencies)

# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "IF_frequencies": IFs,
    "resontor_frequencies": resontor_frequencies,
    "config": config,
}

###################
# The QUA program #
###################
with program() as qubit_spec:
    n = declare(int)  # QUA variable for the averaging loop
    i = declare(int)  # QUA variable for the LO frequency sweep
    f = declare(int)  # QUA variable for the qubit frequency
    resonator_f = declare(int)  # QUA variable for the resonator frequency sweep
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(f, IFs)):
            # Update the frequency of the digital oscillator linked to the qubit element
            update_frequency("qubit", f)
            with for_each_(resonator_f, resontor_frequencies):
                update_frequency("resonator", resonator_f)
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
        I_st.buffer(len(resontor_frequencies)).buffer(len(IFs)).buffer(n_avg).map(
            FUNCTIONS.average()
        ).save_all("I")
        Q_st.buffer(len(resontor_frequencies)).buffer(len(IFs)).buffer(n_avg).map(
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


results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
# Live plotting
fig = plt.figure()
interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
while results.is_processing():
    # Fetch results
    I, Q, iteration = results.fetch_all()
    # Progress bar
    progress_counter(iteration, n_avg, start_time=results.get_start_time())

    # Convert results into Volts
    S = u.demod2volts(I + 1j * Q, readout_len)
    R = np.abs(S)  # Amplitude
    phase = np.angle(S)  # Phase
    # Normalize data
    row_sums = R.sum(axis=0)
    R /= row_sums[np.newaxis, :]

    # 2D spectroscopy plot
    plt.subplot(211)
    plt.suptitle(f"Qubit spectroscopy - LO = {qubit_LO / u.GHz} GHz")
    plt.cla()
    plt.title(r"$R=\sqrt{I^2 + Q^2}$ (normalized)")
    plt.pcolor(resonator_f, IFs / u.MHz, R)
    plt.xscale("log")
    plt.xlim(resonator_f[0], resonator_f[-1])
    plt.ylabel("Qubit IF [MHz]")
    plt.subplot(212)
    plt.cla()
    plt.title("Phase")
    plt.pcolor(resonator_f, IFs / u.MHz, signal.detrend(np.unwrap(phase)))
    plt.ylabel("Qubit IF [MHz]")
    plt.xlabel("Resonator IF [V]")
    plt.xscale("log")
    plt.xlim(resonator_f[0], resonator_f[-1] * readout_amp)
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
