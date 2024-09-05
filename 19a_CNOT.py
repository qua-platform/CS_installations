# %%
"""
                                 CNOT

Prerequisites:
    - 

Next steps before going to the next node:
    - 

Reference: Sarah Sheldon, Easwar Magesan, Jerry M. Chow, and Jay M. Gambetta Phys. Rev. A 93, 060302(R) (2016)
"""

from qm.qua import *
from qm import QuantumMachinesManager
from configuration_mw_fem import *
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


##################
#   Parameters   #
##################

# Qubits and resonators 
qc = 2 # index of control qubit
qt = 3 # index of target qubit

# Parameters Definition
n_avg = 100
cr_type = "direct+cancel+echo" # "direct+cancel", "direct+cancel+echo"
cr_drive_amp = 1.0
cr_drive_phase = 0.25
cr_cancel_amp = 0.2 # ratio
cr_cancel_phase = 0.5 # in units of 2pi
ts_cycles = np.arange(4, 400, 4) # in clock cylcle = 4ns

# Readout Parameters
weights = "rotated_" # ["", "rotated_", "opt_"]
reset_method = "wait" # ["wait", "active"]
readout_operation = "readout" # ["readout", "midcircuit_readout"]

# Derived parameters
qc_xy = f"q{qc}_xy"
qt_xy = f"q{qt}_xy"
cr_drive = f"cr_drive_c{qc}t{qt}"
cr_cancel = f"cr_cancel_c{qc}t{qt}"
qubits = [f"q{i}_xy" for i in [qc, qt]]
resonators = [f"q{i}_rr" for i in [qc, qt]]
ts_ns = 4 * ts_cycles # in clock cylcle = 4ns

# Assertion
assert n_avg <= 10_000, "revise your number of shots"
assert np.all(ts_cycles % 2 == 0) and (ts_cycles.min() >= 4), "ts_cycles should only have even numbers if play echoes"

# Data to save
save_data_dict = {
    "qubits": qubits,
    "resonators": resonators,
    "qc_xy": qc_xy,
    "qt_xy": qt_xy,
    "cr_drive": cr_drive,
    "cr_cancel": cr_cancel,
    "cr_cancel_phase": cr_cancel_phase,
    "cr_drive_phase": cr_drive_phase,
    "ts_ns": ts_ns,
    "n_avg": n_avg,
    "config": config,
}


###################
#   QUA Program   #
###################

with program() as PROGRAM:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(resonators)
    state = [declare(bool) for _ in range(len(resonators))]
    state_st = [declare_stream() for _ in range(len(resonators))]
    st_c = declare(int)
    st_t = declare(int)
    
    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)
        # to allow time to save the data
        wait(1000 * u.ns)
        with for_(st_c, 0, st_c < 2, st_c + 1):
            with for_(st_t, 0, st_t < 2, st_t + 1):
                # Prepare control state in 1
                with if_(st_c == 1):
                    play("x180", qc_xy)
                # Prepare target state in 1 
                with if_(st_t == 1):
                    play("x180", qt_xy)

                # Play ZI(-pi/2) and IX(-pi/2)
                align(qc_xy, qt_xy)
                frame_rotation_2pi(+0.25, qc_xy) # +0.25 for Z(-pi/2)
                play("-x90", qt_xy)

                # Shift frames to the calibrated phases
                frame_rotation_2pi(cr_drive_phase, cr_drive)
                frame_rotation_2pi(cr_cancel_phase, cr_cancel)

                # Play CR
                align(qc_xy, qt_xy, cr_drive, cr_cancel)
                play("square_positive", cr_drive)
                play("square_positive", cr_cancel)
                # echo
                align(qc_xy, cr_drive, cr_cancel)
                play("x180", qc_xy)
                align(qc_xy, cr_drive, cr_cancel)
                play("square_negative", cr_drive)
                play("square_negative", cr_cancel)
                align(qc_xy, cr_drive, cr_cancel)
                play("x180", qc_xy)
    
                align(qc_xy, qt_xy, *resonators)

                # Measure the state of the resonators
                multiplexed_readout(I, I_st, Q, Q_st, state, state_st, resonators=resonators, weights=weights)

                # reset phase shift for cancel drive
                reset_frame(cr_drive)
                reset_frame(cr_cancel)

                # Wait for the qubit to decay to the ground state - Can be replaced by active reset
                if reset_method == "wait":
                    wait(qb_reset_time >> 2)
                elif reset_method == "active":
                    global_state = active_reset(I, None, Q, None, state, None, resonators, qubits, state_to="ground", weights=weights)

    with stream_processing():
        n_st.save("iteration")
        for ind, rr in enumerate(resonators):
            I_st[ind].buffer(2).buffer(2).average().save(f"I_{rr}")
            Q_st[ind].buffer(2).buffer(2).average().save(f"Q_{rr}")
            state_st[ind].boolean_to_int().buffer(2).buffer(2).average().save(f"state_{rr}")


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
        job = qmm.simulate(config, PROGRAM, simulation_config)
        job.get_simulated_samples().con1.plot(analog_ports=['1', '2', '3', '4', '5', '6'])
        plt.show()

    else:
        try:
            # Open the quantum machine
            qm = qmm.open_qm(config)
            # Send the QUA program to the OPX, which compiles and executes it
            job = qm.execute(PROGRAM)
            # Prepare the figure for live plotting
            fig = plt.figure()
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
                    save_data_dict[rr+"_state"] = res[3*ind + 3]
                iterations, I1, Q1, state_c, I2, Q2, state_t = res
                # Progress bar
                progress_counter(iterations, n_avg, start_time=results.start_time)
                # Plot
                plt.suptitle("CNOT calib")
                plt.subplot(1, 2, 1)
                plt.cla()
                plt.imshow(state_c, interpolation='nearest', cmap='Blues')
                plt.xlabel("prepared target state")
                plt.xlabel("prepared control state")
                plt.title(f"measured control state")
                plt.subplot(1, 2, 2)
                plt.cla()
                plt.imshow(state_t, interpolation='nearest', cmap='Blues')
                plt.xlabel("prepared target state")
                plt.xlabel("prepared control state")
                plt.title(f"measured target state")
                plt.tight_layout()
                plt.pause(0.1)

            # Save results
            script_name = Path(__file__).name
            data_handler = DataHandler(root_data_folder=save_dir)
            save_data_dict.update({"fig_live": fig})
            data_handler.additional_files = {script_name: script_name, **default_additional_files}
            data_handler.save_data(data=save_data_dict, name="cnot_calib")

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            # qm.close()
            print("Experiment QM is now closed")
            plt.show(block=True)

# %%
