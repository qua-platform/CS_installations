# %%
"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
# from configuration_opxplus_with_octave import *
from configuration_opxplus_without_octave import *

###################
# The QUA program #
###################

with program() as hello_qua:

    # readout lines
    for rr in list(RR_CONSTANTS.keys()):
        play("cw", rr)

    align()
    # xy drives
    for qubit in list(QUBIT_CONSTANTS.keys()):
        play("cw", qubit)
    
        
if __name__ == "__main__":
    #####################################
    #  Open Communication with the QOP  #
    #####################################
    qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

    ###########################
    # Run or Simulate Program #
    ###########################

    simulate = False

    if simulate:
        # Simulates the QUA program for the specified duration
        simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
        # Simulate blocks python until the simulation is done
        
        job = qmm.simulate(config, hello_qua, simulation_config)
        # Plot the simulated samples
        job.get_simulated_samples().con1.plot()

    else:
        # Open a quantum machine to execute the QUA program
        qm = qmm.open_qm(config)

        # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
        job = qm.execute(hello_qua)

# %%
