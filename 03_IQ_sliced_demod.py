"""
    Example of sliced demod with the OPX to recover pulse envelopes.
"""

import matplotlib.pyplot as plt
from configuration import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from scipy.signal import savgol_filter

###################
# The QUA program #
###################
n_avg = 100  # Number of averaging loops

# Set the sliced demod parameters
division_length = 2  # Size of each demodulation slice in clock cycles
number_of_divisions = int((readout_len) / (4 * division_length))

with program() as raw_trace_prog:
    n = declare(int)  # QUA variable for the averaging loop
    adc_st = declare_stream(adc_trace=True)  # The stream to store the raw ADC trace
    II = declare(fixed, size=number_of_divisions)
    II_st = declare_stream()
    IQ = declare(fixed, size=number_of_divisions)
    IQ_st = declare_stream()
    QI = declare(fixed, size=number_of_divisions)
    QI_st = declare_stream()
    QQ = declare(fixed, size=number_of_divisions)
    QQ_st = declare_stream()
    ind = declare(int)

    with for_(n, 0, n < n_avg, n + 1):
        # Reset the phase of the digital oscillator associated to the resonator element. Needed to average the cosine signal.
        reset_phase("resonator")
        # Sends the readout pulse and stores the raw ADC traces in the stream called "adc_st"
        measure(
            "readout",
            "resonator",
            adc_st,  # Store the raw ADC traces
            demod.sliced(
                "cos", II, division_length, "out1"
            ),  # Demodulate the signals to get the 'I' & 'Q' quadratures.
            demod.sliced("sin", IQ, division_length, "out2"),  # Without integrating the envelope.
            demod.sliced("minus_sin", QI, division_length, "out1"),
            demod.sliced("cos", QQ, division_length, "out2"),
        )
        # Save the slices to the SP and wait for the resonator to deplete
        with for_(ind, 0, ind < number_of_divisions, ind + 1):
            save(II[ind], II_st)
            save(IQ[ind], IQ_st)
            save(QI[ind], QI_st)
            save(QQ[ind], QQ_st)
        wait(2000 * u.ns, "resonator")

    with stream_processing():
        # Will save average:
        adc_st.input1().average().save("adc1")
        adc_st.input2().average().save("adc2")
        # # Will save only last run:
        adc_st.input1().save("adc1_single_run")
        adc_st.input2().save("adc2_single_run")

        II_st.buffer(number_of_divisions).average().save("II")
        IQ_st.buffer(number_of_divisions).average().save("IQ")
        QI_st.buffer(number_of_divisions).average().save("QI")
        QQ_st.buffer(number_of_divisions).average().save("QQ")


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
    job = qmm.simulate(config, raw_trace_prog, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(raw_trace_prog)
    # Creates a result handle to fetch data from the OPX
    res_handles = job.result_handles
    # Waits (blocks the Python console) until all results have been acquired
    res_handles.wait_for_all_values()
    # Fetch the raw ADC traces and convert them into Volts
    adc1 = u.raw2volts(res_handles.get("adc1").fetch_all())
    adc2 = u.raw2volts(res_handles.get("adc2").fetch_all())
    adc1_single_run = u.raw2volts(res_handles.get("adc1_single_run").fetch_all())
    adc2_single_run = u.raw2volts(res_handles.get("adc2_single_run").fetch_all())
    # Fetch the demodulated time traces and convert them into Volts
    I_trace = u.demod2volts(
        res_handles.get("II").fetch_all() + res_handles.get("IQ").fetch_all(),
        division_length,
    )
    Q_trace = u.demod2volts(
        res_handles.get("QI").fetch_all() + res_handles.get("QQ").fetch_all(),
        division_length,
    )

    # Plot data
    fig = plt.figure(figsize=(12, 5))
    plt.subplot(131)
    plt.title("Single run")
    plt.plot(adc1_single_run, "b", label="Input 1")
    plt.plot(adc2_single_run, "r", label="Input 2")
    xl = plt.xlim()
    yl = plt.ylim()
    plt.axhline(y=0.5)
    plt.axhline(y=-0.5)
    plt.xlabel("Time [ns]")
    plt.ylabel("Signal amplitude [V]")
    plt.grid("all")
    plt.legend()
    plt.subplot(132)
    plt.title("Averaged run")
    plt.plot(adc1, "b", label="Input 1")
    plt.plot(adc2, "r", label="Input 2")
    xl = plt.xlim()
    yl = plt.ylim()
    plt.xlabel("Time [ns]")
    plt.grid("all")
    plt.legend()
    plt.subplot(133)
    plt.title("Demodulted I and Q traces")
    plt.plot(
        np.linspace(0, number_of_divisions * division_length * 4, number_of_divisions),
        I_trace,
        "b.--",
        label="Demodulated I trace",
    )
    plt.plot(
        np.linspace(0, number_of_divisions * division_length * 4, number_of_divisions),
        Q_trace,
        "r.--",
        label="Demodulated Q trace",
    )
    plt.legend()
    plt.xlabel("Time [ns]")
    plt.grid("all")
    plt.tight_layout()
    plt.show()
