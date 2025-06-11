# %%
"""
hello_qua.py: template for basic qua program demonstration
"""
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig, LoopbackInterface
from configuration import *
import matplotlib.pyplot as plt
from array_sorting_macros import *
import time


###################
# The QUA program #
###################

num_sites = num_cols * num_rows
readout_threshold = -0.112
delay_from_ext_trigger = 5 * u.us
raw_adc_acquisition = True

col_selectors = [f"col_selector_{i + 1:02d}" for i in range(num_cols)] # elements
row_selectors = [f"row_selector_{i + 1:02d}" for i in range(num_rows)] # elements

target_occupations = [
    1, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 1, 0, 0,
    0, 0, 1, 1, 1, 0, 0, 0,
    0, 0, 1, 1, 1, 0, 0, 0,
    0, 0, 1, 1, 1, 0, 0, 0,
    0, 1, 0, 0, 0, 1, 0, 0,
    1, 0, 0, 0, 0, 0, 1, 0,
    0, 0, 1, 0, 1, 0, 0, 0,
]

assert len(target_occupations) == num_sites, "the length is not consisitent with the expected number of sites!"



with program() as PROG:
    measured_occupations = declare(int, size=num_sites)  # Full 1D occupation matrix
    target_occupations = declare(int, value=target_occupations)
    occupied = declare(bool, value=True)
    occupied_st = declare_stream()
    I = declare(fixed)  # integrated I for occupation matrix readout
    I_st = declare_stream()
    # adc_st = declare_stream(adc_trace=True)
    counter = declare(int)  # Counter for keeping track of the received locations
    readout_done = declare(bool)

    j = declare(int)
    is_matched = declare(bool)
    is_rearranged = declare(bool, value=False)

    with while_(~is_rearranged):

        ########################################################
        # Read occupation matrix
        ########################################################

        assign(readout_done, False)
        assign(counter, 0)
        with while_(~readout_done):
        # with for=...
            wait_for_trigger("detector")
            wait(delay_from_ext_trigger, "detector")
            measure(
                "readout",
                "detector",
                integration.full("const", I, "out1"),
                # adc_stream=adc_st,
            )
            assign(occupied, I < readout_threshold)
            with if_(occupied):
                assign(measured_occupations[counter], 1)
            with else_():
                assign(measured_occupations[counter], 0)
            save(occupied, occupied_st)
            assign(counter, counter + 1)
            assign(readout_done, counter == num_sites)

            save(I, I_st)
            wait(250)


        # this makes sure to wait for any operation on "detector" to finish
        # reminder: element <=> core
        # align("detector", *col_selectors, *row_selectors) # to be explict
        
        align() # this aligns all the elements involved in this protocol 


        ########################################################
        # Play chirp based on the measured occupation matrix
        ########################################################


        # Loop over the rows
        with for_(current_row, 0, current_row < num_rows, current_row + 1):
            # Get the current and target locations and target frequencies of the current row
            atom_location_qua, atom_target_qua, target_freqs_qua = get_current_row(
                current_row,
                num_cols,
                atom_location_full,
                atom_target_full_qua,
                target_freqs_full_qua,
            )
            # Derive number of required tweezers
            num_tweezers = find_num_tweezers(atom_location_qua, atom_target_qua, max_num_tweezers)
            # Assign the tweezers amplitude, initial frequency, phase and detuning using either a dummy logic that
            # will only avoid collisions on left compact targets, or a smarter collision-free algorithm
            if collision_free:
                amp_qua, frequency_qua, phase_qua, detuning_qua = assign_tweezers_to_atoms_collision_free(
                    num_tweezers,
                    max_num_tweezers,
                    atom_location_qua,
                    col_freqs_qua,
                    target_freqs_qua,
                    tweezer_phases_qua,
                )
            else:
                amp_qua, frequency_qua, phase_qua, detuning_qua = assign_tweezers_to_atoms(
                    num_tweezers,
                    max_num_tweezers,
                    atom_location_qua,
                    col_freqs_qua,
                    target_freqs_qua,
                    tweezer_phases_qua,
                )

            # Derive the chirp pulse duration from the default pulse length of the maximum chirp rate if not None.
            chirp_pulse_duration_qua = calculate_pulse_len(detuning_qua, const_pulse_len, max_rate=max_chirp_rate)

            # Derive the chirp rates defined as piecewise or constant
            if piecewise_chirp:
                piecewise_chirp_rates_qua = calculate_piecewise_chirp_rates(
                    max_num_tweezers, detuning_qua, chirp_pulse_duration_qua, n_segment_py
                )
            else:
                const_chirp_rates_qua = calculate_chirp_rates(
                    max_num_tweezers, detuning_qua, chirp_pulse_duration_qua
                )

            # Assign the frequencies and phases to the tweezers
            set_tweezers_freqs_and_phases(max_num_tweezers, frequency_qua, row_freqs_qua[current_row], phase_qua)

            # Convert the chirp pulse duration in clock cycles
            assign(chirp_pulse_duration_qua, chirp_pulse_duration_qua >> 2)

            # align all tweezers/columns and row selector
            align(*elements)

            # Wait to calculate as much as possible before playing the pulses to minimize gaps
            if max_chirp_rate is not None:
                wait(200)

            # ramp up power of occupied tweezers and row selector
            play("blackman_up", "row_selector")
            for element_idx in range(max_num_tweezers):
                play(
                    "blackman_up" * amp(amp_qua[element_idx]),
                    f"col_selector_{element_idx + 1}",
                )

            # chirp tweezers
            play("const", "row_selector")
            for element_idx in range(max_num_tweezers):
                if piecewise_chirp:
                    play(
                        "const" * amp(amp_qua[element_idx]),
                        f"col_selector_{element_idx + 1}",
                        chirp=(piecewise_chirp_rates_qua[element_idx], "mHz/nsec"),
                    )  # chirp is 1D vector
                else:
                    if max_chirp_rate is None:
                        play(
                            "const" * amp(amp_qua[element_idx]),
                            f"col_selector_{element_idx + 1}",
                            chirp=(const_chirp_rates_qua[element_idx], "mHz/nsec"),
                        )
                    else:
                        play(
                            "const" * amp(amp_qua[element_idx]),
                            f"col_selector_{element_idx + 1}",
                            duration=chirp_pulse_duration_qua,
                            chirp=(const_chirp_rates_qua[element_idx], "mHz/nsec"),
                        )

            # ramp down power of occupied tweezers
            play("blackman_down", "row_selector")
            for element_idx in range(max_num_tweezers):
                play(
                    "blackman_down" * amp(amp_qua[element_idx]),
                    f"col_selector_{element_idx + 1}",
                )

            # Measure raw adc trace for spectrograms
            if raw_adc_acquisition:
                measure("readout", "detector", raw_adc)


        # verify the rearrangement is done
        assign(is_rearranged, True)
        with for_(j, 0, j < num_sites, j + 1):
            assign(is_matched, measured_occupations[j] == target_occupations[j])
            assign(is_rearranged, is_rearranged & is_matched)


    ########################################################
    # Play chirp based on the measured occupation matrix
    ########################################################

    align()

    play("on", "trigger_artiq")



    with stream_processing():
        # I_st.buffer(num_sites).save("I")
        occupied_st.boolean_to_int().buffer(num_sites).save("occupation")
        # # occupied_st.boolean_to_int().buffer(num_cols * num_rows).average().save("occupied")


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
            # I = job.result_handles.get("I").fetch_all()
            occupation = job.result_handles.get("occupation").fetch_all()
            # is_occupied = job.result_handles.get("occupied").fetch_all()

            # fig = plt.figure()
            # ys = I[0][0]
            # plt.scatter(x=np.arange(len(ys)), y=ys)

            # for adc_ in adc:
            #     fig = plt.figure()
            #     plt.plot(adc_)
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

