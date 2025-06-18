from qm.qua import *
from configuration_sorting import *


#############################################
# Macros used to derive relevant parameters #
#############################################
def analog_readout(nb_of_rows, nb_of_columns, readout_threshold, readout_done):
    """
    This macro gets the current occupation matrix from the measurement of an analog signal sent by an external device.
    If the receive signal is larger than readout_threshold, then there is no atom and if it is smaller it means that
    there is an atom. The readout_done flag becomes True when all the sites have been received.

    :param nb_of_rows: A python variable for the number of rows in the array (int).
    :param nb_of_columns: A python variable for the number of column in the array (int).
    :param readout_threshold: A python variable for the analog threshold dicriminating between atom and no-atom (float).
    :param readout_done: A QUA variable for stating whether the readout is completed or not (bool).

    :return: Three QUA 1D vectors for the atom locations, target locations and target frequencies of the current row.
    """
    occupation_matrix = declare(
        int, size=nb_of_columns * nb_of_rows
    )  # Full 1D occupation matrix
    num_sites = declare(
        int, value=number_of_columns * number_of_rows
    )  # Total number of sites to be measured
    data = declare(fixed)  # integrated data for occupation matrix readout
    counter = declare(int)  # Counter for keeping track of the received locations
    assign(counter, 0)
    with while_(~readout_done):
        wait_for_trigger("fpga")
        measure(
            "readout_fpga", "fpga", None, integration.full("constant", data, "out1")
        )
        with if_(data < readout_threshold):
            assign(occupation_matrix[counter], 1)
        with else_():
            assign(occupation_matrix[counter], 0)
        save(occupation_matrix[counter], data_stream)
        assign(counter, counter + 1)
        assign(readout_done, counter == num_sites)
    return occupation_matrix, readout_done


def get_current_row(
    this_row,
    nb_of_columns,
    current_location_full,
    target_location_full,
    target_frequencies_full,
):
    """
    This macro gets the current and target locations and target frequencies of the current row from the full 1d vector.

    :param this_row: A QUA variable for the current row (int).
    :param nb_of_columns: A python variable for the number of column in the array (int).
    :param current_location_full: A 1D QUA vector for the atom location in the current row (int).
    :param target_location_full: A 1D QUA vector for the target location in the current row (int).
    :param target_frequencies_full: A 1D QUA vector for the target frequencies in the current row (int).

    :return: Three QUA 1D vectors for the atom locations, target locations and target frequencies of the current row.
    """
    # QUA variable containing the current row atom locations
    current_location = declare(int, size=nb_of_columns)
    # QUA variable containing the current row target locations
    target_location = declare(int, size=nb_of_columns)
    # QUA variable containing the current row target frequencies
    target_frequencies = declare(int, size=nb_of_columns)
    # QUA variable for incrementing the number of target frequencies
    freq_count = declare(int)
    assign(freq_count, 0)
    # Qua variable for looping over the columns
    col = declare(int)
    # Loop over the columns for filling the atom and target frequencies for current row
    with for_(col, 0, col < nb_of_columns, col + 1):
        # Initialize the current atom location vector for this row
        assign(
            current_location[col], current_location_full[this_row * nb_of_columns + col]
        )
        # Initialize the target atom location vector for this row
        assign(
            target_location[col], target_location_full[this_row * nb_of_columns + col]
        )
        # Initialize the target frequency vector for this row
        with if_(~(target_frequencies_full[this_row * nb_of_columns + col] == 0)):
            assign(
                target_frequencies[freq_count],
                target_frequencies_full[this_row * nb_of_columns + col],
            )
            assign(freq_count, freq_count + 1)
    return current_location, target_location, target_frequencies


def find_number_of_tweezers(
    atoms_in_current_row, atoms_in_target_row, max_nb_of_tweezers
):
    """
    This macro finds the number of tweezer required for this arrangment sequence based of the number of atoms in the
    target row, the number of atoms in the current row and the number of available tweezers.

    :param atoms_in_current_row: A 1D QUA vector for the atom location in the current row.
    :param atoms_in_target_row: A 1D QUA vector for the atom location in the target row.
    :param max_nb_of_tweezers: A QUA variable for the waximum number of available tweezers (due to the limited number of available pulse processors).

    :return: A QUA variable (int) for the number of tweezers required for achieving the sorting.
    """

    nb_of_tweezers = declare(int)  # Number of available tweezers
    # generating an integer vector of size=3 and storing three values in it
    atoms_or_targets = declare(int, size=3)
    assign(
        atoms_or_targets[0], Math.sum(atoms_in_current_row)
    )  # how many atoms in the current row?
    assign(
        atoms_or_targets[1], Math.sum(atoms_in_target_row)
    )  # how many atoms are in the target state?
    assign(
        atoms_or_targets[2], max_nb_of_tweezers
    )  # what's the max number of tweezers we are allowed to use?
    assign(nb_of_tweezers, Math.min(atoms_or_targets))
    # The number of required tweezers for this row arrangement is the minimum of the number of atoms in the initial
    # configuration, the number of final atoms needed in the ordered row and the number of tweezers available
    return nb_of_tweezers


def assign_tweezers_to_atoms(
    nb_of_tweezers,
    nb_of_tweezers_python,
    atoms_in_current_row,
    current_frequencies,
    target_frequencies,
    tweezer_phases,
    data_stream,
):
    """
    This function finds the atoms in the row and assign one tweezer to each with the corresponding initial frequency
    Will only avoid collisions on left compact targets. Improvement necessary for arbitrary collision free rearrangement

    :param nb_of_tweezers: A QUA variable for the number of required tweezers (int).
    :param nb_of_tweezers_python: A python variable for the maximum number of available tweezers.
    :param atoms_in_current_row: A 1D QUA vector for the atom location in the current row.
    :param current_frequencies: A 1D QUA vector for the frequencies of the atoms in the current row.
    :param target_frequencies: A 1D QUA vector for the frequencies of the atoms in the target row.
    :param tweezer_phases: A 1D QUA vector for the phases of the tweezers for the current row.

    :return: Four QUA 1D vectors for the amplitude, frequencie, phase and detuning of each tweezer to sort the current row.
    """

    # QUA variables declaration
    amplitudes = declare(fixed, size=nb_of_tweezers_python)
    frequencies = declare(int, size=nb_of_tweezers_python)
    phases = declare(fixed, value=phases_list)
    detunings = declare(int, size=nb_of_tweezers_python)
    i = declare(int)
    j = declare(int)
    column = declare(int)

    # Initialize the amplitude vector
    with for_(column, 0, column < nb_of_tweezers_python, column + 1):
        assign(amplitudes[column], 0.0)
    # debugging save to indicate a change of row
    # save(-1, data_stream)
    # scan the atom locations and update the list of tweezers frequencies
    assign(j, 0)  # assigning 0 to the j index
    assign(i, 0)  # assigning 0 to the i index
    # pick up only the amount of atoms you need to fill the target, if there aren't_int enough atoms or tweezers
    # available then pick as many as you can
    with for_(j, 0, j < nb_of_tweezers, j + 1):
        # with while_(j < nb_of_tweezers):
        with if_(atoms_in_current_row[i] == 1):  # if an atom is present in site i
            assign(
                amplitudes[j], 1.0
            )  # set the amplitude of the tweezer to active (=1)
            assign(
                frequencies[j], current_frequencies[i]
            )  # update the tweezer freq with that of atom index
            assign(
                phases[j], tweezer_phases[i]
            )  # update the tweezer phase j with that of the atom index i
            # Set the detuning vector
            assign(detunings[j], target_frequencies[j] - frequencies[j])
            # Save atom to be moved and target to check the tweezer locations
            save(i, data_stream)
            save(j, data_stream)
            # assign(j, j + 1)
        assign(i, i + 1)

    return amplitudes, frequencies, phases, detunings


def assign_tweezers_to_atoms_collision_free(
    nb_of_tweezers,
    nb_of_tweezers_python,
    atoms_in_current_row,
    current_frequencies,
    target_frequencies,
    tweezer_phases,
    atom_target_qua,
    data_stream,
    count_stream,
):
    """
    This function finds the atoms in the row and assign one tweezer to each with the corresponding initial frequency
    Will avoid any collisions from happening when sorting row by row.

    :param nb_of_tweezers: A QUA variable for the number of required tweezers (int).
    :param nb_of_tweezers_python: A python variable for the maximum number of available tweezers.
    :param atoms_in_current_row: A 1D QUA vector for the atom location in the current row.
    :param current_frequencies: A 1D QUA vector for the frequencies of the atoms in the current row.
    :param target_frequencies: A 1D QUA vector for the frequencies of the atoms in the target row.
    :param tweezer_phases: A 1D QUA vector for the phases of the tweezers for the current row.

    :return: Four QUA 1D vectors for the amplitude, frequencie, phase and detuning of each tweezer to sort the current row.
    """
    # QUA variables declaration
    amplitudes = declare(fixed, size=nb_of_tweezers_python)
    frequencies = declare(int, size=nb_of_tweezers_python)
    phases = declare(fixed, value=phases_list)
    detunings = declare(int, size=nb_of_tweezers_python)
    column = declare(int)
    tot_atom_moved = declare(int, value=0)
    assign(tot_atom_moved, 0)  # Total number of atoms moved in this row

    # Initialize the amplitude vector
    with for_(column, 0, column < nb_of_tweezers_python, column + 1):
        assign(amplitudes[column], 0.0)
    # Ending index of the current atom to find when scanning to the left
    previous_atom = declare(int)
    assign(previous_atom, -1)
    # Number of assigned atoms
    atoms_assigned = declare(int)
    assign(atoms_assigned, 0)
    # Flag to exit loops once the tweezer is assigned --> replaces break statement
    current_is_assigned = declare(bool)
    # Remaining atoms to assign (number_of_tweezers - atoms_assigned)
    nb_of_atoms_to_assign = declare(int)
    # Target atoms index
    target_index = declare(int)
    assign(target_index, 0)
    # Current atoms index
    trial_atom = declare(int)
    # Total number of atoms located to the right of the current index
    nb_of_atoms_to_the_right = declare(int)
    # Corresponding index for calculating the previous number
    sum_index = declare(int)
    # Vector used to find the starting index when scanning to the right (max)
    max_comp = declare(int, size=2)
    # starting index when scanning to the right
    max_result = declare(int)
    # debugging save to indicate a change of row
    # save(-1, data_stream)
    # This logic searches for atoms in the target vector and if there are enough atoms on the right to complete
    # the sorting, then assign one tweezer to the closest atom on the left.
    # else, assign one tweezer to the closest atom on the right
    with for_(atoms_assigned, 0, atoms_assigned < nb_of_tweezers, atoms_assigned + 1):
        # with while_(atoms_assigned < nb_of_tweezers):
        # Current tweezer is not assigned yet
        assign(current_is_assigned, False)
        # Increment until one target atom is found --> index = target atom location
        with while_(atom_target_qua[target_index] == 0):
            assign(target_index, target_index + 1)
        # number of remaining atoms to assign
        assign(nb_of_atoms_to_assign, nb_of_tweezers - atoms_assigned)
        # Look in current site and to the left for a suitable atom
        with for_(
            trial_atom,
            target_index,
            (trial_atom > previous_atom) & ~current_is_assigned,
            trial_atom - 1,
        ):
            # Number of current atoms located to the right of the current target atom
            assign(nb_of_atoms_to_the_right, 0)
            with for_(
                sum_index, trial_atom, sum_index < number_of_columns, sum_index + 1
            ):
                assign(
                    nb_of_atoms_to_the_right,
                    nb_of_atoms_to_the_right + atoms_in_current_row[sum_index],
                )
            # If there are more atoms to the right than needed AND  1 atom is here AND this atom is not already assigned
            # Then assign a tweezer to this atom
            with if_(
                (nb_of_atoms_to_the_right >= nb_of_atoms_to_assign)
                & (atoms_in_current_row[trial_atom] == 1)
            ):
                # Keep the atom location for subsequent tweezer assignment
                assign(previous_atom, trial_atom)
                # Update the flag to exit the if statement and simulate a break
                assign(current_is_assigned, True)
        # If no suitable atom was found, look to the right instead
        with if_(~current_is_assigned):
            # Find the center before looking to the right of it
            assign(max_comp[0], previous_atom + 1)
            assign(max_comp[1], target_index + 1)
            assign(max_result, Math.max(max_comp))
            # Look to the right for a suitable atom
            with for_(
                trial_atom,
                max_result,
                (trial_atom < number_of_columns) & ~current_is_assigned,
                trial_atom + 1,
            ):
                # If there is an atom here AND it is not assigned yet, then assign a tweezer to this atom
                with if_((atoms_in_current_row[trial_atom] == 1)):
                    # Keep the atom location for subsequent tweezer assignment
                    assign(previous_atom, trial_atom)
                    # Update the flag to exit the if statement and simulate a break
                    assign(current_is_assigned, True)
        # Once a suitable atom was found, assign a tweezer to it
        with if_(current_is_assigned):
            # Save atom to be moved and target to check the tweezer locations
            save(previous_atom, data_stream)
            save(target_index, data_stream)
            assign(tot_atom_moved, tot_atom_moved + 1)
            # Got to the next target atom
            assign(target_index, target_index + 1)
            # set the amplitude of the tweezer to active (=1)
            assign(amplitudes[atoms_assigned], 1.0)
            # update the tweezer freq with that of atom index
            assign(frequencies[atoms_assigned], current_frequencies[previous_atom])
            # update the tweezer phase j with that of the atom index i
            assign(phases[atoms_assigned], tweezer_phases[previous_atom])
            # Set the detuning vector
            assign(
                detunings[atoms_assigned],
                target_frequencies[atoms_assigned] - frequencies[atoms_assigned],
            )
            # Increment the number of assigned atoms
            # assign(atoms_assigned, atoms_assigned + 1)

    save(tot_atom_moved, count_stream)
    return amplitudes, frequencies, phases, detunings


def calculate_pulse_length(detunings, pulse_duration, max_rate=None):
    """
    This macro derives the maximum and minimum detunings to be applied and derives the minimum chirp pulse duration.

    :param detunings: A 1D QUA vector for each tweezer detuning in Hz (int).
    :param pulse_duration: A python variable for the default constant chirp pulse duration in ns (int).
    :param max_rate: A python variable for the maximum allowed chirp rate in Hz/ns. Default is None which corresponds to using the provided default pulse duration

    :return: A QUA variable for the chirp pulse duration in ns (int)
    """
    # QUA variables declaration
    chirp_pulse_duration = declare(int)  # Duration of the frequency chirp
    # Find the maximum detuning used to set the minimum acceptable pulse duration
    if max_rate is not None:
        min_detuning = declare(int)
        max_detuning = declare(int)
        assign(min_detuning, Math.min(detunings))
        assign(max_detuning, Math.max(detunings))  # find the maximum detuning
        assign(
            max_detuning,
            Util.cond(max_detuning > -min_detuning, max_detuning, -min_detuning),
        )
        assign(chirp_pulse_duration, max_detuning / max_rate)
        # Minimum pulse duration is 16 ns
        with if_(max_detuning < 16):
            assign(chirp_pulse_duration, 16)
        with else_():
            assign(chirp_pulse_duration, max_detuning / max_rate)
    else:
        # pulse duration is assigned to be constant
        assign(chirp_pulse_duration, pulse_duration)

    return chirp_pulse_duration


def calculate_chirp_rates(nb_of_tweezers_python, detunings, pulse_duration):
    """
    This macro derives the constant linear chirp rates needed to arrange the atoms in the current row.

    :param nb_of_tweezers_python: A python variable for the number of available tweezers.
    :param detunings: A 1D QUA vector for each tweezer detuning in Hz (int).
    :param pulse_duration: A QUA variable for the chirp pulse duration in ns (int)

    :return: A QUA 1D vector for each tweezer constant chirp rate in mHz/ns
    """
    # QUA variables declaration
    chirp_rates = declare(int, size=nb_of_tweezers_python)
    j = declare(int)
    # Calculate the chirp rates for all tweezers.
    # Each tweezer has its own chirp rate depending on the initial and final position of the arranged atom.
    with for_(j, 0, j < nb_of_tweezers_python, j + 1):
        assign(
            chirp_rates[j], Cast.to_int(detunings[j] / (pulse_duration / 1000))
        )  # x1000 to go to 'mHz/ns'

    return chirp_rates


def calculate_piecewise_chirp_rates(
    nb_of_tweezers_python, detunings, pulse_duration, nb_of_segments
):
    """
    This macro derives the piecewise decomposition of the total chirp waveform based on the minimum jerk trajectory.

    :param nb_of_tweezers_python: A python variable for the number of available tweezers.
    :param detunings: A 1D QUA vector for each tweezer detuning in Hz (int).
    :param pulse_duration: A QUA variable for the chirp pulse duration in ns (int)
    :param nb_of_segments: A python variable for the number of segments contained in the picewise chirp (int). No gaps if < 50.

    :return: A Python 2D array whose rows are 1D QUA vectors for each tweezer piecewise chirp rate in mHz/ns
    """
    # QUA variables declaration
    n_segment = declare(int, value=nb_of_segments)
    chirp_rates_full = declare(
        int, value=[int(x) for x in np.zeros(nb_of_tweezers_python * nb_of_segments)]
    )
    step = declare(int)
    chirp_rates = [
        declare(int, value=[int(x) for x in np.zeros(nb_of_segments)])
        for _ in range(nb_of_tweezers_python)
    ]
    # Calculate the chirp rates for all Tweezers.
    # Each tweezer has its own chirp rate depending on the initial and final position of the arranged atom.
    tau = declare(fixed)  # Normalized time
    tau_squared = declare(fixed)  # Normalized time squared
    linear_piece = declare(fixed)  # minimal jerk trajectory
    segment_step = declare(int)  # Step variable for incrementing the segments
    one_over_chirp_n_segments = declare(fixed)  # one over the nuber of linear segments
    assign(one_over_chirp_n_segments, Math.div(1, n_segment))
    j = declare(int)

    with for_(j, 0, j < nb_of_tweezers_python, j + 1):
        assign(tau, 0)
        with for_(segment_step, 0, segment_step < n_segment, segment_step + 1):
            assign(
                tau, Cast.mul_fixed_by_int(one_over_chirp_n_segments, segment_step + 1)
            )
            assign(tau_squared, tau * tau)
            assign(
                linear_piece,
                (
                    Cast.mul_fixed_by_int(tau_squared, 30)
                    - Cast.mul_fixed_by_int(tau_squared * tau, 60)
                    + Cast.mul_fixed_by_int(tau_squared * tau_squared, 30)
                ),
            )
            assign(
                chirp_rates_full[segment_step + j * n_segment],
                Cast.to_int(
                    Cast.mul_int_by_fixed(detunings[j], linear_piece)
                    / (pulse_duration / 1000)
                ),
            )  # /1000 to go to 'mHz/ns'
    # Build a 1D chirp vector for each tweezer in a given row. 1st index must be python and 2nd QUA (fake 2D array)
    for tweezer_index in range(nb_of_tweezers_python):
        with for_(step, 0, step < n_segment, step + 1):
            assign(
                chirp_rates[tweezer_index][step],
                chirp_rates_full[tweezer_index * n_segment + step],
            )

    return chirp_rates


def set_tweezers_frequencies_and_phases(
    nb_of_tweezers_python, current_frequencies, row_frequency, tweezer_phases
):
    """
    This macro sets the previously calculated frequencies and phases to the corresponding tweezers.

    :param nb_of_tweezers_python: A python variable for the maximum number of available tweezers.
    :param current_frequencies: A 1D QUA vector for the frequencies of the atoms in the current row.
    :param row_frequency: A QUA variable for the frequency of the current row in Hz (int)
    :param tweezer_phases: A 1D QUA vector for the phases of the tweezers for the current row.

    :return: None
    """
    # set the phases and frequencies of the tweezers
    update_frequency("row_selector", row_frequency)
    for index in range(nb_of_tweezers_python):
        reset_frame(f"column_{index + 1}")
        frame_rotation(tweezer_phases[index + 1], "column_{}".format(index + 1))
        update_frequency("column_{}".format(index + 1), current_frequencies[index])


def print_2d(matrix):
    """
    Nicely prints a 2D array
    :param matrix: 2D python array
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f"{matrix[i][j]}\t", end="")
        print("")
