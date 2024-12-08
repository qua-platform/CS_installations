# %%

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_gst import *
from qualang_tools.results import progress_counter, fetching_tool, wait_until_job_is_paused
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from macros import RF_reflectometry_macro, DC_current_sensing_macro
import pandas as pd


class GSTParser():
    pass


map_prepfiducial = {
    "{}": 0,
    "Gxpi2:0": 1,
    "Gypi2:0": 2,
    "Gxpi2:0Gxpi2:0": 3,
    "Gxpi2:0Gxpi2:0Gxpi2:0": 4,
    "Gypi2:0Gypi2:0Gypi2:0": 5,
}
map_measfiducial = {
    "{}": 0,
    "Gxpi2:0": 1,
    "Gypi2:0": 2,
    "Gxpi2:0Gxpi2:0": 3,
    "Gxpi2:0Gxpi2:0Gxpi2:0": 4,
    "Gypi2:0Gypi2:0Gypi2:0": 5,
}
map_germs = {
    "Gxpi2:0": 0,
    "Gypi2:0": 1,
    "Gxpi2:0Gypi2:0": 2,
    "Gxpi2:0Gxpi2:0Gypi2:0": 3,
    "Gxpi2:0Gypi2:0Gypi2:0": 4,
    "Gxpi2:0Gxpi2:0Gypi2:0Gxpi2:0Gypi2:0Gypi2:0": 5,
}
path = "gate_set_tomography/encoded_parsed_dataset.csv"
dg = pd.read_csv(path, header=0)  # Use header=0 to indicate the first row is the header
dg = dg.head(40)

###################
# The QUA program #
###################

list_n_shots = [1, 4, 10]
# gst_parser = GSTParser()
# list_circuits = gst_parser.get_encoded_circuits()
list_circuits = dg[["P", "G", "d", "M"]].values.tolist()
list_encoded_circuits = dg[["P_enc", "G_enc", "d_enc", "M_enc"]].values.tolist()
num_cicuits = len(list_encoded_circuits)
qb = "qubit"

with program() as PROGRAM:
    n_shots = declare(int)
    n = declare(int)
    m = declare(int)
    d = declare(int)
    circuit_idxs = declare_input_stream(int, name="circuit_idxs_input_stream", size=4) # input stream the sequence
    circuit_st = declare_stream()

    with for_each_(n_shots, list_n_shots):
        
        with for_(n, 0, n < n_shots, n + 1):
            
            with for_(m, 0, m < num_cicuits, m + 1):
            
                advance_input_stream(circuit_idxs)  # ordered or randomized
                
                prep_fiducical_idx = circuit_idxs[0]
                germ_idx = circuit_idxs[1]
                germ_len = circuit_idxs[2]
                meas_fiducical_idx = circuit_idxs[3]

                # TODO: initialize protocol

                # prep fiducials
                with if_(prep_fiducical_idx >= 1):
                    with switch_(prep_fiducical_idx):
                        with case_(1):
                            play("x90", qb)
                        with case_(2):
                            play("y90", qb)
                        with case_(3):
                            play("x90", qb)
                            play("x90", qb)
                        with case_(4):
                            play("x90", qb)
                            play("x90", qb)
                            play("x90", qb)
                        with case_(5):
                            play("y90", qb)
                            play("y90", qb)
                            play("y90", qb)

                # germ
                with if_(germ_idx >= 0):
                    with switch_(germ_idx):
                        with case_(0):
                            with for_(d, 0, d < germ_len, d + 1):
                                play("x90", qb)
                        with case_(1):
                            with for_(d, 0, d < germ_len, d + 1):
                                play("y90", qb)
                        with case_(2):
                            with for_(d, 0, d < germ_len, d + 1):
                                play("x90", qb)
                                play("y90", qb)
                        with case_(3):
                            with for_(d, 0, d < germ_len, d + 1):
                                play("x90", qb)
                                play("x90", qb)
                                play("y90", qb)
                        with case_(4):
                            with for_(d, 0, d < germ_len, d + 1):
                                play("x90", qb)
                                play("y90", qb)
                                play("y90", qb)
                        with case_(5):
                            with for_(d, 0, d < germ_len, d + 1):
                                play("x90", qb)
                                play("x90", qb)
                                play("y90", qb)
                                play("x90", qb)
                                play("y90", qb)

                # meas fiducials
                with if_(meas_fiducical_idx >= 0):
                    with switch_(meas_fiducical_idx):
                        with case_(1):
                            play("x90", qb)
                        with case_(2):
                            play("y90", qb)
                        with case_(3):
                            play("x90", qb)
                            play("x90", qb)
                        with case_(4):
                            play("x90", qb)
                            play("x90", qb)
                            play("x90", qb)
                        with case_(5):
                            play("y90", qb)
                            play("y90", qb)
                            play("y90", qb)

                # TODO: measurement protocol

                save(m, circuit_st)
                save(prep_fiducical_idx, circuit_st)
                save(germ_idx, circuit_st)
                save(germ_len, circuit_st)
                save(meas_fiducical_idx, circuit_st)

    with stream_processing():
        circuit_st.buffer(5).save("circuit_history") 


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)


###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    pass

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PROGRAM)
    
    res_handles = job.result_handles
    # Waits (blocks the Python console) until all results have been acquired
    # results = fetching_tool(job, data_list=["circuit_history"], mode="live")
    for _n_shots in list_n_shots:
        for j, _encoded_circuit in enumerate(list_encoded_circuits):
            print(f"n_shots: {_n_shots}")
            print(f"    encoded_circuit: {_encoded_circuit}")
            job.push_to_input_stream('circuit_idxs_input_stream', _encoded_circuit)
            # circuit_history = results.fetch_all()
            # res_handles.wait_for_all_values()
            circuit_history = res_handles.get("circuit_history").fetch_all()
            print(f"    res: {circuit_history}")

# %%
