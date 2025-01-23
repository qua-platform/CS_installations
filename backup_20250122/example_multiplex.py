# %%
# Single QUA script generated at 2024-10-30 13:18:10.765219
# QUA library version: 1.2.1a2

from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.units import unit

from set_octave import OctaveUnit, octave_declaration

#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)

with program() as prog:
    v1 = declare(int, )
    a1 = declare(fixed, size=9)
    with for_(v1,0,(v1<10),(v1+1)):
        r1 = declare_stream()
        measure("readout", "resonator1", None, dual_demod.full("cos", "sin", a1[0]), timestamp_stream=r1)
        r2 = declare_stream()
        measure("readout", "resonator2", None, dual_demod.full("cos", "sin", a1[1]), timestamp_stream=r2)
        r3 = declare_stream()
        measure("readout", "resonator3", None, dual_demod.full("cos", "sin", a1[2]), timestamp_stream=r3)
        r4 = declare_stream()
        measure("readout", "resonator4", None, dual_demod.full("cos", "sin", a1[3]), timestamp_stream=r4)
        r5 = declare_stream()
        measure("readout", "resonator5", None, dual_demod.full("cos", "sin", a1[4]), timestamp_stream=r5)
        r6 = declare_stream()
        measure("readout", "resonator6", None, dual_demod.full("cos", "sin", a1[5]), timestamp_stream=r6)
        r7 = declare_stream()
        measure("readout", "resonator7", None, dual_demod.full("cos", "sin", a1[6]), timestamp_stream=r7)
        r8 = declare_stream()
        measure("readout", "resonator8", None, dual_demod.full("cos", "sin", a1[7]), timestamp_stream=r8)
        r9 = declare_stream()
        measure("readout", "resonator9", None, dual_demod.full("cos", "sin", a1[8]), timestamp_stream=r9)


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0},  # I readout line
                2: {"offset": 0.0},  # Q readout line
                3: {"offset": 0.0},  # I qubit1 XY
                4: {"offset": 0.0},  # Q qubit1 XY
                5: {"offset": 0.0},  # I qubit2 XY
                6: {"offset": 0.0},  # Q qubit2 XY
                7: {"offset": 0.0},  # I qubit3 XY
                8: {"offset": 0.0},  # Q qubit3 XY
                9: {"offset": 0.0},  # I qubit4 XY
                10: {"offset": 0.0},  # Q qubit4 XY
            },
            "digital_outputs": {
                1: {},
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},  # I from down-conversion
                2: {"offset": 0.0, "gain_db": 0},  # Q from down-conversion
            },
        },
    },
    "octaves": {
        "octave1": {
            "RF_outputs": {
                1: {
                    "LO_frequency": 7 * u.GHz,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": 0,
                },
            },
            "RF_inputs": {
                1: {
                    "LO_frequency": 7 * u.GHz,
                    "LO_source": "internal",
                },
            },
            "connectivity": "con1",
        }
    },
    "elements": {
        "resonator1": {
            "RF_inputs": {"port": ("octave1", 1)},
            "RF_outputs": {"port": ("octave1", 1)},
            "intermediate_frequency": 200 * u.MHz,  # in Hz [-350e6, +350e6]
            'time_of_flight': 28,
            'smearing': 0,
            "operations": {
                "readout": f"readout_pulse",
            },
        },
        "resonator2": {
            "RF_inputs": {"port": ("octave1", 1)},
            "RF_outputs": {"port": ("octave1", 1)},
            "intermediate_frequency": 150 * u.MHz,  # in Hz [-350e6, +350e6]
            'time_of_flight': 28,
            'smearing': 0,
            "operations": {
                "readout": f"readout_pulse",
            },
        },
        "resonator3": {
            "RF_inputs": {"port": ("octave1", 1)},
            "RF_outputs": {"port": ("octave1", 1)},
            "intermediate_frequency": 100 * u.MHz,  # in Hz [-350e6, +350e6]
            'time_of_flight': 28,
            'smearing': 0,
            "operations": {
                "readout": f"readout_pulse",
            },
        },
        "resonator4": {
            "RF_inputs": {"port": ("octave1", 1)},
            "RF_outputs": {"port": ("octave1", 1)},
            "intermediate_frequency": 50 * u.MHz,  # in Hz [-350e6, +350e6]
            'time_of_flight': 28,
            'smearing': 0,
            "operations": {
                "readout": f"readout_pulse",
            },
        },
        "resonator5": {
            "RF_inputs": {"port": ("octave1", 1)},
            "RF_outputs": {"port": ("octave1", 1)},
            "intermediate_frequency": 0 * u.MHz,  # in Hz [-350e6, +350e6]
            'time_of_flight': 28,
            'smearing': 0,
            "operations": {
                "readout": f"readout_pulse",
            },
        },
        "resonator6": {
            "RF_inputs": {"port": ("octave1", 1)},
            "RF_outputs": {"port": ("octave1", 1)},
            "intermediate_frequency": -50 * u.MHz,  # in Hz [-350e6, +350e6]
            'time_of_flight': 28,
            'smearing': 0,
            "operations": {
                "readout": f"readout_pulse",
            },
        },
        "resonator7": {
            "RF_inputs": {"port": ("octave1", 1)},
            "RF_outputs": {"port": ("octave1", 1)},
            "intermediate_frequency": -100 * u.MHz,  # in Hz [-350e6, +350e6]
            'time_of_flight': 28,
            'smearing': 0,
            "operations": {
                "readout": f"readout_pulse",
            },
        },
        "resonator8": {
            "RF_inputs": {"port": ("octave1", 1)},
            "RF_outputs": {"port": ("octave1", 1)},
            "intermediate_frequency": -150 * u.MHz,  # in Hz [-350e6, +350e6]
            'time_of_flight': 28,
            'smearing': 0,
            "operations": {
                "readout": f"readout_pulse",
            },
        },
        "resonator9": {
            "RF_inputs": {"port": ("octave1", 1)},
            "RF_outputs": {"port": ("octave1", 1)},
            "intermediate_frequency": -200 * u.MHz,  # in Hz [-350e6, +350e6]
            'time_of_flight': 28,
            'smearing': 0,
            "operations": {
                "readout": f"readout_pulse",
            },
        },
    },
    "pulses": {
        "readout_pulse": {
            "operation": "measurement",
            "length": 1000,
            "waveforms": {
                "I": "readout_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
            },
        },
        "zero_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "zero_wf",
                "Q": "zero_wf",
            },
        },
    },
    "waveforms": {
        "readout_wf": {"type": "constant", "sample": 0.01},
        "zero_wf": {"type": "constant", "sample": 0.0},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, 1000)],
            "sine": [(0.0, 1000)],
        },
        "sine_weights": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
    },
}

######################
# Network parameters #
######################
qop_ip = "172.16.33.101" # Write the QM router IP address
cluster_name = "Cluster_81" # Write the QM router IP address
qop_port = None  # Write the QOP port if version < QOP220

############################
# Set octave configuration #
############################
con = "con1"
# The Octave port is 11xxx, where xxx are the last three digits of the Octave internal IP that can be accessed from
# the OPX admin panel if you QOP version is >= QOP220. Otherwise, it is 50 for Octave1, then 51, 52 and so on.
octave_1 = OctaveUnit("octave1", qop_ip, port=11232, con=con)
# octave_2 = OctaveUnit("octave2", qop_ip, port=11051, con=con)

# If the control PC or local network is connected to the internal network of the QM router (port 2 onwards)
# or directly to the Octave (without QM the router), use the local octave IP and port 80.
# octave_ip = "192.168.88.X"
# octave_1 = OctaveUnit("octave1", octave_ip, port=80, con=con)

# Add the octaves
octaves = [octave_1]
# Configure the Octaves
octave_config = octave_declaration(octaves)


qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)
# Open the quantum machine
qm = qmm.open_qm(config)
# Send the QUA program to the OPX, which compiles and executes it
job = qm.execute(prog)
# %%
