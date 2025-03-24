# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 11:32:57 2025

@author: BradCole
"""

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

n_avg = 1000

readout_levels = np.linspace(-0.010, 0.010, 10)
delays = np.arange(16, duration_init+duration_manip+duration_readout, 100)


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
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    #I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    #Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    dc_signal = declare(fixed)  # QUA variable for the measured dc signal
    dc_signal_st = declare_stream()
    switch = declare(int)
    # Ensure that the result variables are assigned to the measurement elements
    #assign_variables_to_element("tank_circuit", I, Q)
    assign_variables_to_element("TIA", dc_signal)
    # seq.add_step(voltage_point_name="readout", duration=16)
    with for_(n, 0, n < n_avg, n + 1):  # The averaging loop
        save(n, n_st)
        
        with for_each_(r, readout_levels.tolist()):
            
            with for_ (*from_array(t, delays)):

                with if_(t<duration_manip):
                    assign(switch, 0)
                with elif_(t>duration_manip):
                    with if_(t<(duration_manip+duration_readout)):
                        assign(switch, 1)
                    with else_():
                        assign(switch, 2)

                with switch_(switch):
                    with case_(0):
                        with strict_timing_():  # Ensure that the sequence will be played without gap
                            # Navigate through the charge stability map
                            seq.add_step(level = level_manip, duration= duration_manip+t)
                            seq.add_step(level = [r], duration = duration_readout)
                            seq.add_step(level = level_init, duration = duration_init)
                            seq.add_compensation_pulse(duration=duration_compensation_pulse)
                
                            # Drive the singlet-triplet qubit using an exchange pulse at the end of the manipulation step
                            #wait(duration_init * u.ns, "qubit")  # Need -4 cycles to compensate the gap
                            #play("pi", "qubit")
                
                            # Measure the dot right after the qubit manipulation
                            #wait((duration_manip), "TIA")
                            #I, Q, I_st, Q_st = RF_reflectometry_macro(I=I, Q=Q)
                            wait(t>>2, "TIA")
                            measure("readout", "TIA", None, integration.full("constant", dc_signal, "out1"))
                            # measure("readout", "TIA", None, integration.sliced("constant", dc_signal, "out1"))
                            save(dc_signal, dc_signal_st)
                            
                            
                            # Ramp the background voltage to zero to avoid propagating floating point errors
                        seq.ramp_to_zero()
                        wait(500*u.ns)

                    with case_(1):
                        with strict_timing_():  # Ensure that the sequence will be played without gap
                            # Navigate through the charge stability map
                            seq.add_step(level = level_manip, duration= duration_manip)
                            seq.add_step(level = [r], duration = duration_readout+t-duration_manip)
                            seq.add_step(level = level_init, duration = duration_init)
                            seq.add_compensation_pulse(duration=duration_compensation_pulse)
                
                            # Drive the singlet-triplet qubit using an exchange pulse at the end of the manipulation step
                            #wait(duration_init * u.ns, "qubit")  # Need -4 cycles to compensate the gap
                            #play("pi", "qubit")
                
                            # Measure the dot right after the qubit manipulation
                            #wait((duration_manip), "TIA")
                            #I, Q, I_st, Q_st = RF_reflectometry_macro(I=I, Q=Q)
                            wait(t>>2, "TIA")
                            measure("readout", "TIA", None, integration.full("constant", dc_signal, "out1"))
                            # measure("readout", "TIA", None, integration.sliced("constant", dc_signal, "out1"))
                            save(dc_signal, dc_signal_st)
                            
                            
                            # Ramp the background voltage to zero to avoid propagating floating point errors
                        seq.ramp_to_zero()
                        wait(500*u.ns)
                    with case_(2):
                        with strict_timing_():  # Ensure that the sequence will be played without gap
                            # Navigate through the charge stability map
                            seq.add_step(level = level_manip, duration= duration_manip)
                            seq.add_step(level = [r], duration = duration_readout)
                            seq.add_step(level = level_init, duration = duration_init+t-duration_manip-duration_readout)
                            seq.add_compensation_pulse(duration=duration_compensation_pulse)
                
                            # Drive the singlet-triplet qubit using an exchange pulse at the end of the manipulation step
                            #wait(duration_init * u.ns, "qubit")  # Need -4 cycles to compensate the gap
                            #play("pi", "qubit")
                
                            # Measure the dot right after the qubit manipulation
                            #wait((duration_manip), "TIA")
                            #I, Q, I_st, Q_st = RF_reflectometry_macro(I=I, Q=Q)
                            wait(t>>2, "TIA")
                            measure("readout", "TIA", None, integration.full("constant", dc_signal, "out1"))
                            # measure("readout", "TIA", None, integration.sliced("constant", dc_signal, "out1"))
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
        
        dc_signal_st.buffer(len(delays)).buffer(len(readout_levels)).average().save("dc_signal")

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
    # plt.axhline(level_init[0], color="k", linestyle="--")
    # plt.axhline(level_manip[0], color="k", linestyle="--")
    # plt.axhline(level_readout[0], color="k", linestyle="--")
    # plt.axhline(level_init[1], color="k", linestyle="--")
    # plt.axhline(level_manip[1], color="k", linestyle="--")
    # plt.axhline(level_readout[1], color="k", linestyle="--")
    # plt.yticks(
    #     [
    #         level_readout[1],
    #         level_manip[1],
    #         level_init[1],
    #         0.0,
    #         level_init[0],
    #         level_manip[0],
    #         level_readout[0],
    #     ],
    #     ["readout", "manip", "init", "0", "init", "manip", "readout"],
    #)
    plt.legend("")
    from macros import get_filtered_voltage

    plt.subplot(212)
    get_filtered_voltage(job.get_simulated_samples().con1.analog["1"], 1e-9, bias_tee_cut_off_frequency, True)

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)

    #To do: Set all relevant voltages with Nanonis here

    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(RLC_prog)
    # Get results from QUA program and initialize live plotting
    results = fetching_tool(job, data_list=["dc_signal", "iteration"], mode = "live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch the data from the last OPX run corresponding to the current slow axis iteration
        DC_signal, iteration, = results.fetch_all()
        #print(adc_single_run)
        #print(adc_single_run.shape)
        # Convert results into Volts
        # S = u.demod2volts(I + 1j * Q, reflectometry_readout_length)
        # R = np.abs(S)  # Amplitude
        # phase = np.angle(S)  # Phase
        DC_signal = u.demod2volts(DC_signal, readout_len)
        # adc_data = u.raw2volts(adc_stream_data)
        # Progress bar
        progress_counter(iteration, n_avg)
        # Plot data
        plt.cla()
        plt.pcolor(delays, readout_levels, DC_signal, label = "DC Signal")
        plt.axvline(duration_manip, color="k", linestyle="--")
        plt.axvline(duration_manip+duration_readout, color="k", linestyle="--")
        plt.xlabel("Measurement Time [ns]")
        plt.ylabel("DC_Signal [mV]")
        plt.tight_layout()

        plt.pause(0.1)

plt.show()