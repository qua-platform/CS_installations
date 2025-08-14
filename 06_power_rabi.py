from pathlib import Path
import os

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
import matplotlib.pyplot as plt
import numpy as np
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qm_saas import QmSaas, QOPVersion
from qualang_tools.loops import from_array
from qualang_tools.results.data_handler import DataHandler

u = unit(coerce_to_integer=True)

# User parameters
n_avg = 10           # averages

# Pulse amplitude sweep (as a pre-factor of the qubit pulse amplitude) - must be within [-2; 2)
a_min = 1.1
a_max = 1.9
n_a = 10
amplitudes = np.linspace(a_min, a_max, n_a)


# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "amplitudes": amplitudes,
    "config": config,
}

with program() as power_rabi:
    n = declare(int)
    a = declare(fixed)
    I = declare(fixed)
    Q = declare(fixed)
    I_st = declare_stream()
    Q_st = declare_stream()
    n_st = declare_stream()

    with for_(n, 0, n < n_avg, n+1):
        with for_(*from_array(a, amplitudes)):
            # play TLS drive pulse with variable amplitude
            play("gauss"*amp(a), "tls1")
            align("tls1", "rr1")
            # measure readout from resonator with calibrated integration weights.
            measure("readout", "rr1", 
                    dual_demod.full("cos", "sin", I),
                    dual_demod.full("minus_sin", "cos", Q),)
            wait(thermalization_time* u.ns, "rr1")
            save(I, I_st)
            save(Q, Q_st)
        save(n, n_st)

    with stream_processing():
        I_st.buffer(len(amplitudes)).average().save("I")
        Q_st.buffer(len(amplitudes)).average().save("Q")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################
simulate = True

if simulate:
    simulation_config = SimulationConfig(duration=20_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, power_rabi, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(samples, plot=True, save_path=str(Path(__file__).resolve()))
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(power_rabi)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, iteration = results.fetch_all()
        # Convert the results into Volts
        I, Q = u.demod2volts(I, READOUT_LEN), u.demod2volts(Q, READOUT_LEN)
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot results
        plt.suptitle("Power Rabi")
        plt.subplot(211)
        plt.cla()
        plt.plot(amplitudes * x180_amp, I, ".")
        plt.ylabel("I quadrature [V]")
        plt.subplot(212)
        plt.cla()
        plt.plot(amplitudes * x180_amp, Q, ".")
        plt.xlabel("Rabi pulse amplitude [V]")
        plt.ylabel("Q quadrature [V]")
        plt.pause(0.1)
        plt.tight_layout()
    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"I_data": I})
    save_data_dict.update({"Q_data": Q})
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])