# %%
"""
        COUNTER MW ON OFF
The program consists in playing a laser pulse with/without a mw pulse while measuring SPCM continuously.
This allows adjusting external parameters to validate the experimental set-up.
"""

from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.results.data_handler import DataHandler
from configuration_with_octave import *
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import time

matplotlib.use('TkAgg')


###################
# The QUA program #
###################

# Total duration of the measurement
total_integration_time = int(1000 * u.ms)  # 100ms
# Duration of a single chunk. Needed because the OPX cannot measure for more than ~1ms
single_integration_time_ns = int(10 * u.us)  # 500us
single_integration_time_cycles = single_integration_time_ns // 4
# Number of chunks to get the total measurement time
n_count = int(total_integration_time / single_integration_time_ns)

with program() as counter:
    times = declare(int, size=10000)  # QUA vector for storing the time-tags
    counts = declare(int)  # variable for number of counts of a single chunk
    total_counts = declare(int)  # variable for the total number of counts
    n = declare(int)  # number of iterations
    counts_st = declare_stream()  # stream for counts

    # Infinite loop to allow the user to work on the experimental set-up while looking at the counts
    with infinite_loop_():
        # Play laser pulse with/without mw pulse repeatedyly
        # The expected signal is as below (where the lower(higher) signal corresponds to mw on (off))
        #    __    __    __    __    __
        # __|  |__|  |__|  |__|  |__|  |__...
        for _ in range(2):
            with for_(n, 0, n < n_count, n + 1):
                # Play the laser pulse...
                play("laser_ON", "AOM", duration=single_integration_time_cycles)
                # Play mw
                play("cw", "NV", duration=single_integration_time_cycles)
                # ... while measuring the events from the SPCM
                measure("long_readout", "SPCM", None, time_tagging.analog(times, single_integration_time_ns, counts, "out1"))
                assign(total_counts, total_counts + counts)
            # Save the counts
            save(total_counts, counts_st)
            assign(total_counts, 0)

        for _ in range(2):
            with for_(n, 0, n < n_count, n + 1):
                # Play the laser pulse...
                play("laser_ON", "AOM", duration=single_integration_time_cycles)
                # Play mw
                # play("cw", "NV", duration=single_integration_time_cycles)
                # ... while measuring the events from the SPCM
                measure("long_readout", "SPCM", None, time_tagging.analog(times, single_integration_time_ns, counts, "out1"))
                assign(total_counts, total_counts + counts)
            # Save the counts
            save(total_counts, counts_st)
            assign(total_counts, 0)

    with stream_processing():
        counts_st.with_timestamps().save("counts")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=None, cluster_name=cluster_name, octave=octave_config)

#######################
# Simulate or execute #
#######################
simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job_sim = qmm.simulate(config, counter, simulation_config)
    # Simulate blocks python until the simulation is done
    job_sim.get_simulated_samples().con1.plot()
else:
    qm = qmm.open_qm(config)
    job = qm.execute(counter)
    # Get results from QUA program
    res_handles = job.result_handles
    counts_handle = res_handles.get("counts")
    counts_handle.wait_for_values(1)
    times_ = []
    counts = []
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while res_handles.is_processing():
        new_counts = counts_handle.fetch_all()
        counts.append(new_counts["value"] / (total_integration_time / u.s))
        times_.append(new_counts["timestamp"] / u.s)  # Convert timestamps to seconds
        plt.cla()
        if len(times_) > 50:
            plt.plot(times_[-50:], counts[-50:], marker=".")
        else:
            plt.plot(times_, counts)

        plt.xlabel("Time [s]")
        plt.ylabel("Counts [cps]")
        plt.title("Counter")
        plt.pause(1)

    if save_data:
        # Arrange data to save
        data = {
            "fig_live": fig,
            "times": np.array(times_),
            "counts": np.array(counts),
            # "elapsed_time": np.array([elapsed_time]),  # convert float to np.array of float
        }
        # Initialize the DataHandler
        data_handler = DataHandler(root_data_folder=save_dir)
        data_handler.create_data_folder(name=Path(__file__).stem)
        data_handler.additional_files = {
            Path(__file__).name: Path(__file__).name,
            "configuration_with_octave.py": "configuration_with_octave.py",
        }
        # Save results
        data_folder = data_handler.save_data(data=data)

# %%
        