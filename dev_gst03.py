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
import math


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
dg.reset_index(inplace=True)
dg = dg.head(800)

###################
# The QUA program #
###################

list_n_shots = [1, 4, 10]
# gst_parser = GSTParser()
# list_circuits = gst_parser.get_encoded_circuits()
list_circuits = dg[["index", "P", "G", "d", "M"]].values.tolist()
list_encoded_circuits = dg[["index", "P_enc", "G_enc", "d_enc", "M_enc"]].values.tolist()
num_cicuits = len(list_encoded_circuits)
num_cicuits_per_batch = 200
num_cicuits_batches = math.ceil(num_cicuits / num_cicuits_per_batch)
qb = "qubit"


with program() as PROGRAM:
    n_shots = declare(int)
    nn = declare(int)
    bb = declare(int)
    mm = declare(int)
    d = declare(int)
    circuit_idxs = declare_input_stream(
        int,
        name="circuit_idxs_input_stream",
        size=5 * num_cicuits_per_batch,
    ) # input stream the sequence
    circuit_st = declare_stream()

    with for_each_(n_shots, list_n_shots):
        
        with for_(bb, 0, bb < num_cicuits_batches, bb + 1):

            advance_input_stream(circuit_idxs)  # ordered or randomized
            
            with for_(mm, 0, mm < num_cicuits_per_batch, mm + 1):
                
                c_idx = circuit_idxs[5 * mm + 0]
                prep_fiducical_idx = circuit_idxs[5 * mm + 1]
                germ_idx = circuit_idxs[5 * mm + 2]
                germ_len = circuit_idxs[5 * mm + 3]
                meas_fiducical_idx = circuit_idxs[5 * mm + 4]
            
                with for_(nn, 0, nn < n_shots, nn + 1):

                    # # TODO: initialize protocol
                    # with if_((germ_idx >= 0)):
                    #     with strict_timing_():
                    #         # prep fiducials
                    #         with switch_(germ_idx, unsafe=True):
                    #             with case_(0):
                    #                 with for_(d, 0, d < germ_len, d + 1):
                    #                     play("x90", qb)
                    #             with case_(1):
                    #                 with for_(d, 0, d < germ_len, d + 1):
                    #                     play("y90", qb)
                    #             with case_(2):
                    #                 with for_(d, 0, d < germ_len, d + 1):
                    #                     play("x90", qb)
                    #                     play("y90", qb)
                    #             with case_(3):
                    #                 with for_(d, 0, d < germ_len, d + 1):
                    #                     play("x90", qb)
                    #                     play("x90", qb)
                    #                     play("y90", qb)
                    #             with case_(4):
                    #                 with for_(d, 0, d < germ_len, d + 1):
                    #                     play("x90", qb)
                    #                     play("y90", qb)
                    #                     play("y90", qb)
                    #             with case_(5):
                    #                 with for_(d, 0, d < germ_len, d + 1):
                    #                     play("x90", qb)
                    #                     play("x90", qb)
                    #                     play("y90", qb)
                    #                     play("x90", qb)
                    #                     play("y90", qb)

                    with if_((prep_fiducical_idx >= 1) & (germ_idx >= 0) & (meas_fiducical_idx >= 1)):
                        with strict_timing_():
                            # prep fiducials
                            with switch_(prep_fiducical_idx, unsafe=True):
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

                            with switch_(meas_fiducical_idx, unsafe=True):
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

                        # # germ
                        # with if_(germ_idx >= 0):
                        #     with switch_(germ_idx, unsafe=True):
                        #         with case_(0):
                        #             with for_(d, 0, d < germ_len, d + 1):
                        #                 play("x90", qb)
                        #         with case_(1):
                        #             with for_(d, 0, d < germ_len, d + 1):
                        #                 play("y90", qb)
                        #         with case_(2):
                        #             with for_(d, 0, d < germ_len, d + 1):
                        #                 play("x90", qb)
                        #                 play("y90", qb)
                        #         with case_(3):
                        #             with for_(d, 0, d < germ_len, d + 1):
                        #                 play("x90", qb)
                        #                 play("x90", qb)
                        #                 play("y90", qb)
                        #         with case_(4):
                        #             with for_(d, 0, d < germ_len, d + 1):
                        #                 play("x90", qb)
                        #                 play("y90", qb)
                        #                 play("y90", qb)
                        #         with case_(5):
                        #             with for_(d, 0, d < germ_len, d + 1):
                        #                 play("x90", qb)
                        #                 play("x90", qb)
                        #                 play("y90", qb)
                        #                 play("x90", qb)
                        #                 play("y90", qb)

                        # # meas fiducials
                        # with if_(meas_fiducical_idx >= 0):
                        #     with switch_(meas_fiducical_idx, unsafe=True):
                        #         with case_(1):
                        #             play("x90", qb)
                        #         with case_(2):
                        #             play("y90", qb)
                        #         with case_(3):
                        #             play("x90", qb)
                        #             play("x90", qb)
                        #         with case_(4):
                        #             play("x90", qb)
                        #             play("x90", qb)
                        #             play("x90", qb)
                        #         with case_(5):
                        #             play("y90", qb)
                        #             play("y90", qb)
                        #             play("y90", qb)

                        # # TODO: measurement protocol

                        # save(c_idx, circuit_st)
                        # save(prep_fiducical_idx, circuit_st)
                        # save(germ_idx, circuit_st)
                        # save(germ_len, circuit_st)
                        # save(meas_fiducical_idx, circuit_st)
                        # wait(5 * u.us)

    # with stream_processing():
    #     circuit_st.buffer(5).buffer(num_cicuits_per_batch).save("circuit_history") 


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
    sourceFile = open('debug.py', 'w')
    print(generate_qua_script(PROGRAM, config), file=sourceFile) 
    sourceFile.close()
    # Open the quantum machine
    qm = qmm.open_qm(config, flags=["not-strict-timing"])
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PROGRAM)
    
    res_handles = job.result_handles
    # Waits (blocks the Python console) until all results have been acquired
    # results = fetching_tool(job, data_list=["circuit_history"], mode="live")
    for _n_shots in list_n_shots:
        for b in range(num_cicuits_batches):
            n_from = b * num_cicuits_per_batch
            n_to = (b + 1) * num_cicuits_per_batch
            encoded_circuit_batch = dg[["index", "P_enc", "G_enc", "d_enc", "M_enc"]].iloc[n_from:n_to,:].values
            encoded_circuit_batch_flattened = encoded_circuit_batch.ravel()
            encoded_circuit_batch_flattened_list = encoded_circuit_batch_flattened.tolist()
            print(f"n_shots: {_n_shots}, n_batch: {b}")
            # print(f"    encoded_circuit: {encoded_circuit_batch_flattened_list}")
            job.push_to_input_stream('circuit_idxs_input_stream', encoded_circuit_batch_flattened_list)
            # circuit_history = results.fetch_all()
            # res_handles.wait_for_values(1)
            # circuit_history = res_handles.get("circuit_history").fetch_all()
            # print(f"    res: {circuit_history}")
            # assert np.allclose(encoded_circuit_batch, circuit_history), "input and output streams don't match!"
            print("    ---> success!")
# %%
