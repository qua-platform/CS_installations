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
        raise ValueError(f"The rr frequency {rr_LO} is outside the MW fem bandwidth [50MHz, 10.5GHz].")

num_qubits = len(machine.active_qubits)


# Update frequencies
rr_freq = np.array([6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0]) * u.GHz
rr_LO =  6.75 * u.GHz
rr_if = rr_freq - rr_LO

xy_freq = np.array([4.20, 4.30, 4.40, 4.50, 4.60, 4.70, 4.80]) * u.GHz
xy_LO = np.array([4.30, 4.40, 4.50, 4.60, 4.70, 4.80, 4.90]) * u.GHz
xy_if_detuning = np.array([-10, -10, -10, -10, -10, -10, -10]) * u.MHz
xy_if = rr_freq - rr_LO

grid_locations = ["0-3", "1-3", "0-2", "1-2", "0-1", "1-1", "0-0"]

# NOTE: be aware of coupled ports for bands
for i, q in enumerate(machine.qubits):
    qb = machine.qubits[q]
    qb.grid_location = grid_locations[i]
    
    print(qb)

    qb.anharmonicity = -200 * u.MHz
    ## Update qubit rr freq and power
    qb.resonator.opx_output.upconverter_frequency = round(rr_LO)
    qb.resonator.opx_output.band = get_band(rr_LO)
    qb.resonator.opx_input.downconverter_frequency = round(rr_LO)
    qb.resonator.opx_input.band = get_band(rr_LO)
    qb.resonator.intermediate_frequency = round(rr_if[i])
    qb.resonator.thread = qb.name

    ## Update qubit xy freq and power
    qb.xy.opx_output.upconverter_frequency = round(xy_LO[i])
    qb.xy.opx_output.band = get_band(xy_LO[i])
    qb.xy.intermediate_frequency = round(xy_if[i])
    qb.xy.thread = qb.name

    ## Update qubit xy detuned freq and power
    qb.xy_detuned.opx_output.upconverter_frequency = round(xy_LO[i])
    qb.xy_detuned.intermediate_frequency = qb.xy.intermediate_frequency + round(xy_if_detuning[i])
    qb.xy_detuned.thread = qb.name

    ## Update pulses
    # readout
    qb.resonator.operations["readout"].length = 1 * u.us
    qb.resonator.operations["readout"].amplitude = 1e-2
    qb.resonator.operations["readout"].rus_exit_threshold = 0
    qb.resonator.operations["readout"].ge_threshold = 0
    # Qubit saturation
    qb.xy.operations["saturation"].length = 20 * u.us
    qb.xy.operations["saturation"].amplitude = 0.25
    # Single qubit gates - DragCosine
    qb.xy.operations["x180_DragCosine"].length = 48
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
    
    print(qb_pair)

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
