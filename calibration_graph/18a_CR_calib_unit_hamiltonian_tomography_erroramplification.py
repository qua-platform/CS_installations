# %%
"""
                                 CR_calib_unit_hamiltonian_tomography

    The CR_calib scripts are designed for calibrating cross-resonance (CR) gates involving a system
with a control qubit and a target qubit. These scripts help estimate the parameters of a Hamiltonian,
which is represented as:
        H = I ⊗ (a_X X + a_Y Y + a_Z Z) + Z ⊗ (b_I I + b_X X + b_Y Y + b_Z Z)


For the calibration sequences, we employ echoed CR drive.
                                   ____      ____ 
            Control(fC): _________| pi |____| pi |________________
                             ____                     
                 CR(fT): ___|    |_____      _____________________
                                       |____|     _____
             Target(fT): ________________________| QST |__________
                                                         ______
            Readout(fR): _______________________________|  RR  |__

Each sequence, which varies in the duration of the CR drive, ends with state tomography of the target state
(across X, Y, and Z bases). This process is repeated with the control state in both |0> and |1> states.
We fit the two sets of CR duration versus tomography data to a theoretical model,
yielding two sets of three parameters: delta, omega_x, and omega_y.
Using these parameters, we estimate the interaction coefficients of the Hamiltonian.
We consider this method a form of unit Hamiltonian tomography.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.

Next steps before going to the next node:
    - This is only to test that you can obtain the data and fit to it successfully.

Reference: Sarah Sheldon, Easwar Magesan, Jerry M. Chow, and Jay M. Gambetta Phys. Rev. A 93, 060302(R) (2016)
"""

# %%
from qualibrate import QualibrationNode, NodeParameters
from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration
from quam_libs.lib.plot_utils import QubitGrid, grid_iter
from quam_libs.lib.save_utils import fetch_results_as_xarray
from quam_libs.lib.fit import peaks_dips
from quam_libs.trackable_object import tracked_updates
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.loops import from_array
from qualang_tools.multi_user import qm_session
from qualang_tools.units import unit
from qm import SimulationConfig
from qm.qua import *
from typing import Literal, Optional, List
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
from quam_libs.macros import (
    qua_declaration,
    multiplexed_readout,
    node_save,
    active_reset,
    readout_state,
)

import sys
import os
sys.path.append(r"C:\Users\tomdv\Documents\OQC_QUAM\CS_installations\calibration_graph")


from cr_hamiltonian_tomography import (
    CRHamiltonianTomographyAnalysis,
    plot_crqst_result_2D,
    PAULI_2Q,
)


# %% {Node_parameters}
class Parameters(NodeParameters):

    qubit_pairs: Optional[List[str]] = ["q3-4"]
    num_averages: int = 200
    min_wait_time_in_ns: int = 20
    max_wait_time_in_ns: int = 500
    wait_time_step_in_ns: int = 12
    cr_type: Literal["direct", "direct+echo", "direct+cancel", "direct+cancel+echo"] = "direct+echo"
    cr_drive_amp: List[float] = [0.0]
    cr_cancel_amp: List[float] = [0.0]
    cr_drive_amp_scaling: List[float] = [1.0]
    cr_cancel_amp_scaling: List[float] = [0.1]
    cr_drive_phase: List[float] = [0.0]  # Or 0.25
    cr_cancel_phase: List[float] = [0.46]
    use_state_discrimination: bool = False
    reset_type_thermal_or_active: Literal["thermal", "active"] = "active"
    simulate: bool = False
    timeout: int = 100


node = QualibrationNode(name="18a_CR_calib_unit_hamiltonian_tomography_erroramplification", parameters=Parameters())


# Class containing tools to help handle units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
machine = QuAM.load()

# Get the relevant QuAM components
if node.parameters.qubit_pairs is None or node.parameters.qubit_pairs == "":
    qubit_pairs = machine.active_qubit_pairs
else:
    qubit_pairs = [machine.qubit_pairs[qp] for qp in node.parameters.qubit_pairs]

num_qubit_pairs = len(qubit_pairs)


# Update the readout power to match the desired range, this change will be reverted at the end of the node.
tracked_qubits = []
# for i, qp in enumerate(qubit_pairs):
#     cr = qp.cross_resonance
#     cr_name = cr.name
#     qt_xy = qp.qubit_target.xy
#     with tracked_updates(cr, auto_revert=False, dont_assign_to_none=True) as cr:
#         cr.operations["square"].amplitude = node.parameters.cr_drive_amp[i]
#         # cr.operations["square"].axis_angle = node.parameters.cr_drive_phase[i] * 360
#         tracked_qubits.append(cr)
#     with tracked_updates(qt_xy, auto_revert=False, dont_assign_to_none=True) as qt_xy:
#         qt_xy.operations[f"{cr_name}_Square"].amplitude = node.parameters.cr_cancel_amp[i]
#         # qt_xy.operations[f"{cr_name}_Square"].axis_angle = node.parameters.cr_cancel_phase[i] * 360
#         tracked_qubits.append(qt_xy)


# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.get_octave_config()
# Open Communication with the QOP
qmm = machine.connect()


# %% {QUA_program}
n_avg = node.parameters.num_averages  # The number of averages
# Dephasing time sweep (in clock cycles = 4ns) - minimum is 4 clock cycles
idle_time_cycles = np.arange(
    16 // 4,
    2*qubit_pairs[0].cross_resonance.operations["square"].length // 4,
    2*qubit_pairs[0].cross_resonance.operations["square"].length // 101 // 4,
)
idle_time_ns = idle_time_cycles * 4

N_pi_vec = np.arange(1, 15, 2).astype("int")
###################
#   QUA Program   #
###################

with program() as cr_calib_unit_ham_tomo:
    n = declare(int)
    n_st = declare_stream()
    state_control = [declare(int) for _ in range(num_qubit_pairs)]
    state_target = [declare(int) for _ in range(num_qubit_pairs)]
    state_st_control = [declare_stream() for _ in range(num_qubit_pairs)]
    state_st_target = [declare_stream() for _ in range(num_qubit_pairs)]
    t = declare(int)
    s = declare(int)  # QUA variable for the control state
    k = declare(int)  # QUA variable for the projection index in QST
    npi = declare(int)  # QUA variable for the projection index in QST

    for i, qp in enumerate(qubit_pairs):
        qc = qp.qubit_control
        qt = qp.qubit_target
        cr = qp.cross_resonance

        with for_(n, 0, n < n_avg, n + 1):
            save(n, n_st)
            with for_(*from_array(npi, N_pi_vec)):
                with for_(*from_array(t, idle_time_cycles)):
                    with for_(s, 0, s < 2, s + 1):  # states
                        with if_(s == 1):
                            qc.xy.play("x180")
                            align(qc.xy.name, qt.xy.name, cr.name)

                        cr.frame_rotation_2pi(0.5)  # To play CR -pi/2
                        with for_(k, 0, k<npi, k+1):
                            # phase shift for cr drive
                            qc.xy.frame_rotation_2pi(0.25)  # Z/2
                            qt.xy.play("x90")  # X/2
                            # direct + cancel
                            align(qc.xy.name, cr.name, qt.xy.name)
                            cr.play("square", duration=t, amplitude_scale=node.parameters.cr_drive_amp_scaling[i])
                            # pi pulse on control
                            align(qc.xy.name, cr.name)
                            qc.xy.play("x180")
                            # echoed direct + cancel
                            align(qc.xy.name, cr.name)
                            cr.play("square", duration=t, amplitude_scale=-node.parameters.cr_drive_amp_scaling[i])
                            # pi pulse on control
                            align(qc.xy.name, cr.name)
                            qc.xy.play("x180")
                            # align for the next step and clear the phase shift
                            align(qc.xy.name, qt.xy.name)
                            # qc.xy.play("-x90")
                            # qc.xy.play("-y90")
                        reset_frame(qc.xy.name)
                        reset_frame(cr.name)


                        align(qt.xy.name, qc.resonator.name, qt.resonator.name)
                        # Measure the state of the resonators
                        readout_state(qc, state_control[i])
                        readout_state(qt, state_target[i])
                        save(state_control[i], state_st_control[i])
                        save(state_target[i], state_st_target[i])

                        # Wait for the qubit to decay to the ground state - Can be replaced by active reset
                        wait(machine.thermalization_time * u.ns)

    with stream_processing():
        n_st.save("n")
        for i in range(num_qubit_pairs):
            state_st_control[i].buffer(2).buffer(len(idle_time_cycles)).buffer(len(N_pi_vec)).average().save(f"state_control{i + 1}")
            state_st_target[i].buffer(2).buffer(len(idle_time_cycles)).buffer(len(N_pi_vec)).average().save(f"state_target{i + 1}")


# %% {Simulate_or_execute}
if node.parameters.simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, cr_calib_unit_ham_tomo, simulation_config)
    job.get_simulated_samples().con1.plot()
    node.results = {"figure": plt.gcf()}
    node.machine = machine
    node.save()

# %% {Data_fetching_and_dataset_creation}
if not node.parameters.simulate:
    qm = qmm.open_qm(config, close_other_machines=True)
    # with qm_session(qmm, config, timeout=node.parameters.timeout) as qm:
    job = qm.execute(cr_calib_unit_ham_tomo)

    results = fetching_tool(job, ["n"], mode="live")
    while results.is_processing():
        # Fetch results
        n = results.fetch_all()[0]
        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)
        
# %% {Data_fetching_and_dataset_creation}
if not node.parameters.simulate:
    # Fetch the data from the OPX and convert it into a xarray with corresponding axes (from most inner to outer loop)
    ds = fetch_results_as_xarray(
        job.result_handles,
        qubit_pairs,
        {"qc_state": ["0", "1"], "times": idle_time_ns, "N": N_pi_vec},
    )
    # Then, add new data variables based on existing ones
    ds = ds.assign(
        bloch_control=-2 * ds["state_control"] + 1,
        bloch_target=-2 * ds["state_target"] + 1,
    )

    for qp in qubit_pairs:
        ds_sliced = ds.sel(qubit=qp.name)
    
        # plotting data
        fig = plt.figure(figsize=(15,10))
        plt.subplot(221)
        ds_sliced.sel(qc_state="0").bloch_target.plot()
        plt.subplot(222)
        ds_sliced.sel(qc_state="1").bloch_target.plot()
        plt.subplot(223)
        # ds.sel(qubit="q3-4", qt_component="Z", qc_state="0").bloch_target.plot.line(hue="N")
        ds_sliced.sel(qc_state="0").bloch_target.sum("N").plot()
        plt.subplot(224)
        # ds.sel(qubit="q3-4", qt_component="Z", qc_state="1").bloch_target.plot.line(hue="N")
        ds_sliced.sel(qc_state="1").bloch_target.sum("N").plot()
        plt.tight_layout()
        plt.show()

        node.results[f"figure_{qp.name}"] = fig

        # Perform CR Hamiltonian tomography
        print("-" * 40)
        print(f"fitting for {qp.name}")
        node.results[f"Best_CR_time_{qp.name}"] = float(ds_sliced.sel(qc_state="1").bloch_target.mean("N").idxmin(dim="times"))

    plt.show(block=False)


# %% {Update_state}
if not node.parameters.simulate:
    with node.record_state_updates():
        # cr_drive_phases = [0.5]
        # cr_cancel_phases = [0.5]
        for i, qp in enumerate(qubit_pairs):
            cr = qp.cross_resonance
            qt = qp.qubit_target
            print(node.results[f"Best_CR_time_{qp.name}"])
            cr.operations["square"].length = int(np.round(node.results[f"Best_CR_time_{qp.name}"]/4)*4)




# %% {Save_results}
if not node.parameters.simulate:
    node.outcomes = {qp.name: "successful" for qp in qubit_pairs}
    node.results["initial_parameters"] = node.parameters.model_dump()
    node.machine = machine
    node.save()


# %%