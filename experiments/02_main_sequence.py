# %%
"""
        Description of Main Sequence
"""

from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig

# from configuration import *
from configuration_with_octave import *
import matplotlib.pyplot as plt
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.plot import interrupt_on_close
import warnings
import matplotlib
from utils import save_files_and_get_dir_data
import os

matplotlib.use("TKAgg")
warnings.filterwarnings("ignore")


###################
# The QUA program #
###################
cycle_ns = 4 # ns
n_avg = 5  # The number of averages
# Pulse duration sweep (in clock cycles = 4ns) - must be larger than 4 clock cycles
t_min = 1000 // cycle_ns # 16 // cycle_ns
t_max = 10_000 // cycle_ns
dt = 100 // cycle_ns
bias_len_cycle = bias_len // cycle_ns
pump_delay_cycle = bias_len_cycle - 5 * u.us // cycle_ns
delays = np.arange(t_min, t_max, dt)

with program() as main_sequence:
    n = declare(int) # QUA variable for averaging loop
    d = declare(int) # QUA variable for time delay
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature --> signed 4.28 [-8, 8)
    Q = declare(fixed) # QUA variable for the measured 'Q' quadrature --> signed 4.28 [-8, 8)

    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'
    
    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        with for_(*from_array(d, delays)):  # QUA for_ loop for time delays
            # send a pulse for bias at 1f
            play("cw", "bias")
            # Wait for 2f pump
            wait(pump_delay_cycle, "pump_probe")
            # send a pulse for pump at 2f
            play("cw", "pump_probe")
            # Wait for the time delay
            wait(d, "pump_probe")
            # measure with 2f probe (send a readout pulse and demodulate the signals to get the 'I' & 'Q' quadratures)
            measure(
                "readout",
                "pump_probe",
                None,
                dual_demod.full("cos", "out1", "sin", "out2", I),
                dual_demod.full("minus_sin", "out1", "cos", "out2", Q),
            )
            # Wait for thermalization
            wait(thermalization_time, "pump_probe")
            
            # Save the 'I' & 'Q' quadratures to their respective streams
            save(I, I_st)
            save(Q, Q_st)
        # Save the averaging iterations to get the progress bar
        save(n, n_st)
            
    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        I_st.buffer(len(delays)).average().save("I")
        Q_st.buffer(len(delays)).average().save("Q")
        n_st.save("iterations")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)


###########################
# Run or Simulate Program #
###########################
simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, main_sequence, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(main_sequence)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "iterations"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, iterations = results.fetch_all()
        # Convert the results into Volts
        I, Q = u.demod2volts(I, probe_len), u.demod2volts(Q, probe_len)
        # Progress bar
        progress_counter(iterations, n_avg, start_time=results.get_start_time())
        # Plot results
        plt.suptitle("Main Sequence")
        plt.subplot(211)
        plt.cla()
        plt.plot(4 * delays, I, ".")
        plt.ylabel("I quadrature [V]")
        plt.subplot(212)
        plt.cla()
        plt.plot(4 * delays, Q, ".")
        plt.xlabel("time delay [ns]")
        plt.ylabel("Q quadrature [V]")
        plt.pause(0.3)
        plt.tight_layout()

    # save the numpy arrays
    if save_data:    
        dir_data = save_files_and_get_dir_data(
            base_dir=base_dir,
            save_dir=save_dir,
            script_path=__file__
        )
        np.savez(
            file=os.path.join(dir_data, "data.npz"),
            I1=I,
            Q1=Q,
            delays=delays,
            iterations=iterations,
        )

# %%