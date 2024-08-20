"""
TIME RABI EXPERIMENT

This experiment sweeps the duration of a manipulation pulse which is
calibrated to induce Rabi oscillations.

It includes a sequence of voltage pulses to initialize, manipulate
and readout the charge qubit state.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.addons.variables import assign_variables_to_element
import matplotlib.pyplot as plt
import copy
from qualang_tools.loops.loops import from_array
from qualang_tools.voltage_gates import VoltageGateSequence

times = np.arange(1, 16, 1)

# todo: add baking
# todo: send email with python package instructions
# todo: mention might need adder
# todo: change lock_in frequency to 200Hz and fix comments
# todo: update 2b diagram

with program() as init_search_prog:
    n = declare(int)  # QUA integer used as an index for the averaging loop
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = declare(fixed)
    Q = declare(fixed)
    I_st = declare_stream()
    Q_st = declare_stream()
    t = declare(int)

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("QDS", I, Q)

    with for_(n, 0, n < n_shots, n + 1):
        save(n, n_st)

        with for_(*from_array(t, times)):
            # initialize the charge qubit
            seq.add_step(voltage_point_name="init", ramp_duration=ramp_duration)
            # set detuning to zero for a variable amount of time to induce Rabi oscillations
            seq.add_step(voltage_point_name="manipulation", duration=t)  # to manipulate the detuning
            # pulse to the readout point of the qubit
            seq.add_step(voltage_point_name="readout", ramp_duration=ramp_duration)
            # apply auto-compensation for the capacitive charge build-up on the bias-tee
            seq.add_compensation_pulse(duration=duration_compensation_pulse)
            # Ramp the voltage down to zero at the end of the triangle (needed with sticky elements)
            seq.ramp_to_zero()

            # Measure the charge state during readout pulse
            wait((duration_init + t + 2*ramp_duration) * u.ns, readout_element)
            measure(
                "readout",
                readout_element,
                None,
                demod.full("cos", I, "out1"),
                demod.full("cos", Q, "out1")
            )

            # Wait at each iteration in order to ensure that the data will not be transferred faster than 1 sample
            # per µs to the stream processing.
            wait(1_000 * u.ns)  # in ns

    # Stream processing section used to process the data before saving it
    with stream_processing():
        n_st.save("iteration")
        I_st.buffer(len(times)).average().save("I")
        Q_st.buffer(len(times)).average().save("Q")

qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=None)

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(local_config, init_search_prog, simulation_config)
    job.get_simulated_samples().con1.plot()
    plt.show(block=False)
else:
    # Open the quantum machine
    qm = qmm.open_qm(local_config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(init_search_prog)
    # Get results from QUA program and initialize live plotting
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():
        # Fetch the data from the last OPX run corresponding to the current slow axis iteration
        I, Q, iteration = results.fetch_all()
        # Convert results into Volts
        S = u.demod2volts(I + 1j * Q, rf_readout_length)
        R = np.abs(S)  # Amplitude
        phase_d = np.angle(S)  # Phase
        # Progress bar
        progress_counter(iteration, n_shots, start_time=results.start_time)
        plt.clf()
        plt.pcolor(times * 4, amps, R)
        plt.colorbar()
        plt.tight_layout()
        plt.xlabel('X4 duration [ns]')
        plt.ylabel('X4 scaling amp [a.u.]')
        plt.pause(0.1)

qdac.close()
plt.show()
