from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *
from typing import Union
from numpy.typing import NDArray
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, bilinear
from qualang_tools.digital_filters import highpass_correction
import plotly.io as pio
pio.renderers.default='browser'

def highpass_correction(tau: float, Ts: float = 1):
    """
    Calculate the best FIR and IIR filter taps to correct for a highpass decay (HPF) of the shape `exp(-t/tau)`.
    The OPX has hardware constraints that may limit the filter implementation and this is why the running QOP version can be specified as an enum of the class QOPVersion.
    The possible options are returned by the `QOPVersion.get_options()` method and the default value is given by `QOPVersion.get_latest()`.

    Args:
        tau: The time constant for the exponential decay, given in ns.
        Ts: The sampling rate (in ns) of the system and filter taps.
        qop_version: running QOP version used to format the taps according to the corresponding hardware limitations (ex: QOPVersion.QOP222).
    Returns:
        A tuple of two items.
        The first is a list of 2 FIR (feedforward) taps starting at 0 and spaced `Ts` apart.
        The second is a single IIR (feedback) tap.
    """
    Ts *= 1e-9
    flt = butter(1, np.array([1 / tau / Ts]), btype="highpass", analog=True)
    ahp2, bhp2 = bilinear(flt[1], flt[0], 1e9)
    feedforward_taps = list(np.array([1 + (ahp2[0] - 1) * 3.16, (ahp2[0] - 1) * 3.16 - 1]))
    feedback_tap = [1 - 2**-20]
    return feedforward_taps, feedback_tap

def get_filtered_voltage(
    voltage_list: Union[NDArray, list], step_duration: float, bias_tee_cut_off_frequency: float, plot: bool = False
):
    """Get the voltage after filtering through the bias-tee

    :param voltage_list: List of voltages outputted by the OPX in V.
    :param step_duration: Duration of each step in s.
    :param bias_tee_cut_off_frequency: Cut-off frequency of the bias-tee in Hz.
    :param plot: Flag to plot the voltage values if set to True.
    :return: the filtered and unfiltered voltage lists with 1Gs/s sampling rate.
    """

    def high_pass(data, f_cutoff):
        res = butter(1, f_cutoff, btype="highpass", analog=False)
        return lfilter(res[0], res[1], data)

    def high_pass_compensation(data, f_cutoff):
        res = butter(1, f_cutoff, btype="highpass", analog=False)
        return lfilter(res[1], res[0], data)

    y = [val for val in voltage_list for _ in range(int(step_duration * 1e9))]
    y_filtered = high_pass(y, bias_tee_cut_off_frequency * 1e-9)
    y_corrected = high_pass_compensation(y, bias_tee_cut_off_frequency * 1e-9)

    if plot:
        # plt.figure()
        plt.plot(y, label="before bias-tee")
        plt.plot(y_filtered, label="after bias-tee")
        plt.plot(y_corrected, label="after correction before bias-tee")
        plt.xlabel("Time [ns]")
        plt.ylabel("Voltage [V]")
        plt.legend()
    print(f"Error: {np.mean(np.abs((y-y_filtered)/(max(y)-min(y))))*100:.2f} %")
    return np.array(y), y_filtered, y_corrected


# get the config
config = get_config(sampling_rate=1e9)

###################
# The QUA program #
###################
f_cutoff = 50e3
wf_ideal = [0.0] * 1000 + [0.1]*10000 + [-0.1] * 10000 + [0.0]*20000

wf, wf_filtered, wf_corrected = get_filtered_voltage(wf_ideal, 1e-9, f_cutoff, True)

iir, fir = highpass_correction(1e9/f_cutoff)
config["waveforms"]["arbitrary_wf"] = {"type": "arbitrary", "samples": wf_filtered.tolist()}
config["pulses"]["arbitrary_pulse"]["length"] = len(wf_filtered)
config["controllers"]["con1"]["fems"][2]["analog_outputs"][1] = {
    "offset": 0.0, "sampling_rate": 1e9, "output_mode": "direct", "upsampling_mode": "mw",
    "delay": 0, "filter": {"feedforward": iir, "feedback": fir}}

with program() as biastee_compensation:
    play("const", "scope_trigger")
    play("arbitrary", "lf_element_1")
    play("arbitrary", "lf_element_2")

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
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, biastee_compensation, simulation_config)
    # Plot the simulated samples
    plt.figure()
    job.get_simulated_samples().con1.plot()
    # Get the waveform report
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)
    plt.show()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(biastee_compensation)
