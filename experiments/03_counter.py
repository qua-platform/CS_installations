# %%
"""
        COUNTER
The program consists in playing a laser pulse while measuring PD continuously.
This allows adjusting external parameters to validate the experimental set-up.
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
single_integration_time_ns = int(1 * u.us)  # 5us
single_integration_time_cycles = single_integration_time_ns // 4

with program() as counter:
    I_st = declare_stream(adc_trace=True)  # stream for PD reading 

    # Infinite loop to allow the user to work on the experimental set-up while looking at the counts
    with infinite_loop_():
        # Play the laser pulse...
        play("laser_ON", "AOM", duration=single_integration_time_cycles)
        # ... while measuring the events from the PD
        # measure("readout", "PD", None, integration.full("const", I, "out1"))
        measure("long_readout", "PD", I_st)
        wait(wait_between_runs * u.ns, "PD")

    with stream_processing():
        I_st.input1().save("I")

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
    I_handle.wait_for_values(1)

    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while res_handles.is_processing():
        I = I_handle.fetch_all()
        plt.cla()
        plt.plot(I)
        plt.xlabel("time [ns]")
        plt.ylabel("PD Voltage [V]")
        plt.title("PD Reading")
        plt.pause(0.1)

    if save_data:
        dir_data = save_files_and_get_dir_data(
            base_dir=base_dir,
            save_dir=save_dir,
            script_path=__file__,
        )
        # Suppose we want to save I, Q, iterations. 
        np.savez(
            file=dir_data / "data.npz",
            I=I,
        )
        # If a matplotlib figure object is available.
        fig.savefig(dir_data / "data_live.png")

# %%