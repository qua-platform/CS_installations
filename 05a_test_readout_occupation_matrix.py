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


###################
# The QUA program #
###################

num_sites = num_cols * num_rows

with program() as PROG:
    occupation_matrix = declare(int, size=num_sites)  # Full 1D occupation matrix
    I = declare(fixed)  # integrated I for occupation matrix readout
    I_st = declare_stream()
    adc_st = declare_stream(adc_trace=True)
    counter = declare(int)  # Counter for keeping track of the received locations
    readout_done = declare(bool)

    assign(readout_done, False)
    assign(counter, 0)
    with while_(~readout_done):
        wait_for_trigger("detector")
        wait(5 * u.us, "detector")
        measure(
            "readout",
            "detector",
            integration.full("const", I, "out1"),
            adc_stream=adc_st,
        )
        # with if_(I < readout_threshold):
        #     assign(occupation_matrix[counter], 1)
        # with else_():
        #     assign(occupation_matrix[counter], 0)
        # save(occupation_matrix[counter], data_stream)
        assign(counter, counter + 1)
        assign(readout_done, counter == num_sites)

        save(I, I_st)
        # assign(occupied, I < threashold)
        # save(occupied, occupied_st)
        wait(250)

    with stream_processing():
        I_st.buffer(num_sites).save_all("I")
        # occupied_st.boolean_to_int().buffer(num_cols * num_rows).average().save("occupied")
        if config["elements"]["detector"]["outputs"]["out1"][1] == 1:
            # # Will save average:
            # adc_st.input1().average().save(f"adc")
            # Will save only last run:
            adc_st.input1().save_all(f"adc_single_run")
        else:
            # # Will save average:
            # adc_st.input2().average().save(f"adc")
            # Will save only last run:
            adc_st.input2().save_all(f"adc_single_run")


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
        job = qmm.simulate(config, PROG, simulation_config)
        # Plot the simulated samples
        job.get_simulated_samples().con1.plot()
        plt.show(block=False)
    else:
        try:
            # Open a quantum machine to execute the QUA PROG
            qm = qmm.open_qm(config)
            # Send the QUA PROG to the OPX, which compiles and executes it
            job = qm.execute(PROG)
            res_handles = job.result_handles
            # Waits (blocks the Python console) until all results have been acquired
            res_handles.wait_for_all_values()
            # # Get results from QUA PROG
            I = job.result_handles.get("I").fetch_all()
            adc = job.result_handles.get("adc_single_run").fetch_all()
            adc = [u.raw2volts(adc_[0]) for adc_ in adc]
            # is_occupied = job.result_handles.get("occupied").fetch_all()

            fig = plt.figure()
            ys = I[0][0]
            plt.scatter(x=np.arange(len(ys)), y=ys)

            for adc_ in adc:
                fig = plt.figure()
                plt.plot(adc_)
            # # plotting
            # fig = plt.figure()
            # # plt.suptitle(f"Resonator spectroscopy for {resonator} - LO = {resonator_LO / u.GHz} GHz")
            # ax1 = plt.subplot(211)
            # xs = np.arange(len(I))
            # plt.plot(xs, I, ".")
            # plt.axhline(y=threashold, linestyle="--")
            # plt.ylabel("I [V]")
            # plt.subplot(212, sharex=ax1)
            # plt.plot(xs, occupation_matrix_dummy, ".", markersize=20, alpha=0.5)
            # plt.plot(xs, is_occupied, "*", color="r")
            # plt.ylabel(r"Occupied")
            # plt.legend(["preset", "data"])
            # plt.xlabel("Atom Site Index")
            # plt.tight_layout()

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


# %%
