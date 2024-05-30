#%% Readout 
from qm import QuantumMachinesManager, DictQuaConfig, LoopbackInterface, SimulationConfig
from qm.qua import program, declare, fixed, declare_stream, pause
from qm.qua._dsl import measure, stream_processing, play, save,wait
import matplotlib.pyplot as plt 

readout_len = 300

#con_ip = "172.16.32.116"
# con_ip = "172.17.2.101"
con_ip = "172.16.32.102"
# con_ip =  "172.16.32.102"
mw_fem = 1

config: DictQuaConfig = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                mw_fem: {  # MW-FEM
                    "type": "MW",
                    "analog_outputs": {
                        2: {"sampling_rate": 1e9, "full_scale_power_dbm": -10, "band": 3},
                    },
                    "digital_outputs": {
                        1: {"level": "LVTTL",
                            "shareable": False,
                            "inverted": False
                        },
                        2: {},
                        3: {},
                    },
                    "analog_inputs": {
                        1: {"sampling_rate": 1e9, "band": 3,"gain_db" : 6},
                    },
                },
            },
        },
    },
    "elements": {
		"resonator": {
            "MWInput": {
                "port": ("con1", mw_fem, 2),
                "oscillator_frequency": 7.54e9,  # in Hz
            },
            "intermediate_frequency": 21e6,  # in Hz
            "MWOutput": {
                "port": ("con1", mw_fem, 1),
            },
			'time_of_flight': 160,
            'smearing': 0,
			"operations": {
				"readout": "readout_pulse"
			},
        },
    },
    "pulses": {
        "readout_pulse": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {"cos": "cosine_weights", "sin": "sine_weights"},
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": 0.2},
        "zero_wf": {"type": "constant", "sample": 0.0},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, readout_len)],
            "sine": [(0.0, readout_len)],
        },
        "sine_weights": {
            "cosine": [(0.0, readout_len)],
            "sine": [(1.0, readout_len)],
        },
    },
    "mixers": {
        "octave_oct1_1": [
            {
                "intermediate_frequency": 50e6,
                "lo_frequency": 1e9,
                "correction": (1, 0, 0, 1),
            },
        ],
    }
}
tof = 200
config["elements"]["resonator"]["time_of_flight"] = tof
with program() as prog:
    Raw_ADC = declare_stream(adc_trace=True)
    measure("readout", "resonator", Raw_ADC)

    with stream_processing():
        Raw_ADC.input1().save_all("raw_adc_data")

qmm = QuantumMachinesManager(con_ip, 9510)
qm = qmm.open_qm(config)
job = qm.execute(prog)
job.result_handles.wait_for_all_values()
res = job.result_handles.get("raw_adc_data").fetch_all()[0]
print(f"complex data={res}")

re = [ele.real for ele in res][0]
im = [ele.imag for ele in res][0]

# plot the complex numbers 
plt.figure(4)
plt.clf()
print(f"real={re}")
print(f"imaginary={im}")
plt.plot(re, "-b", label="real")
plt.plot(im, "-r", label="imaginary")
plt.legend(loc="upper left")
plt.show()