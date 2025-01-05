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

# # matplotlib.use('TkAgg')


###################
# The QUA program #
###################

qubit = "qubit1"
plungers = "P1-P2"
do_feedback = False # False for test. True for actual.
full_read_init = False
num_output_streams = 6 if full_read_init else 2
do_simulate = True

list_n_shots = [10, 100]
df_enc_seqs = get_dataframe_encoded_sequence()
sequence_max_len = 2 + df_enc_seqs["full_sequence_length"].max() # 2 for circ_idx and circ_len
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
duration_compensation_pulse = int(0.3 * duration_compensation_pulse_full_initialization + duration_compensation_pulse_gst + duration_compensation_pulse_full_readout)
duration_compensation_pulse = 100 * (duration_compensation_pulse // 100)

seq.add_points("operation_P1-P2", level_ops["P1-P2"], duration_gst)
seq.add_points("operation_P4-P5", level_ops["P4-P5"], duration_gst)
seq.add_points("operation_P3", level_ops["P3"], duration_gst)

save_data_dict = {
    "sweep_gates": sweep_gates,
    "qubit": qubit,
    "config": config,
}


with program() as PROGRAM_GST:
    n = declare(int)
    n_shots = declare(int)
    circ = declare(int)
    case_idx = declare(int)
    count = declare(int, value=0)
    division = declare(int, value=1)

    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    n_shots_st = declare_stream()
    circ_idx_st = declare_stream()
    circ_len_st = declare_stream()
    
    I = [declare(fixed) for _ in range(num_tank_circuits)]
    Q = [declare(fixed) for _ in range(num_tank_circuits)]
    P = [declare(bool) for _ in range(num_tank_circuits)]  # true if even parity
    I_st = [declare_stream() for _ in range(num_output_streams)]
    Q_st = [None for _ in range(num_output_streams)]
    P_st = [None for _ in range(num_output_streams)]
    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit1", I[0], Q[0], P[0])
    assign_variables_to_element("tank_circuit2", I[1], Q[1], P[1])

    if do_simulate:
        encoded_circuit = declare(int, value=[112, 8195, 9, 4, 4, 4, 4, 5] + [0] * 8188 + [1])
    else:
        encoded_circuit = declare_input_stream(
            int,
            name="_encoded_circuit",
            size=sequence_max_len + 3, # 2 to account for [circ_idx, seq_len, remaining_duraiton_case]
        )  # input stream the sequence


    with for_each_(n_shots, list_n_shots):

        with for_(circ, 0, circ < num_cicuits, circ + 1):
            
            if not do_simulate:
                advance_input_stream(encoded_circuit)  # ordered or randomized

            circ_idx = encoded_circuit[0] # just a sequential index for this circuit 
            circ_len = encoded_circuit[1] # gate sequence length for this circuit

            with for_(n, 0, n < n_shots, n + 1):
                assign(count, count + 1)

                with strict_timing_():

                    if full_read_init:
                        # RI12 -> 2 x (R3 -> R12) -> RI45
                        perform_initialization(I, Q, P, I_st, Q_st, P_st)
                    else:
                        # RI12
                        read_init12(I[0], Q[0], P[0], None, None, None, I_st[0], None, None, do_save=[False, True])

                    # Navigate through the charge stability map
                    seq.add_step(voltage_point_name=f"operation_{plungers}")
                    wait(delay_gst_start * u.ns, qubit) if delay_gst_start >= 16 else None

                    other_elements = get_other_elements(elements_in_use=[qubit] + sweep_gates, all_elements=all_elements)
                    wait(duration_gst * u.ns, *other_elements)

                    with for_(case_idx, 2, case_idx < circ_len + 2, case_idx + 1):

                        with switch_(encoded_circuit[case_idx], unsafe=True):
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
                                play("x90_kaiser", qubit)
                                play("x90_kaiser", qubit)
                                play("x90_kaiser", qubit)
                                play("x90_kaiser", qubit)
                            with case_(5):
                                play("x90_kaiser", qubit)
                            with case_(6):
                                play("y90_kaiser", qubit)
                            with case_(7):
                                play("x90_kaiser", qubit)
                                play("x90_kaiser", qubit)
                            with case_(8):
                                play("x90_kaiser", qubit)
                                play("y90_kaiser", qubit)
                            with case_(9):
                                play("x90_kaiser", qubit)
                                play("x90_kaiser", qubit)
                                play("x90_kaiser", qubit)
                            with case_(10):
                                play("y90_kaiser", qubit)
                                play("y90_kaiser", qubit)
                                play("y90_kaiser", qubit)
                            with case_(11):
                                play("x90_kaiser", qubit)
                                play("x90_kaiser", qubit)
                                play("y90_kaiser", qubit)

                    wait(delay_gst_end * u.ns, qubit) if delay_gst_end >= 16 else None

                    if full_read_init:
                        # RI12 -> R3 -> RI45
                        perform_readout(I, Q, P, I_st, Q_st, P_st)
                    else:
                        # RI12
                        read_init12(I[0], Q[0], P[0], I_st[1], None, None, None, None, None, do_save=[True, False])

                    seq.add_compensation_pulse(duration=duration_compensation_pulse)
                
                save(n, n_st)
                save(n_shots, n_shots_st)
                save(circ_idx, circ_idx_st)

                seq.ramp_to_zero()
                wait(1000 * u.ns)

            with if_(count == division * batch_size):
                assign(division, division + 1)
                # pause to outstream the data
                pause()


    with stream_processing():
        n_st.buffer(batch_size).save("n_history")
        n_shots_st.buffer(batch_size).save("n_shots_history")
        circ_idx_st.buffer(batch_size).save("circ_idx_history")
        for k in range(num_output_streams):
            I_st[k].buffer(batch_size).save(f"I{k:d}")
            # Q_st[k].buffer(batch_size).save(f"Q{k:d}")
            # P_st[k].boolean_to_int().buffer(batch_size).save(f"P{k:d}")


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
simulate = do_simulate
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=4_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, PROGRAM_GST, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    from qm import generate_qua_script

    sourceFile = open("debug_20b_gate_set_tomography.py", "w")
    print(generate_qua_script(PROGRAM_GST, config), file=sourceFile)
    sourceFile.close()

    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PROGRAM_GST, compiler_options=CompilerOptionArguments(flags=["not-strict-timing"]))


    fetch_names = ["n_history", "n_shots_history", "circ_idx_history"]
    fetch_names.extend([f"I{k:d}" for k in range(num_output_streams)])
    # fetch_names.extend([f"Q{k:d}" for k in range(num_output_streams)])
    # fetch_names.extend([f"P{k:d}" for k in range(num_output_streams)])

    if save_data:
        from qualang_tools.results.data_handler import DataHandler
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        data_handler.create_data_folder(name=Path(__file__).stem)


    batch_idx = 1
    ress = []
    start_time = datetime.now()
    for _n_shots in list_n_shots:
        this_df = df_enc_seqs.sample(frac=1, random_state=_n_shots)

        for i_row, (_, row) in enumerate(this_df.iterrows()):
            _encoded_circuit, seq_len, C, P, G, d, M, Ph4, Ph = get_encoded_circuit(row)

            current_datetime = datetime.now()
            current_datetime_str = current_datetime.strftime("%Y/%m/%d-%H:%M:%S")
            elapsed_time = current_datetime - start_time
            elapsed_time_secs = int(elapsed_time.total_seconds())
            _log_this = f"{current_datetime_str}, batch_idx: {batch_idx} / {num_batches}, no: {i_row + 1}, n_shots: {_n_shots}, seq_len: {seq_len}, circ_idx = {C}, n_circuits: P={P}, G={G}, d={d}, M={M}, Ph4={Ph4}, Ph={Ph}, elapsed_secs: {elapsed_time_secs}"
            print(_log_this)
            with open(data_handler.path / "log.txt", encoding="utf8", mode="a") as f:
                f.write(_log_this.replace("_", "") + "\n")  # Append the log message to the file

            job.push_to_input_stream("_encoded_circuit", _encoded_circuit)

            if job.is_paused():

                # Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
                if batch_idx == 1:
                    print("get a fetching tool")
                    results = fetching_tool(job, data_list=fetch_names, mode="live")

                # Fetch results
                print("fetch result!")
                res = results.fetch_all()
                ress.append(res)
                data_dict = {name: arr for name, arr in zip(fetch_names, res)}

                # Data to save
                print("save result!")
                np.savez(file = data_handler.path / f"data_{batch_idx:08d}.npz", **data_dict)
                batch_idx +=1
                job.resume()

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    data_handler.additional_files = {
        script_name: script_name,
        "macros_initialization_and_readout.py": "macros_initialization_and_readout.py"
        **default_additional_files,
    }
    data_handler.save_data(data=save_data_dict, name=Path(__name__).stem)

    qm.close()

# %%
