# %%
"""
                                    Cross-Resonance Time Rabi
The sequence consists two consecutive pulse sequences with the qubit's thermal decay in between.
In the first sequence, we set the control qubit in |g> and play a rectangular cross-resonance pulse to
the target qubit; the cross-resonance pulse has a variable duration. In the second sequence, we initialize the control
qubit in |e> and play the variable duration cross-resonance pulse to the target qubit. Note that in
the second sequence after the cross-resonance pulse we send a x180_c pulse. With it, the target qubit starts
in |g> in both sequences when CR lenght -> zero.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.

Reference: A. D. Corcoles et al., Phys. Rev. A 87, 030301 (2013)

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


##############################
# Program-specific variables #
##############################

qc = 2 # index of control qubit
qt = 3 # index of target qubit

cr_cancel_amp = 0.8 # ratio
cr_cancel_phase = 0.5 # in units of 2pi

qc_xy = f"q{qc}_xy"
qt_xy = f"q{qt}_xy"
cr_drive = f"cr_drive_c{qc}t{qt}"
cr_cancel = f"cr_cancel_c{qc}t{qt}"
qubits = [f"q{i}_xy" for i in [qc, qt]]
resonators = [f"q{i}_rr" for i in [qc, qt]]
qubits_all = list(QUBIT_CONSTANTS.keys())
resonators_all = [key for key in RR_CONSTANTS.keys()]
remaining_resonators = list(set(resonators_all) - set(resonators))
weights = "rotated_" # ["", "rotated_", "opt_"] 
reset_method = "wait" # can also be "active"

n_avg = 100

ts_cycles = np.arange(4, 400, 4) # in clock cylcle = 4ns
ts_ns = 4 * ts_cycles # in clock cylcle = 4ns

assert len(qubits_all) == len(resonators_all), "qubits and resonators don't have the same length"
assert len(qubits) == len(resonators), "qubits and resonators under study don't have the same length"
assert all([qb.replace("_xy", "") == rr.replace("_rr", "") for qb, rr in zip(qubits, resonators)]), "qubits and resonators don't correspond"
assert weights in ["", "rotated_", "opt_"], 'weight_type must be one of ["", "rotated_", "opt_"]'
assert reset_method in ["wait", "active"], "Invalid reset_method, use either wait or active"
assert n_avg <= 10_000, "revise your number of shots"
save_data_dict = {
    "qubits_all": qubits_all,
    "resonators_all": resonators_all,
    "qubits": qubits,
    "resonators": resonators,
    "qc_xy": qc_xy,
    "qt_xy": qt_xy,
    "cr_drive": cr_drive,
    "cr_cancel": cr_cancel,
    "cr_cancel_amp": cr_cancel_amp,
    "cr_cancel_phase": cr_cancel_phase,
    "ts_ns": ts_ns,
    "n_avg": n_avg,
    "config": config,
}


with program() as cr_time_rabi_one_qst:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(resonators)
    state = [declare(bool) for _ in range(len(resonators))]
    state_st = [declare_stream() for _ in range(len(resonators))]
    t = declare(int)
    s = declare(int)  # QUA variable for the control state
    c = declare(int)  # QUA variable for the projection index in QST

    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)
        with for_(*from_array(t, ts_cycles)):
            with for_(c, 0, c < 3, c + 1): # bases 
                with for_(s, 0, s < 2, s + 1): # states
                    with if_(s == 1):
                        play("x180", qc_xy)
                        align(qc_xy, cr_drive)

                    # phase shift for cancel drive
                    frame_rotation_2pi(cr_cancel_phase, cr_cancel)

                    # direct + cancel
                    align(qc_xy, qt_xy, cr_drive, cr_cancel)
                    play("square_positive", cr_drive, duration=t)
                    play("square_positive" * amp(cr_cancel_amp), cr_cancel, duration=t)

                    # pi pulse on control
                    align(qc_xy, cr_drive, cr_cancel)
                    play("x180", qc_xy)

                    # echoed direct + cancel
                    align(qc_xy, cr_drive, cr_cancel)
                    play("square_negative", cr_drive, duration=t)
                    play("square_negative" * amp(cr_cancel_amp), cr_cancel, duration=t)

                    # pi pulse on control
                    align(qc_xy, cr_drive, cr_cancel)
                    play("x180", qc_xy)

                    # QST on Target
                    align(qc_xy, qt_xy)
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

                    # reset phase shift for cancel drive
                    reset_frame(cr_cancel)

                    # Wait for the qubit to decay to the ground state - Can be replaced by active reset
                    if reset_method == "wait":
                        wait(qb_reset_time >> 2)
                    elif reset_method == "active":
                        global_state = active_reset(I, None, Q, None, state, None, resonators, qubits, state_to="ground", weights=weights)

    with stream_processing():
        n_st.save("iteration")
        for ind, rr in enumerate(resonators):
            I_st[ind].buffer(2).buffer(3).buffer(len(ts_cycles)).average().save(f"I_{rr}")
            Q_st[ind].buffer(2).buffer(3).buffer(len(ts_cycles)).average().save(f"Q_{rr}")
            state_st[ind].boolean_to_int().buffer(2).buffer(3).buffer(len(ts_cycles)).average().save(f"state_{rr}")


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
        job = qmm.simulate(config, cr_time_rabi_one_qst, simulation_config)
        job.get_simulated_samples().con1.plot(analog_ports=['1', '2', '3', '4', '5', '6'])
        plt.show()

    else:
        try:
            # Open the quantum machine
            qm = qmm.open_qm(config)
            # Send the QUA program to the OPX, which compiles and executes it
            job = qm.execute(cr_time_rabi_one_qst)
            # Prepare the figure for live plotting
            fig, axss = plt.subplots(3, 2, figsize=(8, 8), sharex=True)
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
                    save_data_dict[f"I_{rr}"] = res[3*ind + 1]
                    save_data_dict[f"Q_{rr}"] = res[3*ind + 2]
                    save_data_dict[f"state_{rr}"] = res[3*ind + 3]
                iterations, I1, Q1, state1, I2, Q2, state2 = res

                # Progress bar
                progress_counter(iterations, n_avg, start_time=results.start_time)
                # calculate the elapsed time
                elapsed_time = time.time() - start_time
                # Convert the results into Volts
                I1, Q1 = u.demod2volts(I1, READOUT_LEN), u.demod2volts(Q1, READOUT_LEN)
                I2, Q2 = u.demod2volts(I2, READOUT_LEN), u.demod2volts(Q2, READOUT_LEN)
                # Plots
                plt.suptitle("echo CR Time Rabi")
                for i, (axs, bss) in enumerate(zip(axss, ["X", "y", "z"])):
                    for ax, q in zip(axs, ["c", "t"]):
                        I = I1 if q == "c" else I2
                        ax.cla()
                        for j, st in enumerate(["0", "1"]):
                            ax.plot(ts_ns, I[:, i, j], label=[f"|{st}>"])
                        ax.legend(["0", "1"])
                        ax.set_title(f"Q_{q}") if i == 0 else None
                        ax.set_xlabel("cr durations [ns]") if i == 2 else None
                        ax.set_ylabel(f"I quadrature of <{bss}> [V]") if q == "c" else None
                plt.tight_layout()
                plt.pause(0.1)

            # Save results
            script_name = Path(__file__).name
            data_handler = DataHandler(root_data_folder=save_dir)
            data_handler.additional_files = {script_name: script_name, **default_additional_files}
            data_handler.save_data(data=save_data_dict, name="cr_echo_time_rabi")

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            qm.close()
            print("Experiment QM is now closed")
            plt.show(block=True)

# %%
