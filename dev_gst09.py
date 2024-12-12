# %%
from qm import *
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
# from configuration_gst_lffem import *
from configuration_gst_opxplus import *
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
dg = dg.tail(600)
dg = dg.head(10)


###################
# The QUA program #
###################

list_n_shots = [4, 10]
# gst_parser = GSTParser()
# list_circuits = gst_parser.get_encoded_circuits()
list_circuits = dg[["index", "P", "G", "d", "M"]].values.tolist()
list_encoded_circuits = dg[["index", "P_enc", "G_enc", "d_enc", "M_enc"]].values.tolist()
num_cicuits = len(list_encoded_circuits)
qb = "qubit"


with program() as PROGRAM:
    n = declare(int)
    n_shots = declare(int)
    m = declare(int)
    d = declare(int)
    idx = declare(int)
    idxes = declare(int, size=3)
    encoded_circuits = declare_input_stream(
        int,
        name="_encoded_circuit_input_stream",
        size=5 * num_cicuits,
    ) # input stream the sequence

    n_shots_st = declare_stream()
    c_idx_st = declare_stream()
    prep_fiducical_idx_st = declare_stream()
    germ_idx_st = declare_stream()
    germ_len_st = declare_stream()
    meas_fiducical_idx_st = declare_stream()

    with for_each_(n_shots, list_n_shots):

        advance_input_stream(encoded_circuits)  # ordered or randomized

        with for_(m, 0, m < num_cicuits, m + 1):
            
            c_idx = encoded_circuits[5 * m + 0]
            prep_fiducical_idx = encoded_circuits[5 * m + 1]
            germ_idx = encoded_circuits[5 * m + 2]
            germ_len = encoded_circuits[5 * m + 3]
            meas_fiducical_idx = encoded_circuits[5 * m + 4]

            assign(idxes[0], prep_fiducical_idx)
            assign(idxes[1], germ_idx)
            assign(idxes[2], meas_fiducical_idx)

            save(n_shots, n_shots_st)
            save(c_idx, c_idx_st)
            save(prep_fiducical_idx, prep_fiducical_idx_st)
            save(germ_idx, germ_idx_st)
            save(germ_len, germ_len_st)
            save(meas_fiducical_idx, meas_fiducical_idx_st)

            with for_(n, 0, n < n_shots, n + 1):
            
                wait(250)

                with strict_timing_():
        
                    # # TODO: initialization step
                    # play("const" , qb, duration=200 * u.ns) # dummy I

                    with for_each_(idx, idxes):

                        with switch_(idx, unsafe=True):
                            
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
                            with case_(7):
                                with for_(d, 0, d < germ_len, d + 1):
                                    play("x90", qb)
                            with case_(8):
                                with for_(d, 0, d < germ_len, d + 1):
                                    play("y90", qb)
                            with case_(9):
                                with for_(d, 0, d < germ_len, d + 1):
                                    play("x90", qb)
                                    play("y90", qb)
                            with case_(10):
                                with for_(d, 0, d < germ_len, d + 1):
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

                # # TODO: readout
                # wait(250)
                # play("const" , qb, duration=200 * u.ns) # dummy I


    with stream_processing():
        n_shots_st.save_all("n_shots")
        c_idx_st.save_all("c_idx")
        prep_fiducical_idx_st.save_all("prep_fiducical_idx")
        germ_idx_st.save_all("germ_idx")
        germ_len_st.save_all("germ_len")
        meas_fiducical_idx_st.save_all("meas_fiducical_idx")
        

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
    sourceFile = open('debug09.py', 'w')
    print(generate_qua_script(PROGRAM, config), file=sourceFile) 
    sourceFile.close()

    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PROGRAM, compiler_options=CompilerOptionArguments(flags=["not-strict-timing"]))
    # job = qm.execute(PROGRAM)
    
    res_handles = job.result_handles
    # Waits (blocks the Python console) until all results have been acquired
    results = fetching_tool(job, data_list=["n_shots",
        "c_idx",
        "prep_fiducical_idx",
        "germ_idx",
        "germ_len",
        "meas_fiducical_idx",
    ])
    for _n_shots in list_n_shots:
        _encoded_circuit_batch = dg[["index", "P_enc_seq", "G_enc_seq", "d_enc_seq", "M_enc_seq"]].values
        _encoded_circuit_batch_flattened = _encoded_circuit_batch.ravel()
        _encoded_circuit_batch_flattened_list = _encoded_circuit_batch_flattened.tolist()
        print(f"n_shots: {_n_shots}, n_circuits: {num_cicuits}")
        job.push_to_input_stream('_encoded_circuit_input_stream', _encoded_circuit_batch_flattened_list)
        print("    ---> success!")

    _n_shots, _c_idx, _prep_fiducical_idx, _germ_idx, _germ_len, _meas_fiducical_idx = results.fetch_all()

    print(len(_n_shots))
    print(len(_c_idx))
    print(len(_prep_fiducical_idx))
    print(len(_germ_idx))
    print(len(_germ_len))
    print(len(_meas_fiducical_idx))

    # for a, b, c, d, e, f in zip(
    #     _n_shots,
    #     _c_idx,
    #     _prep_fiducical_idx,
    #     _germ_idx,
    #     _germ_len,
    #     _meas_fiducical_idx,
    # ):
    #     print(a, b, c, d, e, f)

# %%
