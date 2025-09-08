# Time of flight calibration helper:
# TX: OPX AO1/2 -> Octave RF OUT1 -> fridge
# RX: fridge -> Octave RF IN1 -> OPX AI1/2
# Captures raw ADC traces to estimate TOF, AI offsets, and check AI gain.
from pathlib import Path
import os
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import numpy as np
from qm.simulate import LoopbackInterface
from qm_saas import QmSaas, QOPVersion

u = unit(coerce_to_integer=True)

# User parameters
n_avg = 100               # averages

# loopback simulated experimental parameters
lb_latency = 80     # cable+fridge delay
lb_noise_power = 1e-4   # V^2 (≈22 mVrms)

# Choice of element for time of flight calibration (rr1, rr2, rr3)
RR_ELEM = "rr1"

with program() as raw_trace_prog:
    n = declare(int)
    adc_st = declare_stream(adc_trace=True)  # captures raw AI samples

    with for_(n, 0, n < n_avg, n + 1):
        reset_if_phase(RR_ELEM)                   # keep demod phase coherent across averages
        measure("readout", RR_ELEM, adc_stream=adc_st)
        wait(DEPLETION_TIME * u.ns, RR_ELEM)

    with stream_processing():
        # Averages over n_avg for each ADC:
        adc_st.input1().average().save("adc1")
        adc_st.input2().average().save("adc2")
        # Keep last-shot traces:
        adc_st.input1().save("adc1_single_run")
        adc_st.input2().save("adc2_single_run")


# Toggle between simulate and run-on-hardware
simulate = False

if simulate:
        # --- SaaS login ---
    client = QmSaas(
    host="qm-saas.dev.quantum-machines.co",
    email="benjamin.safvati@quantum-machines.co",
    password="ubq@yvm3RXP1bwb5abv"
    )

    with client.simulator(QOPVersion(os.environ.get("QM_QOP_VERSION", "v2_5_0"))) as inst:
        inst.spawn()
        qmm = QuantumMachinesManager(
            host=inst.host,
            port=inst.port,
            connection_headers=inst.default_connection_headers,
        )
        # Duration in QUA clock cycles (1 cc = 4 ns)
        sim_dur_cc = 40_000

        # AO1->AI1 and AO2->AI2 loopback with latency & noise
        sim_if = LoopbackInterface(
            [("con1", 1, "con1", 1), ("con1", 2, "con1", 2)],
            latency=lb_latency,
            noisePower=lb_noise_power,
        )

        job = qmm.simulate(
            config,
            raw_trace_prog,
            SimulationConfig(duration=sim_dur_cc, simulation_interface=sim_if),
        )

        # (optional) still see the DAC activity
        samples = job.get_simulated_samples()
        samples.con1.plot()
        wr = job.get_simulated_waveform_report()
        wr.create_plot(samples, plot=True, save_path=str(Path(__file__).resolve()))

        # fetch the same result streams as on hardware
        res = job.result_handles
        res.wait_for_all_values()
        adc1 = u.raw2volts(res.get("adc1").fetch_all())
        adc2 = u.raw2volts(res.get("adc2").fetch_all())
        adc1_single_run = u.raw2volts(res.get("adc1_single_run").fetch_all())
        adc2_single_run = u.raw2volts(res.get("adc2_single_run").fetch_all())

        adc1_mean = np.mean(adc1)
        adc2_mean = np.mean(adc2)
        adc1_unbiased = adc1 - adc1_mean
        adc2_unbiased = adc2 - adc2_mean
        signal = savgol_filter(np.abs(adc1_unbiased + 1j * adc2_unbiased), 11, 3)
        th = (np.mean(signal[:100]) + np.mean(signal[:-100])) / 2
        delay = np.where(signal > th)[0][0]
        delay = np.round(delay / 4) * 4  # closest multiple of 4 ns

        fig = plt.figure()
        plt.subplot(121)
        plt.title("Single run (simulate)")
        plt.plot(adc1_single_run, "b", label="Input 1")
        plt.plot(adc2_single_run, "r", label="Input 2")
        xl = plt.xlim()
        yl = plt.ylim()
        plt.axhline(y=0.5)
        plt.axhline(y=-0.5)
        plt.plot(xl, adc1_mean * np.ones(2), "k--")
        plt.plot(xl, adc2_mean * np.ones(2), "k--")
        plt.plot(delay * np.ones(2), yl, "k--")
        plt.xlabel("Time [ns]")
        plt.ylabel("Signal amplitude [V]")
        plt.legend()

        plt.subplot(122)
        plt.title("Averaged run (simulate)")
        plt.plot(adc1, "b", label="Input 1")
        plt.plot(adc2, "r", label="Input 2")
        xl = plt.xlim()
        yl = plt.ylim()
        plt.plot(xl, adc1_mean * np.ones(2), "k--")
        plt.plot(xl, adc2_mean * np.ones(2), "k--")
        plt.plot(delay * np.ones(2), yl, "k--")
        plt.xlabel("Time [ns]")
        plt.legend()
        plt.grid("both")
        plt.tight_layout()
        plt.show()

        print(f"[SIM] DC offset to add to I in the config: {-adc1_mean:.6f} V")
        print(f"[SIM] DC offset to add to Q in the config: {-adc2_mean:.6f} V")
        print(f"[SIM] Time Of Flight to add in the config: {delay} ns")
else:
    qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave_calibration_db_path=os.getcwd()
)
    qm = qmm.open_qm(config)
    job = qm.execute(raw_trace_prog)
    res = job.result_handles
    res.wait_for_all_values()

    # Fetch the raw ADC traces and convert them into Volts
    adc1 = u.raw2volts(res.get("adc1").fetch_all())
    adc2 = u.raw2volts(res.get("adc2").fetch_all())
    adc1_single_run = u.raw2volts(res.get("adc1_single_run").fetch_all())
    adc2_single_run = u.raw2volts(res.get("adc2_single_run").fetch_all())
    # Derive the average values
    adc1_mean = np.mean(adc1)
    adc2_mean = np.mean(adc2)
    # Remove the average values
    adc1_unbiased = adc1 - np.mean(adc1)
    adc2_unbiased = adc2 - np.mean(adc2)
    # Filter the data to get the pulse arrival time
    signal = savgol_filter(np.abs(adc1_unbiased + 1j * adc2_unbiased), 11, 3)
    # Detect the arrival of the readout signal
    th = (np.mean(signal[:100]) + np.mean(signal[:-100])) / 2
    delay = np.where(signal > th)[0][0]
    delay = np.round(delay / 4) * 4  # Find the closest multiple integer of 4ns

    # Plot data
    fig = plt.figure()
    plt.subplot(121)
    plt.title("Single run")
    plt.plot(adc1_single_run, "b", label="Input 1")
    plt.plot(adc2_single_run, "r", label="Input 2")
    xl = plt.xlim()
    yl = plt.ylim()
    plt.axhline(y=0.5)
    plt.axhline(y=-0.5)
    plt.plot(xl, adc1_mean * np.ones(2), "k--")
    plt.plot(xl, adc2_mean * np.ones(2), "k--")
    plt.plot(delay * np.ones(2), yl, "k--")
    plt.xlabel("Time [ns]")
    plt.ylabel("Signal amplitude [V]")
    plt.legend()
    plt.subplot(122)
    plt.title("Averaged run")
    plt.plot(adc1, "b", label="Input 1")
    plt.plot(adc2, "r", label="Input 2")
    xl = plt.xlim()
    yl = plt.ylim()
    plt.plot(xl, adc1_mean * np.ones(2), "k--")
    plt.plot(xl, adc2_mean * np.ones(2), "k--")
    plt.plot(delay * np.ones(2), yl, "k--")
    plt.xlabel("Time [ns]")
    plt.legend()
    plt.grid("all")
    plt.tight_layout()
    plt.show()

    # Update the config
    print(f"DC offset to add to I in the config: {-adc1_mean:.6f} V")
    print(f"DC offset to add to Q in the config: {-adc2_mean:.6f} V")
    print(f"Time Of Flight to add in the config: {delay} ns")