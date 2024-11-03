# %%

import numpy as np
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
import matplotlib.pyplot as plt
from qualang_tools.loops import from_array
from qualang_tools.units import unit
from qualang_tools.voltage_gates import VoltageGateSequence

#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)


######################
# Network parameters #
######################
qop_ip = "172.16.33.101" # Write the QM router IP address
cluster_name = "Cluster_83" # Write the QM router IP address
qop_port = None  # Write the QOP port if version < QOP220
octave_config = None


###################
#     Config      #
###################

hold_offset_duration_ns = 100

config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": +0.0},
                2: {"offset": +0.0},
                3: {"offset": +0.0},
            },
        }
    },
    "elements": {
        "Vg1_sticky": {
            "singleInput": {"port": ("con1", 1)},
            "sticky": {"analog": True, "duration": hold_offset_duration_ns},
            "operations": {
                "step": "step_pulse_Vg1",
            },
        },
        "Vg2_sticky": {
            "singleInput": {"port": ("con1", 2)},
            "sticky": {"analog": True, "duration": hold_offset_duration_ns},
            "operations": {
                "step": "step_pulse_Vg2",
            },
        },
        "Vg3_sticky": {
            "singleInput": {"port": ("con1", 3)},
            "sticky": {"analog": True, "duration": hold_offset_duration_ns},
            "operations": {
                "step": "step_pulse_Vg3",
            },
        },
    },
    "pulses": {
        "step_pulse_Vg1": {
            "operation": "control",
            "length": 1000,  # in ns
            "waveforms": {"single": "step_wf_Vg1"},
        },
        "step_pulse_Vg2": {
            "operation": "control",
            "length": 1000,  # in ns
            "waveforms": {"single": "step_wf_Vg1"},
        },
        "step_pulse_Vg3": {
            "operation": "control",
            "length": 1000,  # in ns
            "waveforms": {"single": "step_wf_Vg1"},
        },
    },
    "waveforms": {
        "step_wf_Vg1": {"type": "constant", "sample": 0.1},
        "step_wf_Vg2": {"type": "constant", "sample": 0.1},
        "step_wf_Vg3": {"type": "constant", "sample": 0.1},
    },
}

###################
# The QUA program #
###################

# The number of averages
n_avg = 10
# gate elements
Vg_elements = ["Vg1_sticky", "Vg2_sticky", "Vg3_sticky"]
# number of gates
num_Vgs = len(Vg_elements)
# This is to ensure the numpy arrays of the gate voltages have the same length
n_gate_voltages = 6
# Define the gate voltages as a list of numpy array so we can loop with enumerate and python index (i) 
dynamic_level_array_py = np.array([
    np.linspace(0, 0.005, n_gate_voltages),
    np.linspace(0, 0.011, n_gate_voltages),
    np.linspace(0, 0.017, n_gate_voltages),
])
dynamic_level_list_py = [row for row in dynamic_level_array_py]
assert all([len(dll) == n_gate_voltages for dll in dynamic_level_list_py]), "all the list have the same length"

# Initialize VoltageGateSequence
seq = VoltageGateSequence(config, Vg_elements)

with program() as prog:
    n = declare(int) # QUA variable for the averaging loop
    k = declare(int) # QUA variable for the Vg_fast
    Vgs_qua = [declare(fixed) for _ in range(num_Vgs)]  # QUA variable for the gate voltages

    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        # python for loop to iterate over elements           
        with for_each_(Vgs_qua, dynamic_level_list_py):
            # dynamic_level_list_py: python list of 1d numpy arrays
            # Vg_qua: python list of QUA fixed variables
            seq.add_step(level=Vgs_qua, duration=hold_offset_duration_ns)
        seq.ramp_to_zero(duration=hold_offset_duration_ns // 4)
        wait(200 * u.ns)


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
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, prog, simulation_config)
    job.get_simulated_samples().con1.plot()
    plt.show(block=False)
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(prog)
# %%
