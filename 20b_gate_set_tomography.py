# %%
import math

# from configuration_gst_opxplus import *
import matplotlib.pyplot as plt
import pandas as pd
from qm import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.voltage_gates import VoltageGateSequence

# from configuration_gst_lffem import *
from configuration_with_lffem import *



path = "./encoded_parsed_dataset.csv"
df = pd.read_csv(path, header=0)  # Use header=0 to indicate the first row is the header
df["full_gate_sequence_duration"] = PI_HALF_LEN * df["full_native_gate_count"]
df.reset_index(inplace=True)
df = df.tail(60)
df = df.head(10)


###################
# The QUA program #
###################

qubit = "qubit3"
tank_circuit = "tank_circuit1"
measure_init = True
sweep_gates = ["P1_sticky", "P2_sticky"]

list_n_shots = [10, 100]
sequence_max_len = 1 + 8192 + 1
num_cicuits = len(df)

# duration_init includes the manipulation
delay_init_qubit = 16 # TODO: replace 
delay_qubit_read = 16 # TODO: replace 
max_gate_counts = df["full_native_gate_count"].max()
max_gate_duration = max_gate_counts * PI_HALF_LEN
duration_init = delay_init_qubit + max_gate_duration + delay_qubit_read
assert delay_init_qubit == 0 or delay_init_qubit >= 16
assert delay_qubit_read == 0 or delay_qubit_read >= 16

duration_compensation_pulse_readinit = 4 * u.us
duration_compensation_pulse_gst = duration_init

# Add the relevant voltage points describing the "slow" sequence (no qubit pulse)
seq = VoltageGateSequence(config, sweep_gates)
seq.add_points("initialization", level_init, duration_init)
seq.add_points("readout", level_readout, duration_readout)


with program() as PROGRAM:
    n = declare(int)
    n_shots = declare(int)
    circ = declare(int)
    idx = declare(int)
    encoded_circuit = declare_input_stream(
        int,
        name="_encoded_circuit_input_stream",
        size=sequence_max_len + 2, # 2 to account for [circ_idx, seq_len]
    )  # input stream the sequence
    idx_st = declare_stream()

    with for_each_(n_shots, list_n_shots):
        with for_(circ, 0, circ < num_cicuits, circ + 1):
            advance_input_stream(encoded_circuit)  # ordered or randomized

            circ_idx = encoded_circuit[0] # just a sequential index for this circuit 
            circ_len = encoded_circuit[1] # gate sequence length for this circuit

            with for_(n, 0, n < n_shots, n + 1):
                
                # play("square_const", qubit)
                # play("square_step", "P1", duration=const_len * u.ns)

                with strict_timing_():

                    # TODO: Implement initialization
                    # perform_read_init_12()
                    # perform_read_init_3()
                    # perform_read_init_12()
                    # perform_read_init_3()
                    # perform_read_init_12()
                    # perform_read_init_45()


                    # Navigate through the charge stability map
                    seq.add_step(voltage_point_name="initialization")  # includes manipulation
                    seq.add_step(voltage_point_name="readout")
                    seq.add_compensation_pulse(duration=duration_compensation_pulse_gst)
                    
                    # wait((duration_init - const_len) * u.ns, qubit)
                    wait(duration_init // 4, qubit)

                    # with for_(idx, 2, idx < circ_len + 2, idx + 1):
                    with for_(idx, 2, idx < sequence_max_len + 2, idx + 1):
                        with switch_(encoded_circuit[idx], unsafe=True):
                            # baseband operation is fixed regardless L
                            # normal:just run till the end with Null
                            # option: adjust the length accoridngly

                            with case_(0):
                                # TODO: initialization step
                                wait(PI_HALF_LEN * u.ns, qubit)

                            # prep fiducials
                            with case_(1): #   I = XXXX
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                            with case_(2):
                                play("square_x90", qubit)
                            with case_(3):
                                play("square_y90", qubit)
                            with case_(4):
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                            with case_(5):
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                            with case_(6):
                                play("square_y90", qubit)
                                play("square_y90", qubit)
                                play("square_y90", qubit)

                            # germs
                            with case_(7): #   I = XXXX
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                            with case_(8):
                                play("square_x90", qubit)
                            with case_(9):
                                play("square_y90", qubit)
                            with case_(10):
                                play("square_x90", qubit)
                                play("square_y90", qubit)
                            with case_(11):
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                                play("square_y90", qubit)

                            # meas fiducial
                            with case_(12): #   I = XXXX
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                            with case_(13):
                                play("square_x90", qubit)
                            with case_(14):
                                play("square_y90", qubit)
                            with case_(15):
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                            with case_(16):
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                            with case_(17):
                                play("square_y90", qubit)
                                play("square_y90", qubit)
                                play("square_y90", qubit)

                    # TODO: Implement readout
                    # perform_read_init_12()
                    # perform_read_init_3()
                    # perform_read_init_45()


            save(n_shots, idx_st)
            save(circ_idx, idx_st)
            save(circ_len, idx_st)
            wait(1000)

    with stream_processing():
        idx_st.buffer(3).save_all("idx_history")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)


###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, PROGRAM, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()
    plt.show()

else:
    # from qm import generate_qua_script

    # sourceFile = open("debug08.py", "w")
    # print(generate_qua_script(PROGRAM, config), file=sourceFile)
    # sourceFile.close()

    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(
        PROGRAM, compiler_options=CompilerOptionArguments(flags=["not-strict-timing"])
    )
    # job = qm.execute(PROGRAM)

    res_handles = job.result_handles
    # Waits (blocks the Python console) until all results have been acquired
    # results = fetching_tool(job, data_list=["circuit_history"], mode="live")

    record = []
    for _n_shots in list_n_shots:
        encoded_circuit_batch = df[
            ["index", "P_enc_seq", "G_enc_seq", "d_enc_seq", "M_enc_seq", "full_gate_sequence_duration"]
            ].sample(frac=1, random_state=_n_shots)

        for i, row in encoded_circuit_batch.iterrows():
            P = int(row["P_enc_seq"])
            G = int(row["G_enc_seq"])
            d = int(row["d_enc_seq"])
            M = int(row["M_enc_seq"])
            D = int(row["full_gate_sequence_duration"])

            seq_len = 0
            _encoded_circuit_input_stream = [i]
            if P != -1:
                _encoded_circuit_input_stream.append(P)
                seq_len += 1
            if G != -1:
                _encoded_circuit_input_stream.extend([G] * d)
                seq_len += d
            if M != -1:
                _encoded_circuit_input_stream.append(M)
                seq_len += 1

            # sequence length
            _encoded_circuit_input_stream.insert(1, seq_len)

            # # sequence duration
            # _encoded_circuit_input_stream.insert(2, D)

            record.append([_n_shots] + _encoded_circuit_input_stream)

            print(f"n_shots: {_n_shots}, circ_idx = {i}, n_circuits: P={P}, G={G}, d={d}, M={M}")
            job.push_to_input_stream("_encoded_circuit_input_stream", _encoded_circuit_input_stream)
            print("    ---> success!")

    idx_history = res_handles.get("idx_history").fetch_all()

    qm.close()
# %%
