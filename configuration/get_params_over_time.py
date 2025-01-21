# %%
import json
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.quam_builder.machine import save_machine
import numpy as np
from quam_libs.macros import *
from qualibrate import QualibrationNode, NodeParameters


node = QualibrationNode(name="05_T1")
node = node.load_from_id("2376")
ds = node.results["ds"]

qubits = node.results["initial_parameters"]["qubits"]
if qubits is None:
    qubits = node.machine.active_qubit_names

node.machine.qubits[qubits[0]].
