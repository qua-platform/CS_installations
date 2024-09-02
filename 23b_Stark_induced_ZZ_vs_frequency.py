# %%
"""
        RAMSEY CHEVRON (IDLE TIME VS FREQUENCY)
The program consists in playing a Ramsey sequence (x90 - idle_time - x90 - measurement) for different qubit intermediate
frequencies and idle times.
From the results, one can estimate the qubit frequency more precisely than by doing Rabi and also gets a rough estimate
of the qubit coherence time.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.

Next steps before going to the next node:
    - Update the qubit frequency (qubit_IF_q) in the configuration.
"""

from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
# from configuration_opxplus_with_octave import *
from configuration_opxplus_without_octave import *
import matplotlib.pyplot as plt
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import progress_counter
from macros import qua_declaration, multiplexed_readout, active_reset
import math
from qualang_tools.results.data_handler import DataHandler

###################
# The QUA program #
###################

qc = 2 # index of control qubit
qt = 3 # index of target qubit

qc_xy = f"q{qc}_xy"
qt_xy = f"q{qt}_xy"
zz_control = f"zz_control_c{qc}t{qt}"
zz_target = f"zz_target_c{qc}t{qt}"
rrc = f"q{qc}_rr"
rrt = f"q{qt}_rr"

config["waveforms"][f"square_wf_{zz_control}"]["sample"] = 0.1
config["waveforms"][f"square_wf_{zz_target}"]["sample"] = 0.1

n_avg = 10  # The number of averages
t_max = 2_000
t_min = 4
t_step = 4

df_max = 40e6
df_min = -40e6
df_step = 10e6
dfs = np.arange(df_min, df_max, df_step)

freq_detuning = -4 * u.MHz

delta_phase = 4e-9 * freq_detuning * t_step
ts_cycle = np.arange(t_min, t_max, t_step)  # Idle time sweep in clock cycles (Needs to be a list of integers)
ts_ns = 4 * ts_cycle # in clock cylcle = 4ns

qubits = [f"q{i}_xy" for i in [qc, qt]]
resonators = [f"q{i}_rr" for i in [qc, qt]]
qubits_all = list(QUBIT_CONSTANTS.keys())
resonators_all = [key for key in RR_CONSTANTS.keys()]
remaining_resonators = list(set(resonators_all) - set(resonators))
weights = "" # ["", "rotated_", "opt_"] 
reset_method = "wait" # can also be "active"

assert len(qubits_all) == len(resonators_all), "qubits and resonators don't have the same length"
assert len(qubits) == len(resonators), "qubits and resonators under study don't have the same length"
assert all([qb.replace("_xy", "") == rr.replace("_rr", "") for qb, rr in zip(qubits, resonators)]), "qubits and resonators don't correspond"
assert weights in ["", "rotated_", "opt_"], 'weight_type must be one of ["", "rotated_", "opt_"]'
assert reset_method in ["wait", "active"], "Invalid reset_method, use either wait or active"
assert len(resonators) == 2, "only control and target qubits & resonators"
assert n_avg <= 10_000, "revise your number of shots"

save_data_dict = {
    "qubits_all": qubits_all,
    "resonators_all": resonators_all,
    "qubits": qubits,
    "resonators": resonators,
    "qc_xy": qc_xy,
    "qt_xy": qt_xy,
    "zz_control": zz_control,
    "zz_target": zz_target,
    "ts_ns": ts_ns,
    "dfs": dfs,
    "n_avg": n_avg,
    "config": config,
}

with program() as prog:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(resonators)
    state = [declare(bool) for _ in range(len(resonators))]
    t = declare(int)  # QUA variable for the idle time
    df = declare(int)
    s = declare(int)
    phase = declare(fixed)

    with for_(n, 0, n < n_avg, n + 1):
        # Save the averaging iteration to get the progress bar
        save(n, n_st)
        
        with for_(*from_array(df, dfs)):
            assign(phase, 0)
            update_frequency(zz_control, df + ZZ_CONTROL_CONSTANTS[zz_control]["IF"])
            update_frequency(zz_target, df + ZZ_TARGET_CONSTANTS[zz_target]["IF"])

            with for_(*from_array(t, ts_cycle)):
                assign(phase, phase + delta_phase)

                with for_(s, 0, s < 2, s + 1): # states 0:g or 1:e

                    with if_(s == 1):
                        play("x180", qc_xy)
                        align(qc_xy, qt_xy)

                    play('x90', qt_xy)
                    align(qt_xy, zz_control, zz_target)
                    play("square", zz_control, duration=t)
                    play("square", zz_target, duration=t)
                    frame_rotation_2pi(phase, qt_xy)
                    align(qt_xy, zz_control, zz_target)
                    play('x90', qt_xy)

                    # Align the elements to measure after having waited a time "tau" after the qubit pulses.
                    align()

                    # Measure the state of the resonators
                    multiplexed_readout(I, I_st, Q, Q_st, None, None, resonators=resonators, weights=weights)

                    reset_frame(qt_xy)

                    # Wait for the qubit to decay to the ground state
                    if reset_method == "wait":
                        wait(qb_reset_time >> 2)
                    elif reset_method == "active":
                        global_state = active_reset(I, None, Q, None, state, None, resonators, qubits, state_to="ground", weights=weights)

    with stream_processing():
        n_st.save("iteration")
        for ind, rr in enumerate(resonators):
            I_st[ind].buffer(2).buffer(len(ts_cycle)).buffer(len(dfs)).average().save(f"I_{rr}")
            Q_st[ind].buffer(2).buffer(len(ts_cycle)).buffer(len(dfs)).average().save(f"Q_{rr}")


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
        simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
        job = qmm.simulate(config, prog, simulation_config)
        job.get_simulated_samples().con1.plot()
        plt.show(block=False)
    else:
        try:
            # Open the quantum machine
            qm = qmm.open_qm(config)
            # Send the QUA program to the OPX, which compiles and executes it
            job = qm.execute(prog)
            fetch_names = ["iteration"]
            for rr in resonators:
                fetch_names.append(f"I_{rr}")
                fetch_names.append(f"Q_{rr}")
            # Tool to easily fetch results from the OPX (results_handle used in it)
            results = fetching_tool(job, fetch_names, mode="live")
            # Prepare the figure for live plotting
            fig, axss = plt.subplots(4, 2, figsize=(8, 10), sharex=True, sharey=True)
            interrupt_on_close(fig, job)
            # Live plotting
            while results.is_processing():
                # Fetch results
                res = results.fetch_all()
                iteration, Ic, Qc, It, Qt = res
                Ic_g, Qc_g, It_g, Qt_g = Ic[..., 0], Qc[..., 0], It[..., 0], Qt[..., 0]
                Ic_e, Qc_e, It_e, Qt_e = Ic[..., 1], Qc[..., 1], It[..., 1], Qt[..., 1]
                Ic_g, Qc_g, It_g, Qt_g = u.demod2volts(Ic_g, READOUT_LEN), u.demod2volts(Qc_g, READOUT_LEN), u.demod2volts(It_g, READOUT_LEN), u.demod2volts(Qt_g, READOUT_LEN)
                Ic_e, Qc_e, It_e, Qt_e = u.demod2volts(Ic_e, READOUT_LEN), u.demod2volts(Qc_e, READOUT_LEN), u.demod2volts(It_e, READOUT_LEN), u.demod2volts(Qt_e, READOUT_LEN)
                Vs = [Ic_g, Qc_g, Ic_e, Qc_e, It_g, Qt_g, It_e, Qt_e]
                Vnames = ["Ic_g", "Qc_g", "Ic_e", "Qc_e", "It_g", "Qt_g", "It_e", "Qt_e"]
                # Progress bar
                progress_counter(iteration, n_avg, start_time=results.start_time)

                # Live plot data
                plt.suptitle("Off-resonant Stark shift - I & Q")
                for ax, V, Vname in zip(axss.T.ravel(), Vs, Vnames):
                    ax.pcolor(ts_ns, dfs, V)
                    ax.set_xlabel("Idle time [ns]")
                    ax.set_ylabel("Drive Frequency")
                    ax.set_title(Vname)
                plt.tight_layout()
                plt.pause(0.1)

            # Save data
            for fname, r in zip(fetch_names, res):
                save_data_dict[fname] = r

            # Fit the data
            from qualang_tools.plot.fitting import Fit
            St_g = It_g + 1j * Qt_g
            St_e = It_e + 1j * Qt_e
            detuning_qt = np.zeros((2, len(dfs)))
            # fit & plot
            for i, (s, St) in enumerate(zip(["g", "e"], [St_g, St_e])):
                for j, amp in enumerate(dfs):
                    try:
                        fig_analysis = plt.figure()
                        fit = Fit()
                        ramsey_fit = fit.ramsey(ts_ns, np.abs(St[j, :]), plot=True)
                        qb_T2 = np.abs(ramsey_fit["T2"][0])
                        detuning_qt[i, j] = ramsey_fit["f"][0] * u.GHz - freq_detuning
                        plt.xlabel("Idle time [ns]")
                        plt.ylabel("abs(I + iQ) [V]")
                        plt.legend((f"qubit detuning = {-detuning_qt[i, j] / u.kHz:.3f} kHz", f"T2* = {qb_T2:.0f} ns"))
                        plt.title(f"Ramsey with off-resonant drive for Qc = {s} at amp = {amp}")
                    except (Exception,):
                        pass
                    finally:
                        save_data_dict.update({f"fig_analysis_target_{i:03d}_qc={s}_amp={amp:4.3f}": fig_analysis})
            
            # Summary
            fig_summary, axs = plt.subplots(2, 1, figsize=(5, 6), sharex=True)
            # conditional qubit detuning
            axs[0].plot(dfs, detuning_qt[0])
            axs[0].plot(dfs, detuning_qt[1])
            axs[0].set_xlabel("Amplitudes scale")
            axs[0].set_ylabel("Freq detuning [Hz]")
            axs[0].set_title("Off-resonant Stark shift")
            axs[0].legend(["Qc=g", "Qc=e"])
            # zz interaction
            axs[1].plot(dfs, detuning_qt[1] - detuning_qt[0], color='m')
            axs[1].set_xlabel("Amplitudes scale")
            axs[1].set_ylabel("Freq detuning [Hz]")
            axs[1].set_title("Stark-induce ZZ interaction")
            plt.tight_layout()
            save_data_dict.update({f"fig_summary": fig_summary})
            save_data_dict.update({"detuning_qt": detuning_qt})

            # Save results
            script_name = Path(__file__).name
            data_handler = DataHandler(root_data_folder=save_dir)
            save_data_dict.update({"fig_live": fig})
            data_handler.additional_files = {script_name: script_name, **default_additional_files}
            data_handler.save_data(data=save_data_dict, name="Stark_induced_ZZ_vs_frequenc")

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            qm.close()
            print("Experiment QM is now closed")
            plt.show(block=True)

# %%
