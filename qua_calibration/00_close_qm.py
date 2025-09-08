# %%
from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
from configuration_mw_fem import *
"""
A simple program to close all other open QMs.
"""
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)
qmm.close_all_qms()
# Generate the OPX and Octave configurations
# Open Communication with the QOP