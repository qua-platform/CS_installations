# %%
"""
                                 CR_calib_cancel_drive_amplitude

The CR_calib scripts are designed for calibrating cross-resonance (CR) gates involving a system
with a control qubit and a target qubit. These scripts help estimate the parameters of a Hamiltonian,
which is represented as:
    H = I ⊗ (a_X X + a_Y Y + a_Z Z) + Z ⊗ (b_X X + b_Y Y + b_Z Z)

For the calibration sequences, we employ echoed CR drive.
                                   ____      ____ 
            Control(fC): _________| pi |____| pi |________________
                             ____                     
                 CR(fT): ___| CR |_____      _____________________
                                       |____|     _____
             Target(fT): ________________________| QST |__________
                                                         ______
            Readout(fR): _____________________ _________|  RR  |__

This script is to calibrate the phase of CR cancellation drive.
CR cancellation pulse is applied to the target qubit at the target qubit frequency.
Each sequence, which varies in the duration of the CR drive and the phase of CR cancel drive,
ends with state tomography of the target state (across X, Y, and Z bases).
This process is repeated with the control state in both |0> and |1> states.
We fit the two sets of CR duration versus tomography data to a theoretical model,
yielding two sets of three parameters: delta, omega_x, and omega_y.
Using these parameters, we estimate the interaction coefficients of the Hamiltonian.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.

Next steps before going to the next node:
    - Find the amplitude where a_X (coeff of I_X) and a_Y (coeff of I_Y) is zero simultaneously.
      If the two coeffs do not vanish simultaneously, the value of phi could be wrong.
      Set cr_c1t2_drive_am in the configuration file.
      Set cr_cancel_c1t2_square_positive_amp in the configuration file accordingly.

Reference: Sarah Sheldon, Easwar Magesan, Jerry M. Chow, and Jay M. Gambetta Phys. Rev. A 93, 060302(R) (2016)
"""

from qm.qua import *
from qm import QuantumMachinesManager
# from configuration_opxplus_with_octave import *
from configuration_opxplus_without_octave import *
import matplotlib.pyplot as plt
from qm import SimulationConfig
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import progress_counter
from macros import qua_declaration, multiplexed_readout, active_reset
from qualang_tools.results.data_handler import DataHandler
import time
import warnings
import matplotlib
from macros import qua_declaration, multiplexed_readout
from cr_hamiltonian_tomography import (
    CRHamiltonianTomographyAnalysis, plot_cr_duration_vs_scan_param, 
    plot_interaction_coeffs, plot_crqst_result_3D,
)


##############################
# Program-specific variables #
##############################

qc = 2 # index of control qubit
qt = 3 # index of target qubit

cr_type = "direct+cancel+echo" # "direct+cancel", "direct+cancel+echo"

cr_cancel_amp = 0.2 # ratio
cr_cancel_phase = 0.5 # in units of 2pi

qc_xy = f"q{qc}_xy"
qt_xy = f"q{qt}_xy"
cr_drive = f"cr_drive_c{qc}t{qt}"
cr_cancel = f"cr_cancel_c{qc}t{qt}"
rrc = f"q{qc}_rr"
rrt = f"q{qt}_rr"

qubits = [f"q{i}_xy" for i in [qc, qt]]
resonators = [f"q{i}_rr" for i in [qc, qt]]
qubits_all = list(QUBIT_CONSTANTS.keys())
resonators_all = [key for key in RR_CONSTANTS.keys()]
remaining_resonators = list(set(resonators_all) - set(resonators))
weights = "rotated_" # ["", "rotated_", "opt_"] 
reset_method = "wait" # can also be "active"

n_avg = 3

ts_cycle = np.arange(8, 100, 32) # in clock cylcle = 4ns
ts_ns = 4 * ts_cycle # in clock cylcle = 4ns
amps = np.arange(0.05, 1.95, 0.5) # scaling factor for amplitude
cr_drive_phase = 0.0
cr_cancel_phase = 0.0

assert len(qubits_all) == len(resonators_all), "qubits and resonators don't have the same length"
assert len(qubits) == len(resonators), "qubits and resonators under study don't have the same length"
assert all([qb.replace("_xy", "") == rr.replace("_rr", "") for qb, rr in zip(qubits, resonators)]), "qubits and resonators don't correspond"
assert weights in ["", "rotated_", "opt_"], 'weight_type must be one of ["", "rotated_", "opt_"]'
assert reset_method in ["wait", "active"], "Invalid reset_method, use either wait or active"
assert n_avg <= 10_000, "revise your number of shots"
assert np.all(ts_cycle % 2 == 0) and (ts_cycle.min() >= 8), "ts_cycle should only have even numbers if play echoes"

save_data_dict = {
    "qubits_all": qubits_all,
    "resonators_all": resonators_all,
    "qubits": qubits,
    "resonators": resonators,
    "qc_xy": qc_xy,
    "qt_xy": qt_xy,
    "cr_drive": cr_drive,
    "cr_cancel": cr_cancel,
    "cr_cancel_phase": cr_cancel_phase,
    "cr_drive_phase": cr_drive_phase,
    "ts_ns": ts_ns,
    "amps": amps,
    "n_avg": n_avg,
    "config": config,
}


with program() as cr_calib:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(resonators)
    state = [declare(bool) for _ in range(len(resonators))]
    state_st = [declare_stream() for _ in range(len(resonators))]
    t = declare(int)
    t_half = declare(int)
    a = declare(fixed)
    s = declare(int)  # QUA variable for the control state
    c = declare(int)  # QUA variable for the projection index in QST

    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)
        with for_(*from_array(a, amps)):
            with for_(*from_array(t, ts_cycle)):
                with for_(c, 0, c < 3, c + 1): # bases 
                    with for_(s, 0, s < 2, s + 1): # states
                        with if_(s == 1):
                            play("x180", qc_xy)
                            align(qc_xy, cr_drive)

                        if cr_type == "direct+cancel":
                            # phase shift for cancel drive
                            frame_rotation_2pi(cr_drive_phase, cr_drive)
                            frame_rotation_2pi(cr_cancel_phase, cr_cancel)
                            # direct + cancel
                            align(qc_xy, cr_drive, cr_cancel)
                            play("square_positive", cr_drive, duration=t)
                            play("square_positive" * amp(a), cr_cancel, duration=t)
                            # align for the next step and clear the phase shift
                            align(qt_xy, cr_drive, cr_cancel)
                            reset_frame(cr_drive)
                            reset_frame(cr_cancel)

                        elif cr_type == "direct+cancel+echo":
                            # phase shift for cancel drive
                            frame_rotation_2pi(cr_drive_phase, cr_drive)
                            frame_rotation_2pi(cr_cancel_phase, cr_cancel)
                            # direct + cancel
                            align(qc_xy, cr_drive, cr_cancel)
                            play("square_positive", cr_drive, duration=t)
                            play("square_positive" * amp(a), cr_cancel, duration=t)
                            # pi pulse on control
                            align(qc_xy, cr_drive, cr_cancel)
                            play("x180", qc_xy)
                            # echoed direct + cancel
                            align(qc_xy, cr_drive, cr_cancel)
                            play("square_negative", cr_drive, duration=t)
                            play("square_negative" * amp(a), cr_cancel, duration=t)
                            # pi pulse on control
                            align(qc_xy, cr_drive, cr_cancel)
                            play("x180", qc_xy)
                            # align for the next step and clear the phase shift
                            align(qc_xy, qt_xy)
                            reset_frame(cr_drive)
                            reset_frame(cr_cancel)

                        # QST on Target
                        with switch_(c):
                            with case_(0):  # projection along X
                                play("-y90", qt_xy)
                            with case_(1):  # projection along Y
                                play("x90", qt_xy)
                            with case_(2):  # projection along Z
                                wait(PI_LEN * u.ns, qt_xy)

                        align(qt_xy, *resonators)

                        # Measure the state of the resonators
                        multiplexed_readout(I, I_st, Q, Q_st, state, state_st, resonators=resonators, weights=weights)

                        # Wait for the qubit to decay to the ground state - Can be replaced by active reset
                        if reset_method == "wait":
                            wait(qb_reset_time >> 2)
                        elif reset_method == "active":
                            global_state = active_reset(I, None, Q, None, state, None, resonators, qubits, state_to="ground", weights=weights)

    with stream_processing():
        n_st.save("iteration")
        for ind, rr in enumerate(resonators):
            I_st[ind].buffer(2).buffer(3).buffer(len(ts_cycle)).buffer(len(amps)).average().save(f"I_{rr}")
            Q_st[ind].buffer(2).buffer(3).buffer(len(ts_cycle)).buffer(len(amps)).average().save(f"Q_{rr}")
            state_st[ind].boolean_to_int().buffer(2).buffer(3).buffer(len(ts_cycle)).buffer(len(amps)).average().save(f"state_{rr}")        


if __name__ == "__main__":
    #####################################
    #  Open Communication with the QOP  #
    #####################################
    qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

    ###########################
    # Run or Simulate Program #
    ###########################
    simulate = False

    if simulate:
        # Simulates the QUA program for the specified duration
        simulation_config = SimulationConfig(duration=3_000)  # In clock cycles = 4ns
        job = qmm.simulate(config, cr_calib, simulation_config)
        job.get_simulated_samples().con1.plot(analog_ports=['1', '2', '3', '4', '5', '6'])
        plt.show()

    else:
        try:
            # Open the quantum machine
            qm = qmm.open_qm(config)
            # Send the QUA program to the OPX, which compiles and executes it
            job = qm.execute(cr_calib)
            # Prepare the figure for live plotting
            fig, axss = plt.subplots(3, 4, figsize=(12, 9), sharex=True, sharey=True)
            interrupt_on_close(fig, job)
            # Tool to easily fetch results from the OPX (results_handle used in it)
            fetch_names = ["iteration"]
            for rr in resonators:
                fetch_names.append(f"I_{rr}")
                fetch_names.append(f"Q_{rr}")
                fetch_names.append(f"state_{rr}")
            results = fetching_tool(job, fetch_names, mode="live")
            # Live plotting
            while results.is_processing():
                start_time = results.get_start_time()
                # Fetch results
                res = results.fetch_all()
                for ind, rr in enumerate(resonators):
                    save_data_dict[f"I_{rr}"] = u.demod2volts(res[3*ind + 1], READOUT_LEN)
                    save_data_dict[f"Q_{rr}"] = u.demod2volts(res[3*ind + 2], READOUT_LEN)
                    save_data_dict[f"state_{rr}"] = res[3*ind + 3]
                iterations, _, _, state_c, _, _, state_t = res

                # Progress bar
                progress_counter(iterations, n_avg, start_time=results.start_time)
                # calculate the elapsed time
                elapsed_time = time.time() - start_time
                # plotting data
                # control qubit
                plot_cr_duration_vs_scan_param(state_c, state_t, ts_ns, amps, "amplitude", axss)
                plt.tight_layout()
                plt.pause(0.1)

            # Perform CR Hamiltonian tomography
            coeffs = []
            for a in range(len(amps)):
                crht = CRHamiltonianTomographyAnalysis(
                    ts=ts_ns,
                    data=state_t[a, ...], # target data: len(amps) x len(t_vec_cycle) x 3 x 2
                )
                crht.fit_params()
                coeffs.append(crht.interaction_coeffs)

            # Plot the estimated interaction coefficients
            fig_analysis = plot_interaction_coeffs(coeffs, amps, xlabel="cr amplitude")

            # plot 3D
            fig_3d = plot_crqst_result_3D(ts_ns, state_t)
    
            # Save results
            script_name = Path(__file__).name
            data_handler = DataHandler(root_data_folder=save_dir)
            save_data_dict.update({"fig_live": fig})
            data_handler.additional_files = {script_name: script_name, **default_additional_files}
            data_handler.save_data(data=save_data_dict, name="cr_drive_calib_ham_tomo_cancel_vs_amp")

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            qm.close()
            print("Experiment QM is now closed")
            plt.show(block=True)

# %%