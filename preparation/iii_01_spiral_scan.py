from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig, LoopbackInterface
from configuration_OPX1000 import *
from qualang_tools.results import fetching_tool
from qualang_tools.addons.variables import assign_variables_to_element
import matplotlib.pyplot as plt
import numpy as np
import plotly.io as pio
pio.renderers.default='browser'

def round_to_fixed(x, number_of_bits=12):
    """
    function which rounds 'x' to 'number_of_bits' of precision to help reduce the accumulation of fixed point arithmetic errors
    """
    return round((2**number_of_bits) * x) / (2**number_of_bits)


def measurement_macro(measured_element, I, I_stream, Q, Q_stream):
    measure(
        "readout",
        measured_element,
        None,
        demod.full("cos", I, "out1"),
        demod.full("cos", Q, "out1"),
    )
    save(I, I_stream)
    save(Q, Q_stream)


def spiral_order(N: int):
    # casting to int if necessary
    if not isinstance(N, int):
        N = int(N)
    # asserting that N is odd
    N = N if N % 2 == 1 else N + 1

    # setting i, j to be in the middle of the image
    i, j = (N - 1) // 2, (N - 1) // 2

    # creating array to hold the ordering
    order = np.zeros(shape=(N, N), dtype=int)

    sign = +1  # the direction which to move along the respective axis
    number_of_moves = 1  # the number of moves needed for the current edge
    total_moves = 0  # the total number of moves completed so far

    # spiralling outwards along x edge then y
    while total_moves < N**2 - N:
        for _ in range(number_of_moves):
            i = i + sign  # move one step in left (sign = -1) or right (sign = +1)
            total_moves = total_moves + 1
            order[i, j] = total_moves  # updating the ordering array

        for _ in range(number_of_moves):
            j = j + sign  # move one step in down (sign = -1) or up (sign = +1)
            total_moves = total_moves + 1
            order[i, j] = total_moves
        sign = sign * -1  # the next moves will be in the opposite direction
        number_of_moves = number_of_moves + 1  # the next edges will require one more step

    # filling the final x edge, which cannot cleanly be done in the above while loop
    for _ in range(number_of_moves - 1):
        i = i + sign  # move one step in left (sign = -1) or right (sign = +1)
        total_moves = total_moves + 1
        order[i, j] = total_moves

    return order
# get the config
config = get_config(sampling_rate=1e9)

###################
# The QUA program #
###################
#################################
#        spiral scan            #
#################################
Vx_center = 0.0
Vx_span = 0.2
Vy_center = 0.0
Vy_span = 0.1
N = 21
Vx_setpoints = np.linspace(Vx_center - Vx_span / 2, Vx_center + Vx_span / 2, N)
Vy_setpoints = np.linspace(Vy_center - Vy_span / 2, Vy_center + Vy_span / 2, N)
wait_time = 100
n_avg = 1
# Check that the resolution is odd to form the spiral
assert N % 2 == 1, "the parameter 'N' must be odd {}".format(N)

# Get the gate pulse amplitude and derive the voltage step
pulse = config["elements"]["lf_element_1_sticky"]["operations"]["bias"]
wf = config["pulses"][pulse]["waveforms"]["single"]
V_step = config["waveforms"][wf].get("sample")
dx = round_to_fixed(Vx_span / ((N - 1) * config["waveforms"][wf].get("sample")))
dy = round_to_fixed(Vy_span / ((N - 1) * config["waveforms"][wf].get("sample")))


def spiral_scan(x_element, y_element, readout_element, simulate=False):
    with program() as prog:
        i = declare(int)  # an index variable for the x index
        j = declare(int)  # an index variable for the y index
        Vx = declare(fixed)  # a variable to keep track of the Vx coordinate
        Vy = declare(fixed)  # a variable to keep track of the Vy coordinate
        last_row = declare(bool)
        Vx_st = declare_stream()
        Vy_st = declare_stream()
        average = declare(int)  # an index variable for the average

        moves_per_edge = declare(int)  # the number of moves per edge [1, N]
        completed_moves = declare(int)  # the number of completed move [0, N ** 2]
        movement_direction = declare(fixed)  # which direction to move {-1., 1.}

        # declaring the measured variables and their streams
        I, Q = declare(fixed), declare(fixed)
        I_st, Q_st = declare_stream(), declare_stream()
        with infinite_loop_():
            if not simulate:
                pause()
            with for_(average, 0, average < n_avg, average + 1):
                # initialising variables
                assign(moves_per_edge, 1)
                assign(completed_moves, 0)
                assign(movement_direction, +1)
                assign(Vx, 0.0)
                assign(Vy, 0.0)
                assign(last_row, False)

                ramp_to_zero(x_element)
                ramp_to_zero(y_element)
                align(x_element, y_element, readout_element)
                # for the first pixel it is unnecessary to move before measuring
                measurement_macro(readout_element, I, I_st, Q, Q_st)
                save(Vx, Vx_st)
                save(Vy, Vy_st)

                with while_(completed_moves < N**2 - 1):
                    # for_ loop to move the required number of moves in the x direction
                    with for_(i, 0, i < moves_per_edge, i + 1):
                        assign(Vx, Vx + movement_direction * dx * V_step)
                        # if the x coordinate should be 0, ramp to zero to remove fixed point arithmetic errors accumulating
                        with if_(Vx == 0.0):
                            ramp_to_zero(x_element)
                        # playing the constant pulse to move to the next pixel
                        with else_():
                            play("bias" * amp(movement_direction * dx), x_element)
                        # Make sure that we measure after the pulse has settled
                        align(x_element, y_element, readout_element)
                        # if logic to enable wait_time = 0 without error
                        if wait_time >= 4:
                            wait(wait_time // 4, readout_element)
                        # Measurement
                        measurement_macro(readout_element, I, I_st, Q, Q_st)
                        save(Vx, Vx_st)
                        save(Vy, Vy_st)
                    # for_ loop to move in the y direction except for the last step which is only along x
                    with if_(~last_row):
                        with for_(j, 0, j < moves_per_edge, j + 1):
                            assign(Vy, Vy + movement_direction * dy * V_step)
                            # if the y coordinate should be 0, ramp to zero to remove fixed point arithmetic errors accumulating
                            with if_(Vy == 0.0):
                                ramp_to_zero(y_element)
                            # playing the constant pulse to move to the next pixel
                            with else_():
                                play("bias" * amp(movement_direction * dy), y_element)
                            # Make sure that we measure after the pulse has settled
                            align(x_element, y_element, readout_element)
                            # if logic to enable wait_time = 0 without error
                            if wait_time >= 4:
                                wait(wait_time // 4, readout_element)
                            # Measurement
                            measurement_macro(readout_element, I, I_st, Q, Q_st)
                            save(Vx, Vx_st)
                            save(Vy, Vy_st)
                        # updating the variables
                        # * 2 because moves in both x and y
                        assign(completed_moves, completed_moves + 2 * moves_per_edge)
                        # *-1 as subsequent steps in the opposite direction
                        assign(movement_direction, movement_direction * -1)
                        # moving one row/column out so need one more move_per_edge except for the last step which is N-1
                        with if_(moves_per_edge < N - 1):
                            assign(moves_per_edge, moves_per_edge + 1)
                        with else_():
                            assign(last_row, True)
                    with else_():
                        # updating the variables
                        # * 1 because moves only along x
                        assign(completed_moves, completed_moves + moves_per_edge)

                # aligning and ramping to zero to return to initial state
                align(x_element, y_element, readout_element)
                ramp_to_zero(x_element)
                ramp_to_zero(y_element)

        with stream_processing():
            I_st.buffer(N**2).buffer(n_avg).map(FUNCTIONS.average()).save_all("I")
            Q_st.buffer(N**2).buffer(n_avg).map(FUNCTIONS.average()).save_all("Q")
            Vx_st.buffer(N**2).buffer(n_avg).map(FUNCTIONS.average()).save_all("x")
            Vy_st.buffer(N**2).buffer(n_avg).map(FUNCTIONS.average()).save_all("y")
    return prog


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    qua_prog = qua_program = spiral_scan(
        "lf_element_1_sticky", "lf_element_2_sticky", "lf_readout_element", simulate=True
    )
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=100_000,
                                         simulation_interface=LoopbackInterface(
                                        latency=280,
                                        connections=[
                                            ("con1", 2, 1, "con1", 2, 1),
                                            ("con1", 2, 2, "con1", 2, 1),
                                        ],  # connecting output 4 to input 1
            ),)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, qua_prog, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    # Get the waveform report
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)
    # fetching the data
    result_handles = job.result_handles
    result_handles.wait_for_all_values()
    I_handle, Q_handle, x_handle, y_handle = (
        result_handles.I,
        result_handles.Q,
        result_handles.x,
        result_handles.y,
    )
    I, Q, x, y = (
        I_handle.fetch_all(),
        Q_handle.fetch_all(),
        x_handle.fetch_all(),
        y_handle.fetch_all(),
    )
    # reshaping the data into the correct order and shape
    order = spiral_order(np.sqrt(I.size))
    I = I[order]
    Q = Q[order]
    plt.figure()
    plt.pcolor(Vx_setpoints, Vy_setpoints, I)
    plt.pcolor(Vx_setpoints, Vy_setpoints, Q)
else:
    qua_prog = qua_program = spiral_scan(
        "lf_element_1_sticky", "lf_element_2_sticky", "lf_readout_element", simulate=False
    )
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(qua_prog)
    # Get results from QUA program


