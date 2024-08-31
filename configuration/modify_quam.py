import json
from pathlib import Path

from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.quam_builder.machine import save_machine

path = Path(".") / "quam_state"

machine = QuAM.load(path)

u = unit(coerce_to_integer=True)

# machine.qubits["q1"].resonator.frequency_converter_up.LO_frequency = 5.9 * u.GHz
# machine.qubits["q1"].resonator.operations["readout"].amplitude = 0.01
# machine.qubits["q1"].resonator.operations["readout"].length = 2000
# machine.qubits["q1"].xy.operations["x180_DragGaussian"].amplitude = 0.1

save_machine(machine, path)

# View the corresponding "raw-QUA" config
with open("qua_config.json", "w+") as f:
    json.dump(machine.generate_config(), f, indent=4)
