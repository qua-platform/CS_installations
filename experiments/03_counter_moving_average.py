# %%
"""
        COUNTER
The program consists in playing a laser pulse while measuring PD continuously.
This allows adjusting external parameters to validate the experimental set-up.
Here, the integration.moving_window parameter is utilized to prevent overloading the stream processor
    in the event that using adc_trace causes such overload.
It also enables the calibration of several parameters:
    - Integration weights: The analog input of OPX must be within the range of [-0.5V, +0.5V].
    Adjust the integration weights so that the integrated values fall within the range of [-8, +8) after integration.
    - The analog inputs gain: if the signal is limited by digitization or saturates the ADC, the variable gain of the
      OPX analog input can be set to adjust the signal within the ADC range +/-0.5V.
      The gain (-12 dB to 20 dB) can also be set in the configuration (config/controllers/"con1"/analog_inputs). 
"""

from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
import matplotlib.pyplot as plt
from qualang_tools.plot import interrupt_on_close
from utils import save_files_and_get_dir_data
from configuration import *

###################
# The QUA program #
###################

# Duration of a single chunk. Needed because the OPX cannot measure for more than ~1ms
single_integration_time_ns = int(5 * u.us)  # 5 us. if too long, SP might crash.
single_integration_time_cycles = single_integration_time_ns // 4

chunk_size = 10 # in clock 
n_chunks_per_window = 2 # number of chunks per window
buffer_size = long_meas_len / (4 * chunk_size) # number of data points over readout duration
assert buffer_size == int(buffer_size), "(long_)meas_len must be integer multiple of 4 * chunk_size"
buffer_size = int(buffer_size)
t_vec = np.linspace(0, long_meas_len, buffer_size) 


with program() as counter:
    c = declare(int)
    I = declare(fixed, size=buffer_size)
    I_st = declare_stream()  # stream for PD reading 
    # I_st = declare_stream(adc_trace=True)  # stream for PD reading 

    # Infinite loop to allow the user to work on the experimental set-up while looking at the counts
    with infinite_loop_():
        # Play the laser pulse...
        play("laser_ON", "AOM", duration=single_integration_time_cycles)
        # The integration.moving_window parameter is utilized to prevent overloading the stream processor
        # in the event that using adc_trace causes such overload.
        measure(
            "long_readout", "PD", None,
            integration.moving_window("const", I, chunk_size, n_chunks_per_window, "out1"),
        )
        with for_(c, 0, c < buffer_size, c + 1):
            save(I[c], I_st)
        wait(relaxation_time)

    with stream_processing():
        I_st.buffer(buffer_size).save("I")
        # I_st.input1().average().save("I")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)


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
    I_handle = res_handles.get("I")
    #I_handle.wait_for_values(1)

    Is = []
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while res_handles.is_processing():
        I = I_handle.fetch_all()
        Is.append(u.demod2volts(data=I, duration=chunk_size*4))
        plt.cla()
        plt.plot(t_vec, I)
        plt.xlabel("iterations")
        plt.ylabel("PD Voltage [V]")
        plt.title("PD Reading")
        plt.pause(0.1)

    if save_data:
        dir_data = save_files_and_get_dir_data(
            base_dir=base_dir,
            save_dir=save_dir,
            script_path=__file__,
        )
        np.savez(
            file=dir_data / "data.npz",
            I=I,
            t_vec=t_vec,
        )
        # If a matplotlib figure object is available.
        fig.savefig(dir_data / "data_live.png")

# %%
