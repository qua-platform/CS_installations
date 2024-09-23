# %%
"""
        Adaptive threshold state preparation

"""
from qualibrate import QualibrationNode, NodeParameters
from typing import Optional, Literal, List


class Parameters(NodeParameters):
    qubits: Optional[List[str]] = 'q2'
    iterations: int = 4
    max_attempts: int = 9
    num_runs: int = 400000
    flux_point_joint_or_independent: Literal['joint', 'independent'] = "joint"
    simulate: bool = False

node = QualibrationNode(
    name="adaptive_threshold_perp",
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

max_attempts_list = np.arange(0, node.parameters.max_attempts,1)
iterations = node.parameters.iterations

# %%
###################
# The QUA program #
###################
n_runs = node.parameters.num_runs  # Number of runs
flux_point = node.parameters.flux_point_joint_or_independent  # 'independent' or 'joint'

def make_program(threshold_list):
    with program() as iq_blobs:
        I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)
        max_attempts = declare(int)
        state = declare(bool)
        iter = declare(int)
        
        for i, qubit in enumerate(qubits):
            threshold_qua = declare(fixed, value=threshold_list[qubit.name])
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
                    wait(machine.thermalization_time * u.ns)
                    qubit.align()
                    qubit.xy.play('x90', amplitude_scale=0.9)
                    with for_(iter, 0, iter < max_attempts, iter + 1):
                        qubit.align()
                        qubit.resonator.measure("readout", qua_vars=(I[i], Q[i]))
                        assign(state, I[i] > threshold_qua[iter])
                        wait(qubit.resonator.depletion_time // 4)
                        qubit.xy.play('x180', condition=state)
                    # save data
                    qubit.resonator.measure("readout", qua_vars=(I[i], Q[i]))
                    wait(qubit.resonator.depletion_time // 4)
                    save(I[i], I_st[i])
                    save(Q[i], Q_st[i])
                    
            align()
                

        with stream_processing():
            n_st.save("n")
            for i in range(num_qubits):
                I_st[i].buffer(len(max_attempts_list)).buffer(n_runs).save_all(f"I{i + 1}")
                Q_st[i].buffer(len(max_attempts_list)).buffer(n_runs).save_all(f"Q{i + 1}")

    return iq_blobs

# %%
threshold_list = { qubit.name : [qubit.resonator.operations['readout'].threshold]*len(max_attempts_list) for qubit in qubits }
all_thresholds = [threshold_list]
all_fidelities = []
all_fidelities_error = []

qm = qmm.open_qm(config)

node.results = {}
node.results['results'] = {}
    
for iteration in range(iterations):
    print(f"Iteration {iteration}")
    print("********************")
    print("********************")
    print(" ")
    job = qm.execute(make_program(threshold_list), flags=['auto-element-thread'])
    for i in range(num_qubits):
        print(f"Fetching results for qubit {qubits[i].name}")
        data_list = ['n']
        results = fetching_tool(job, data_list, mode="live")
        while results.is_processing():
            fetched_data = results.fetch_all()
            n = fetched_data[0]
            progress_counter(n, n_runs, start_time=results.start_time)
            
    handles = job.result_handles
    Is = []
    Qs = []
    for i in range(num_qubits):
        Is.append(handles.get(f"I{i + 1}").fetch_all()[0][0])
        Qs.append(handles.get(f"Q{i + 1}").fetch_all()[0][0])
    ds = xr.Dataset({
        "I": (["qubit", "n", "max_attempts"], Is),
        "Q": (["qubit", "n", "max_attempts"], Qs),
    }, coords={
        "qubit": range(num_qubits),
        "n": range(n_runs),
        "max_attempts": range(len(max_attempts_list))
    })



    init_fidelities = []
    init_fidelities_error = []
    threshold_list = {qubit.name : [] for qubit in qubits}
    if iteration == 0:
        popt0 =  find_threshold_with_error(ds.I.sel(max_attempts = 0))[0]
    
    qubit = qubits[0]
    
    for i in range(len(max_attempts_list)):
        print(f"Max attempts: {max_attempts_list[i]}")
        popt_final, perr_final, intersection, infidelity, infidelity_error, fit_dataset = find_threshold_with_error_and_guess_fixed(ds.I.sel(max_attempts = i), popt0)
        threshold_list[qubit.name].append(intersection)
        fig = plot_threshold_analysis(ds.sel(max_attempts = i), popt_final, perr_final, intersection, infidelity, infidelity_error, fit_dataset)
        plt.show()
        node.results[f"threshold_analysis_iter{iteration}_max_attempts{i}"] = fig
        node.results[f"results"]["threshold_analysis_iter{iteration}_max_attempts{i}"] = {
            "popt_final": popt_final,
            "perr_final": perr_final,
            "intersection": intersection,
            "infidelity": infidelity,
            "infidelity_error": infidelity_error,
            "fit_dataset": fit_dataset,
        }
        init_fidelities.append(infidelity)
        init_fidelities_error.append(infidelity_error)

    all_thresholds.append(threshold_list)
    all_fidelities.append(init_fidelities)
    all_fidelities_error.append(init_fidelities_error)

    if iteration == 0:
        all_I = ds.I
        all_Q = ds.Q
    else:
        all_I = xr.concat([all_I, ds.I], dim="iteration")
        all_Q = xr.concat([all_Q, ds.Q], dim="iteration")

    print("********************")
    print("********************")
    
qm.close()
# %%
node.results['I'] = xr.Dataset({'I': all_I})
node.results['Q'] = xr.Dataset({'Q': all_Q})
node.results['all_fidelities'] = all_fidelities
node.results['all_fidelities_error'] = all_fidelities_error
node.results['used_thresholds'] = all_thresholds


# %%

f,ax = plt.subplots()
for i in range(len(all_fidelities)):
    ax.errorbar(max_attempts_list[1:], 1-np.array(all_fidelities)[i][1:], yerr=np.array(all_fidelities_error)[i][1:], fmt='o-', capsize=5, label=f"Iteration {i}")
ax.set_xlabel("Max Attempts")
ax.set_ylabel("Fidelity")
ax.set_title("Fidelity vs Max Attempts")
plt.show()
node.results[f"fidelity_vs_max_attempts"] = f

# %%
f,ax = plt.subplots()
for i in range(len(all_thresholds)):
    ax.plot(max_attempts_list, all_thresholds[i][qubit.name],'.')
ax.set_xlabel("Max Attempts")
ax.set_ylabel("Threshold")
ax.set_title("Threshold vs Max Attempts")
plt.show()
node.results[f"threshold_vs_max_attempts"] = f
# %%
node.results['initial_parameters'] = node.parameters.model_dump()
node.machine = machine
node.save()
# %%
