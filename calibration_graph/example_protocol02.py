# %%
"""
Example protocol

•	Apply an X gate to qubit q1.
•	Apply an X gate to qubit q2.
•	Measure q1 and q2 simultaneously, using multiplexing readout.

"""
from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.components import QuAM
from quam_libs.macros import *
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
# path = "../configuration/quam_state"
machine = QuAM.load()
# Generate the OPX and Octave configurations
config = machine.generate_config()
# octave_config = machine.get_octave_config()
# Open Communication with the QOP
qmm = machine.connect()
calibrate_octave = False

qubits = machine.active_qubits
resonators = [qubit.resonator for qubit in machine.active_qubits]
num_qubits = len(qubits)
num_resonators = len(resonators)
q1 = machine.qubits["q1"]
q2 = machine.qubits["q2"]

n_avg = 100

##########################
# not working
##########################
import os
from quam.core import quam_dataclass
from quam.components import pulses
from quam_libs.quam_builder.machine import save_machine

new_arb_wf = [
    0.15, 0.30, 0.30, 0.20,
    0.40, 0.10, 0.15, 0.05,
    0.00, 0.40, 0.35, 0.40,
    0.25, 0.45, 0.30, 0.20
]

@quam_dataclass
class NewArbitaryPulse(pulses.Pulse):
    def waveform_function(self):
        return new_arb_wf

q1.xy.operations["new_arb"] = NewArbitaryPulse(length=len(new_arb_wf))
save_machine(machine, os.environ["QUAM_STATE_PATH"])
##########################


with program() as prog:
    # Declare 'I' and 'Q' and the corresponding streams for the two resonators.
    # For instance, here 'I' is a python list containing two QUA fixed variables.
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)

    with for_(n, 0, n < n_avg, n + 1):
        # Apply an X gate to qubit q1.
        play(q1.xy.name, "new_arb")
        # Align all the elements
        align()
        
        #Measure q1 and q2 simultaneously, using multiplexing readout.
        multiplexed_readout(qubits, I, I_st, Q, Q_st)

        # Wait for the qubits to decay to the ground state
        wait(machine.thermalization_time * u.ns)
        
        # save iterations
        save(n, n_st)

    with stream_processing():
        n_st.save("n")
        for i in range(num_resonators):
            I_st[i].average().save(f"I{i + 1}")
            Q_st[i].average().save(f"Q{i + 1}")


#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, prog, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    from qm import generate_qua_script
    sourceFile = open('debug.py', 'w')
    print(generate_qua_script(prog, config), file=sourceFile)
    sourceFile.close()
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Calibrate the active qubits
    # machine.calibrate_octave_ports(qm)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(prog)
    # Get results from QUA program
    data_list = ["n"] + sum(
        [[f"I{i + 1}", f"Q{i + 1}", f"state{i + 1}"] for i in range(num_resonators)], []
    )
    results = fetching_tool(job, data_list, mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        fetched_data = results.fetch_all()
        n = fetched_data[0]
        I = fetched_data[1::3]
        Q = fetched_data[2::3]
        s = fetched_data[3::3]

        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)

    # Close the quantum machines at the end
    qm.close()

    # Save data from the node
    data = {}
    fetched_data = results.fetch_all()
    for i, (qubit, rr) in enumerate(zip(qubits, resonators)):
        data[f"I_{rr.name}"] = fetched_data[3 * i + 1]
        data[f"Q_{rr.name}"] = fetched_data[3 * i + 2]
        data[f"state_{rr.name}"] = fetched_data[3 * i + 3]
    node_save(machine, "example_protocol", data, additional_files=True)


# %%