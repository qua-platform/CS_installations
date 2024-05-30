import numpy as np
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *
from qualang_tools.results import fetching_tool
import matplotlib.pyplot as plt


###################
# The QUA program #
###################
slice_length = 10  # Size of each demodulation slice in clock cycles
number_of_slices = int(readout_len / (4 * slice_length))

with program() as sliced_demodulation:
    i = declare(int)
    n = declare(int)
    I = declare(fixed, size=number_of_slices)
    Q = declare(fixed, size=number_of_slices)
    dc_signal = declare(fixed, size=number_of_slices)
    I_st = declare_stream()
    Q_st = declare_stream()
    dc_signal_st = declare_stream()

    with for_(n, 0, n < 1, n + 1):  # The averaging loop
        reset_phase("lf_readout_element_twin")
        reset_phase("lf_readout_element")
        # Play a long pulse to record
        wait(800 * u.ns, "lf_readout_element_twin")
        # update_frequency("lf_readout_element_twin", 1 * u.MHz)
        play("readout", "lf_readout_element_twin", duration=600 * u.ns)
        wait(400 * u.ns, "lf_readout_element_twin")
        play("readout", "lf_readout_element_twin", duration=600 * u.ns)
        wait(400 * u.ns, "lf_readout_element_twin")
        play("readout", "lf_readout_element_twin", duration=600 * u.ns)
        wait(400 * u.ns, "lf_readout_element_twin")
        play("readout", "lf_readout_element_twin", duration=600 * u.ns)
        wait(400 * u.ns, "lf_readout_element_twin")

        measure(
            "readout" * amp(0), "lf_readout_element", None,
            demod.sliced("cos", I, slice_length),
            demod.sliced("sin", Q, slice_length)
        )
        measure(
            "readout", "dc_readout_element", None,
            integration.sliced("const", dc_signal, slice_length, "out1"),
        )
        with for_(i, 0, i<number_of_slices, i+1):
            save(I[i], I_st)
            save(Q[i], Q_st)
            save(dc_signal[i], dc_signal_st)
            wait(100)  # Needed for SP

    with stream_processing():
        I_st.buffer(number_of_slices).average().save("I")
        Q_st.buffer(number_of_slices).average().save("Q")
        dc_signal_st.buffer(number_of_slices).average().save("dc_signal")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, sliced_demodulation, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(sliced_demodulation)
    print("run prog")
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "dc_signal"], mode="live")
    # Fetch results
    I, Q, dc = results.fetch_all()
    S = u.demod2volts(I + 1j * Q, slice_length * 4, single_demod=True)
    dc = u.demod2volts(dc, slice_length * 4)
    R = np.abs(S)
    time = np.linspace(0, readout_len, number_of_slices)
    # Plot
    plt.figure()
    plt.subplot(211)
    plt.plot(time, R, "-")
    plt.ylabel("Demodulated amplitude [V]")
    plt.xlabel("Time [s]")
    plt.subplot(212)
    plt.plot(time, dc, "-")
    plt.ylabel("DC signal [V]")
    plt.xlabel("Time [s]")