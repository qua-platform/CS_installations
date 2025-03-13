# %%
import os
from configuration import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.results import fetching_tool
import matplotlib.pyplot as plt


n_rep = 5_000


with program() as prog:
    avg = declare(int)
    n = declare(int)
    n2 = declare(int)
    dc = [declare(fixed) for _ in range(2)]
    dc_st = declare_stream()
    avg_st = declare_stream()
    with for_(avg, 0, avg < 10, avg + 1):
        save(avg, avg_st)
        with for_(n, 0, n < n_rep // 2, n + 1):  # Loop 1
            measure(
                "readout",
                "TIA",
                None,
                integration.full("constant", dc[0], "out2"),
            )
            save(dc[0], dc_st)
            wait(readout_len * u.ns, "TIA")

        wait(readout_len * u.ns, "TIA_copy")  # wait for loop 1 first iteration to end
        with for_(n2, 0, n2 < n_rep // 2, n2 + 1):  # Loop 2
            measure(
                "readout",
                "TIA_copy",
                None,
                integration.full("constant", dc[1], "out2"),
            )
            save(dc[1], dc_st)
            wait(readout_len * u.ns, "TIA_copy")

    with stream_processing():
        dc_st.buffer(n_rep).average().save("dc")
        dc_st.buffer(n_rep).average().fft("abs").save("dc_fft")
        avg_st.save("avg")


qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)
# %%
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, prog, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(samples, plot=True)
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(prog)
    # Get results from QUA program and initialize live plotting
    res_handles = job.result_handles
    res_handles.wait_for_all_values()
    dc = u.demod2volts(res_handles.get("dc").fetch_all(), duration=readout_len)
    fft_dc = res_handles.get("dc_fft").fetch_all()

    plt.subplot(121)
    plt.plot(dc, '.--')
    plt.subplot(122)

    fft = fft_dc[: int(np.ceil(len(fft_dc) / 2))][:]  # Get only the positive frequencies

    freq = np.fft.fftfreq(len(fft_dc), readout_len / 1000)  # Create frequency vector
    freq = freq[: int(np.ceil(len(fft_dc) / 2))][:] * 1e3  # Get positive frequencies in kHz units

    plt.loglog(freq, fft, ".--")



    plt.show()


# %%
