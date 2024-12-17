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
from cr_hamiltonian_tomography import (
    CRHamiltonianTomographyAnalysis,
    plot_crqst_result_2D,
    PAULI_2Q,
)


# %% {Node_parameters}
class Parameters(NodeParameters):

    qubit_pairs: Optional[List[str]] = ["q3-4"]
    num_averages: int = 100
    min_wait_time_in_ns: int = 16
    max_wait_time_in_ns: int = 2000
    wait_time_step_in_ns: int = 4
    cr_type: Literal["direct", "direct+echo", "direct+cancel", "direct+cancel+echo"] = "direct+echo"
    cr_drive_amp: List[float] = [0.0]
    cr_cancel_amp: List[float] = [0.0]
    cr_drive_amp_scaling: List[float] = [1.0]
    cr_cancel_amp_scaling: List[float] = [0.1]
    cr_drive_phase: List[float] = [0.0]  # Or 0.25
    cr_cancel_phase: List[float] = [0.46]
    use_state_discrimination: bool = False
    reset_type_thermal_or_active: Literal["thermal", "active"] = "thermal"
    simulate: bool = False
    timeout: int = 100


node = QualibrationNode(name="18a_CR_calib_cr_drive_phaseshift", parameters=Parameters())


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
idle_time_ns = np.arange(
    node.parameters.min_wait_time_in_ns,
    node.parameters.max_wait_time_in_ns,
    node.parameters.wait_time_step_in_ns,
) // 4 * 4
idle_time_cycles = idle_time_ns // 4


###################
#   QUA Program   #
###################
phases = np.arange(0.0, 1.01, 0.05)  # ratio relative to 2 * pi
with program() as cr_calib_unit_ham_tomo:
    n = declare(int)
    n_st = declare_stream()
    state_control = [declare(int) for _ in range(num_qubit_pairs)]
    state_target = [declare(int) for _ in range(num_qubit_pairs)]
    state_st_control = [declare_stream() for _ in range(num_qubit_pairs)]
    state_st_target = [declare_stream() for _ in range(num_qubit_pairs)]
    ph = declare(fixed)
    s = declare(int)  # QUA variable for the control state
    c = declare(int)  # QUA variable for the projection index in QST

    for i, qp in enumerate(qubit_pairs):
        qc = qp.qubit_control
        qt = qp.qubit_target
        cr = qp.cross_resonance

        with for_(n, 0, n < n_avg, n + 1):
            save(n, n_st)

            with for_(*from_array(ph, phases)):
                with for_(c, 0, c < 3, c + 1):  # bases
                    with for_(s, 0, s < 2, s + 1):  # states
                        with if_(s == 1):
                            qc.xy.play("x180")
                            align(qc.xy.name, qt.xy.name, cr.name)
                        # Bring Qc to x axis
                        qt.xy.play("y90")
                        align()
                        if node.parameters.cr_type == "direct":
                            # phase shift for cr drive
                            cr.frame_rotation_2pi(node.parameters.cr_drive_phase[i])
                            align(qc.xy.name, cr.name)
                            cr.play("square", amplitude_scale=node.parameters.cr_drive_amp_scaling[i])
                            align(qc.xy.name, cr.name)
                            reset_frame(cr.name)

                        elif node.parameters.cr_type == "direct+echo":
                            # phase shift for cr drive
                            cr.frame_rotation_2pi(node.parameters.cr_drive_phase[i])
                            qt.xy.frame_rotation_2pi(node.parameters.cr_cancel_phase[i])
                            # direct + cancel
                            align(qc.xy.name, cr.name)
                            cr.play("square", amplitude_scale=node.parameters.cr_drive_amp_scaling[i])
                            # pi pulse on control
                            align(qc.xy.name, cr.name)
                            qc.xy.play("x180")
                            # echoed direct + cancel
                            align(qc.xy.name, cr.name)
                            cr.play("square", amplitude_scale=-node.parameters.cr_drive_amp_scaling[i])
                            # pi pulse on control
                            align(qc.xy.name, cr.name)
                            qc.xy.play("x180")
                            # align for the next step and clear the phase shift
                            align(qc.xy.name, qt.xy.name)
                            reset_frame(cr.name)
                            reset_frame(qt.xy.name)

                        elif node.parameters.cr_type == "direct+cancel":
                            # phase shift for cr drive
                            cr.frame_rotation_2pi(node.parameters.cr_drive_phase[i])
                            qt.xy.frame_rotation_2pi(node.parameters.cr_cancel_phase[i])
                            # direct + cancel
                            align(qc.xy.name, qt.xy.name, cr.name)
                            cr.play("square", amplitude_scale=node.parameters.cr_drive_amp_scaling[i])
                            qt.xy.play(f"{cr.name}_Square", amplitude_scale=node.parameters.cr_cancel_amp_scaling[i])
                            # align for the next step and clear the phase shift
                            align(qt.xy.name, cr.name)
                            reset_frame(cr.name)
                            reset_frame(qt.xy.name)

                        elif node.parameters.cr_type == "direct+cancel+echo":
                            # phase shift for cr drive
                            cr.frame_rotation_2pi(node.parameters.cr_drive_phase[i])
                            qt.xy.frame_rotation_2pi(node.parameters.cr_cancel_phase[i])
                            # direct + cancel
                            align(qc.xy.name, qt.xy.name, cr.name)
                            cr.play("square", amplitude_scale=node.parameters.cr_drive_amp_scaling[i])
                            qt.xy.play(f"{cr.name}_Square", amplitude_scale=node.parameters.cr_cancel_amp_scaling[i])
                            # pi pulse on control
                            align(qc.xy.name, qt.xy.name, cr.name)
                            qc.xy.play("x180")
                            # echoed direct + cancel
                            align(qc.xy.name, qt.xy.name, cr.name)
                            cr.play("square", amplitude_scale=-node.parameters.cr_drive_amp_scaling[i])
                            qt.xy.play(f"{cr.name}_Square", amplitude_scale=-node.parameters.cr_cancel_amp_scaling[i])
                            # pi pulse on control
                            align(qc.xy.name, qt.xy.name, cr.name)
                            qc.xy.play("x180")
                            # align for the next step and clear the phase shift
                            align(qc.xy.name, qt.xy.name)
                            reset_frame(cr.name)
                            reset_frame(qt.xy.name)
                        align()
                        # phase shift
                        qc.xy.frame_rotation_2pi(ph)
                        # Bring Qc back to z axis
                        # qt.xy.play("-y90")

                        # QST on Target
                        align(qt.xy.name, cr.name)
                        with switch_(c):
                            with case_(0):  # projection along X
                                qt.xy.play("-y90")
                            with case_(1):  # projection along Y
                                qt.xy.play("x90")
                            with case_(2):  # projection along Z
                                qt.xy.wait(qt.xy.operations["x180"].length * u.ns)

                        align(qt.xy.name, qc.resonator.name, qt.resonator.name)
                        reset_frame(qt.xy.name)
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
            state_st_control[i].buffer(2).buffer(3).buffer(len(phases)).average().save(f"state_control{i + 1}")
            state_st_target[i].buffer(2).buffer(3).buffer(len(phases)).average().save(f"state_target{i + 1}")


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
        {"qc_state": ["0", "1"], "qt_component": ["X", "Y", "Z"], "phases": phases},
    )
    # Then, add new data variables based on existing ones
    ds = ds.assign(
        bloch_control=-2 * ds["state_control"] + 1,
        bloch_target=-2 * ds["state_target"] + 1,
    )

    for qp in qubit_pairs:
        ds_sliced = ds.sel(qubit=qp.name)
    
        # Prepare the figure for live plotting
        fig, axss = plt.subplots(4, 2, figsize=(10, 10))
        # plotting data
        fig = plot_crqst_result_2D(
            ds_sliced.times.data,
            ds_sliced.bloch_control.data,
            ds_sliced.bloch_target.data,
            fig,
            axss,
        )
        plt.tight_layout()
        node.results[f"figure_{qp.name}"] = fig

        # Perform CR Hamiltonian tomography
        print("-" * 40)
        print(f"fitting for {qp.name}")
        crht = CRHamiltonianTomographyAnalysis(
            ts=ds_sliced.times.data,
            data=ds_sliced.bloch_target.data,  # target data: len(cr_drive_phases) x len(t_vec_cycle) x 3 x 2
        )
        try:
            crht.fit_params()
            fig_analysis = crht.plot_fit_result(do_show=False)
            node.results[f"figure_analysis_{qp.name}"] = fig_analysis
        except:
            print(f"-> failed")
            crht.interaction_coeffs_MHz = {p: None for p in PAULI_2Q}
        node.results[f"interaction_coefficients_{qp.name}"] = crht.interaction_coeffs_MHz

    qm.close()
    print("Experiment QM is now closed")
    plt.show(block=False)


# %% {Update_state}
# if not node.parameters.simulate:
#     with node.record_state_updates():
#         cr_drive_amps = [0.1]
#         cr_cancel_amps = [0.1]
#         cr_drive_amp_scalings = [0.5]
#         cr_cancel_amp_scalings = [0.5]
#         cr_drive_phases = [0.5]
#         cr_cancel_phases = [0.5]
#         for i, qp in enumerate(qubit_pairs):
#             cr = qp.cross_resonance
#             qt = qp.qubit_target
#             cr.operations["square"].amplitude = cr_drive_amps[i] * cr_drive_amp_scalings[i]
#             cr.operations["square"].axis_angle = cr_drive_phases[i] * 360
#             qt.xy.operations[f"{cr.name}_Square"].amplitude = cr_cancel_amps[i] * cr_cancel_amp_scalings[i]
#             qt.xy.operations[f"{cr.name}_Square"].axis_angle = cr_cancel_phases[i] * 360


    # Revert the change done at the beginning of the node
    for tracked_qubit in tracked_qubits:
        tracked_qubit.revert_changes()


# %% {Save_results}
if not node.parameters.simulate:
    node.outcomes = {qp.name: "successful" for qp in qubit_pairs}
    node.results["initial_parameters"] = node.parameters.model_dump()
    node.machine = machine
    node.save()


# %%