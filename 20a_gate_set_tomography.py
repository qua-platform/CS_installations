# %%
from qm import *
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_gst_lffem import *
# from configuration_gst_opxplus import *
import matplotlib.pyplot as plt
import pandas as pd
import math


class GSTParser():
    pass


map_prepfiducial = {
    "{}": 1,
    "Gxpi2:0": 2,
    "Gypi2:0": 3,
    "Gxpi2:0Gxpi2:0": 4,
    "Gxpi2:0Gxpi2:0Gxpi2:0": 5,
    "Gypi2:0Gypi2:0Gypi2:0": 6,
}
map_germs = {
    "Gxpi2:0": 1 + 6,
    "Gypi2:0": 2 + 6,
    "Gxpi2:0Gypi2:0": 3 + 6,
    "Gxpi2:0Gxpi2:0Gypi2:0": 4 + 6,
}
map_measfiducial = {
    "{}": 1 + 6 + 4,
    "Gxpi2:0": 2 + 6 + 4,
    "Gypi2:0": 3 + 6 + 4,
    "Gxpi2:0Gxpi2:0": 4 + 6 + 4,
    "Gxpi2:0Gxpi2:0Gxpi2:0": 5 + 6 + 4,
    "Gypi2:0Gypi2:0Gypi2:0": 6 + 6 + 4,
}
path = "gate_set_tomography/encoded_parsed_dataset.csv"
dg = pd.read_csv(path, header=0)  # Use header=0 to indicate the first row is the header
dg.reset_index(inplace=True)
dg = dg.tail(70)
dg = dg.head(30)


###################
# The QUA program #
###################

list_n_shots = [128, 8192]
# gst_parser = GSTParser()
# list_circuits = gst_parser.get_encoded_circuits()
sequence_max_len = 2 + 1 + 8192 + 1
list_circuits = dg[["index", "P", "G", "d", "M"]].values.tolist()
list_encoded_circuits = dg[["index", "P_enc", "G_enc", "d_enc", "M_enc"]].values.tolist()
num_cicuits = len(list_encoded_circuits)
qb = "qubit"


with program() as PROGRAM:
    n = declare(int)
    n_shots = declare(int)
    circ = declare(int)
    idx = declare(int)
    encoded_circuit = declare_input_stream(
        int,
        name="_encoded_circuit_input_stream",
        size=sequence_max_len,
    ) # input stream the sequence
    idx_st = declare_stream()
    

    with for_each_(n_shots, list_n_shots):

        with for_(circ, 0, circ < num_cicuits, circ + 1):

            advance_input_stream(encoded_circuit)  # ordered or randomized
            
            circ_idx = encoded_circuit[0]
            circ_len = encoded_circuit[1]

            with for_(n, 0, n < n_shots, n + 1):

                with strict_timing_():
                    
                    with for_(idx, 2, idx < circ_len + 2, idx + 1):
                        
                        with switch_(encoded_circuit[idx], unsafe=True):
                            
                            with case_(0):
                                # TODO: initialization step
                                play("const", qb) # dummy I
                                # play("const" * amp(0), qb, duration=4)

                            # prep fiducials
                            with case_(1):
                                play("const", qb) # dummy I
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
                            # TODO: with case():
                            #   I = XXXX
                            with case_(7):
                                play("x90", qb)
                            with case_(8):
                                play("y90", qb)
                            with case_(9):
                                play("x90", qb)
                                play("y90", qb)
                            with case_(10):
                                play("x90", qb)
                                play("x90", qb)
                                play("y90", qb)

                            # meas fiducial
                            with case_(11):
                                play("const", qb) # dummy I
                            with case_(12):
                                play("x90", qb)
                            with case_(13):
                                play("y90", qb)
                            with case_(14):
                                play("x90", qb)
                                play("x90", qb)
                            with case_(15):
                                play("x90", qb)
                                play("x90", qb)
                                play("x90", qb)
                            with case_(16):
                                play("y90", qb)
                                play("y90", qb)
                                play("y90", qb)

                            with case_(17):
                                # TODO: readout step
                                play("const", qb) # dummy I

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
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)


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

else:
    from qm import generate_qua_script
    sourceFile = open('debug08.py', 'w')
    print(generate_qua_script(PROGRAM, config), file=sourceFile) 
    sourceFile.close()

    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PROGRAM, compiler_options=CompilerOptionArguments(flags=["not-strict-timing"]))
    # job = qm.execute(PROGRAM)
    
    res_handles = job.result_handles
    # Waits (blocks the Python console) until all results have been acquired
    # results = fetching_tool(job, data_list=["circuit_history"], mode="live")
    
    record = []
    for _n_shots in list_n_shots:
        encoded_circuit_batch = dg[["index", "P_enc_seq", "G_enc_seq", "d_enc_seq", "M_enc_seq"]]
        
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
                _encoded_circuit_input_stream.extend([G] * d )
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

            print(f"n_shots: {_n_shots}, circ_idx = {i}, n_circuits: P={P}, G={G}, d={d}, M={M}")
            job.push_to_input_stream("_encoded_circuit_input_stream", _encoded_circuit_input_stream)
            print("    ---> success!")

    idx_history = res_handles.get("idx_history").fetch_all()

# %%
