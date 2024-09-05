import json
from pathlib import Path

from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.quam_builder.machine import save_machine

path = Path(".") / "quam_state"

machine = QuAM.load(path)

u = unit(coerce_to_integer=True)

# Change active qubits
# machine.active_qubit_names = ["q0"]

for _ in machine.ports.analog_outputs.con1:
    for r in machine.ports.analog_outputs.con1[_]:
            machine.ports.analog_outputs.con1[_][r].sampling_rate = 1e9
            machine.ports.analog_outputs.con1[_][r].upsampling_mode = 'pulse'
            machine.ports.analog_outputs.con1[_][r].output_mode = "amplified"

save_machine(machine, path)

# View the corresponding "raw-QUA" config
with open("qua_config.json", "w+") as f:
    json.dump(machine.generate_config(), f, indent=4)
