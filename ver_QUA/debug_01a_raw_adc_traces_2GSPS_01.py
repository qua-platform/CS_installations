# %%
# Single QUA script generated at 2025-03-13 12:12:10.988402
# QUA library version: 1.2.2a3

from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    with for_(v1,0,(v1<1),(v1+1)):
        reset_if_phase("rr_test7")
        atr_r1 = declare_stream(adc_trace=True)
        measure("single", "rr_test7", adc_stream=atr_r1)
        wait(250, "rr_test7")
    with stream_processing():
        atr_r1.input1().average().save("adc1")
        atr_r1.input2().average().save("adc2")
        atr_r1.input1().save("adc1_single_run")
        atr_r1.input2().save("adc2_single_run")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "5": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "2": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "3": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "4": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "5": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "6": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "7": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "8": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                    },
                    "digital_outputs": {},
                    "analog_inputs": {
                        "1": {
                            "offset": 0.0,
                            "gain_db": 0,
                            "sampling_rate": 2000000000.0,
                        },
                        "2": {
                            "offset": 0.0,
                            "gain_db": 0,
                            "sampling_rate": 2000000000.0,
                        },
                    },
                },
            },
        },
    },
    "elements": {
        "rr_test7": {
            "singleInput": {
                "port": ('con1', 5, 7),
            },
            "intermediate_frequency": 750000000,
            "operations": {
                "single": "single_pulse",
            },
            "outputs": {
                "out1": ('con1', 5, 1),
                "out2": ('con1', 5, 2),
            },
            "time_of_flight": 160,
            "smearing": 0,
        },
        "rr_test8": {
            "singleInput": {
                "port": ('con1', 5, 8),
            },
            "intermediate_frequency": 750000000,
            "operations": {
                "single": "single_pulse",
            },
            "outputs": {
                "out1": ('con1', 5, 1),
                "out2": ('con1', 5, 2),
            },
            "time_of_flight": 160,
            "smearing": 0,
        },
    },
    "pulses": {
        "single_pulse": {
            "operation": "measurement",
            "length": 100,
            "waveforms": {
                "single": "single_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "single_wf": {
            "type": "constant",
            "sample": 0.25,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, 100)],
            "sine": [(0.0, 100)],
        },
        "sine_weights": {
            "cosine": [(0.0, 100)],
            "sine": [(1.0, 100)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, 100)],
            "sine": [(-1.0, 100)],
        },
    },
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "5": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "2": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "3": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "4": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "5": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "6": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "7": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "8": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "offset": 0.0,
                            "gain_db": 0,
                            "shareable": False,
                            "sampling_rate": 2000000000.0,
                        },
                        "2": {
                            "offset": 0.0,
                            "gain_db": 0,
                            "shareable": False,
                            "sampling_rate": 2000000000.0,
                        },
                    },
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "rr_test7": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 5, 1),
                "out2": ('con1', 5, 2),
            },
            "operations": {
                "single": "single_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 7),
            },
            "smearing": 0,
            "time_of_flight": 160,
            "intermediate_frequency": 750000000.0,
        },
        "rr_test8": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 5, 1),
                "out2": ('con1', 5, 2),
            },
            "operations": {
                "single": "single_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 8),
            },
            "smearing": 0,
            "time_of_flight": 160,
            "intermediate_frequency": 750000000.0,
        },
    },
    "pulses": {
        "single_pulse": {
            "length": 100,
            "waveforms": {
                "single": "single_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "single_wf": {
            "type": "constant",
            "sample": 0.25,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, 100)],
            "sine": [(0.0, 100)],
        },
        "sine_weights": {
            "cosine": [(0.0, 100)],
            "sine": [(1.0, 100)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, 100)],
            "sine": [(-1.0, 100)],
        },
    },
    "mixers": {},
}




from qm import QuantumMachinesManager
from qualang_tools.units import unit
import matplotlib.pyplot as plt
import numpy as np

qop_ip = "172.16.33.115"
cluster_name = "Cluster_1" 
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

# Open a quantum machine to execute the QUA program
qm = qmm.open_qm(config)
# Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
job = qm.execute(prog)


u = unit(coerce_to_integer=True)
# Creates a result handle to fetch data from the OPX
res_handles = job.result_handles
# Waits (blocks the Python console) until all results have been acquired
res_handles.wait_for_all_values()
# Fetch the raw ADC traces and convert them into Volts
adc1_single_run = u.raw2volts(res_handles.get("adc1_single_run").fetch_all())
# adc2_single_run = adc1_single_run # u.raw2volts(res_handles.get("adc2_single_run").fetch_all())
sampling_rate = 2e9
ts1 = np.arange(len(adc1_single_run)) * (1e9 / sampling_rate)

# Compute FFT
fft_adc1 = np.fft.fft(adc1_single_run)

# Frequency axis (in MHz)
rr_if = 750 * u.MHz
freqs = np.fft.fftfreq(len(adc1_single_run), d=1 / sampling_rate) / 1e6

# Plot data
fig, axs = plt.subplots(2, 1, figsize=(7, 5))
ax = axs[0]
ax.set_title(f"IF at {rr_if / u.MHz} MHz")
ax.plot(ts1, adc1_single_run, label="Input 1")
# ax.plot(ts2, adc2_single_run, label="Input 2")
ax.set_xlabel("Time [ns]")
ax.set_ylabel("Signal amplitude [V]")
ax.legend()

ax = axs[1]
ax.set_title("FFT")
ax.plot(freqs[:len(freqs) // 2], np.abs(fft_adc1)[:len(freqs) // 2], label="Input 1")
# ax.plot(freqs[:len(freqs) // 2], np.abs(fft_adc2)[:len(freqs) // 2], label="Input 2")
ax.set_xlabel("Frequency [MHz]")
ax.set_ylabel("Magnitude")
ylim = ax.get_ylim()
for f in [250, 500, 750]:
    ax.vlines(x=f, ymin=ylim[0], ymax=ylim[1], color='m', alpha=0.2)
    ax.annotate(f"f = {f} MHz", xy=(f, ylim[1] * 0.9), xytext=(f + 10, ylim[1] * 0.9), color='m')
ax.set_ylim(ylim)
ax.legend()
plt.tight_layout()
plt.show()
qm.close()

# %%