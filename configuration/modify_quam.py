# %%
import json
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.quam_builder.machine import save_machine
import numpy as np


path = "./quam_state"

machine = QuAM.load()

u = unit(coerce_to_integer=True)
def get_band(frequency: float):
    ## Update qubit rr freq and power
    if frequency > 7.5 * u.GHz:
        return 3
    elif 5.5 * u.GHz < frequency <= 7.5 * u.GHz:
        return 2
    elif frequency <= 5.5 * u.GHz:
        return 1
    else:
        raise ValueError(f"The rr frequency {rr_LO[i]} is outside the MW fem bandwidth [50MHz, 10.5GHz].")
# Change active qubits
# machine.active_qubit_names = ["q0"]

# Update frequencies
rr_freq = np.array([10.033, 9.622, 9.946, 9.424, 9.747, 9.325, 9.842, 9.518]) * u.GHz
rr_if = 50 * u.MHz
rr_LO = rr_freq - rr_if

xy_freq_01 = np.array([4.601, 4.370, 4.353, 4.103, 4.511, 4.456, 4.514, 4.318]) * u.GHz
xy_freq_12 = np.array([4.432, 4.196, 4.179, 3.926, 4.338, 4.283, 4.343, 4.144]) * u.GHz
anaharmonicity = np.abs(xy_freq_12 - xy_freq_01)
xy_if = 50 * u.MHz
xy_LO = xy_freq_01 - xy_if

# Update qubit parameters
T1 = np.array([23, 41, 49, 33, 49, 14, 19, 34]) * 1e-6
grid_locations = ["0-2", "1-2", "2-2", "2-1", "2-0", "1-0", "0-0", "0-1"]
# NOTE: be aware of coupled ports for bands
for i, q in enumerate(machine.qubits):
    qb = machine.qubits[q]
    qb.grid_location = grid_locations[i]

    qb.resonator.opx_output.upconverter_frequency = round(rr_LO[i])
    qb.resonator.opx_output.band = get_band(rr_LO[i])
    qb.resonator.opx_input.downconverter_frequency = round(rr_LO[i])
    qb.resonator.opx_input.band = get_band(rr_LO[i])
    qb.resonator.intermediate_frequency = rr_if
    ## Update qubit xy freq and power
    qb.xy.opx_output.upconverter_frequency = round(xy_LO[i])
    qb.xy.opx_output.band = get_band(xy_LO[i])
    qb.xy.intermediate_frequency = xy_if

    qb.anharmonicity = int(anaharmonicity[i])
    ## Update qubit xy detuned freq and power
    # qb.xy_detuned.frequency_converter_up.LO_frequency = round(xy_LO[i])
    # qb.xy_detuned.intermediate_frequency = qb.xy.intermediate_frequency + round(xy_if_detuning[i])
    # qb.xy_detuned.thread = qb.name

    # Qubit T1
    qb.T1 = T1[i]
    ## Update pulses
    # readout
    qb.resonator.opx_output.full_scale_power_dbm = -8
    qb.resonator.operations["readout"].length = 2 * u.us
    qb.resonator.operations["readout"].amplitude = 0.1
    # Qubit saturation
    qb.xy.opx_output.full_scale_power_dbm = 1
    qb.xy.operations["saturation"].length = 40 * u.us
    qb.xy.operations["saturation"].amplitude = 0.5
    # Single qubit gates - DragCosine
    qb.xy.operations["x180_DragCosine"].length = 40
    qb.xy.operations["x180_DragCosine"].amplitude = 0.2
    qb.xy.operations["x90_DragCosine"].amplitude = qb.xy.operations["x180_DragCosine"].amplitude / 2
    # Single qubit gates - Square
    qb.xy.operations["x180_Square"].length = 40
    qb.xy.operations["x180_Square"].amplitude = 0.1
    qb.xy.operations["x90_Square"].amplitude = qb.xy.operations["x180_Square"].amplitude / 2

from quam.components import pulses

for i, qp in enumerate(machine.qubit_pairs):
    qb_pair = machine.qubit_pairs[qp]
    qbc = qb_pair.qubit_control
    qbt = qb_pair.qubit_target
    cr = qb_pair.cross_resonance
    zz = qb_pair.zz_drive

    # CR gates - Square
    cr.thread = qbc.name
    qbt.xy.operations[f"{cr.name}_Square"] = pulses.SquarePulse(amplitude=-0.25, length=100, axis_angle=0, digital_marker="ON")
    qbt.xy.operations[f"{cr.name}_Square"].amplitude = 0.1
    qbt.xy.operations[f"{cr.name}_Square"].length = f"#/qubit_pairs/{qb_pair.name}/cross_resonance/operations/square/length"
    qbt.xy.operations[f"{cr.name}_Square"].axis_angle = 0

    # ZZ gates - Square
    zz.thread = qbc.name
    zz.detuning = -15 * u.MHz
    # qbt.xy_detuned.detuning = f"#/qubit_pairs/{qb_pair.name}/zz_drive/intermediate_frquencys"
    qbt.xy_detuned.operations[f"{zz.name}_Square"] = pulses.SquarePulse(amplitude=-0.25, length=100, axis_angle=0, digital_marker="ON")
    qbt.xy_detuned.operations[f"{zz.name}_Square"].amplitude = 0.1
    qbt.xy_detuned.operations[f"{zz.name}_Square"].length = f"#/qubit_pairs/{qb_pair.name}/zz_drive/operations/square/length"
    qbt.xy_detuned.operations[f"{zz.name}_Square"].axis_angle = 0
        

# %%
# save into state.json
save_machine(machine, path)

# %%
# View the corresponding "raw-QUA" config
with open("qua_config.json", "w+") as f:
    json.dump(machine.generate_config(), f, indent=4)

# %%
