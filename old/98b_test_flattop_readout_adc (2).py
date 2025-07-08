# %%
"""
A simple program that plays CW tones to all relevant MW channels and takse the DC offsets for the LF FEM channels from the config.
"""

from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
from configuration_flattop_without_octave import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt

###################
# The QUA program #
###################

rr = "q1_rr"
n_avg = 1000
a = 1.5

with program() as prog:
    n = declare(int)

    I_full = declare(fixed)
    Q_full = declare(fixed)
    I_rise = declare(fixed)
    Q_rise = declare(fixed)
    I_flat = declare(fixed)
    Q_flat = declare(fixed)
    I_fall = declare(fixed)
    Q_fall = declare(fixed)

    I_full_st = declare_stream()
    Q_full_st = declare_stream()
    I_rise_st = declare_stream()
    Q_rise_st = declare_stream()
    I_flat_st = declare_stream()
    Q_flat_st = declare_stream()
    I_fall_st = declare_stream()
    Q_fall_st = declare_stream()

    adc_full = declare_stream(adc_trace=True)
    adc_rise = declare_stream(adc_trace=True)
    adc_flat = declare_stream(adc_trace=True)
    adc_fall = declare_stream(adc_trace=True)

    with for_(n, 0, n < n_avg, n + 1):
        # reset phases
        reset_phase(rr)
        reset_phase(f"{rr}_twin")
        reset_phase(f"{rr}_gaussian_flattop")

        align()
        # measure by parts (rise + flattop + fall)
        measure(
            "gaussian_rise" * amp(a),
            f"{rr}_twin",
            adc_rise,
            demod.full("cos", I_rise, "out1"),
            demod.full("sin", Q_rise, "out2"),
        )
        wait(READOUT_GAUSSIAN_RISE_LEN, rr)
        measure(
            "flattop" * amp(a),
            rr,
            adc_flat,
            demod.full("cos", I_flat, "out1"),
            demod.full("sin", Q_flat, "out2"),
        )
        wait(READOUT_FLATTOP_LEN, f"{rr}_twin")
        measure(
            "gaussian_fall" * amp(a),
            f"{rr}_twin",
            adc_fall,
            demod.full("cos", I_fall, "out1"),
            demod.full("sin", Q_fall, "out2"),
        )

        align()

        # measure as 1wf
        measure(
            "gaussian_flattop" * amp(a),
            f"{rr}_gaussian_flattop",
            adc_full,
            demod.full("cos", I_full, "out1"),
            demod.full("sin", Q_full, "out2"),
        )

        save(I_full, I_full_st)
        save(Q_full, Q_full_st)
        save(I_rise, I_rise_st)
        save(Q_rise, Q_rise_st)
        save(I_flat, I_flat_st)
        save(Q_flat, Q_flat_st)
        save(I_fall, I_fall_st)
        save(Q_fall, Q_fall_st)
        wait(10 * u.us)

    with stream_processing():
        # demod singals
        I_rise_st.average().save("I_rise")
        Q_rise_st.average().save("Q_rise")
        I_flat_st.average().save("I_flat")
        Q_flat_st.average().save("Q_flat")
        I_fall_st.average().save("I_fall")
        Q_fall_st.average().save("Q_fall")
        I_full_st.average().save("I_full")
        Q_full_st.average().save("Q_full")

        # adc traces
        adc_rise.input1().average().save("adc_rise1")
        adc_rise.input2().average().save("adc_rise2")
        adc_flat.input1().average().save("adc_flat1")
        adc_flat.input2().average().save("adc_flat2")
        adc_fall.input1().average().save("adc_fall1")
        adc_fall.input2().average().save("adc_fall2")
        adc_full.input1().average().save("adc_full1")
        adc_full.input2().average().save("adc_full2")


if __name__ == "__main__":
    #####################################
    #  Open Communication with the QOP  #
    #####################################
    qmm = QuantumMachinesManager(
        host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
    )

    ###########################
    # Run or Simulate Program #
    ###########################

    simulate = False

    if simulate:
        # Simulates the QUA program for the specified duration
        simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
        # Simulate blocks python until the simulation is done
        job = qmm.simulate(config, prog, simulation_config)
        # Plot the simulated samples
        job.get_simulated_samples().con1.plot()
    else:
        from qm import generate_qua_script

        sourceFile = open("debug_98b_test_flattop_readout_adc.py", "w")
        print(generate_qua_script(prog, config), file=sourceFile)
        sourceFile.close()

        # Open a quantum machine to execute the QUA program
        qm = qmm.open_qm(config)
        # Send the QUA program to the OPX, which compiles and executes it
        job = qm.execute(prog)
        fetch_names = [
            "I_rise",
            "Q_rise",
            "I_flat",
            "Q_flat",
            "I_fall",
            "Q_fall",
            "I_full",
            "Q_full",
            "adc_rise1",
            "adc_rise2",
            "adc_flat1",
            "adc_flat2",
            "adc_fall1",
            "adc_fall2",
            "adc_full1",
            "adc_full2",
        ]
        # Tool to easily fetch results from the OPX (results_handle used in it)
        results = fetching_tool(job, fetch_names)
        # Prepare the figure for live plotting
        (
            I_rise,
            Q_rise,
            I_flat,
            Q_flat,
            I_fall,
            Q_fall,
            I_full,
            Q_full,
            adc_rise1,
            adc_rise2,
            adc_flat1,
            adc_flat2,
            adc_fall1,
            adc_fall2,
            adc_full1,
            adc_full2,
        ) = results.fetch_all()

        I_rise, Q_rise = u.raw2volts(I_rise), u.raw2volts(Q_rise)
        I_flat, Q_flat = u.raw2volts(I_flat), u.raw2volts(Q_flat)
        I_fall, Q_fall = u.raw2volts(I_fall), u.raw2volts(Q_fall)
        I_full, Q_full = u.raw2volts(I_full), u.raw2volts(Q_full)

        adc_rise1, adc_rise2 = u.raw2volts(adc_rise1), u.raw2volts(adc_rise2)
        adc_flat1, adc_flat2 = u.raw2volts(adc_flat1), u.raw2volts(adc_flat2)
        adc_fall1, adc_fall2 = u.raw2volts(adc_fall1), u.raw2volts(adc_fall2)
        adc_full1, adc_full2 = u.raw2volts(adc_full1), u.raw2volts(adc_full2)

        print()
        print(f"I_full                   = {1e6 * I_full:4.3f}")
        print(f"I_rise + I_flat + I_fall = {1e6 * (I_rise + I_flat + I_fall):4.3f}\n")
        print(f"Q_full                   = {1e6 * Q_full:4.3f}")
        print(f"Q_rise + Q_flat + Q_fall = {1e6 * (Q_rise + Q_flat + Q_fall):4.3f}\n")

        t1 = READOUT_GAUSSIAN_RISE_LEN
        t2 = READOUT_FLATTOP_LEN
        t3 = READOUT_GAUSSIAN_FALL_LEN
        t4 = READOUT_FLATTOP_TOTAL_LEN

        ts01 = np.arange(t1)
        ts12 = np.arange(t1, t1 + t2, 1)
        ts23 = np.arange(t1 + t2, t1 + t2 + t3, 1)
        ts03 = np.arange(t4)

        # plot adc traces
        fig, axs = plt.subplots(2, 2, figsize=(8, 6), sharey="col", sharex=True)

        ax = axs[0, 0]
        ax.plot(ts01, adc_rise1, c="c")
        ax.plot(ts12, adc_flat1, c="g")
        ax.plot(ts23, adc_fall1, c="m")
        # ax.set_xlabel("time [ns]")
        ax.set_ylabel("signal [V]")
        ax.legend(["gauss rise", "flattop", "gauss fall"])
        ax.set_title("gauss rise + flattop + fall [I]")

        ax = axs[1, 0]
        ax.plot(ts03, adc_full1, c="b")
        ax.set_xlabel("time [ns]")
        ax.set_ylabel("signal [V]")
        ax.set_title("gaussian flattop in 1wf [I]")

        ax = axs[0, 1]
        ax.plot(ts01, adc_rise2, c="c")
        ax.plot(ts12, adc_flat2, c="g")
        ax.plot(ts23, adc_fall2, c="m")
        # ax.set_xlabel("time [ns]")
        ax.set_ylabel("signal [V]")
        ax.set_title("gauss rise + flattop + fall [Q]")

        ax = axs[1, 1]
        ax.plot(ts03, adc_full2, c="b")
        ax.set_xlabel("time [ns]")
        ax.set_ylabel("signal [V]")
        ax.set_title("gaussian flattop in 1wf [Q]")

        plt.tight_layout()
        plt.show()
# %%
