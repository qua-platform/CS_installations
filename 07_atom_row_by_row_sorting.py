# %%
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from qm import LoopbackInterface
from array_sorting_macros import *
from configuration_sorting import *

# from configuration import *

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

#####################################################################
# Configuration start

#############################
# Define run configurations #
#############################
# Enables the collision free sorting algorithm
collision_free = True
# Enables the piecewise chirp decomposition for minimal jerk trajectory
piecewise_chirp = False
# Reads the current occupation matrix via analog readout
analog_occupation_matrix = False
# Acquires chirp tones to plot spectrograms - output should be connected to OPX analog input
raw_adc_acquisition = True
# Runs the sorting only once, else is infinite loop
single_run = True
# Maximum constant chirp rate in Hz/ns, None uses default pulse length from config
maximum_chirp_rate = None
# Run simulation instead of real execution
Simulation = False


############################
# Target occupation matrix #
############################
# Defined pattern
# atom_target_list = [
#     1, 0, 0, 0, 1,
#     0, 1, 0, 1, 0,
#     0, 0, 1, 0, 0,
#     0, 1, 0, 1, 0,
#     1, 0, 0, 0, 1
# ]

# Random pattern
# atom_target_list = [
#     list(map(int, np.random.choice([0, 1], size=number_of_columns, p=[0.4, 0.6]))) for i in range(number_of_rows)
# ]

# Centered pattern
n_border = 2
atom_target_list = np.ones((number_of_rows, number_of_columns), dtype=int)
atom_target_list[:n_border, :] = 0  # top border
atom_target_list[-n_border:, :] = 0  # bottom border
atom_target_list[:, :n_border] = 0  # left border
atom_target_list[:, -n_border:] = 0  # right border

# Configuration end
#####################################################################

# Target occupation matrix in 1D
atom_target_1d_python = [j for sub in atom_target_list for j in sub]
# Target column frequencies in 1D and of size sum of 1s in target
target_frequencies_full_python = [
    [
        int(column_if[i]) if atom_target_list[j][i] else 0
        for i in range(len(atom_target_list[0]))
    ]
    for j in range(number_of_rows)
]
target_frequencies_1d = [j for sub in target_frequencies_full_python for j in sub]

################
# Verification #
################
if maximum_chirp_rate is not None and piecewise_chirp:
    raise NotImplementedError(
        "Dynamic pulse duration with piecewise chirps is not implemented."
    )
if not analog_occupation_matrix:
    # Initial occupation matrix in 2D
    atom_location_list = [
        list(map(int, np.random.choice([0, 1], size=number_of_columns, p=[0.4, 0.6])))
        for i in range(number_of_rows)
    ]
else:
    raise NotImplementedError("Analog occupation matrix reading is not implemented.")
# Initial occupation matrix in 1D
atom_location_list_1d = [j for sub in atom_location_list for j in sub]

print("Initial occupation matrix:")
print_2d(atom_location_list)
print("Atom target matrix:")
print_2d(atom_target_list)

# Get all relevant elements in a list for easy align
elements = list(config["elements"].keys())
elements.remove("qubit")

###############
# QUA program #
###############

# --> Play single tweezer for frequency calibration
with program() as freq_calibration:
    update_frequency("row_selector", row_frequencies_list[0])
    update_frequency("column_1", column_if[0])
    # Keep playing row selector and column selector at constant amplitude, tone at 0,0, freq
    with infinite_loop_():
        play("constant", "row_selector")
        play("constant", "column_1")

# --> Full atom rearrangment program
with program() as atom_sorting:
    # Variables that need resetting
    received_full_array = declare(
        bool, value=False
    )  # Flag indicating the end of occupation matrix readout

    # Debug variables
    raw_adc = declare_stream(
        adc_trace=True
    )  # Raw ADC trace for spectrograms or occupation matrix readout
    data_stream = declare_stream()  # stream used to extract variables for debug
    count_stream = declare_stream()  # stream used to extract variables for debug
    infinite_run = declare(
        bool, value=True
    )  # Flag used to perform the sorting only once instead of infinite_loop_()

    # QUA variable representing the current row
    current_row = declare(int)
    # QUA variable containing the full 1D target locations
    atom_target_full_qua = declare(int, value=atom_target_1d_python)
    # QUA variable containing the full 1D target frequencies
    target_frequencies_full_qua = declare(int, value=target_frequencies_1d)
    # QUA variable containing the row frequencies
    row_frequencies_qua = declare(int, value=[int(x) for x in row_frequencies_list])
    # QUA variable containing the column frequencies
    column_frequencies_qua = declare(int, value=[int(x) for x in column_if])
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
                number_of_rows, number_of_columns, threshold, received_full_array
            )
        else:
            atom_location_full = declare(int, value=atom_location_list_1d)
            assign(received_full_array, True)

        ################
        # Atom sorting #
        ################
        with if_(received_full_array):
            # Loop over the rows
            with for_(current_row, 0, current_row < number_of_rows, current_row + 1):
                # Get the current and target locations and target frequencies of the current row
                (
                    atom_location_qua,
                    atom_target_qua,
                    target_frequencies_qua,
                ) = get_current_row(
                    current_row,
                    number_of_columns,
                    atom_location_full,
                    atom_target_full_qua,
                    target_frequencies_full_qua,
                )
                # Derive number of required tweezers
                number_of_tweezers = find_number_of_tweezers(
                    atom_location_qua, atom_target_qua, max_number_of_tweezers
                )
                # Assign the tweezers amplitude, initial frequency, phase and detuning using either a dummy logic that
                # will only avoid collisions on left compact targets, or a smarter collision-free algorithm
                if collision_free:
                    (
                        amplitude_qua,
                        frequency_qua,
                        phase_qua,
                        detuning_qua,
                    ) = assign_tweezers_to_atoms_collision_free(
                        number_of_tweezers,
                        max_number_of_tweezers,
                        atom_location_qua,
                        column_frequencies_qua,
                        target_frequencies_qua,
                        tweezer_phases_qua,
                        atom_target_qua,
                        data_stream,
                        count_stream,
                    )
                else:
                    (
                        amplitude_qua,
                        frequency_qua,
                        phase_qua,
                        detuning_qua,
                    ) = assign_tweezers_to_atoms(
                        number_of_tweezers,
                        max_number_of_tweezers,
                        atom_location_qua,
                        column_frequencies_qua,
                        target_frequencies_qua,
                        tweezer_phases_qua,
                        data_stream,
                    )
                # Derive the chirp pulse duration from the default pulse length of the maximum chirp rate if not None.
                chirp_pulse_duration_qua = calculate_pulse_length(
                    detuning_qua, constant_pulse_length, max_rate=maximum_chirp_rate
                )
                # Derive the chirp rates defined as piecewise or constant
                if piecewise_chirp:
                    piecewise_chirp_rates_qua = calculate_piecewise_chirp_rates(
                        max_number_of_tweezers,
                        detuning_qua,
                        chirp_pulse_duration_qua,
                        n_segment_python,
                    )
                else:
                    constant_chirp_rates_qua = calculate_chirp_rates(
                        max_number_of_tweezers, detuning_qua, chirp_pulse_duration_qua
                    )
                # Assign the frequencies and phases to the tweezers
                set_tweezers_frequencies_and_phases(
                    max_number_of_tweezers,
                    frequency_qua,
                    row_frequencies_qua[current_row],
                    phase_qua,
                )
                # Convert the chirp pulse duration in clock cycles
                assign(chirp_pulse_duration_qua, chirp_pulse_duration_qua >> 2)
                # align all tweezers/columns and row selector
                align(*elements)
                # Wait to calculate as much as possible before playing the pulses to minimize gaps
                if maximum_chirp_rate is not None:
                    wait(200)
                # ramp up power of occupied tweezers and row selector
                play("blackman_up", "row_selector")
                for element_index in range(max_number_of_tweezers):
                    play(
                        "blackman_up" * amp(amplitude_qua[element_index]),
                        "column_{}".format(element_index + 1),
                    )
                # chirp tweezers
                play("constant", "row_selector")
                for element_index in range(max_number_of_tweezers):
                    if piecewise_chirp:
                        play(
                            "constant" * amp(amplitude_qua[element_index]),
                            "column_{}".format(element_index + 1),
                            chirp=(
                                piecewise_chirp_rates_qua[element_index],
                                "mHz/nsec",
                            ),
                        )  # chirp is 1D vector
                    else:
                        if maximum_chirp_rate is None:
                            play(
                                "constant" * amp(amplitude_qua[element_index]),
                                "column_{}".format(element_index + 1),
                                chirp=(
                                    constant_chirp_rates_qua[element_index],
                                    "mHz/nsec",
                                ),
                            )
                        else:
                            play(
                                "constant" * amp(amplitude_qua[element_index]),
                                "column_{}".format(element_index + 1),
                                duration=chirp_pulse_duration_qua,
                                chirp=(
                                    constant_chirp_rates_qua[element_index],
                                    "mHz/nsec",
                                ),
                            )
                # ramp down power of occupied tweezers
                play("blackman_down", "row_selector")
                for element_index in range(max_number_of_tweezers):
                    play(
                        "blackman_down" * amp(amplitude_qua[element_index]),
                        "column_{}".format(element_index + 1),
                    )
                # Measure raw adc trace for spectrograms
                if raw_adc_acquisition:
                    measure("readout", "detector", adc_stream=raw_adc)
            # Exit the infinite loop in case just a single sorting sequence is needed
            if single_run:
                assign(infinite_run, False)

    with stream_processing():
        data_stream.save_all("data")
        count_stream.save_all("count")
        if raw_adc_acquisition:
            raw_adc.input2().save_all("raw_data")

#####################################
#  Open Communication with the QOP  #
#####################################

# qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name, timeout=1000)


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

    # Get the final atom locations
    tot_atom_moved_list = res.get("count").fetch_all()["value"]
    atom_final_list = []
    cur_idx = 0
    for i, tot_atom_moved in enumerate(tot_atom_moved_list):
        # Check row by row and obtain the moved and unmoved atom locations
        print(f"Row {i + 1} - Total atoms moved: {tot_atom_moved}")
        row_assign = assign[cur_idx : cur_idx + tot_atom_moved * 2]
        initial_atom_row_idx = row_assign.reshape((-1, 2))[:, 0]
        final_atom_row_idx = row_assign.reshape((-1, 2))[:, 1]
        unmoved_atom_row_idx = set(np.nonzero(atom_location_list[i])[0]) - set(
            initial_atom_row_idx
        )
        final_atom_row_idx = np.concatenate(
            [final_atom_row_idx, list(unmoved_atom_row_idx)], None
        ).astype(int)
        final_atom_row_loc = np.zeros(number_of_columns, dtype=int)
        final_atom_row_loc[final_atom_row_idx] = 1
        atom_final_list.append(list(final_atom_row_loc))
        cur_idx += tot_atom_moved * 2

    if raw_adc_acquisition:
        fs = 14
        raw1 = res.get("raw_data").fetch_all()["value"]
        subplot_ncols = 4
        subplot_nrows = number_of_rows // subplot_ncols + 3
        plt.figure(figsize=(25, 6 * subplot_nrows))
        for i in range(number_of_rows):
            # plt.figure(figsize=(14,9))
            # ax1 = plt.subplot(121)
            # plt.plot(raw1[i][:])
            # plt.axvline(x=blackman_pulse_length+159, color='k')
            # plt.axvline(x=blackman_pulse_length + constant_pulse_length + 159, color='k')
            # plt.ylabel('Pulse amplitude [arb. unit]', fontsize=fs)
            # plt.xlabel('Time [ns]', fontsize=fs)

            # ax2 = plt.subplot(241 + i)
            ax2 = plt.subplot(subplot_nrows, subplot_ncols, i + 1)
            for j in range(len(column_if)):
                plt.axhline(column_if[j], color="k", linewidth=1, linestyle="--")
            Pxx, freqs, time, im = plt.specgram(
                raw1[i], NFFT=2**14, Fs=1e9, noverlap=100, cmap=plt.cm.gist_heat
            )

            for atom_loc in np.nonzero(atom_location_list[i])[0]:
                atom_freq = column_if[atom_loc]
                plt.scatter(time[3], atom_freq, s=100, color="g")

            for target_freq in target_frequencies_full_python[i]:
                plt.scatter(time[-3], target_freq, s=100, color="b")

            plt.ylabel("Frequency [MHz]", fontsize=fs)
            plt.xlabel("Time [µs]", fontsize=fs)
            freq_min = min(column_if) - 2 * abs(column_spacing)
            freq_max = max(column_if) + 2 * abs(column_spacing)
            plt.axis([0, time[-1], freq_min, freq_max])
            plt.title(f"Row {i + 1}", fontsize=fs)
            xticks = ax2.get_xticks()
            yticks = ax2.get_yticks()
            ax2.set_xticks(xticks, xticks * 1e6, fontsize=fs)
            ax2.set_yticks(yticks, yticks / 1e6, fontsize=fs)

        # 2D grid of atom locations
        # red = -1 = needs atom
        # black = 0 = no atom
        # white = 1 = has atom
        # cyan = 2 = has additional atom
        cmap = ListedColormap(["red", "black", "white", "cyan"])  # -1, 0, 1, 2
        bounds = [-1.5, -0.5, 0.5, 1.5, 2.5]
        norm = BoundaryNorm(bounds, cmap.N)
        atom_diff_list = 2 * np.array(atom_final_list) - np.array(atom_target_list)
        for i, (title, mat) in enumerate(
            zip(
                ["Initial", "Target", "Current"],
                [atom_location_list, atom_target_list, atom_diff_list],
            )
        ):
            ax2 = plt.subplot(subplot_nrows, subplot_ncols, number_of_rows + 1 + i)
            plt.pcolormesh(mat, edgecolor="gray", cmap=cmap, norm=norm, linewidth=3)
            plt.gca().invert_yaxis()
            ax2.set_xticklabels(labels="")
            ax2.set_yticklabels(labels="")
            plt.title(title, fontsize=fs)
        plt.tight_layout()

else:
    simulation_duration = 300  # simulate for 2e4 clock cycles or 120µs
    job = qmm.simulate(
        config,
        atom_sorting,
        SimulationConfig(
            simulation_duration,
            simulation_interface=LoopbackInterface(
                [("con1", 1, "con1", 1), ("con1", 2, "con1", 2)]
            ),
        ),
    )

# %%
