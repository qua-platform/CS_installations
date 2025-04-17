# %%
import json
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.quam_builder.machine import save_machine
import numpy as np


def get_band(freq):
    if 50e6 <= freq < 5.5e9:
        return 1
    elif 4.5e9 <= freq < 7.5e9:
        return 2
    elif 6.5e9 <= freq <= 10.5e9:
        return 3
    else:
        raise ValueError(f"The specified frequency {freq} HZ is outside of the MW fem bandwidth [50 MHz, 10.5 GHz]")


path = "./quam_state"

machine = QuAM.load(path)

u = unit(coerce_to_integer=True)

# Change active qubits
# machine.active_qubit_names = ["q0"]

for i in range(len(machine.rf_qubits.items())):
    machine.rf_qubits[f"q{i+1}"].grid_location = f"{i},0"

# Update frequencies
rr_freq = np.array([7, 7.1]) * u.GHz
rr_LO = 7.3 * u.GHz
rr_if = rr_freq - rr_LO
rr_max_power_dBm = 4

xy_freq = np.array([100, 200]) * u.MHz

c12_freq = np.array([4]) * u.GHz
c12_LO = 4.2 * u.GHz
c12_if = c12_freq - c12_LO
c12_max_power_dBm = 4

# NOTE: be aware of coupled ports for bands
for i, q in enumerate(machine.rf_qubits):
    ## Update qubit rr freq and power
    machine.rf_qubits[q].resonator.opx_output.full_scale_power_dbm = rr_max_power_dBm
    machine.rf_qubits[q].resonator.opx_output.upconverter_frequency = rr_LO
    machine.rf_qubits[q].resonator.opx_input.downconverter_frequency = rr_LO
    machine.rf_qubits[q].resonator.opx_input.band = get_band(rr_LO)
    machine.rf_qubits[q].resonator.opx_output.band = get_band(rr_LO)
    machine.rf_qubits[q].resonator.intermediate_frequency = rr_if[i]

    ## Update qubit xy freq and power
    machine.rf_qubits[q].I.intermediate_frequency = xy_freq[i]
    machine.rf_qubits[q].I.opx_output.output_mode = "amplified"
    machine.rf_qubits[q].Q.intermediate_frequency = xy_freq[i]
    machine.rf_qubits[q].Q.opx_output.output_mode = "amplified"

    # Update flux channels
    machine.rf_qubits[q].z.opx_output.output_mode = "amplified"
    machine.rf_qubits[q].z.opx_output.upsampling_mode = "pulse"

    ## Update pulses
    # readout
    machine.rf_qubits[q].resonator.operations["readout"].length = 2.5 * u.us
    machine.rf_qubits[q].resonator.operations["readout"].amplitude = 1e-3
    machine.rf_qubits[q].resonator.operations["const"].length = 2.5 * u.us
    machine.rf_qubits[q].resonator.operations["const"].amplitude = 1e-3

    # Qubit saturation
    machine.rf_qubits[q].I.operations["saturation"].length = 20 * u.us
    machine.rf_qubits[q].I.operations["saturation"].amplitude = 0.25
    machine.rf_qubits[q].Q.operations["saturation"].length = 20 * u.us
    machine.rf_qubits[q].Q.operations["saturation"].amplitude = 0.25
    # Single qubit gates - Square
    machine.rf_qubits[q].I.operations["x180_Square"].length = 40
    machine.rf_qubits[q].I.operations["x180_Square"].amplitude = 0.1
    machine.rf_qubits[q].I.operations["x90_Square"].amplitude = (
        machine.rf_qubits[q].I.operations["x180_Square"].amplitude / 2
    )
    machine.rf_qubits[q].Q.operations["x180_Square"].length = 40
    machine.rf_qubits[q].Q.operations["x180_Square"].amplitude = 0.1
    machine.rf_qubits[q].Q.operations["x90_Square"].amplitude = (
        machine.rf_qubits[q].Q.operations["x180_Square"].amplitude / 2
    )
    # Single qubit gates - Cosine
    machine.rf_qubits[q].I.operations["x180_Cosine"].length = 40
    machine.rf_qubits[q].I.operations["x180_Cosine"].amplitude = 0.2
    machine.rf_qubits[q].I.operations["x90_Cosine"].amplitude = (
        machine.rf_qubits[q].I.operations["x180_Cosine"].amplitude / 2
    )
    machine.rf_qubits[q].Q.operations["x180_Cosine"].length = 40
    machine.rf_qubits[q].Q.operations["x180_Cosine"].amplitude = 0.2
    machine.rf_qubits[q].Q.operations["x90_Cosine"].amplitude = (
        machine.rf_qubits[q].Q.operations["x180_Cosine"].amplitude / 2
    )
    # Single qubit gates - DragCosine
    machine.rf_qubits[q].I.operations["x180_DragCosine"].length = 40
    machine.rf_qubits[q].I.operations["x180_DragCosine"].amplitude = 0.2
    machine.rf_qubits[q].I.operations["x180_DragCosine"].alpha = 1.0
    machine.rf_qubits[q].I.operations["x90_DragCosine"].amplitude = (
        machine.rf_qubits[q].I.operations["x180_DragCosine"].amplitude / 2
    )

    machine.rf_qubits[q].Q.operations["x180_DragCosine"].length = 40
    machine.rf_qubits[q].Q.operations["x180_DragCosine"].amplitude = 0.2
    machine.rf_qubits[q].Q.operations["x180_DragCosine"].alpha = machine.rf_qubits[q].I.operations["x180_DragCosine"].alpha
    machine.rf_qubits[q].Q.operations["x180_DragCosine"].amplitude = 0.2
    machine.rf_qubits[q].Q.operations["x90_DragCosine"].amplitude = (
        machine.rf_qubits[q].Q.operations["x180_DragCosine"].amplitude / 2
    )


# NOTE: be aware of coupled ports for bands
for i, q in enumerate(machine.qubits):
    ## Update qubit c12 freq and power
    machine.qubits[q].xy.opx_output.full_scale_power_dbm = c12_max_power_dBm
    machine.qubits[q].xy.opx_output.upconverter_frequency = c12_LO
    machine.qubits[q].xy.opx_output.band = get_band(c12_LO)
    machine.qubits[q].xy.intermediate_frequency = c12_if[i]

    # Update flux channel
    machine.qubits[q].z.opx_output.output_mode = "amplified"
    machine.qubits[q].z.opx_output.upsampling_mode = "pulse"

    ## Update pulses

    # c12 saturation
    machine.qubits[q].xy.operations["saturation"].length = 20 * u.us
    machine.qubits[q].xy.operations["saturation"].amplitude = 0.25



# %%
# save into state.json
save_machine(machine, path)

# %%
# View the corresponding "raw-QUA" config
with open("qua_config.json", "w+") as f:
    json.dump(machine.generate_config(), f, indent=4)

# %%
