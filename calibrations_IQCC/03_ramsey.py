# %% Initial configuration
from qualibrate import QualibrationNode, NodeParameters
from typing import Optional, List
import matplotlib.pyplot as plt
import numpy as np

from qm.qua import *
from qualang_tools.loops import from_array
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.execute import execute_local, execute_IQCC


class Parameters(NodeParameters):
    qubits: Optional[List[str]] = None
    num_averages: int = 250
    operation: str = "x90_DragCosine"

    operation_length: Optional[int] = None

    tau_min: float = 16
    tau_max: float = 10000
    tau_step: float = 20


node = QualibrationNode(name="ramsey", parameters_class=Parameters)

node.parameters = params = Parameters(qubits=["q1"])


# %% Load QuAM and create program

# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)

# Instantiate the QuAM class from the state file
machine = QuAM.load()

# Get the relevant QuAM components
qubit = machine.qubits[node.parameters.qubits[0]]

# Generate the OPX and Octave configurations
config = machine.generate_config()

# Qubit detuning sweep with respect to their resonance frequencies
tau_vals = np.arange(params.tau_min // 4, params.tau_max // 4, params.tau_step // 4)

with program() as prog:
    n = declare(int)
    n_st = declare_stream()
    I_st = declare_stream()
    Q_st = declare_stream()
    tau = declare(int)  # QUA variable for the qubit frequency

    machine.apply_all_flux_to_joint_idle()

    qubit.wait(1000)
    with for_(n, 0, n < params.num_averages, n + 1):
        save(n, n_st)
        with for_(*from_array(tau, tau_vals)):
            with strict_timing_():
                qubit.xy.play(params.operation)
                qubit.xy.wait(tau)
                qubit.xy.play(params.operation)

            qubit.align()

            I, Q = qubit.resonator.measure("readout")

            # Wait for the qubit to decay to the ground state
            qubit.resonator.wait(machine.thermalization_time * u.ns)

            # save data
            save(I, I_st)
            save(Q, Q_st)

    qubit.align()

    with stream_processing():
        n_st.save("n")
        I_st.buffer(len(tau_vals)).average().save("I")
        Q_st.buffer(len(tau_vals)).average().save("Q")

# %% Run on IQCC
results = execute_IQCC(prog, machine, debug=True)

# %% Run Program
results = execute_local(prog, machine)

# %% Fetch results and plot
fig, ax = plt.subplots()
ax.plot(tau_vals, results["I"])
ax.plot(tau_vals, results["Q"])

# %% Save results
node.results = {**results, "fig": fig}
node.machine = machine
node.save()

# %%
