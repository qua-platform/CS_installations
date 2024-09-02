# %%
"""
                                 CNOT_bakery

Prerequisites:
    - 

Next steps before going to the next node:
    - 

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
from qualang_tools.bakery import baking

import time
import warnings
import matplotlib
from macros import qua_declaration, multiplexed_readout


##############################
# Program-specific variables #
##############################

qc = 2 # index of control qubit
qt = 3 # index of target qubit

cr_cancel_amp = 0.2 # ratio
cr_cancel_phase = 0.5 # in units of 2pi

cr_c1t2_drive_phase = 0.5
cr_cancel_c1t2_drive_phase = 0.5

qc_xy = f"q{qc}_xy"
qt_xy = f"q{qt}_xy"
cr_drive = f"cr_drive_c{qc}t{qt}"
cr_cancel = f"cr_cancel_c{qc}t{qt}"
rrc = f"q{qc}_rr"
rrt = f"q{qt}_rr"

qubits = [f"q{i}_xy" for i in [qc, qt]]
resonators = [f"q{i}_rr" for i in [qc, qt]]
qubits_all = list(QUBIT_CONSTANTS.keys()) # [qc_xy, qt_xy]
resonators_all = [key for key in RR_CONSTANTS.keys()]
remaining_resonators = list(set(resonators_all) - set(resonators))
weights = "rotated_" # ["", "rotated_", "opt_"] 
reset_method = "wait" # can also be "active"

n_avg = 10

ts_cycle = np.arange(8, 400, 4) # in clock cylcle = 4ns
ts_ns = 4 * ts_cycle # in clock cylcle = 4ns
amps = np.arange(0.05, 1.95, 0.05) # scaling factor for amplitude
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

# # remove the thread sharing
# for qubit in qubits:
#     config["elements"][qubit].pop("thread")
# config["elements"][cr_drive].pop("thread")
# config["elements"][cr_cancel].pop("thread")


# # baking
# def bake_cnot():
#     with baking(config, padding_method="right") as b:
#         # Play ZI(-pi/2) and IX(-pi/2)
#         b.align(qc_xy, qt_xy)
#         b.frame_rotation_2pi(+0.25, qc_xy) # +0.25 for Z(-pi/2)
#         b.play("-x90", qt_xy)

#         # Shift frames to the calibrated phases
#         b.frame_rotation_2pi(cr_c1t2_drive_phase, cr_drive)
#         b.frame_rotation_2pi(cr_cancel_c1t2_drive_phase, cr_cancel)

#         # Play CR
#         # b.align(qc_xy, cr_drive, cr_cancel)
#         # b.align()
#         # main
#         b.wait(PI_LEN, cr_drive)
#         b.wait(PI_LEN, cr_cancel)
#         b.play("square_positive", cr_drive)
#         b.play("square_positive", cr_cancel)
#         # echo
#         # b.align(qc_xy, cr_drive, cr_cancel)
#         # b.align()
#         b.wait(PI_LEN+CR_DRIVE_SQUARE_LEN, qc_xy)
#         b.play("x180", qc_xy)
#         # b.align(qc_xy, cr_drive, cr_cancel)
#         # b.align()
#         b.wait(PI_LEN, cr_drive)
#         b.wait(PI_LEN, cr_cancel)
#         b.play("square_negative", cr_drive)
#         b.play("square_negative", cr_cancel)
#         # b.align(qc_xy, cr_drive, cr_cancel)
#         # b.align()
#         b.wait(CR_DRIVE_SQUARE_LEN, qc_xy)
#         b.play("x180", qc_xy)
#     return b

# baking
def bake_cnot():
    with baking(config, padding_method="right") as b:
        # Play ZI(-pi/2) and IX(-pi/2)
        b.align(qc_xy, qt_xy)
        b.frame_rotation_2pi(+0.25, qc_xy) # +0.25 for Z(-pi/2)
        b.play("-x90", qt_xy)

        # Shift frames to the calibrated phases
        b.frame_rotation_2pi(cr_c1t2_drive_phase, cr_drive)
        b.frame_rotation_2pi(cr_cancel_c1t2_drive_phase, cr_cancel)

        # Play CR
        b.align(qc_xy, cr_drive)
        b.align(qc_xy, cr_cancel)
        # main
        b.play("square_positive", cr_drive)
        b.play("square_positive", cr_cancel)
        # echo
        b.align(qc_xy, cr_drive)
        b.align(qc_xy, cr_cancel)
        # b.wait(PI_LEN+CR_DRIVE_SQUARE_LEN, qc_xy)
        b.play("x180", qc_xy)
        b.align(qc_xy, cr_drive)
        b.align(qc_xy, cr_cancel)
        # b.align()
        # b.wait(PI_LEN, cr_drive)
        # b.wait(PI_LEN, cr_cancel)
        b.play("square_negative", cr_drive)
        b.play("square_negative", cr_cancel)
        b.align(qc_xy, cr_drive)
        b.align(qc_xy, cr_cancel)
        # b.align()
        # b.wait(CR_DRIVE_SQUARE_LEN, qc_xy)
        b.play("x180", qc_xy)

    return b


# back cr for combinations of state_c and state_t
baked_cnot = bake_cnot()

with program() as cnot_calib:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(resonators)
    state = [declare(bool) for _ in range(len(resonators))]
    state_st = [declare_stream() for _ in range(len(resonators))]
    st_c = declare(int)
    st_t = declare(int)
    
    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)
        # to allow time to save the data
        wait(400 * u.ns)
        with for_(st_c, 0, st_c < 2, st_c + 1):
            with for_(st_t, 0, st_t < 2, st_t + 1):
                # Prepare control state in 1
                with if_(st_c == 1):
                    play("x180", qc_xy)
                # Prepare target state in 1 
                with if_(st_t == 1):
                    play("x180", qt_xy)
                
                align()
                
                # Play baked CR
                baked_cnot.run()
                
                align()
                
                # Measure the state of the resonators
                multiplexed_readout(I, I_st, Q, Q_st, state, state_st, resonators=resonators, weights=weights)

                # Wait for the qubit to decay to the ground state - Can be replaced by active reset
                if reset_method == "wait":
                    wait(200 * u.ns)
                    # wait(qb_reset_time >> 2)
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
        simulation_config = SimulationConfig(duration=2000)  # In clock cycles = 4ns
        job = qmm.simulate(config, cnot_calib, simulation_config)
        # job.get_simulated_samples().con1.plot(analog_ports=['1', '2', '3', '4', '5', '6'])
        job.get_simulated_samples().con1.plot(analog_ports=['1', '3', '5'])
        plt.show()

    else:
        from qm import generate_qua_script
        sourceFile = open('debug_19b_CNOT_bakery_after_align.py', 'w')
        print(generate_qua_script(cnot_calib, config), file=sourceFile) 
        sourceFile.close()

        try:
            # Open the quantum machine
            qm = qmm.open_qm(config)
            # Send the QUA program to the OPX, which compiles and executes it
            job = qm.execute(cnot_calib)
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
                    save_data_dict[f"state_{rr}"] = res[3*ind + 3]
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
            data_handler.save_data(data=save_data_dict, name="cnot_calib_bakery")

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            qm.close()
            print("Experiment QM is now closed")
            plt.show(block=True)

# %%
