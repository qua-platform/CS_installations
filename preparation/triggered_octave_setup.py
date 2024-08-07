from quam_components import QuAM
from macros import node_save
from quam.components import DigitalOutputChannel

###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Instantiate the QuAM class from the state file
machine = QuAM.load("state.json")
# Generate the OPX and Octave configurations

for qubit in machine.active_qubits:
    for element in [qubit.xy, qubit.resonator]:
        element.frequency_converter_up.output_mode = "triggered"
    qubit.resonator.digital_outputs = {
        "octave_switch": DigitalOutputChannel(
            opx_output="#/wiring/resonator/digital_port",
            delay=87,  # 57ns for QOP222 and above
            buffer=15,  # 18ns for QOP222 and above
        )
    }
    qubit.xy.digital_outputs = {
        "octave_switch": DigitalOutputChannel(
            opx_output="#/wiring/qubits/0/digital_port",
            delay=87,  # 57ns for QOP222 and above
            buffer=15,  # 18ns for QOP222 and above
        )
    }

config = machine.generate_config()
with open('test_config.json', 'w') as f:
    json.dump(config, f, indent=4)

node_save("triggered_mode_octave", {}, machine)
