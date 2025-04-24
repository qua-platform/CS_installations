# %%

"""
A simple program to close all other open QMs.
"""

from typing import Optional, List
from qualibrate import QualibrationNode, NodeParameters

from quam_libs.components import QuAM


# %% {Node_parameters}
class Parameters(NodeParameters):
    qubits: Optional[List[str]] = None


from pathlib import Path
script_name = Path(__file__).stem
node = QualibrationNode(name=script_name, parameters=Parameters())

# Instantiate the QuAM class from the state file
machine = QuAM.load()

# Generate the OPX and Octave configurations
config = machine.generate_config()
# Open Communication with the QOP
qmm = machine.connect()
qmm.clear_all_job_results()
qmm.close_all_qms()
