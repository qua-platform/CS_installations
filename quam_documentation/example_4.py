from quam.examples.superconducting_qubits import Quam, Transmon
from quam.components import *
from quam.core import quam_dataclass


loaded_machine = Quam.load("/Users/kalidu_laptop/QUA/CS_installations/quam_documentation/state.json")
print(loaded_machine.generate_config)



