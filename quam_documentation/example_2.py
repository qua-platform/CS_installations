

# Creating a Quam from scratch: 
from quam.components import Qubit, IQChannel, SingleChannel
from quam.examples.superconducting_qubits import Quam, Transmon
from quam.components import *
from quam.core import quam_dataclass # This is a decorator

# Instantiate your machine

machine = Quam()

q1 = machine.qubits["q1"] = Transmon(
    id = "Qubit1",
    xy = IQChannel(
        opx_output_I = ("con1", 5, 1), 
        opx_output_Q = ("con1", 5, 2), 
        frequency_converter_up = FrequencyConverter(
            local_oscillator = None, mixer = None
        )
    ),
    z = SingleChannel(
        opx_output = ("con1", 5, 3)
    )
)

machine.save("/Users/kalidu_laptop/QUA/CS_installations/quam_documentation")


# Another example creation:

from quam_builder.architecture.superconducting.qpu import FluxTunableQuam
machine = FluxTunableQuam()



