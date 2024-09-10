# %% Initial configuration
from qualibrate import QualibrationNode, NodeParameters
from typing import Optional, List
import matplotlib.pyplot as plt
import numpy as np

from qm.qua import *
from qualang_tools.loops import from_array
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.macros import get_job_results


class Parameters(NodeParameters):
    qubits: Optional[List[str]] = None
    num_averages: int = 250
    operation: str = "saturation"
    operation_amplitude_factor: Optional[float] = 0.01
    operation_length: Optional[int] = None
    frequency_span: float = 20e6
    frequency_step: float = 0.25e6


node = QualibrationNode(name="qubit_spectroscopy", parameters_class=Parameters)

node.parameters = params = Parameters(qubits=["q1"])


# %% Load QuAM and create program

# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)

# Instantiate the QuAM class from the state file
machine = QuAM.load()
# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.get_octave_config()

# Get the relevant QuAM components
qubit = machine.qubits[node.parameters.qubits[0]]

# Qubit detuning sweep with respect to their resonance frequencies
frequency_shifts = np.arange(
    -params.frequency_span // 2,
    params.frequency_span // 2,
    params.frequency_step,
)

with program() as qubit_spec:
    n = declare(int)
    n_st = declare_stream()
    I_st = declare_stream()
    Q_st = declare_stream()
    df = declare(int)  # QUA variable for the qubit frequency

    machine.apply_all_flux_to_joint_idle()

    qubit.wait(1000)
    with for_(n, 0, n < params.num_averages, n + 1):
        save(n, n_st)
        with for_(*from_array(df, frequency_shifts)):
            # Update the qubit frequency
            qubit.xy.update_frequency(df + qubit.xy.intermediate_frequency)

            # Play the saturation pulse
            qubit.xy.play(
                params.operation,
                amplitude_scale=params.operation_amplitude_factor,
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
        I_st.buffer(len(frequency_shifts)).average().save("I")
        Q_st.buffer(len(frequency_shifts)).average().save("Q")

# %% Run Program

# Open Communication with the QOP
qmm = machine.connect()
# Open the quantum machine
qm = qmm.open_qm(config, close_other_machines=False)
try:
    job = qm.execute(qubit_spec)
    job.result_handles.wait_for_all_values()
finally:
    qm.close()

# Fetch results
results = get_job_results(job)

# %% Fetch results and plot
fig, ax = plt.subplots()
ax.plot(frequency_shifts, results["I"])
ax.plot(frequency_shifts, results["Q"])

# %% Save results
node.results = {**results, "fig": fig}
node.machine = machine
node.save()

# %%
