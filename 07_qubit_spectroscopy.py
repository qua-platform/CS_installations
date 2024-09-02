# %%
"""
        QUBIT SPECTROSCOPY
This sequence involves sending a saturation pulse to the qubit, placing it in a mixed state,
and then measuring the state of the resonator across various qubit drive intermediate dfs.
In order to facilitate the qubit search, the qubit pulse duration and amplitude can be changed manually in the QUA
program directly without having to modify the configuration.

The data is post-processed to determine the qubit resonance frequency, which can then be used to adjust
the qubit intermediate frequency in the configuration under "qubit_IF".

Note that it can happen that the qubit is excited by the image sideband or LO leakage instead of the desired sideband.
This is why calibrating the qubit mixer is highly recommended.

This step can be repeated using the "x180" operation to adjust the pulse parameters (amplitude, duration, frequency)
before performing the next calibration steps.

Prerequisites:
    - Identification of the resonator's resonance frequency when coupled to the qubit in question (referred to as "resonator_spectroscopy_multiplexed").
    - Calibration of the IQ mixer connected to the qubit drive line (whether it's an external mixer or an Octave port).
    - Configuration of the cw pulse amplitude (const_amp) and duration (CONST_LEN) to transition the qubit into a mixed state.
    - Specification of the expected qubits T1 in the configuration.

Before proceeding to the next node:
    - Update the qubit frequency, labeled as "qubit_IF_q", in the configuration.
"""

from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
# from configuration_opxplus_with_octave import *
from configuration_opxplus_without_octave import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from macros import qua_declaration, multiplexed_readout
import matplotlib.pyplot as plt
import math
from qualang_tools.results.data_handler import DataHandler

###################
# The QUA program #
###################

qubits = ["q2_xy", "q3_xy"]
resonators = ["q2_rr", "q3_rr"]
qubits_all = list(QUBIT_CONSTANTS.keys())
resonators_all = [key for key in RR_CONSTANTS.keys()]
remaining_resonators = list(set(resonators_all) - set(resonators))

n_avg = 1_000  # The number of averages
# Adjust the pulse duration and amplitude to drive the qubit into a mixed state
# Qubit detuning sweep with respect to qubit_IF
span = 2.0 * u.MHz
freq_step = 125 * u.kHz
dfs = np.arange(-span, +span, freq_step)
scaling_factor = 1.0

assert len(qubits_all) == len(resonators_all), "qubits and resonators don't have the same length"
assert len(qubits) == len(resonators), "qubits and resonators under study don't have the same length"
assert all([qb.replace("_xy", "") == rr.replace("_rr", "") for qb, rr in zip(qubits, resonators)]), "qubits and resonators don't correspond"
assert len(dfs) <= 400, "check your frequencies"
for qb in qubits:
    assert scaling_factor * QUBIT_CONSTANTS[qb]['amplitude'] <= 0.499, f"{qb} scaling factor times amplitude exceeded 0.499"

save_data_dict = {
    "qubits_all": qubits_all,
    "resonators_all": resonators_all,
    "qubits": qubits,
    "resonators": resonators,
    "n_avg": n_avg,
    "dfs": dfs,
    "config": config,
    "scaling_factor": scaling_factor
}


with program() as multi_qubit_spec:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(resonators)
    df = declare(int)  # QUA variable for the readout frequency

    with for_(n, 0, n < n_avg, n + 1):
        # Save the averaging iteration to get the progress bar
        save(n, n_st)
        with for_(*from_array(df, dfs)):
            # Update the frequency of the two qubit elements
            for qb in qubits:
                update_frequency(qb, df + QUBIT_CONSTANTS[qb]["IF"])
                play("saturation" * amp(scaling_factor), qb)
                
            align()

            # Multiplexed readout, also saves the measurement outcomes
            multiplexed_readout(I, I_st, Q, Q_st, None, None, resonators=resonators)

            # Wait 
            wait(rr_reset_time >> 2)

    with stream_processing():
        n_st.save("iteration")
        for ind, rr in enumerate(resonators):
            I_st[ind].buffer(len(dfs)).average().save(f"I_{rr}")
            Q_st[ind].buffer(len(dfs)).average().save(f"Q_{rr}")


if __name__ == "__main__":
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
        job = qmm.simulate(config, multi_qubit_spec, simulation_config)
        job.get_simulated_samples().con1.plot()
        plt.show(block=False)
    else:
        try:
            # Open a quantum machine to execute the QUA program
            qm = qmm.open_qm(config)
            # Send the QUA program to the OPX, which compiles and executes it
            job = qm.execute(multi_qubit_spec)
            fetch_names = ["iteration"]
            for rr in resonators:
                fetch_names.append(f"I_{rr}")
                fetch_names.append(f"Q_{rr}")
            # Tool to easily fetch results from the OPX (results_handle used in it)
            results = fetching_tool(job, fetch_names, mode="live")
            # Prepare the figure for live plotting
            fig = plt.figure()
            interrupt_on_close(fig, job)
            num_resonators = len(resonators)
            num_rows = math.ceil(math.sqrt(num_resonators))
            num_cols = math.ceil(num_resonators / num_rows)
            # Live plotting
            while results.is_processing():
                # Fetch results
                res = results.fetch_all()
                # Progress bar
                progress_counter(res[0], n_avg, start_time=results.start_time)

                plt.suptitle("Multiplexed qubit spec")

                for ind, rr in enumerate(resonators):
                    # Data analysis
                    S = res[2*ind+1] + 1j * res[2*ind+2]
                    R = np.abs(S) 
                    # R = np.unwarp(np.angle(S))

                    save_data_dict[f"I_{rr}"] = res[2*ind + 1]
                    save_data_dict[f"Q_{rr}"] = res[2*ind + 2]

                    # Plot
                    plt.subplot(num_rows, num_cols, ind + 1)
                    plt.cla()
                    plt.plot((dfs + QUBIT_CONSTANTS[qb]["IF"]) / u.MHz, R, color='r')
                    lo_val = QUBIT_CONSTANTS[qb]["LO"] / u.GHz
                    plt.title(f"Qb - {qb}, LO {lo_val}")
                    plt.ylabel(r"R=$\sqrt{I^2 + Q^2}$ [V]")

                plt.tight_layout()
                plt.pause(0.1)

            # Save results
            script_name = Path(__file__).name
            data_handler = DataHandler(root_data_folder=save_dir)
            save_data_dict.update({"fig_live": fig})
            data_handler.additional_files = {script_name: script_name, **default_additional_files}
            data_handler.save_data(data=save_data_dict, name="qubit_spectroscopy")

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            qm.close()
            print("Experiment QM is now closed")
            plt.show(block=True)

# %%
