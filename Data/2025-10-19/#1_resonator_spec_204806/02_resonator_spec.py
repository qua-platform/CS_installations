import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
from qualang_tools.loops import from_array
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from configuration import * 
from qualang_tools.results.data_handler import DataHandler
from macros import *
u = unit(coerce_to_integer=True)

# program parameters
n_avg = 10000  

# Frequency sweep (full range)
IF_min = 150 * u.MHz
IF_max = 200 * u.MHz
dIF    = 1000 * u.kHz
frequencies = np.arange(IF_min, IF_max + 0.1, dIF)

# Pull readout / depletion from config (ns).
READOUT_LEN_NS = int(config["pulses"]["readout_pulse"]["length"])
DEPL_CC = int(DEPLETION_TIME/4)

# Choice of element for resonator spectroscopy (rr1, rr2, rr3)
res_keys = ["rr1", "rr2", "rr3"]
multiplexed = True

# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "IF_frequencies": frequencies,
    "config": config,
}

# =============================================================================
#                                QUA PROGRAM
# =============================================================================
with program() as res_spec:
    n = declare(int)
    f = declare(int)
    I = [declare(fixed) for _ in range(len(res_keys))]
    Q = [declare(fixed) for _ in range(len(res_keys))]
    I_st = [declare_stream() for _ in range(len(res_keys))]
    Q_st = [declare_stream() for _ in range(len(res_keys))]
    n_st = declare_stream()

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(f, frequencies)):
            for i in range(len(res_keys)):
                update_frequency(res_keys[i], f)
                measure(
                    "readout", res_keys[i],
                    dual_demod.full("cos", "out1", "sin", "out2", I[i]),
                    dual_demod.full("minus_sin", "out1", "cos", "out2", Q[i]),
                )
                save(I[i], I_st[i])
                save(Q[i], Q_st[i])
                if multiplexed:
                    wait(DEPL_CC, res_keys[i])
                else:
                    align()
                    if i == len(res_keys)-1:
                        wait(DEPL_CC)

        save(n, n_st)

    with stream_processing():
        n_st.save("iteration")
        for j in range(len(res_keys)):
            I_st[j].buffer(len(frequencies)).average().save("I_"+str(j))
            Q_st[j].buffer(len(frequencies)).average().save("Q_"+str(j))

simulate = False
# =============================================================================
#                           SIMULATE OR EXECUTE
# =============================================================================
if simulate:
    qmm = QuantumMachinesManager(host=qop_ip, 
                                    cluster_name=cluster_name)

    simulation_config = SimulationConfig(duration=1_000) # duration is in units of clock cycles, i.e., 4 nanoseconds

    # --- simulate ---
    job = qmm.simulate(config, res_spec, simulation_config)
    samples = job.get_simulated_samples()
    samples.con1.plot()
    wr = job.get_simulated_waveform_report()
    wr.create_plot(samples, plot=True, save_path=str(Path(__file__).resolve()))
        

else:
    qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave_calibration_db_path=os.getcwd())
    qm = qmm.open_qm(config)
    job = qm.execute(res_spec)
    result_names = mp_result_names(res_keys, single_tags = ["iteration"], mp_tags = ["I", "Q"])
    res_handles = fetching_tool(job, data_list = result_names, mode = "live")
    # Waits (blocks the Python console) until all results have been acquired
    fig = plt.figure()
    interrupt_on_close(fig, job)  #  Interrupts the job when closing the figure
    while res_handles.is_processing():
        iteration, I, Q = mp_fetch_all(res_handles, res_keys, num_single_tags=1)
        # Convert results into Volts
        for j in range(len(res_keys)):
            I[j] = u.demod2volts(I[j], READOUT_LEN)
            Q[j] = u.demod2volts(Q[j], READOUT_LEN)
        S = I + 1j * Q
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        # Progress bar
        progress_counter(iteration, n_avg, start_time=res_handles.get_start_time())
        # Plot results
        plt.suptitle(f"Resonator spectroscopy - LO = {LO_RR / u.GHz} GHz")
        ax1 = plt.subplot(211)
        plt.cla()
        for j in range(len(res_keys)):
            plt.plot((frequencies + LO_RR) / u.MHz, R[j], ".")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.subplot(212, sharex=ax1)
        plt.cla()
        for j in range(len(res_keys)):
            plt.plot((frequencies + LO_RR) / u.MHz, signal.detrend(np.unwrap(phase[j])), ".")
        plt.xlabel("Frequency [MHz]")
        plt.ylabel("Phase [rad]")
        plt.pause(0.1)
        plt.tight_layout()
# Fit the results to extract the resonance frequency
    try:
        from qualang_tools.plot.fitting import Fit

        fit = Fit()
        plt.figure()
        res_spec_fit = fit.reflection_resonator_spectroscopy(frequencies / u.MHz, R, plot=True)
        plt.title(f"Resonator spectroscopy - LO = {LO_RR / u.GHz} GHz")
        plt.xlabel("Intermediate frequency [MHz]")
        plt.ylabel(r"R=$\sqrt{I^2 + Q^2}$ [V]")
        print(f"Resonator IF to update in the config: resonator_IF = {res_spec_fit['f'][0]:.6f} MHz")
        print(f"Resonator resonance frequency to update in the config: resonator_freq = {(res_spec_fit['f'][0] + LO_RR/1e6):.6f} MHz")

    except (Exception,):
        pass

    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()
    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"I_data": I})
    save_data_dict.update({"Q_data": Q})
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])