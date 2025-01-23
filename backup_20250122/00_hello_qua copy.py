# %%
# Single QUA script generated at 2024-10-30 13:18:10.765219
# QUA library version: 1.2.1a2

from qm.qua import *
from qualang_tools.units import unit
from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig

import matplotlib
import matplotlib.pyplot as plt
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.loops import from_array
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.results.data_handler import DataHandler
from qualang_tools.voltage_gates import VoltageGateSequence
from scipy import signal

from configuration_with_lffem import *

matplotlib.use('TkAgg')


#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)

n_avg = 100  # Number of averaging loops
offset_max = +0.4
offset_min = -offset_max
offset_step = 0.01
offsets = np.arange(offset_min, offset_max + offset_step, offset_step)
num_offsets = len(offsets)




config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                3: {
                    "type": "LF",
                    "analog_outputs": {
                        2: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1e9,
                            "upsampling_mode": "pulse",
                        },
                    },
                    "digital_outputs": {},
                    "analog_inputs": {},
                },
            },
        },
    },
    "elements": {
        "Psd1_sticky": {
            "singleInput": {
                "port": ("con1", 3, 2),
            },
            "sticky": {"analog": True, "duration": 4},
            "operations": {
                "step": f"Psd1_step_pulse",
            },
        },
    },
    "pulses": {
        "Psd1_step_pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": f"Psd1_step_wf",
            },
        },
    },
    "waveforms": {
        "Psd1_step_wf": {"type": "constant", "sample": 0.2},
        "zero_wf": {"type": "constant", "sample": 0.0},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
}


with program() as charge_sensor_sweep:
    i = declare(int)  # QUA variable for the voltage sweep
    n = declare(int)  # QUA variable for the averaging loop
    n_st = declare_stream()  # Stream for the averaging iteration 'n'


    # Set the voltage to the 1st point of the sweep]
    play("step" * amp(offset_min / 0.2), "Psd1_sticky")

    with for_(i, 0, i < num_offsets, i + 1):

        with if_(i > 0):
            play("step" * amp(offset_step / 0.2), "Psd1_sticky")

        ramp_to_zero("Psd1_sticky")


######################
# Network parameters #
######################
qop_ip = "192.168.1.41"  # Write the QM router IP address
cluster_name = "Cluster_1"  # "Beta_8"  # Write your cluster_name if version >= QOP220
qop_port = 9510  # Write the QOP port if version < QOP220
octave_config = None




qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)
# Open the quantum machine
simulation_config = SimulationConfig(duration=6_000)  # In clock cycles = 4ns
# Simulate blocks python until the simulation is done
job = qmm.simulate(config, charge_sensor_sweep, simulation_config)
# Plot the simulated samples
job.get_simulated_samples().con1.plot()
plt.show()

# %%