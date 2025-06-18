# %%
"""
hello_qua.py: template for basic qua program demonstration
"""
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig, LoopbackInterface
from configuration import *
import matplotlib.pyplot as plt
import time
from qualang_tools.results import fetching_tool
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from scipy import signal
from qualang_tools.results.data_handler import DataHandler


###################
# The QUA program #
###################

n_avg = 100
threashold = -0.2290
occupation_matrix_dummy = np.random.randint(low=0, high=2, size=num_cols * num_rows)


with program() as PROGRAM:
    n = declare(int)
    I = declare(fixed)  # integrated I for occupation matrix readout
    I_st = declare_stream()
    do_play = declare(int)
    occupied = declare(bool)
    occupied_st = declare_stream()

    with for_(n, 0, n < n_avg, n + 1):
        with for_each_(do_play, occupation_matrix_dummy):
            with if_(do_play == 1):
                play("on", "occupation_matrix_dummy")
                wait(100, "fpga")
            with else_():
                play("off", "occupation_matrix_dummy")
                wait(100, "fpga")

            measure("readout_fpga", "fpga", None, integration.full("const", I, "out1"))

            save(I, I_st)
            assign(occupied, I < threashold)
            save(occupied, occupied_st)
            wait(2_500)

    with stream_processing():
        I_st.buffer(num_cols * num_rows).average().save("I")
        occupied_st.boolean_to_int().buffer(num_cols * num_rows).average().save(
            "occupied"
        )


if __name__ == "__main__":
    #####################################
    #  Open Communication with the QOP  #
    #####################################
    qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

    #######################
    # Simulate or execute #
    #######################
    simulate = False

    if simulate:
        # Simulates the QUA program for the specified duration
        simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
        # Simulate blocks python until the simulation is done
        job = qmm.simulate(config, PROGRAM, simulation_config)
        # Plot the simulated samples
        job.get_simulated_samples().con1.plot()
        plt.show(block=False)
    else:
        try:
            # Open a quantum machine to execute the QUA program
            qm = qmm.open_qm(config)
            # Send the QUA program to the OPX, which compiles and executes it
            job = qm.execute(PROGRAM)
            res_handles = job.result_handles
            # Waits (blocks the Python console) until all results have been acquired
            res_handles.wait_for_all_values()
            # # Get results from QUA program
            I = job.result_handles.get("I").fetch_all()
            is_occupied = job.result_handles.get("occupied").fetch_all()

            # plotting
            fig = plt.figure()
            # plt.suptitle(f"Resonator spectroscopy for {resonator} - LO = {resonator_LO / u.GHz} GHz")
            ax1 = plt.subplot(211)
            xs = np.arange(len(I))
            plt.plot(xs, I, ".")
            plt.axhline(y=threashold, linestyle="--")
            plt.ylabel("I [V]")
            plt.subplot(212, sharex=ax1)
            plt.plot(xs, occupation_matrix_dummy, ".", markersize=20, alpha=0.5)
            plt.plot(xs, is_occupied, "*", color="r")
            plt.ylabel(r"Occupied")
            plt.legend(["preset", "data"])
            plt.xlabel("Atom Site Index")
            plt.tight_layout()

            # save_data_dict[resonator+"_I"] = I
            # save_data_dict[resonator+"_Q"] = Q

            # # Save results
            # script_name = Path(__file__).name
            # data_handler = DataHandler(root_data_folder=save_dir)
            # save_data_dict.update({"fig_live": fig})
            # data_handler.additional_files = {script_name: script_name, **default_additional_files}
            # data_handler.save_data(data=save_data_dict, name="resonator_spectroscopy_single")

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            qm.close()
            print("Experiment QM is now closed")
            plt.show()

# %%
