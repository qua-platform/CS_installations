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

import matplotlib
import matplotlib.pyplot as plt
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.loops import from_array
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.results.data_handler import DataHandler
from scipy import signal

from configuration_with_lffem_csrack import *
# from configuration_with_lffem import *
from macros_voltage_gate_sequence import VoltageGateSequence

# matplotlib.use('TkAgg')

###################
# The QUA program #
###################
tank_circuit = "tank_circuit2"
n_avg = 100  # Number of averaging loops
# The frequency axis
frequencies = np.linspace(50 * u.MHz, 350 * u.MHz, 101)

save_data_dict = {
    "tank_circuit": tank_circuit,
    "frequencies": frequencies,
    "n_avg": n_avg,
    "config": config,
}


with program() as reflectometry_spectro:
    f = declare(int)  # QUA variable for the frequency sweep
    n = declare(int)  # QUA variable for the averaging loop
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(f, frequencies)):
            # Update the frequency of the tank_circuit element
            update_frequency(tank_circuit, f)
            # RF reflectometry: the voltage measured by the analog input 2 is recorded, demodulated at the readout
            # frequency and the integrated quadratures are stored in "I" and "Q"
            # Please choose the right "out1" or "out2" according to the connectivity
            measure(
                "readout",
                tank_circuit,
                None,
                demod.full("cos", I, "out1"),
                demod.full("sin", Q, "out1"),
            )
            save(I, I_st)
            save(Q, Q_st)
            # Wait at each iteration in order to ensure that the data will not be transferred faster than 1 sample
            # per µs to the stream processing. Otherwise, the processor will receive the samples faster than it can
            # process them which can cause the OPX to crash.
            wait(1_000 * u.ns)  # in ns
        save(n, n_st)

    with stream_processing():
        I_st.buffer(len(frequencies)).average().save("I")
        Q_st.buffer(len(frequencies)).average().save("Q")
        n_st.save("iteration")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)


#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, reflectometry_spectro, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(reflectometry_spectro)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, iteration = results.fetch_all()
        S = I + 1j * Q
        # Convert results into Volts
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot results
        plt.suptitle("RF-reflectometry spectroscopy")
        plt.subplot(211)
        plt.cla()
        plt.plot(frequencies / u.MHz, R)
        plt.xlabel("Readout frequency [MHz]")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.subplot(212)
        plt.cla()
        plt.plot(frequencies / u.MHz, signal.detrend(np.unwrap(phase)))
        plt.xlabel("Readout frequency [MHz]")
        plt.ylabel("Phase [rad]")
        plt.tight_layout()
        plt.pause(1)

    # Fetch results
    res = results.fetch_all()
    save_data_dict["I"] = I
    save_data_dict["Q"] = Q
    save_data_dict["S"] = S

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {
        script_name: script_name,
        **default_additional_files,
    }
    data_handler.save_data(data=save_data_dict, name=script_name.replace(".py", ""))

    qm.close()

# %%
