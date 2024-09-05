# %%
"""
        STARK INDUCED ZZ VS CONTROL AND TARGET AMPLITUDE
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
from qualang_tools.results.data_handler import DataHandler


##################
#   Parameters   #
##################

# Qubits and resonators 
qc = 2 # index of control qubit
qt = 3 # index of target qubit
qubit_to_sweep_amp = qc

# Parameters Definition
n_avg = 10  # The number of averages
t_max = 2_000
t_min = 4
t_step = 4
ts_cycles = np.arange(t_min, t_max, t_step)  # Idle time sweep in clock cycles (Needs to be a list of integers)
drive_phase = 0.25
amps_c = np.arange(0.25, 1.2, 0.25) # scaling factor for amplitude
amps_t = np.arange(0.25, 1.2, 0.25) # scaling factor for amplitude
freq_detuning = -4 * u.MHz

# Readout Parameters
weights = "rotated_" # ["", "rotated_", "opt_"]
reset_method = "wait" # ["wait", "active"]
readout_operation = "readout" # ["readout", "midcircuit_readout"]

# Derived parameters
qc_xy = f"q{qc}_xy"
qt_xy = f"q{qt}_xy"
zz_control = f"zz_control_c{qc}t{qt}"
zz_target = f"zz_target_c{qc}t{qt}"
qubits = [f"q{i}_xy" for i in [qc, qt]]
resonators = [f"q{i}_rr" for i in [qc, qt]]
delta_phase = 4e-9 * freq_detuning * t_step
ts_ns = 4 * ts_cycles # in clock cylcle = 4ns

config["waveforms"][f"square_wf_{zz_control}"]["sample"] = 0.1
config["waveforms"][f"square_wf_{zz_target}"]["sample"] = 0.1
amp_actual_c = config["waveforms"][f"square_wf_{zz_control}"]["sample"]
amp_actual_t = config["waveforms"][f"square_wf_{zz_target}"]["sample"]

# Assertion
assert n_avg <= 10_000, "revise your number of shots"
assert np.all(ts_cycles % 2 == 0) and (ts_cycles.min() >= 4), "ts_cycles should only have even numbers if play echoes"

# Data to save
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
    "amps_c": amps_c,
    "amps_t": amps_t,
    "drive_phase": drive_phase,
    "n_avg": n_avg,
    "config": config,
}


###################
#   QUA Program   #
###################

with program() as prog:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(resonators)
    state = [declare(bool) for _ in range(len(resonators))]
    t = declare(int)  # QUA variable for the idle time
    ac = declare(fixed)
    at = declare(fixed)
    s = declare(int)
    ph = declare(fixed)
    phase = declare(fixed)

    with for_(n, 0, n < n_avg, n + 1):
        # Save the averaging iteration to get the progress bar
        save(n, n_st)
        
        with for_(*from_array(ac, amps_c)):

            with for_(*from_array(at, amps_t)):
                assign(phase, 0)
                reset_frame(zz_target)
                frame_rotation_2pi(drive_phase, zz_target)

                with for_(*from_array(t, ts_cycles)):
                    assign(phase, phase + delta_phase)

                    with for_(s, 0, s < 2, s + 1): # states 0:g or 1:e

                        with if_(s == 1):
                            play("x180", qc_xy)
                            align(qc_xy, qt_xy)

                        play('x90', qt_xy)
                        align(qt_xy, zz_control, zz_target)

                        play("square" * amp(ac), zz_control, duration=t)
                        play("square" * amp(at), zz_target, duration=t)
 
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
            I_st[ind].buffer(2).buffer(len(ts_cycles)).buffer(len(amps_t)).buffer(len(amps_c)).average().save(f"I_{rr}")
            Q_st[ind].buffer(2).buffer(len(ts_cycles)).buffer(len(amps_t)).buffer(len(amps_c)).average().save(f"Q_{rr}")


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
            fig_axss = [plt.subplots(4, 2, figsize=(8, 10)) for _ in amps_c]
            interrupt_on_close(fig_axss[0][0], job)
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
                for i, (ampc, (fig, axss)) in enumerate(zip(amps_c, fig_axss)):
                    fig.suptitle(f"Off-resonant Stark shift at Qc amp scale = {ampc} - I & Q")
                    for ax, V, Vname in zip(axss.T.ravel(), Vs, Vnames):
                        ax.pcolor(ts_ns, amps_t * amp_actual_t, V[i, ...])
                        ax.set_xlabel("Idle time [ns]")
                        ax.set_ylabel("Drive amplitude [V]")
                        ax.set_title(Vname)
                    fig.tight_layout()
                plt.pause(1)

            # Save data
            for fname, r in zip(fetch_names[1:], res[1:]):
                save_data_dict[fname] = r

            for i, (ampc, (fig, axss)) in enumerate(zip(amps_c, fig_axss)):
                save_data_dict.update({f"fig_live_{i:02d}_Qc_amp_scale={ampc:4.3f}": fig})

            # Fit the data
            from qualang_tools.plot.fitting import Fit
            St_g = It_g + 1j * Qt_g
            St_e = It_e + 1j * Qt_e
            detuning_qt = np.zeros((2, len(amps_c), len(amps_t)))
            # fit & plot
            for i, (s, St) in enumerate(zip(["g", "e"], [St_g, St_e])):
                for j, ampc in enumerate(amps_c):
                    for k, ampt in enumerate(amps_t):
                        try:
                            fig_analysis = plt.figure()
                            fit = Fit()
                            ramsey_fit = fit.ramsey(ts_ns, np.abs(St[j, k, :]), plot=True)
                            qb_T2 = np.abs(ramsey_fit["T2"][0])
                            detuning_qt[i, j, k] = ramsey_fit["f"][0] * u.GHz - freq_detuning
                            plt.xlabel("Idle time [ns]")
                            plt.ylabel("abs(I + iQ) [V]")
                            plt.legend((f"qubit detuning = {-detuning_qt[i, j, k] / u.kHz:.3f} kHz", f"T2* = {qb_T2:.0f} ns"))
                            plt.title(f"Ramsey with off-resonant drive and Qc = {s} at amp_c = {ampc * amp_actual_c:5.4f} amp_t = {ampt * amp_actual_t:5.4f}")
                        except (Exception,):
                            pass
                        finally:
                            save_data_dict.update({f"fig_analysis_target_{i:03d}_qc={s}_amp_scale_c={ampc:4.3f}_amp_scale_t={ampt:4.3f}": fig_analysis})
            
            # Summary
            fig_summary, axs = plt.subplots(3, 1, figsize=(5, 9), sharex=True)
            # conditional qubit detuning
            for i, ampc in enumerate(amps_c):
                # Qc = g
                axs[0].plot(amps_t, detuning_qt[0, i])
                # axs[0].set_xlabel("Drive amps_t [2pi rad.]")
                axs[0].set_ylabel("Freq detuning [Hz]")
                axs[0].set_title("Off-resonant Stark shift: Qc=g")
                # axs[0].legend([f"amp scale = {amp:4.3f}" for amp in amps])
                # Qc = e
                axs[1].plot(amps_t, detuning_qt[0, i])
                # axs[1].set_xlabel("Drive amps_t [2pi rad.]")
                axs[1].set_ylabel("Freq detuning [Hz]")
                axs[1].set_title("Off-resonant Stark shift: Qc=e")
                # axs[1].legend([f"amp scale = {amp:4.3f}" for amp in amps])
                # zz interaction
                axs[2].plot(amps_t, detuning_qt[1, i] - detuning_qt[0, i])
                axs[2].set_xlabel("Drive phase [2pi rad.]")
                axs[2].set_ylabel("ZZ interaction [Hz]")
                axs[2].legend([f"qc amp = {ampc * amp_actual_c:5.4f}" for ampc in amps_c])
                axs[2].set_title("Stark-induce ZZ interaction")
            plt.tight_layout()
            save_data_dict.update({f"fig_summary": fig_summary})
            save_data_dict.update({"detuning_qt": detuning_qt})

            # Save results
            script_name = Path(__file__).name
            data_handler = DataHandler(root_data_folder=save_dir)
            data_handler.additional_files = {script_name: script_name, **default_additional_files}
            data_handler.save_data(data=save_data_dict, name="Stark_induced_ZZ_vs_control_and_target_amplitude")

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            qm.close()
            print("Experiment QM is now closed")
            plt.show(block=True)

# %%
