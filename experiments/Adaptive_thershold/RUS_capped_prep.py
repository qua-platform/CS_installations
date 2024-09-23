# %%
"""
        Repeat until success state preparation

"""
from qualibrate import QualibrationNode, NodeParameters
from typing import Optional, Literal, List


class Parameters(NodeParameters):
    qubits: Optional[List[str]] = 'q2'
    num_runs: int = 400000
    flux_point_joint_or_independent: Literal['joint', 'independent'] = "joint"
    simulate: bool = False

node = QualibrationNode(
    name="RUS_capped_prep",
    parameters_class=Parameters
)

node.parameters = Parameters()


from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.analysis.discriminator import two_state_discriminator
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration, multiplexed_readout, active_reset

import matplotlib.pyplot as plt
import numpy as np

import matplotlib
from quam_libs.lib.plot_utils import QubitGrid, grid_iter
from quam_libs.lib.save_utils import fetch_results_as_xarray
import xarray as xr

# matplotlib.use("TKAgg")
# %%
# Reload the adaptive threshold functions
from importlib import reload
import experiments.Adaptive_thershold.adaptive_threshold_function as atf
reload(atf)
from experiments.Adaptive_thershold.adaptive_threshold_function import *

# %%

###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Class containing tools to help handling units and conversions.
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

max_attempts_list = np.arange(0, 10,1)
# %%
###################
# The QUA program #
###################
n_runs = node.parameters.num_runs  # Number of runs
flux_point = node.parameters.flux_point_joint_or_independent  # 'independent' or 'joint'

with program() as iq_blobs:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)
    attempts = [declare(int) for _ in range(num_qubits)]
    attempts_st = [declare_stream() for _ in range(num_qubits)]
    max_attempts = declare(int)
    state = declare(bool)
    
    for i, qubit in enumerate(qubits):

        # Bring the active qubits to the minimum frequency point
        if flux_point == "independent":
            machine.apply_all_flux_to_min()
            qubit.z.to_independent_idle()
        elif flux_point == "joint":
            machine.apply_all_flux_to_joint_idle()
        else:
            machine.apply_all_flux_to_zero()
            
        for qb in qubits:
            wait(1000, qb.z.name)
        
        align()
        
        with for_(n, 0, n < n_runs, n + 1):
            # ground iq blobs for all qubits
            save(n, n_st)
            with for_(*from_array(max_attempts, max_attempts_list)):
                assign(attempts[i], 1)
                qubit.align()
                qubit.xy.play('x90', amplitude_scale=0.9)
                qubit.resonator.measure("readout", qua_vars=(I[i], Q[i]))
                assign(state, I[i] > qubit.resonator.operations['readout'].threshold)
                wait(qubit.resonator.depletion_time // 4)
                # qubit.xy.play('x180', condition=state)
                qubit.align()
                with while_((I[i] > qubit.resonator.operations['readout'].rus_exit_threshold)&(attempts[i] <= max_attempts)):
                    qubit.align()
                    qubit.resonator.measure("readout", qua_vars=(I[i], Q[i]))
                    assign(state, I[i] > qubit.resonator.operations['readout'].threshold)
                    wait(qubit.resonator.depletion_time // 4)
                    qubit.xy.play('x180', condition=state)
                    qubit.align()
                    assign(attempts[i], attempts[i] + 1)                
                with while_(attempts[i] <= max_attempts):
                    qubit.align()
                    wait(qubit.resonator.operations['readout'].length // 4)
                    wait(qubit.resonator.depletion_time // 4)
                    qubit.align()
                    assign(attempts[i], attempts[i] + 1)                                     
                qubit.resonator.measure("readout", qua_vars=(I[i], Q[i]))
                wait(qubit.resonator.depletion_time // 4)
                # save data
                save(I[i], I_st[i])
                save(Q[i], Q_st[i])
                save(attempts[i], attempts_st[i])
                
        align()
            

    with stream_processing():
        n_st.save("n")
        for i in range(num_qubits):
            I_st[i].buffer(len(max_attempts_list)).buffer(n_runs).save_all(f"I{i + 1}")
            Q_st[i].buffer(len(max_attempts_list)).buffer(n_runs).save_all(f"Q{i + 1}")
            attempts_st[i].buffer(len(max_attempts_list)).buffer(n_runs).save_all(f"attempts{i + 1}")


###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, iq_blobs, simulation_config)
    job.get_simulated_samples().con1.plot()
    node.results = {"figure": plt.gcf()}
    node.machine = machine
    node.save()
    quit()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Calibrate the active qubits
    # machine.calibrate_octave_ports(qm)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(iq_blobs, flags=['auto-element-thread'])

    for i in range(num_qubits):
        print(f"Fetching results for qubit {qubits[i].name}")
        data_list = ['n']
        results = fetching_tool(job, data_list, mode="live")
        while results.is_processing():
            fetched_data = results.fetch_all()
            n = fetched_data[0]
            progress_counter(n, n_runs, start_time=results.start_time)
    qm.close()

    # node_save(machine, "iq_blobs", data, additional_files=True)

# %%
handles = job.result_handles

Is = []
Qs = []
attempts = []

for i in range(num_qubits):
    Is.append(handles.get(f"I{i + 1}").fetch_all()[0][0])
    Qs.append(handles.get(f"Q{i + 1}").fetch_all()[0][0])
    attempts.append(handles.get(f"attempts{i + 1}").fetch_all()[0][0])

ds = xr.Dataset({
    "I": (["qubit", "n", "max_attempts"], Is),
    "Q": (["qubit", "n", "max_attempts"], Qs),
    "attempts": (["qubit", "n", "max_attempts"], attempts),
}, coords={
    "qubit": range(num_qubits),
    "n": range(n_runs),
    "max_attempts": range(len(max_attempts_list))
})
# %%
node.results = {}
node.results['ds'] = ds

init_fidelities = []
init_fidelities_error = []
all_figs = []
node.results['results'] = {}

popt0 =  find_threshold_with_error(ds.I.sel(max_attempts = 0))[0]

for i in range(len(max_attempts_list)):
    popt_final, perr_final, intersection, infidelity, infidelity_error, fit_dataset = find_threshold_with_error_and_guess_fixed(ds.I.sel(max_attempts = i), popt0)
    fig = plot_threshold_analysis(ds.sel(max_attempts = i), popt_final, perr_final, intersection, infidelity, infidelity_error, fit_dataset)
    plt.show()
    node.results[f"threshold_analysis_{i}"] = fig
    node.results[f"results"]["threshold_analysis_{i}"] = {
        "popt_final": popt_final,
        "perr_final": perr_final,
        "intersection": intersection,
        "infidelity": infidelity,
        "infidelity_error": infidelity_error,
        "fit_dataset": fit_dataset,
    }
    init_fidelities.append(infidelity)
    init_fidelities_error.append(infidelity_error)

# %%

f,ax = plt.subplots()
ax.errorbar(max_attempts_list[1:], 1-np.array(init_fidelities)[1:], yerr=np.array(init_fidelities_error)[1:], fmt='o-', capsize=5)
ax.set_xlabel("Max Attempts")
ax.set_ylabel("Fidelity")
ax.set_title("Fidelity vs Max Attempts")
plt.show()
node.results[f"fidelity_vs_max_attempts"] = f
# %%
node.results['initial_parameters'] = node.parameters.model_dump()
node.machine = machine
node.save()
# %%

# %%
