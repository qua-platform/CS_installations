from qualibrate import QualibrationNode, NodeParameters
from typing import Optional, Literal


class Parameters(NodeParameters):
    qubits: Optional[str] = 'q5'
    num_averages: int = 100
    min_wait_time_in_ns: int = 16
    max_wait_time_in_ns: int = 4000
    wait_time_step_in_ns: int = 20
    flux_point_joint_or_independent: Literal['joint', 'independent'] = "joint"
    simulate: bool = False

node = QualibrationNode(
    name="t1_experiment",
    parameters_class=Parameters
)

node.parameters = Parameters()


from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array, get_equivalent_log_array
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration, multiplexed_readout, node_save

import matplotlib.pyplot as plt
import numpy as np

import matplotlib
from quam_libs.lib.plot_utils import QubitGrid, grid_iter
from quam_libs.lib.save_utils import fetch_results_as_xarray
from quam_libs.lib.fit import fit_oscillation_decay_exp, oscillation_decay_exp

# matplotlib.use("TKAgg")


###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Class containing tools to help handle units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
machine = QuAM.load()
# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.get_octave_config()
# Open Communication with the QOP
qmm = machine.connect()

# Get the relevant QuAM components
if node.parameters.qubits is None or node.parameters.qubits == '':
    qubits = machine.active_qubits
else:
    qubits = [machine.qubits[q] for q in node.parameters.qubits.replace(' ', '').split(',')]
num_qubits = len(qubits)
# %%
###################
# The QUA program #
###################
n_avg = node.parameters.num_averages  # The number of averages

# Dephasing time sweep (in clock cycles = 4ns) - minimum is 4 clock cycles
idle_times = np.arange(
    node.parameters.min_wait_time_in_ns // 4,
    node.parameters.max_wait_time_in_ns // 4,
    node.parameters.wait_time_step_in_ns // 4,
)

flux_point = node.parameters.flux_point_joint_or_independent  # 'independent' or 'joint'

with program() as t1:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)
    t = declare(int)  # QUA variable for the idle time
    sign = declare(int)  # QUA variable to change the sign of the detuning
    phi = declare(fixed)  # QUA variable for dephasing the second pi/2 pulse (virtual Z-rotation)

    for i, q in enumerate(qubits):

        # Bring the active qubits to the minimum frequency point
        if flux_point == "independent":
            machine.apply_all_flux_to_min()
            q.z.to_independent_idle()
        elif flux_point == "joint":
            machine.apply_all_flux_to_joint_idle()
        else:
            machine.apply_all_flux_to_zero()

        for qb in qubits:
            wait(1000, qb.z.name)

        align()

        with for_(n, 0, n < n_avg, n + 1):
            save(n, n_st)
            with for_(*from_array(t, idle_times)):

                q.xy.play("x180")

                q.xy.wait(t)

                # Align the elements to measure after playing the qubit pulse.
                align()

                # Measure the state of the resonators
                q.resonator.measure("readout", qua_vars=(I[i], Q[i]))

                # save data
                save(I[i], I_st[i])
                save(Q[i], Q_st[i])

                # Wait for the qubits to decay to the ground state
                q.resonator.wait(machine.thermalization_time * u.ns)

        align()

    with stream_processing():
        n_st.save("n")
        for i in range(num_qubits):
            I_st[i].buffer(len(idle_times)).average().save(f"I{i + 1}")
            Q_st[i].buffer(len(idle_times)).average().save(f"Q{i + 1}")

###########################
# Run or Simulate Program #
###########################
simulate = node.parameters.simulate

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, t1, simulation_config)
    job.get_simulated_samples().con1.plot()
    node.results = {"figure": plt.gcf()}
    node.machine = machine
    node.save()
    quit()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config,keep_dc_offsets_when_closing=False)
    # Calibrate the active qubits
    # machine.calibrate_octave_ports(qm)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(t1, flags=['auto-element-thread'])
    # Get results from QUA program
    for i in range(num_qubits):
        print(f"Fetching results for qubit {qubits[i].name}")
        data_list = sum([[f"I{i + 1}", f"Q{i + 1}"] ], ["n"])
        results = fetching_tool(job, data_list, mode="live")
    # Live plotting
    # fig, axes = plt.subplots(2, num_qubits, figsize=(4 * num_qubits, 8))
    # interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
        while results.is_processing():
        # Fetch results
            fetched_data = results.fetch_all()
            n = fetched_data[0]

            progress_counter(n, n_avg, start_time=results.start_time)

    qm.close()

    for i in range(num_qubits):
        print(f"Fetching results for qubit {qubits[i].name}")
        data_list = sum([[f"I{i + 1}", f"Q{i + 1}"] ], ["n"])
        results = fetching_tool(job, data_list)

    data = results.fetch_all()

    fig = plt.figure()
    plt.plot(idle_times * 4, data[1])
    plt.show()

    # Fit the results to extract the qubit decay time T1
    try:
        from qualang_tools.plot.fitting import Fit

        fit = Fit()
        fig2 = plt.figure()
        decay_fit = fit.T1(4 * idle_times, data[1], plot=True)
        qubit_T1 = np.round(np.abs(decay_fit["T1"][0]) / 4) * 4
        plt.xlabel("Delay [ns]")
        plt.ylabel("I quadrature [V]")
        print(f"Qubit decay time to update in the config: qubit_T1 = {qubit_T1:.0f} ns")
        plt.legend((f"Relaxation time T1 = {qubit_T1:.0f} ns",))
        plt.title("T1 measurement")
    except (Exception,):
        pass

    node.results['figure'] = fig
    node.results['figure_fit'] = fig2

    node.save()
