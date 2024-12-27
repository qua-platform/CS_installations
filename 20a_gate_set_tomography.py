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
from configuration_gst_lffem_gates import *

path = "gate_set_tomography/encoded_parsed_dataset.csv"
dg = pd.read_csv(path, header=0)  # Use header=0 to indicate the first row is the header
dg.reset_index(inplace=True)
dg = dg.tail(60)
dg = dg.head(10)



###################
# The QUA program #
###################

list_n_shots = [10, 100]
# gst_parser = GSTParser()
# list_circuits = gst_parser.get_encoded_circuits()
sequence_max_len = 2 + 1 + 8192 + 1
list_circuits = dg[["index", "P", "G", "d", "M"]].values.tolist()
list_encoded_circuits = dg[
    ["index", "P_enc", "G_enc", "d_enc", "M_enc"]
].values.tolist()
num_cicuits = len(list_encoded_circuits)
qb = "qubit"


# Delay in ns before stepping to the readout point after playing the qubit pulse - must be a multiple of 4ns and >= 16ns
# Relevant points in the charge stability map as ["P1", "P2"] in V
level_init = [0.1, -0.1]
level_manip = [0.05, -0.05]
level_readout = [0.0, 0.0]

# Duration of each step in ns
duration_init = 400
duration_manip = 400
duration_readout = reflectometry_readout_len + 100
duration_compensation_pulse = 400 * u.us

delay_before_readout = 16

# Add the relevant voltage points describing the "slow" sequence (no qubit pulse)
seq = VoltageGateSequence(config, sweep_gates)
seq.add_points("initialization", level_init, duration_init)
seq.add_points("manipulation", level_manip, duration_manip)
seq.add_points("readout", level_readout, duration_readout)



with program() as PROGRAM:
    n = declare(int)
    n_shots = declare(int)
    circ = declare(int)
    idx = declare(int)
    encoded_circuit = declare_input_stream(
        int,
        name="_encoded_circuit_input_stream",
        size=sequence_max_len,
    )  # input stream the sequence
    idx_st = declare_stream()

    with for_each_(n_shots, list_n_shots):
        with for_(circ, 0, circ < num_cicuits, circ + 1):
            advance_input_stream(encoded_circuit)  # ordered or randomized

            circ_idx = encoded_circuit[0]
            circ_len = encoded_circuit[1]

            with for_(n, 0, n < n_shots, n + 1):
                
                # play("const", qb)
                # play("step", "P1", duration=const_len * u.ns)

                with strict_timing_():
                    
                    # Navigate through the charge stability map
                    seq.add_step(voltage_point_name="initialization")  # includes manipulation
                    seq.add_step(voltage_point_name="manipulation")  # includes manipulation
                    seq.add_step(voltage_point_name="readout")
                    seq.add_compensation_pulse(duration=duration_compensation_pulse)
                    
                    
                    # wait((duration_init - const_len) * u.ns, qb)
                    wait(duration_init * u.ns, qb)

                    with for_(idx, 2, idx < circ_len + 2, idx + 1):
                        with switch_(encoded_circuit[idx], unsafe=True):
                            # baseband operation is fixed regardless L
                            # normal:just run till the end with Null
                            # option: adjust the length accoridngly

                            with case_(0):
                                # TODO: initialization step
                                play("const", qb)  # dummy I
                                # play("const" * amp(0), qb, duration=4)

                            # prep fiducials
                            with case_(1):
                                play("const", qb)  # Null -> wait for pi/2 pulse length
                            with case_(2):
                                play("x90", qb)
                            with case_(3):
                                play("y90", qb)
                            with case_(4):
                                play("x90", qb)
                                play("x90", qb)
                            with case_(5):
                                play("x90", qb)
                                play("x90", qb)
                                play("x90", qb)
                            with case_(6):
                                play("y90", qb)
                                play("y90", qb)
                                play("y90", qb)

                            # germs
                            with case_(7): #   I = XXXX
                                play("x90", qb)
                                play("x90", qb)
                                play("x90", qb)
                                play("x90", qb)
                            with case_(8):
                                play("x90", qb)
                            with case_(9):
                                play("y90", qb)
                            with case_(10):
                                play("x90", qb)
                                play("y90", qb)
                            with case_(11):
                                play("x90", qb)
                                play("x90", qb)
                                play("y90", qb)

                            # meas fiducial
                            with case_(12):
                                play("const", qb)  # dummy I
                            with case_(13):
                                play("x90", qb)
                            with case_(14):
                                play("y90", qb)
                            with case_(15):
                                play("x90", qb)
                                play("x90", qb)
                            with case_(16):
                                play("x90", qb)
                                play("x90", qb)
                                play("x90", qb)
                            with case_(17):
                                play("y90", qb)
                                play("y90", qb)
                                play("y90", qb)

                            with case_(18):
                                # TODO: readout step
                                play("const", qb)  # dummy I

                    # # TODO: readout step
                    # play("const", qb) # dummy I
                    # wait(100)

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
        encoded_circuit_batch = dg[
            ["index", "P_enc_seq", "G_enc_seq", "d_enc_seq", "M_enc_seq"]
        ]

        for i, row in encoded_circuit_batch.iterrows():
            P = int(row["P_enc_seq"])
            G = int(row["G_enc_seq"])
            d = int(row["d_enc_seq"])
            M = int(row["M_enc_seq"])

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

            # initialization
            _encoded_circuit_input_stream.insert(1, 0)
            seq_len += 1

            # readout
            _encoded_circuit_input_stream.append(17)
            seq_len += 1

            # sequence length
            _encoded_circuit_input_stream.insert(1, seq_len)

            record.append([_n_shots] + _encoded_circuit_input_stream)

            print(
                f"n_shots: {_n_shots}, circ_idx = {i}, n_circuits: P={P}, G={G}, d={d}, M={M}"
            )
            job.push_to_input_stream(
                "_encoded_circuit_input_stream", _encoded_circuit_input_stream
            )
            print("    ---> success!")

    idx_history = res_handles.get("idx_history").fetch_all()

# %%
