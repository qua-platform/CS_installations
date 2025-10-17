# %% {Imports}
import numpy as np
import xarray as xr
from pathlib import Path
import json

from qm.qua import *
from qm_saas import QmSaas, QOPVersion, ClusterConfig        
from qm import QuantumMachinesManager

from qualang_tools.loops import from_array
from qualang_tools.multi_user import qm_session
from qualang_tools.results import progress_counter
from qualang_tools.units import unit

from qualibrate import QualibrationNode
from quam_config import Quam
from calibration_utils.hello_qua import Parameters
from qualibration_libs.parameters import get_qubits
from qualibration_libs.runtime import simulate_and_plot
from qualibration_libs.data import XarrayDataFetcher


description = """
        Basic script to play with the QUA program and test the QOP connectivity.
"""


node = QualibrationNode[Parameters, Quam](name="00_hello_qua", description=description, parameters=Parameters())


# Any parameters that should change for debugging purposes only should go in here
# These parameters are ignored when run through the GUI or as part of a graph
@node.run_action(skip_if=node.modes.external)
def custom_param(node: QualibrationNode[Parameters, Quam]):
    """Allow the user to locally set the node parameters for debugging purposes, or execution in the Python IDE."""
    # You can get type hinting in your IDE by typing node.parameters.
    # node.parameters.multiplexed = True
    # node.parameters.num_shots = 2
    node.parameters.simulate = True
    node.parameters.use_waveform_report = True
    pass


# Instantiate the QUAM class from the state file
node.machine = Quam.load()



# %% {Create_QUA_program}
@node.run_action(skip_if=node.parameters.load_data_id is not None)
def create_qua_program(node: QualibrationNode[Parameters, Quam]):
    """Create the sweep axes and generate the QUA program from the pulse sequence and the node parameters."""
    # Class containing tools to help handle units and conversions.
    u = unit(coerce_to_integer=True)
    # Get the active qubits from the node and organize them by batches
    node.namespace["qubits"] = qubits = get_qubits(node)

    amps = np.linspace(-1, 1, 3)
    # Register the sweep axes to be added to the dataset when fetching data
    node.namespace["sweep_axes"] = {
        "qubit": xr.DataArray(qubits.get_names()),
        "amplitude": xr.DataArray(amps, attrs={"long_name": "amplitude scale", "units": ""}),
    }
    # node.namespace["sweep"]
    # The QUA program stored in the node namespace to be transfer to the simulation and execution run_actions
    with program() as node.namespace["qua_program"]:
        n = declare(int) 
        n_st = declare_stream() 
        a = declare(fixed)
        
        for multiplexed_qubits in qubits.batch()[:9]:
            align()
            with for_(n, 0, n < 5, n + 1):
                save(n, n_st)
                with for_(*from_array(a, amps)):
                    for i, qubit in multiplexed_qubits.items():
                        #qubit.z.play("const", duration=qubit.xy.operations["x180"].length * u.ns)
                        qubit.xy.play("x180", amplitude_scale=a)
                        qubit.wait(250 * u.ns)
                    align()

        with stream_processing():
            n_st.save("n")



# %% {Simulate}
@node.run_action(skip_if=node.parameters.load_data_id is not None or not node.parameters.simulate)
def simulate_qua_program(node: QualibrationNode[Parameters, Quam]):
    """Connect to the QOP and simulate the QUA program"""
    client = QmSaas(
    host="qm-saas.dev.quantum-machines.co",
    email="benjamin.safvati@quantum-machines.co",
    password="ubq@yvm3RXP1bwb5abv"
)

    cluster_config = ClusterConfig()
    controller = cluster_config.controller()
    controller.lf_fems(1, 2)
    controller.mw_fems(3, 4, 5)

    with client.simulator(QOPVersion("v3_5_0"), cluster_config) as inst:
        # Connect to the QOP
        #qmm = node.machine.connect()
        qmm = QuantumMachinesManager(
        host=inst.host,
        port=inst.port,
        connection_headers=inst.default_connection_headers, log_level="DEBUG"
    )
        # Get the config from the machine
        config = node.machine.generate_config()
        #config = json.loads(Path("qua_config.json").read_text())
        # Simulate the QUA program, generate the waveform report and plot the simulated samples
        samples, fig, wf_report = simulate_and_plot(qmm, config, node.namespace["qua_program"], node.parameters)
        # Store the figure, waveform report and simulated samples
        node.results["simulation"] = {"figure": fig, "wf_report": wf_report, "samples": samples}


# %% {Execute}
@node.run_action(skip_if=node.parameters.load_data_id is not None or node.parameters.simulate)
def execute_qua_program(node: QualibrationNode[Parameters, Quam]):
    """Connect to the QOP, execute the QUA program and fetch the raw data and store it in a xarray dataset called "ds_raw"."""
    # Connect to the QOP
    qmm = node.machine.connect()
    # Get the config from the machine
    config = node.machine.generate_config()
    # Execute the QUA program only if the quantum machine is available (this is to avoid interrupting running jobs).
    with qm_session(qmm, config, timeout=node.parameters.timeout) as qm:
        # The job is stored in the node namespace to be reused in the fetching_data run_action
        node.namespace["job"] = job = qm.execute(node.namespace["qua_program"])
        # Display the progress bar
        data_fetcher = XarrayDataFetcher(job, node.namespace["sweep_axes"])
        for dataset in data_fetcher:
            progress_counter(
                data_fetcher["n"],
                node.parameters.num_shots,
                start_time=data_fetcher.t_start,
            )
        # Display the execution report to expose possible runtime errors
        print(job.execution_report())
    # Register the raw dataset
    node.results["ds_raw"] = dataset


# %% {Save_results}
@node.run_action()
def save_results(node: QualibrationNode[Parameters, Quam]):
    """Save the node results and state."""
    node.save()
