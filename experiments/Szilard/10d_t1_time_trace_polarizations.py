# %%
from qualibrate import QualibrationNode, NodeParameters
from typing import Optional, Literal, List


# %% {Node_parameters}
class Parameters(NodeParameters):
    qubits: Optional[List[str]] = ["q2"]
    num_averages: int = 200
    num_time_points: int = 20
    flux_point_joint_or_independent_or_arbitrary: Literal['joint', 'independent', 'arbitrary'] = "joint"
    simulate: bool = False
    timeout: int = 100
    use_state_discrimination: bool = True
    reset_type: Literal['active', 'thermal'] = "thermal"
    polarization_min: int = 1
    polarization_max: int = 1e4
    polarization_number: int = 8

node = QualibrationNode(
    name="10d_t1_time_trace_polarizations",
    parameters=Parameters()
)


from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array, get_equivalent_log_array
from qualang_tools.multi_user import qm_session
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration, multiplexed_readout, node_save, active_reset, readout_state

import matplotlib.pyplot as plt
import numpy as np

import matplotlib
from quam_libs.lib.plot_utils import QubitGrid, grid_iter
from quam_libs.lib.save_utils import fetch_results_as_xarray
from quam_libs.lib.fit import fit_decay_exp, decay_exp
import xarray as xr




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
    qubits = [machine.qubits[q] for q in node.parameters.qubits]
num_qubits = len(qubits)


# %% {QUA_program}
n_avg = node.parameters.num_averages  # The number of averages

polarizations =  np.unique(
    np.geomspace(
        node.parameters.polarization_min, node.parameters.polarization_max, node.parameters.polarization_number
    )
).astype(int)

flux_point = node.parameters.flux_point_joint_or_independent_or_arbitrary  # 'independent' or 'joint'
if flux_point == "arbitrary":
    detunings = {q.name : q.arbitrary_intermediate_frequency for q in qubits}
    arb_flux_bias_offset = {q.name: q.z.arbitrary_offset for q in qubits}
else:
    arb_flux_bias_offset = {q.name: 0.0 for q in qubits}
    detunings = {q.name: 0.0 for q in qubits}

with program() as t1:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)
    t = declare(int)  # QUA variable for the idle time  
    p_num = declare(int)
    
    p = declare(int)
    state_p = declare(int)
    if node.parameters.use_state_discrimination:
        state = [declare(int) for _ in range(num_qubits)]
        state_st = [declare_stream() for _ in range(num_qubits)]
    for i, qubit in enumerate(qubits):

        # Bring the active qubits to the minimum frequency point
        if flux_point == "independent":
            machine.apply_all_flux_to_min()
            qubit.z.to_independent_idle()
        elif flux_point == "joint" or "arbitrary":
            machine.apply_all_flux_to_joint_idle()
        else:
            machine.apply_all_flux_to_zero()

        # Wait for the flux bias to settle
        for qb in qubits:
            wait(1000, qb.z.name)

        align()


        with for_each_(p_num, polarizations):
            with for_(n, 0, n < n_avg, n + 1):
                save(n, n_st)            
                if node.parameters.reset_type == "active":
                    active_reset(qubit)
                else:
                    qubit.resonator.wait(30*qubit.thermalization_time * u.ns)
                    qubit.align()
                    
                with for_(p, 0, p < p_num, p + 1):
                    qubit.resonator.measure("readout", qua_vars=(I[i], Q[i]))
                    qubit.align()
                    qubit.xy.play("x180", condition = (I[i] < qubit.resonator.operations["readout"].threshold))
                    qubit.align()
                    # wait(qubit.resonator.depletion_time // 4, qubit.resonator.name)
                    qubit.align()
                # readout_state(qubit, state_p)
                # qubit.align()
                # qubit.xy.play("x180", condition = (state_p == 0))
                qubit.align()
                wait(qubit.resonator.depletion_time // 4, qubit.resonator.name)
                qubit.align()                                   
                # qubit.align()
                with for_(t, 0, t < node.parameters.num_time_points, t + 1):
                    # Measure the state of the resonators
                    if node.parameters.use_state_discrimination:
                        readout_state(qubit, state[i])
                        save(state[i], state_st[i])
                    else:
                        qubit.resonator.measure("readout", qua_vars=(I[i], Q[i]))
                        wait(qubit.resonator.depletion_time // 4, qubit.resonator.name)
                        save(I[i], I_st[i])
                        save(Q[i], Q_st[i])

        align()

    with stream_processing():
        n_st.save("n")
        for i in range(num_qubits):
            if node.parameters.use_state_discrimination:
                state_st[i].buffer(node.parameters.num_time_points).buffer(n_avg).buffer(len(polarizations)).save(f"state{i + 1}")
            else:
                I_st[i].buffer(node.parameters.num_time_points).buffer(n_avg).buffer(len(polarizations)).save(f"I{i + 1}")
                Q_st[i].buffer(node.parameters.num_time_points).buffer(n_avg).buffer(len(polarizations)).save(f"Q{i + 1}")


# %% {Simulate_or_execute}
if node.parameters.simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, t1, simulation_config)
    job.get_simulated_samples().con1.plot()
    node.results = {"figure": plt.gcf()}
    node.machine = machine
    node.save()

else:
    with qm_session(qmm, config, timeout=node.parameters.timeout) as qm:
        job = qm.execute(t1)
        # Get results from QUA program
        for i in range(num_qubits):
            print(f"Fetching results for qubit {qubits[i].name}")
            data_list = ["n"]
            results = fetching_tool(job, data_list, mode="live")

            while results.is_processing():
            # Fetch results
                fetched_data = results.fetch_all()
                n = fetched_data[0]

                progress_counter(n, n_avg, start_time=results.start_time)


# %%
# %% {Data_fetching_and_dataset_creation}
if not node.parameters.simulate:
    # Fetch the data from the OPX and convert it into a xarray with corresponding axes (from most inner to outer loop)
    ds = fetch_results_as_xarray(job.result_handles, qubits, {"N_meas": np.arange(node.parameters.num_time_points), "N_avg": np.arange(n_avg) , "polarization": polarizations})

    def abs_time(q, time):
        return time *  (q.resonator.operations["readout"].length + q.resonator.depletion_time *1  )

    ds = ds.assign_coords(
        {"idle_time": (["qubit", "N_meas"], np.array([abs_time(q, ds.N_meas) for q in qubits]))}
    )
    

    # # Add attributes to the new coordinate
    # ds.readout_length.attrs = {'long_name': 'Readout pulse length', 'units': 'ns'}
    # ds = ds.assign_coords(
    #     {"freq_full": (["qubit", "freq"], np.array([abs_freq(q, dfs) for q in qubits]))}
    # )

# %% {Data_analysis}


# %% {Plotting}
if not node.parameters.simulate:
    
    # grid = QubitGrid(ds, [q.grid_location for q in qubits])
    # for ax, qubit in grid_iter(grid):
    #     if node.parameters.use_state_discrimination:
    #         ds.assign_coords({"idle_time_us": ds.idle_time/1e3}).sel(qubit = qubit['qubit']).state.plot(ax = ax, x = "idle_time_us", y = "N_avg")
    #         ax.set_ylabel('State')
    #     else:
    #         ds.assign_coords({"idle_time_us": ds.idle_time/1e3}).sel(qubit = qubit['qubit']).I.plot(ax = ax, x = "idle_time_us", y = "N_avg")
    #         ax.set_ylabel('I (V)')
    #     ax.set_title(qubit['qubit'])
    #     ax.set_xlabel('Idle_time (uS)')
    # grid.fig.suptitle('Raw traces')
    # plt.tight_layout()
    # plt.show()
    # node.results['figure_raw'] = grid.fig

    grid = QubitGrid(ds, [q.grid_location for q in qubits])
    for ax, qubit in grid_iter(grid):
        if node.parameters.use_state_discrimination:
            ds.assign_coords({"idle_time_us": ds.idle_time/1e3, "log_polarization": np.log10(ds.polarization)}).sel(qubit = qubit['qubit']).state.mean(dim = "N_avg").plot(ax = ax, x = "idle_time_us", y = "log_polarization")
            ax.set_ylabel('Polarization')
        else:
            ds.assign_coords({"idle_time_us": ds.idle_time/1e3, "log_polarization": np.log10(ds.polarization)}).sel(qubit = qubit['qubit']).I.mean(dim = "N_avg").plot(ax = ax, x = "idle_time_us", y = "log_polarization")
            ax.set_ylabel('Polarization')
        ax.set_title(qubit['qubit'])
        ax.set_xlabel('Idle_time (uS)')
    grid.fig.suptitle('Average of traces')
    plt.tight_layout()
    plt.show()
    node.results['figure_avg'] = grid.fig


    grid = QubitGrid(ds, [q.grid_location for q in qubits])
    for ax, qubit in grid_iter(grid):
        if node.parameters.use_state_discrimination:
            for i in range(len(polarizations)):
                ds.assign_coords({"idle_time_us": ds.idle_time/1e3}).sel(qubit = qubit['qubit']).isel(polarization = i).state.mean(dim = "N_avg").plot(ax = ax, x = "idle_time_us")
            ax.set_ylabel('State')
        else:
            for i in range(len(polarizations)):
                ds.assign_coords({"idle_time_us": ds.idle_time/1e3}).sel(qubit = qubit['qubit']).isel(polarization = i).I.mean(dim = "N_avg").plot(ax = ax, x = "idle_time_us")
            ax.set_ylabel('I (V)')
            ax.axhline(machine.qubits[qubit['qubit']].resonator.operations["readout"].threshold, color = 'k', linestyle = '--')
        ax.set_title(qubit['qubit'])
        ax.set_xlabel('Idle_time (uS)')
    grid.fig.suptitle('Examples of traces')
    plt.tight_layout()
    plt.show()
    node.results['figure_examples'] = grid.fig

# %% {Save_results}
if not node.parameters.simulate:    
    node.results['initial_parameters'] = node.parameters.model_dump()
    node.machine = machine
    node.save()
# %%


# %%
