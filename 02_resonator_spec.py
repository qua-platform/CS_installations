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
DEPL_NS_CONF = int(DEPLETION_TIME)

# Choice of element for resonator spectroscopy (rr1, rr2, rr3)
RR_ELEM = "rr2"


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
    I = declare(fixed)
    Q = declare(fixed)
    I_st = declare_stream()
    Q_st = declare_stream()
    n_st = declare_stream()

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(f, frequencies)):
            update_frequency(RR_ELEM, f)
            measure(
                "readout", RR_ELEM,
                dual_demod.full("cos", "out1", "sin", "out2", I),
                dual_demod.full("minus_sin", "out1", "cos", "out2", Q),
            )
            wait(DEPL_NS_CONF * u.ns, RR_ELEM)
            save(I, I_st)
            save(Q, Q_st)
        save(n, n_st)

    with stream_processing():
        I_st.buffer(len(frequencies)).average().save("I")
        Q_st.buffer(len(frequencies)).average().save("Q")
        n_st.save("iteration")

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
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")

    fig = plt.figure()
    interrupt_on_close(fig, job)
    while results.is_processing():
        I, Q, iteration = results.fetch_all()
        S = u.demod2volts(I + 1j * Q, READOUT_LEN_NS)
        R = np.abs(S)
        phase = np.angle(S)
        progress_counter(iteration, n_avg, start_time=results.get_start_time())

        plt.suptitle(f"Resonator spectroscopy - LO = {LO_RR / u.GHz} GHz")
        ax1 = plt.subplot(211)
        plt.cla()
        plt.plot((frequencies + LO_RR) / u.MHz, R, ".")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.subplot(212, sharex=ax1)
        plt.cla()
        plt.plot((frequencies + LO_RR) / u.MHz, signal.detrend(np.unwrap(phase)), ".")
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