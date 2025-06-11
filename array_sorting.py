# %%

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig, LoopbackInterface
from configuration import *
import matplotlib.pyplot as plt
from array_sorting_macros import *


###############
# QUA program #
###############

# --> Play single tweezer for frequency calibration
with program() as freq_calibration:
    update_frequency("row_selector_01", row_IFs[0])
    update_frequency("col_selector_01", col_IFs[0])
    # Keep playing row selector and column selector at constant amplitude, tone at 0,0, freq
    with infinite_loop_():
        play("const", "row_selector_01")
        play("const", "col_selector_01")


# --> Full atom rearrangment program
with program() as atom_sorting:
    # Variables that need resetting
    received_full_array = declare(bool, value=False)  # Flag indicating the end of occupation matrix readout

    # Debug variables
    raw_adc = declare_stream(adc_trace=True)  # Raw ADC trace for spectrograms or occupation matrix readout
    data_stream = declare_stream()  # stream used to extract variables for debug
    infinite_run = declare(bool, value=True)  # Flag used to perform the sorting only once instead of infinite_loop_()

    # QUA variable representing the current row
    current_row = declare(int)
    # QUA variable containing the full 1D target locations
    atom_target_full_qua = declare(int, value=atom_target_1d_py)
    # QUA variable containing the full 1D target frequencies
    target_freqs_full_qua = declare(int, value=target_freqs_1d)
    # QUA variable containing the row frequencies
    row_freqs_qua = declare(int, value=[int(x) for x in row_IFs])
    # QUA variable containing the column frequencies
    col_freqs_qua = declare(int, value=[int(x) for x in col_IFs])
    # QUA variable containing the tweezer phases
    tweezer_phases_qua = declare(fixed, value=phases_list)

    with while_(infinite_run):
        # Reset variables for new loop
        assign(received_full_array, False)

        ###############################################
        # Measure occupation matrix from analog input #
        ###############################################
        if analog_occupation_matrix:
            atom_location_full, received_full_array = analog_readout(
                num_rows, num_cols, threshold, received_full_array, data_stream
            )
        else:
            atom_location_full = declare(int, value=atom_location_list_1d)
            assign(received_full_array, True)

        ################
        # Atom sorting #
        ################
        with if_(received_full_array):
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

            # Exit the infinite loop in case just a single sorting sequence is needed
            if single_run:
                assign(infinite_run, False)

    with stream_processing():
        data_stream.save_all("data")
        if raw_adc_acquisition:
            raw_adc.input2().save_all("raw_data")


#####################################
#  Open Communication with the QOP  #
#####################################
Simulation = False

qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

if not Simulation:
    # Open a quantum machine
    qm = qmm.open_qm(config)

    job = qm.execute(atom_sorting)  # order_atoms
    # job = qm.execute(freq_calibration)
    res = job.result_handles
    res.wait_for_all_values()

    # Print atom displacement fo reach row: each pair is current --> target
    row_count = 0
    assign = res.get("data").fetch_all()["value"]

    for item in assign:
        if item == -1:
            print(f"\nrow {row_count}")
            row_count += 1
        else:
            print(f"{item} ", end="")

    if raw_adc_acquisition:
        fs = 14
        raw1 = res.raw_data.fetch_all()["value"]
        plt.figure(figsize=(25, 12))
        for i in range(num_rows):
            # plt.figure(figsize=(14,9))
            # ax1 = plt.subplot(121)
            # plt.plot(raw1[i][:])
            # plt.axvline(x=blackman_pulse_len+159, color='k')
            # plt.axvline(x=blackman_pulse_len + const_pulse_len + 159, color='k')
            # plt.ylabel('Pulse amplitude [arb. unit]', fontsize=fs)
            # plt.xlabel('Time [ns]', fontsize=fs)

            ax2 = plt.subplot(241 + i)
            for j in range(len(col_IFs)):
                plt.axhline(col_IFs[j], color="k", linewidth=1, linestyle="--")
            Pxx, freqs, time, im = plt.specgram(raw1[i], NFFT=2**14, Fs=1e9, noverlap=100, cmap=plt.cm.gist_heat)

            for target_freq in target_freqs_full_py[i]:
                plt.scatter(time[-3], target_freq, s=100, color="b")

            plt.ylabel("Frequency [MHz]", fontsize=fs)
            plt.xlabel("Time [µs]", fontsize=fs)
            plt.axis([0, time[-1], 68e6, 79e6])
            ax2.set_xticklabels((ax2.get_xticks() * 1e6).astype(int), fontsize=fs)
            ax2.set_yticklabels((ax2.get_yticks() / 1e6).astype(int), fontsize=fs)

        ax2 = plt.subplot(248)
        goal2 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        plt.pcolormesh(goal2, shading="gouraud", edgecolors="k")
        ax2.set_xticklabels(labels="")
        ax2.set_yticklabels(labels="")

else:
    simulation_duration = 300  # simulate for 2e4 clock cycles or 120µs
    job = qmm.simulate(
        config,
        atom_sorting,
        SimulationConfig(
            simulation_duration,
            simulation_interface=LoopbackInterface([("con1", 1, "con1", 1), ("con1", 2, "con1", 2)]),
        ),
    )
