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

n_avg = 100

with program() as PROG:
    n = declare(int)
    adc_st = declare_stream(adc_trace=True)

    with for_(n, 0, n < n_avg, n + 1):

        reset_if_phase("detector")
        for i in range(n_tweezers):
            col_sel = f"col_selector_{i + 1:02d}"
            # col
            reset_if_phase(col_sel)
            play("const", col_sel, chirp=(+250, "GHz/sec"))
            play("const", col_sel, chirp=(-250, "GHz/sec"))
        #     # row
        #     play("const", f"row_selector_{i + 1:02d}", chirp=(+25, "GHz/sec"))
        #     play("const", f"row_selector_{i + 1:02d}", chirp=(-25, "GHz/sec"))
        #     # done
        #     wait(250_000)

        measure("readout", "detector", adc_stream=adc_st)
        # save(I, I_st)
        wait(250_000)

    with stream_processing():
        if config["elements"]["detector"]["outputs"]["out1"][1] == 1:
            # Will save average:
            adc_st.input1().average().save(f"adc")
            # Will save only last run:
            adc_st.input1().save(f"adc_single_run")
        else:
            # Will save average:
            adc_st.input2().average().save(f"adc")
            # Will save only last run:
            adc_st.input2().save(f"adc_single_run")


if __name__ == "__main__":
    #####################################
    #  Open Communication with the QOP  #
    #####################################
    qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

    ###########################
    # Run or Simulate Program #
    ###########################

    simulate = False

    if simulate:
        # Simulates the QUA program for the specified duration
        simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
        # Simulate blocks python until the simulation is done
        job = qmm.simulate(config, PROG, simulation_config)
        # Plot the simulated samples
        job.get_simulated_samples().con1.plot()

    else:
        try:
            # Open a quantum machine to execute the QUA program
            qm = qmm.open_qm(config)
            # Send the QUA program to the OPX, which compiles and executes it
            job = qm.execute(PROG)
            # Creates a result handle to fetch data from the OPX
            res_handles = job.result_handles
            # Waits (blocks the Python console) until all results have been acquired
            res_handles.wait_for_all_values()
            # Fetch the raw ADC traces and convert them into Volts
            adc0 = u.raw2volts(res_handles.get("adc").fetch_all())
            adc0_single_run = u.raw2volts(res_handles.get("adc_single_run").fetch_all())

            # save_data_dict["adc"] = adc0
            # save_data_dict["adc_single"] = adc0_single_run

            # Derive the average values
            adc0_mean = np.mean(adc0)
            # Remove the average values
            adc0_unbiased = adc0 - np.mean(adc0)
            # Plot data for each rl
            fig = plt.figure(figsize=(12, 6))
            plt.suptitle(f"Readout")

            # Plot for single run
            plt.subplot(121)
            plt.title("Single run")
            plt.plot(adc0_single_run, label="Input")
            plt.axhline(y=0)
            plt.xlabel("Time [ns]")
            plt.ylabel("Signal amplitude [V]")
            plt.legend()

            # Plot for averaged run
            plt.subplot(122)
            plt.title("Averaged run")
            plt.plot(adc0, label="Input")
            plt.axhline(y=0)
            plt.xlabel("Time [ns]")
            plt.legend()
            plt.tight_layout()


            NFFT = 2**10
            Fs = 1e9
            ax1 = plt.subplot(111)
            Pxx, freqs, bins, im = plt.specgram(x=adc0, NFFT=NFFT, Fs=Fs, noverlap=100, cmap=plt.cm.gist_heat)
            ax1.set_xticklabels((ax1.get_xticks() * 1e6).astype(int))
            ax1.set_yticklabels((ax1.get_yticks() / 1e6).astype(int))
            plt.xlabel("t [us]")
            plt.ylabel("f [MHz]")
            # plt.ylim([80e6, 120e6])
            plt.show()

            # # Save results
            # script_name = Path(__file__).name
            # data_handler = DataHandler(root_data_folder=save_dir)
            # save_data_dict.update({"fig_live": fig})
            # data_handler.additional_files = {script_name: script_name, **default_additional_files}
            # data_handler.save_data(data=save_data_dict, name="time_of_flight")

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            qm.close()
            print("Experiment QM is now closed")
            plt.show()

# %%
