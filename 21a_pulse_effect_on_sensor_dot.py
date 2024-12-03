# %%
"""
        RF REFLECTOMETRY SPECTROSCOPY
The goal of this script is to perform the spectroscopy of the RF-reflectometry readout.
For this, the frequency of the element (pulser) used for reflectometry readout is being swept and the signal reflected
by the tank circuit is being acquired, demodulated and integrated by the OPX.

A global averaging is performed (averaging on the most outer loop) and the data is extracted while the program is running
to display the frequency response of the tank circuit with increasing SNR.

Prerequisites:
    - Connect the tank circuit to the corresponding output and input channels.

Before proceeding to the next node:
    - Update the config with the resonance frequency for reflectometry readout.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_with_lf_fem import *

# from configuration import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from scipy import signal
from qualang_tools.bakery import baking


###################
# The QUA program #
###################
n_avg = 10  # number of averages
ramp_rate = 3e-4
ramp_duration = 1 * u.us  # ramp_rate * ramp_duration will be the voltage applied
flat_duration = 4 * u.us
# Set the sliced demod parameters
division_length = 1  # Size of each demodulation slice in clock cycles
number_of_divisions = int(
    (reflectometry_readout_long_length) / (4 * division_length)
)  # Number of slices
print("Integration weights chunk-size length in clock cycles:", division_length)
print(
    "The readout has been sliced in the following number of divisions",
    number_of_divisions,
)
# Time axis for the plots at the end
ts_plot = np.arange(
    division_length * 4, reflectometry_readout_long_length + 1, division_length * 4
)

with program() as PROG:
    n = declare(int)  # QUA variable for the averaging loop
    m = declare(int)  # QUA variable for the averaging loop
    I = declare(
        fixed, size=number_of_divisions
    )  # QUA variable for the measured 'I' quadrature
    Q = declare(
        fixed, size=number_of_divisions
    )  # QUA variable for the measured 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature

    with for_(n, 0, n < n_avg, n + 1):
        play(ramp(ramp_rate), "P1_sticky", duration=ramp_duration)  # 1Vpp
        wait(flat_duration, "P1_sticky")
        play(ramp(-ramp_rate), "P1_sticky", duration=ramp_duration)  # 1Vpp

        # RF reflectometry: the voltage measured by the analog input 2 is recorded, demodulated at the readout
        # Please choose the right "out1" or "out2" according to the connectivity
        measure(
            "long_readout",
            "tank_circuit",
            None,
            demod.sliced("cos", I, division_length, "out1"),
            demod.sliced("sin", Q, division_length, "out1"),
        )
        with for_(m, 0, m < number_of_divisions, m + 1):
            save(I[m], I_st)
            save(Q[m], Q_st)
        # Wait at each iteration in order to ensure that the data will not be transferred faster than 1 sample
        # per µs to the stream processing. Otherwise, the processor will receive the samples faster than it can
        # process them which can cause the OPX to crash.
        wait(1_000 * u.ns)  # in ns
        save(n, n_st)

    with stream_processing():
        n_st.save("iteration")
        I_st.buffer(number_of_divisions).average().save("I")
        Q_st.buffer(number_of_divisions).average().save("Q")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)


#######################
# Simulate or execute #
#######################
simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, PROG, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PROG)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, iteration = results.fetch_all()
        # Convert results into Volts
        S = I + 1j * Q
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot results
        plt.suptitle("RF-reflectometry spectroscopy")
        plt.cla()
        plt.plot(ts_plot, R)
        plt.xlabel("Readout frequency [MHz]")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.tight_layout()
        plt.pause(1)

    if save_data:
        from qualang_tools.results.data_handler import DataHandler

        # Data to save
        save_data_dict = {}
        # save_data_dict["elapsed_time"] =  np.array([elapsed_time])
        save_data_dict["I"] = I
        save_data_dict["Q"] = Q

        # Save results
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        save_data_dict.update({"fig_live": fig})
        data_handler.additional_files = {
            script_name: script_name,
            **default_additional_files,
        }
        data_handler.save_data(data=save_data_dict, name="pulse_effect_on_sensor_dot")

    plt.show()
    qm.close()

# %%
