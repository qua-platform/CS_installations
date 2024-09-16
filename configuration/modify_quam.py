# %%
import json
# from pathlib import Path

# from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.quam_builder.machine import save_machine

path = r"C:\\Users\\tomdv\\Documents\\QCC_QUAM\\CS_installations\\configuration\\quam_state"

machine = QuAM.load(path)

# u = unit(coerce_to_integer=True)

# Change active qubits
# machine.active_qubit_names = ["q0"]

# %%
resonators_dict = {
    "q1": {"LO": 7380000000, "IF": -226e6, "RF_gain": -15},
    "q2": {"LO": 7380000000, "IF": 40e6, "RF_gain": -15},
    "q3": {"LO": 7380000000, "IF": 144e6, "RF_gain": -15},
    "q4": {"LO": 7380000000, "IF": -110e6, "RF_gain": -15},
}

drive_dict = {
    "q1": {"LO": 4800000000, "IF": 153e6, "RF_gain": 10},
    "q2": {"LO": 5590000000, "IF": 262e6, "RF_gain": 10},
    "q3": {"LO": 5590000000, "IF": 84e6, "RF_gain": 10},
    "q4": {"LO": 4800000000, "IF": 316e6, "RF_gain": 10},
}

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



qubits = machine.active_qubits
for qubit in qubits:
    machine.qubits[qubit.name].resonator.frequency_converter_up.gain = resonators_dict[qubit.name]["RF_gain"]
    machine.qubits[qubit.name].resonator.frequency_converter_up.LO_frequency = resonators_dict[qubit.name]["LO"]
    machine.qubits[qubit.name].resonator.frequency_converter_down.LO_frequency  = resonators_dict[qubit.name]["LO"]
    machine.qubits[qubit.name].resonator.depletion_time = 2500
    machine.qubits[qubit.name].resonator.time_of_flight = 264
    machine.qubits[qubit.name].resonator.operations["readout"].length = 1500
    
    machine.qubits[qubit.name].resonator.intermediate_frequency = resonators_dict[qubit.name]["IF"]
    machine.qubits[qubit.name].xy.frequency_converter_up.gain = drive_dict[qubit.name]["RF_gain"]
    machine.qubits[qubit.name].xy.frequency_converter_up.LO_frequency = drive_dict[qubit.name]["LO"]
    machine.qubits[qubit.name].xy.intermediate_frequency = drive_dict[qubit.name]["IF"]
    

# %%
# save into state.json
save_machine(machine, path)

# %%
# View the corresponding "raw-QUA" config
with open("qua_config.json", "w+") as f:
    json.dump(machine.generate_config(), f, indent=4)

# %%
