import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.simulate import LoopbackInterface
from qm_saas import QmSaas, QOPVersion
from qualang_tools.loops import from_array
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from configuration import * 

u = unit(coerce_to_integer=True)

# USER / SIMULATION SETTINGS
simulate = False   
n_avg = 100          # averages

# Frequency sweep (full range)
IF_min = 150 * u.MHz
IF_max = 200 * u.MHz
dIF    = 1000 * u.kHz
IF_array = np.arange(IF_min, IF_max + 0.1, dIF)

# LO candidates (used only on hardware; sim uses one LO pass)
LO_min = 3e9
LO_max = 5e9
dLO    = (IF_max - IF_min) / 2
LO_array = np.arange(LO_min, LO_max + 0.1, dLO)

# ---------- (limit memory usage of simulation) ----------
SIM_N_IF   = 32   # IF points in sim
SIM_N_AVG  = 2    # averages in sim
IF_sweep   = IF_array[:SIM_N_IF] if simulate else IF_array
n_avg_eff  = SIM_N_AVG if simulate else n_avg
N_LO_SWEEPS = 1 if simulate else len(LO_array)

# Absolute frequency axis (Hz) for plotting
freq_axis = IF_sweep + (LO_array[0] if (simulate and len(LO_array)) else 0.0)
points_per_sweep = len(IF_sweep)

# Loopback (sim) settings
loopback_latency_ns  = 200
loopback_noise_power = 5e-4

# Pull readout / depletion from config (ns).
READOUT_LEN_NS = int(config["pulses"]["readout_pulse"]["length"])
DEPL_NS_CONF = int(DEPLETION_TIME)

# Choice of element for resonator spectroscopy (rr1, rr2, rr3)
RR_ELEM = "rr2"

# =============================================================================
#                                QUA PROGRAM
# =============================================================================
with program() as res_spec:
    n = declare(int)
    l = declare(int)
    f = declare(int)
    I = declare(fixed)
    Q = declare(fixed)
    I_st = declare_stream()
    Q_st = declare_stream()
    n_st = declare_stream()

    with for_(l, 0, l < N_LO_SWEEPS, l + 1):
        if not simulate:
            pause()  # real LO change gate
        with for_(n, 0, n < n_avg_eff, n + 1):
            with for_(*from_array(f, IF_sweep)):
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
        I_st.buffer(points_per_sweep).average().save("I")
        Q_st.buffer(points_per_sweep).average().save("Q")
        n_st.save("iteration")


# =============================================================================
#                           SIMULATE OR EXECUTE
# =============================================================================
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

        # Duration estimate
        point_ns   = READOUT_LEN_NS + DEPL_NS_CONF
        total_ns   = point_ns * points_per_sweep * n_avg_eff * N_LO_SWEEPS
        sim_dur_cc = max(10_000, int(total_ns / 4) + 2_000)   # 1 cc = 4 ns

        sim_if = LoopbackInterface(
            [("con1", 1, "con1", 1), ("con1", 2, "con1", 2)],
            latency=loopback_latency_ns,
            noisePower=loopback_noise_power,
        )
        sim_cfg = SimulationConfig(
            duration=sim_dur_cc,
            simulation_interface=sim_if,
            extraProcessingTimeoutInMs=100_000,
        )

        # --- simulate ---
        job = qmm.simulate(config, res_spec, sim_cfg)

        # --- fetch demod results from stream_processing ---
        res = job.result_handles
        res.wait_for_all_values()
        I = res.get("I").fetch_all()
        Q = res.get("Q").fetch_all()
        if I is None or Q is None:
            raise RuntimeError("Streams not filled — reduce duration or points_per_sweep mismatch")

        # Convert to Volts (complex)
        S = u.demod2volts(I + 1j * Q, READOUT_LEN_NS)
        # Plot
        R = np.abs(S)
        phase = np.angle(S)
        plt.figure()
        ax1 = plt.subplot(211)
        plt.plot(freq_axis / u.MHz, R, ".")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        ax2 = plt.subplot(212, sharex=ax1)
        plt.plot(freq_axis / u.MHz, signal.detrend(np.unwrap(phase)), ".")
        plt.xlabel("Frequency [MHz]")
        plt.ylabel("Phase [rad]")
        plt.tight_layout()
        plt.show()

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
        plt.plot((IF_array + LO_RR) / u.MHz, R, ".")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.subplot(212, sharex=ax1)
        plt.cla()
        plt.plot((IF_array + LO_RR) / u.MHz, signal.detrend(np.unwrap(phase)), ".")
        plt.xlabel("Frequency [MHz]")
        plt.ylabel("Phase [rad]")
        plt.pause(0.1)
        plt.tight_layout()