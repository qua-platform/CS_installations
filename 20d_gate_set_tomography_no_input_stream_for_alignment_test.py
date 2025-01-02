# %%

import math
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from qm import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.addons.variables import assign_variables_to_element
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter, wait_until_job_is_paused
from qualang_tools.voltage_gates import VoltageGateSequence
from macros import get_other_elements

from macros_initialization_and_readout import *
from configuration_with_lffem import *

matplotlib.use('TkAgg')


###################
# The QUA program #
###################

qubit = "qubit1"
plungers = "P1-P2"
do_feedback = False # False for test. True for actual.
full_read_init = False
num_output_streams = 6 if full_read_init else 2
simulate = True

list_n_shots = [2]
df_enc_seqs = get_dataframe_encoded_sequence()
sequence_max_len = 1 + 3 + 1
num_cicuits = len(df_enc_seqs)
batch_size = max(list_n_shots)
result_array_len = num_cicuits * sum(list_n_shots)
result_array_len = batch_size * math.ceil(result_array_len / batch_size)
num_batches = math.ceil(result_array_len / batch_size)

# duration_init includes the manipulation
max_gate_counts = 4 + int(df_enc_seqs["full_native_gate_count"].max())
max_gate_duration = max_gate_counts * PI_HALF_LEN
delay_gst_start = 16
delay_gst_end = 16
duration_gst = delay_init_qubit_start + max_gate_duration + delay_init_qubit_end

duration_compensation_pulse_gst = duration_gst
duration_compensation_pulse_full = int(0.3 * duration_compensation_pulse_initialization + duration_compensation_pulse_gst + duration_compensation_pulse_readout)
duration_compensation_pulse_full = 100 * (duration_compensation_pulse_full // 100)

seq.add_points("operation_P1-P2", level_ops["P1-P2"], duration_gst)
seq.add_points("operation_P4-P5", level_ops["P4-P5"], duration_gst)
seq.add_points("operation_P3", level_ops["P3"], duration_gst)


with program() as PROGRAM_GST:
    n = declare(int)
    n_shots = declare(int)
    circ = declare(int)
    idx = declare(int)
    count = declare(int, value=0)
    division = declare(int, value=1)
    encoded_circuit = declare(int, value=[52, 4, 5, 7, 11, 2])
    # encoded_circuit = declare(int, value=[52, 4, 0, 0, 0, 0])

    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    n_shots_st = declare_stream()
    circ_idx_st = declare_stream()
    circ_len_st = declare_stream()
    
    I = [declare(fixed) for _ in range(num_tank_circuits)]
    Q = [declare(fixed) for _ in range(num_tank_circuits)]
    P = [declare(bool) for _ in range(num_tank_circuits)]  # true if even parity
    I_st = [declare_stream() for _ in range(num_output_streams)]
    # Q_st = [declare_stream() for _ in range(num_output_streams)]
    # P_st = [declare_stream() for _ in range(num_output_streams)]

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit1", I[0], Q[0], P[0])
    assign_variables_to_element("tank_circuit2", I[1], Q[1], P[1])

    with for_each_(n_shots, list_n_shots):

        with for_(circ, 0, circ < num_cicuits, circ + 1):

            circ_idx = encoded_circuit[0] # just a sequential index for this circuit 
            circ_len = encoded_circuit[1] # gate sequence length for this circuit

            with for_(n, 0, n < n_shots, n + 1):
                assign(count, count + 1)

                with strict_timing_():

                    if full_read_init:
                        # RI12 -> 2 x (R3 -> R12) -> RI45
                        perform_initialization(I, Q, P, I_st[0], I_st[1], I_st[2])
                    else:                    # RI12 -> 2 x (R3 -> R12) -> RI45
                        # RI12
                        read_init12(I[0], Q[0], P[0], None, I_st[0], do_save=[False, True])

                    # Navigate through the charge stability map
                    seq.add_step(voltage_point_name=f"operation_{plungers}")
                    wait(delay_init_qubit_start * u.ns, qubit) if delay_init_qubit_start >= 16 else None

                    other_elements = get_other_elements(elements_in_use=[qubit] + sweep_gates, all_elements=all_elements)
                    wait(duration_gst * u.ns, *other_elements)

                    with for_(idx, 2, idx < circ_len + 2, idx + 1):

                        with switch_(encoded_circuit[idx], unsafe=True):
                            # baseband operation is fixed regardless L
                            # normal:just run till the end with Null
                            # option: adjust the length accoridngly

                            with case_(0):
                                wait(4 * PI_HALF_LEN * u.ns, qubit)
                            with case_(1):
                                wait(PI_HALF_LEN * u.ns, qubit)
                            with case_(2):
                                wait(2 * PI_HALF_LEN * u.ns, qubit)
                            with case_(3):
                                wait(3 * PI_HALF_LEN * u.ns, qubit)
                            
                            # '{}': 4, # I
                            # 'Gxpi2:0': 5,
                            # 'Gypi2:0': 6,
                            # 'Gxpi2:0Gxpi2:0': 7,
                            # 'Gxpi2:0Gxpi2:0Gxpi2:0': 9,
                            # 'Gypi2:0Gypi2:0Gypi2:0': 10,
                            # 'Gxpi2:0Gypi2:0': 8,
                            # 'Gxpi2:0Gxpi2:0Gypi2:0': 11
                            
                            # prep & meas fiducials and germs
                            with case_(4): #   I = XXXX
                                play("x90_square", qubit)
                                play("x90_square", qubit)
                                play("x90_square", qubit)
                                play("x90_square", qubit)
                            with case_(5):
                                play("x90_square", qubit)
                            with case_(6):
                                play("y90_square", qubit)
                            with case_(7):
                                play("x90_square", qubit)
                                play("x90_square", qubit)
                            with case_(8):
                                play("x90_square", qubit)
                                play("y90_square", qubit)
                            with case_(9):
                                play("x90_square", qubit)
                                play("x90_square", qubit)
                                play("x90_square", qubit)
                            with case_(10):
                                play("y90_square", qubit)
                                play("y90_square", qubit)
                                play("y90_square", qubit)
                            with case_(11):
                                play("x90_square", qubit)
                                play("x90_square", qubit)
                                play("y90_square", qubit)

                    wait(delay_init_qubit_end * u.ns, qubit) if delay_init_qubit_start >= 16 else None

                    if full_read_init:
                        # RI12 -> R3 -> RI45
                        perform_readout(I, Q, P, I_st[3], I_st[4], I_st[5])
                    else:
                        # RI12
                        read_init12(I[0], Q[0], P[0], I_st[1], None, do_save=[True, False])

                    seq.add_compensation_pulse(duration=duration_compensation_pulse_full)
                
                save(n, n_st)
                save(n_shots, n_shots_st)
                save(circ_idx, circ_idx_st)

                seq.ramp_to_zero()
                wait(1000 * u.ns)

            # with if_(count == division * batch_size):
            #     assign(division, division + 1)
            #     # pause to outstream the data
            #     pause()


    with stream_processing():
        n_st.buffer(batch_size).save("n_history")
        n_shots_st.buffer(batch_size).save("n_shots_history")
        circ_idx_st.buffer(batch_size).save("circ_idx_history")
        for k in range(num_output_streams):
            I_st[k].buffer(batch_size).save(f"I{k:d}")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)
qmm.clear_all_job_results()
qmm.close_all_qms()


###########################
# Run or Simulate Program #
###########################
simulate = True
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=6_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, PROGRAM_GST, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PROGRAM_GST, compiler_options=CompilerOptionArguments(flags=["not-strict-timing"]))
    # job = qm.execute(PROGRAM)

# %%