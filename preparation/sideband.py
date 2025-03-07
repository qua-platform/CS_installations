from quam_components  import QuAM
from quam.components.channels import SingleChannel
from quam.components.pulses import SquarePulse, Pulse
from macros import node_save


machine = QuAM.load("state.json")
for qubit in machine.qubits.values():
    qubit.z_sb = SingleChannel(opx_output="#../z/opx_output",intermediate_frequency=80e6)
    qubit.z_sb.operations={
        "const": SquarePulse(
            amplitude=-0.25 / 2, length="#../z/operations/const/length", axis_angle=0
        )
    }

node_save("test", {}, machine)