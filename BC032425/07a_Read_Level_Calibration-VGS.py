# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 10:32:23 2025

@author: BradCole
"""

"""
Read-level Calibration
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.addons.variables import assign_variables_to_element
import matplotlib.pyplot as plt
from macros import RF_reflectometry_macro, DC_current_sensing_macro

###########################
# Run or Simulate Program #
###########################
simulate = False
###################
# The QUA program #
###################

n_avg = 100

readout_levels = np.linspace(-0.010, 0.010, 10)
durations = np.arange(0, readout_len, 1)

# Add the relevant voltage points describing the "slow" sequence (no qubit pulse)
seq = OPX_virtual_gate_sequence(config, ["Vd1_sticky"])
seq.add_points("load/wait", level_manip, duration_manip)
#seq.add_points("read", level_readout, readout_len)
seq.add_points("empty", level_init, duration_init)

with program() as RLC_prog:
    r = declare(fixed)
    n = declare(int)  # QUA integer used as an index for the averaging loop
    t = declare(int)  # QUA variable for the qubit pulse duration
    Vpi = declare(fixed)  # QUA variable for the qubit drive amplitude
    t1 = declare(int)
    t1_st = declare_stream()
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    #I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    #Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    dc_signal = declare(fixed)  # QUA variable for the measured dc signal
    dc_signal_st = declare_stream()
    adc_stream = declare_stream(adc_trace = True)

    # Ensure that the result variables are assigned to the measurement elements
    #assign_variables_to_element("tank_circuit", I, Q)
    assign_variables_to_element("TIA", dc_signal)
    # seq.add_step(voltage_point_name="readout", duration=16)
    with for_(n, 0, n < n_avg, n + 1):  # The averaging loop
        save(n, n_st)
        
        with for_each_(r, readout_levels.tolist()):
    
            with strict_timing_():  # Ensure that the sequence will be played without gap
                # Navigate through the charge stability map
                seq.add_step(voltage_point_name="load/wait", duration= duration_manip )
                seq.add_step(level = [r], duration = duration_readout)
                seq.add_step(voltage_point_name="empty", duration = duration_init)
                seq.add_compensation_pulse(duration=duration_compensation_pulse)
    
                # Drive the singlet-triplet qubit using an exchange pulse at the end of the manipulation step
                #wait(duration_init * u.ns, "qubit")  # Need -4 cycles to compensate the gap
                #play("pi", "qubit")
    
                # Measure the dot right after the qubit manipulation
                #wait((duration_manip), "TIA")
                #I, Q, I_st, Q_st = RF_reflectometry_macro(I=I, Q=Q)
                # wait(delay, "TIA")
                measure("readout", "TIA", adc_stream, integration.full("constant", dc_signal, "out1"), timestamp_stream = t1_st)
                save(dc_signal, dc_signal_st)
                
                
                # Ramp the background voltage to zero to avoid propagating floating point errors
            seq.ramp_to_zero()
            wait(500*u.ns)

    # Stream processing section used to process the data before saving it.
    with stream_processing():
        n_st.save("iteration")
        # Cast the data into a 1D vector and performs a global averaging of the received 1D vectors together.
        # RF reflectometry
        #I_st.buffer(len(durations)).average().save("I")
        #Q_st.buffer(len(durations)).average().save("Q")
        # DC current sensing
        adc_stream.input1().buffer(len(readout_levels)).average().save("adc_stream")
        dc_signal_st.buffer(len(readout_levels)).average().save("dc_signal")
        t1_st.buffer(len(readout_levels)).save_all("times")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)


if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, RLC_prog, simulation_config)
    # Plot the simulated samples
    plt.figure()
    plt.subplot(211)
    job.get_simulated_samples().con1.plot()
    plt.axhline(level_init[0], color="k", linestyle="--")
    plt.axhline(level_manip[0], color="k", linestyle="--")
    plt.axhline(level_readout[0], color="k", linestyle="--")
    plt.axhline(level_init[1], color="k", linestyle="--")
    plt.axhline(level_manip[1], color="k", linestyle="--")
    plt.axhline(level_readout[1], color="k", linestyle="--")
    plt.yticks(
        [
            level_readout[1],
            level_manip[1],
            level_init[1],
            0.0,
            level_init[0],
            level_manip[0],
            level_readout[0],
        ],
        ["readout", "manip", "init", "0", "init", "manip", "readout"],
    )
    plt.legend("")
    from macros import get_filtered_voltage

    plt.subplot(212)
    get_filtered_voltage(job.get_simulated_samples().con1.analog["1"], 1e-9, bias_tee_cut_off_frequency, True)

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it


    #To do: Set all relevant voltages with Nanonis here

    job = qm.execute(RLC_prog)
    # Get results from QUA program and initialize live plotting
    results = fetching_tool(job, data_list=["dc_signal", "adc_stream", "iteration", "times"])
    # Live plotting
    # fig = plt.figure()
    # interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    # while results.is_processing():
    # Fetch the data from the last OPX run corresponding to the current slow axis iteration
    DC_signal, adc_stream_data, iteration, times = results.fetch_all()
    #print(adc_single_run)
    #print(adc_single_run.shape)
    # Convert results into Volts
    # S = u.demod2volts(I + 1j * Q, reflectometry_readout_length)
    # R = np.abs(S)  # Amplitude
    # phase = np.angle(S)  # Phase
    DC_signal = u.demod2volts(DC_signal, readout_len)
    print(DC_signal, DC_signal.shape)
    #adc_data = u.raw2volts(adc_stream_data)
    # Progress bar
    # progress_counter(iteration, n_avg)
    # Plot data
    # plt.cla()
    # plt.pcolor(durations, readout_levels, DC_signal, label = "DC_signal Average")
    # plt.axvline(duration_manip, color="k", linestyle="--")
    # plt.axvline(duration_manip+duration_readout, color="k", linestyle="--")
    # plt.xlabel("Measurement Time [ns]")
    # plt.ylabel("ADC_data [mV]")
    # plt.tight_layout()

    # plt.pause(0.1)
    
    # fig2 = plt.figure()
    # plt.plot(durations, DC_signal[2])
    # plt.axvline(duration_manip, color="k", linestyle="--")
    # plt.axvline(duration_manip+duration_readout, color="k", linestyle="--")
    # plt.xlabel("Measurement Time [ns]")
    # plt.ylabel("DC_Signal_data [mV]")
    # plt.title(f"DC_Signal_data_{np.round(readout_levels[2],3)} [mV]")
    # plt.tight_layout()

# plt.show()