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
is_flipped = False

qc_xy = f"q{qc}_xy"
qt_xy = f"q{qt}_xy"
zz_control = f"zz_control_c{qc}t{qt}"
zz_target = f"zz_target_c{qc}t{qt}"
rrc = f"q{qc}_rr"
rrt = f"q{qt}_rr"
ramsey_control = qt_xy if is_flipped else qc_xy
ramsey_target = qc_xy if is_flipped else qt_xy

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

phases = np.arange(0, 2, 0.25)
drive_phase = 0.25
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
    "phases": phases,
    "dfs": dfs,
    "drive_phase": drive_phase,
    "n_avg": n_avg,
    "config": config,
}

with program() as prog:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(resonators)
    state = [declare(bool) for _ in range(len(resonators))]
    state_st = [declare_stream() for _ in range(len(resonators))]
    t = declare(int)  # QUA variable for the idle time
    s = declare(int) # 0:s, 1:e for control state
    ph = declare(fixed)

    with for_(n, 0, n < n_avg, n + 1):
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

        # Phase shift for zz target
        reset_frame(zz_target)
        frame_rotation_2pi(drive_phase, zz_target)

        with for_(*from_array(ph, phases)):

            with for_(s, 0, s < 2, s + 1): # states

                # Bring Qc to x axis
                play("y90", ramsey_control)

                # Prepare Qt to |1>
                with if_(s == 1):
                    play("x180", ramsey_target)

                align()
                play("square", zz_control)
                play("square", zz_target)
                align()

                frame_rotation(ph, ramsey_control)

                # Bring Qc back to z axis                
                play("-y90", ramsey_control)

                # Align the elements to measure after having waited a time "tau" after the qubit pulses.
                align()

                # Measure the state of the resonators
                multiplexed_readout(I, I_st, Q, Q_st, state, state_st, resonators=resonators, weights=weights)

                # Wait for the qubit to decay to the ground state
                if reset_method == "wait":
                    wait(qb_reset_time >> 2)
                elif reset_method == "active":
                    global_state = active_reset(I, None, Q, None, state, None, resonators, qubits, state_to="ground", weights=weights)

                reset_frame(ramsey_control)

    with stream_processing():
        n_st.save("iteration")
        for ind, rr in enumerate(resonators):
            I_st[ind].buffer(2).buffer(len(phases)).average().save(f"I_{rr}")
            Q_st[ind].buffer(2).buffer(len(phases)).average().save(f"Q_{rr}")
            state_st[ind].boolean_to_int().buffer(2).buffer(len(phases)).average().save(f"state_{rr}")


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
            fig, axss = plt.subplots(3, 2, figsize=(8, 8))
            interrupt_on_close(fig, job)
            # Live plotting
            while results.is_processing():
                # Fetch results
                res = results.fetch_all()
                iteration, Ic, Qc, Sc, It, Qt, St = res
                Ic, Qc, It, Qt = u.demod2volts(Ic, READOUT_LEN), u.demod2volts(Qc, READOUT_LEN), u.demod2volts(It, READOUT_LEN), u.demod2volts(Qt, READOUT_LEN),
                Vnames = ["Ic", "Qc", "Sc", "It", "Qt", "St"]

                # Progress bar
                progress_counter(iteration, n_avg, start_time=results.start_time)

                # Live plot data
                fig.suptitle(f"Local phase calibration for {ramsey_control}")
                for ax, Vname, V, fname in zip(axss.T.ravel(), Vnames, res[1:], fetch_names[1:]):
                    ax.plot(phases, V[..., 0], color="b", label=[f"{ramsey_target} = |0>"])
                    ax.plot(phases, V[..., 1], color="r", label=[f"{ramsey_target} = |1>"])
                    ax.set_xlabel("Phase [2pi rad.]")
                    ax.set_ylabel(Vname)
                    ax.set_title(fname)
                fig.tight_layout()
                plt.pause(1)

            # Save data
            save_data_dict.update({"fig_live": fig})
            for fname, r in zip(fetch_names[1:], res[1:]):
                save_data_dict[fname] = r

            # Save results
            script_name = Path(__file__).name
            data_handler = DataHandler(root_data_folder=save_dir)
            data_handler.additional_files = {script_name: script_name, **default_additional_files}
            data_handler.save_data(data=save_data_dict, name="cz_local_phase_calibration")

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            qm.close()
            print("Experiment QM is now closed")
            plt.show(block=True)

# %%
