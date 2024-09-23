# %%
"""
        Thermal state preparation

"""
from qualibrate import QualibrationNode, NodeParameters
from typing import Optional, Literal, List


class Parameters(NodeParameters):
    qubits: Optional[List[str]] = 'q2'
    num_runs: int = 400000
    flux_point_joint_or_independent: Literal['joint', 'independent'] = "joint"
    simulate: bool = False

node = QualibrationNode(
    name="thermal_perp",
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
# %%
###################
# The QUA program #
###################
n_runs = node.parameters.num_runs  # Number of runs
flux_point = node.parameters.flux_point_joint_or_independent  # 'independent' or 'joint'

with program() as iq_blobs:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)

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
            wait(machine.thermalization_time * u.ns)

            qubit.align()
            qubit.resonator.measure("readout", qua_vars=(I[i], Q[i]))
            align()
            # save data
            save(I[i], I_st[i])
            save(Q[i], Q_st[i])
            
        align()
            

    with stream_processing():
        n_st.save("n")
        for i in range(num_qubits):
            I_st[i].save_all(f"I{i + 1}")
            Q_st[i].save_all(f"Q{i + 1}")


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
ds = fetch_results_as_xarray(handles, qubits, {"N": np.linspace(1, n_runs, n_runs)})


# Fix the structure of ds to avoid tuples
def extract_value(element):
    if isinstance(element, tuple):
        return element[0]
    return element
ds = xr.apply_ufunc(
    extract_value,
    ds,
    vectorize=True,  # This ensures the function is applied element-wise
    dask='parallelized',  # This allows for parallel processing
    output_dtypes=[float]  # Specify the output data type
)

node.results = {}
node.results['ds'] = ds

# %%
node.results["figs"] = {}
node.results["results"] = {}

popt_final, perr_final, intersection, infidelity, infidelity_error, fit_dataset = find_threshold_with_error(ds.I)
fig = plot_threshold_analysis(ds, popt_final, perr_final, intersection, infidelity, infidelity_error, fit_dataset)
node.results["threshold_analysis"] = fig
node.results["results"]["threshold_analysis"] = {
    "popt_final": popt_final,
    "perr_final": perr_final,
    "intersection": intersection,
    "infidelity": infidelity,
    "infidelity_error": infidelity_error,
}
# %%

# %%
node.results['initial_parameters'] = node.parameters.model_dump()
node.machine = machine
node.save()
# %%

# %%
