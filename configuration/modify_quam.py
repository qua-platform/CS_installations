import json
from pathlib import Path

from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.quam_builder.machine import save_machine

path = Path(".") / "quam_state"

machine = QuAM.load(path)

u = unit(coerce_to_integer=True)

machine.active_qubit_names = ["q0"]

# for qubit in machine.active_qubits:
#     qubit.xy.frequency_converter_up.LO_frequency = 4.5 * u.GHz
#     qubit.xy.intermediate_frequency = 50 * u.MHz
#     qubit.resonator.frequency_converter_up.LO_frequency = \
#     qubit.resonator.frequency_converter_down.LO_frequency = 7.175 * u.GHz
#     qubit.resonator.operations["readout"].amplitude = 0.2
#
# machine.qubits["q0"].resonator.intermediate_frequency = -114 * u.MHz
# machine.qubits["q1"].resonator.intermediate_frequency = -23 * u.MHz
# machine.qubits["q2"].resonator.intermediate_frequency = 135 * u.MHz
#
# machine.qubits["q2"].xy.frequency_converter_up.LO_frequency = 4.5 * u.GHz

save_machine(machine, path)

# View the corresponding "raw-QUA" config
with open("qua_config.json", "w+") as f:
    json.dump(machine.generate_config(), f, indent=4)
