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
    operation: str = "DragCosine"

    operation_length: Optional[int] = None

    amplitude_min: float = 0.01
    amplitude_max: float = 2
    amplitude_step: float = 0.01


node = QualibrationNode(name="rabi", parameters_class=Parameters)

node.parameters = params = Parameters(qubits=["q1"])


# %% Load QuAM and create program

# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)

# Instantiate the QuAM class from the state file
machine = QuAM.load()

# Get the relevant QuAM components
qubit = machine.qubits[node.parameters.qubits[0]]

from quam.components.pulses import DragCosinePulse

qubit.xy.operations["DragCosine"] = DragCosinePulse(
    length=32,
    axis_angle=0,
    amplitude=0.2,
    alpha=-1.054045595373771,
    anharmonicity=206500000,
    detuning=580000,
)

# Generate the OPX and Octave configurations
config = machine.generate_config()

# Qubit detuning sweep with respect to their resonance frequencies
amplitude_scales = np.arange(
    params.amplitude_min, params.amplitude_max, params.amplitude_step
)

with program() as prog:
    n = declare(int)
    n_st = declare_stream()
    I_st = declare_stream()
    Q_st = declare_stream()
    amplitude_scale = declare(fixed)  # QUA variable for the qubit frequency

    machine.apply_all_flux_to_joint_idle()

    qubit.wait(1000)
    with for_(n, 0, n < params.num_averages, n + 1):
        save(n, n_st)
        with for_(*from_array(amplitude_scale, amplitude_scales)):
            qubit.xy.play(
                params.operation,
                amplitude_scale=amplitude_scale,
                duration=params.operation_length,
            )
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
        I_st.buffer(len(amplitude_scales)).average().save("I")
        Q_st.buffer(len(amplitude_scales)).average().save("Q")


# %% Run on IQCC
with program() as prog:
    a = declare(fixed)
    r1 = declare_stream()
    r2 = declare_stream()
    v2 = declare(
        bool,
    )

    with for_(a, 0, a < 1.1, a + 0.05):

        # play("pi" * amp(a), "qubit")
        save(a, r1)
        assign(v2, (a > 0.2))
        save(v2, r2)
    with stream_processing():
        r1.save_all("measurements")
        r2.save_all("state")


# %% Run on IQCC
results = execute_IQCC(prog, machine, debug=True)

# %% Run Program
results = execute_local(prog, machine)

# %% Fetch results and plot
fig, ax = plt.subplots()
ax.plot(amplitude_scales, results["I"])
ax.plot(amplitude_scales, results["Q"])

# %% Save results
node.results = {**results, "fig": fig}
node.machine = machine
node.save()

# %%
