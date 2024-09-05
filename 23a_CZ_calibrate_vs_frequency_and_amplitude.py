# %%
"""
        CZ CALIBRATE VS FREQUENCY AND AMPLITUDE
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

df_max = 40e6
df_min = -40e6
df_step = 10e6
dfs = np.arange(df_min, df_max, df_step)

drive_phase = 0.25
amps = np.arange(0.25, 1.2, 0.25) # scaling factor for amplitude
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
    "qubits": qubits,
    "resonators": resonators,
    "qc_xy": qc_xy,
    "qt_xy": qt_xy,
    "zz_control": zz_control,
    "zz_target": zz_target,
    "ts_ns": ts_ns,
    "amps": amps,
    "dfs": dfs,
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
    state_st = [declare_stream() for _ in range(len(resonators))]
    t = declare(int)  # QUA variable for the idle time
    s = declare(int) # 0:s, 1:e for control state
    c = declare(int) # 0:x, 1:y, 2:z for QST on target
    a = declare(fixed)
    df = declare(int)
    phase = declare(fixed)

    with for_(n, 0, n < n_avg, n + 1):
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

        # Phase shift for zz target
        reset_frame(zz_target)
        frame_rotation_2pi(drive_phase, zz_target)

        with for_(*from_array(df, dfs)):
            # Update IF
            update_frequency(zz_control, df + ZZ_CONTROL_CONSTANTS[zz_control]["IF"])
            update_frequency(zz_target, df + ZZ_TARGET_CONSTANTS[zz_target]["IF"])

            with for_(*from_array(a, amps)):
                
                with for_(c, 0, c < 3, c + 1): # bases 

                    with for_(s, 0, s < 2, s + 1): # states
                        
                        with if_(s == 1):
                            play("x180", qc_xy)
                            align(qc_xy, qt_xy)

                        play('x90', qt_xy)
                        align(qt_xy, zz_control, zz_target)
                        play("square", zz_control)
                        play("square", zz_target)
                        align(qt_xy, zz_control, zz_target)

                        with switch_(c):
                            with case_(0):  # projection along X
                                play("-y90", qt_xy)
                            with case_(1):  # projection along Y
                                play("x90", qt_xy)
                            with case_(2):  # projection along Z
                                wait(PI_LEN * u.ns, qt_xy)

                        # Align the elements to measure after having waited a time "tau" after the qubit pulses.
                        align()

                        # Measure the state of the resonators
                        multiplexed_readout(I, I_st, Q, Q_st, state, state_st, resonators=resonators, weights=weights)

                        # Wait for the qubit to decay to the ground state
                        if reset_method == "wait":
                            wait(qb_reset_time >> 2)
                        elif reset_method == "active":
                            global_state = active_reset(I, None, Q, None, state, None, resonators, qubits, state_to="ground", weights=weights)

    with stream_processing():
        n_st.save("iteration")
        for ind, rr in enumerate(resonators):
            I_st[ind].buffer(2).buffer(3).buffer(len(amps)).buffer(len(dfs)).average().save(f"I_{rr}")
            Q_st[ind].buffer(2).buffer(3).buffer(len(amps)).buffer(len(dfs)).average().save(f"Q_{rr}")
            state_st[ind].boolean_to_int().buffer(2).buffer(3).buffer(len(amps)).buffer(len(dfs)).average().save(f"state_{rr}")


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
                fetch_names.append(f"state_{rr}")
            # Tool to easily fetch results from the OPX (results_handle used in it)
            results = fetching_tool(job, fetch_names, mode="live")
            # Prepare the figure for live plotting
            fig_axss = [plt.subplots(6, 2, figsize=(8, 10)) for _ in range(3)] # x, y, z
            interrupt_on_close(fig_axss[0][0], job)
            # Live plotting
            while results.is_processing():
                # Fetch results
                res = results.fetch_all()
                iteration, Ic, Qc, Sc, It, Qt, St, = res
                
                Ic_g, Qc_g, Sc_g, It_g, Qt_g, St_g = Ic[..., 0], Qc[..., 0], Sc[..., 0], It[..., 0], Qt[..., 0], St[..., 0]
                Ic_e, Qc_e, Sc_e, It_e, Qt_e, St_e = Ic[..., 1], Qc[..., 1], Sc[..., 1], It[..., 1], Qt[..., 1], St[..., 1]
                Ic_g, Qc_g, It_g, Qt_g = u.demod2volts(Ic_g, READOUT_LEN), u.demod2volts(Qc_g, READOUT_LEN), u.demod2volts(It_g, READOUT_LEN), u.demod2volts(Qt_g, READOUT_LEN)
                Ic_e, Qc_e, It_e, Qt_e = u.demod2volts(Ic_e, READOUT_LEN), u.demod2volts(Qc_e, READOUT_LEN), u.demod2volts(It_e, READOUT_LEN), u.demod2volts(Qt_e, READOUT_LEN)
                Vs = [Ic_g, Qc_g, Sc_g, Ic_e, Qc_e, Sc_e, It_g, Qt_g, St_g, It_e, Qt_e, St_e]
                Vnames = ["Ic_g", "Qc_g", "Sc_g", "Ic_e", "Qc_e", "Sc_e", "It_g", "Qt_g", "St_g", "It_e", "Qt_e", "St_e"]
                # Progress bar
                progress_counter(iteration, n_avg, start_time=results.start_time)

                # Live plot data
                for i, (tb, (fig, axss)) in enumerate(zip(["x", "y", "z"], fig_axss)):
                    fig.suptitle(f"CZ Gate Calibration at QST for {tb}")
                    for ax, V, Vname in zip(axss.T.ravel(), Vs, Vnames):
                        ax.pcolor(amps, dfs, V[..., i])
                        ax.set_xlabel("Amplitude scale")
                        ax.set_ylabel("Drive phase [2pi rad.]")
                        ax.set_title(Vname)
                    fig.tight_layout()
                plt.pause(1)

            # Save data
            for fname, r in zip(fetch_names[1:], res[1:]):
                save_data_dict[fname] = r

            for i, (amp, (fig, axss)) in enumerate(zip(amps, fig_axss)):
                save_data_dict.update({f"fig_live_{i:02d}_amp={amp:4.3f}": fig})

            # Compute the entanglement measure
            r1 = St[..., 1]
            r0 = St[..., 0]
            R = 0.5 * np.sum((r1 - r0) ** 2, axis=2)

            # Summary
            fig_summary = plt.figure()
            plt.pcolor(amps, dfs, R)
            plt.xlabel("Amplitude scale")
            plt.ylabel("Freq detuning [Hz]")
            plt.title("CZ Gate Calibration")
            plt.colorbar()
            plt.tight_layout()
            save_data_dict.update({f"fig_summary": fig_summary})
            save_data_dict.update({"R": R})

            # Save results
            script_name = Path(__file__).name
            data_handler = DataHandler(root_data_folder=save_dir)
            data_handler.additional_files = {script_name: script_name, **default_additional_files}
            data_handler.save_data(data=save_data_dict, name="cz_frequency_and_amplitude_calibration")

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            qm.close()
            print("Experiment QM is now closed")
            plt.show(block=True)

# %%
