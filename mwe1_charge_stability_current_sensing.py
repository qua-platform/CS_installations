"""
        CHARGE STABILITY MAP - fast and slow axes: QDAC2 set to trigger mode
The goal of the script is to acquire the charge stability map.
Here two channels of the QDAC2 are parametrized to step though two preloaded voltage lists on the event of two digital
markers provided by the OPX (connected to ext1 and ext2). This method allows the fast acquisition of a 2D voltage map
and the data can be fetched from the OPX in real time to enable live plotting.
The speed can also be further improved by removing the live plotting and increasing the QDAC2 bandwidth.

The QUA program consists in sending the triggers to the QDAC2 to increment the voltages and measure the charge of the dot
either via dc current sensing or RF reflectometry.
On top of the DC voltage sweeps, the OPX can output a continuous square wave (Coulomb pulse) through the AC line of the
bias-tee. This allows to check the coupling of the fast line to the sample and measure the lever arms between the DC and
AC lines.

A global average is performed (averaging on the most outer loop) and the data is extracted while the program is running
to display the full charge stability map with increasing SNR.

Prerequisites:
    - Readout calibration (resonance frequency for RF reflectometry and sensor operating point for DC current sensing).
    - Setting the parameters of the QDAC2 and preloading the two voltages lists for the slow and fast axes.
    - Connect the two plunger gates (DC line of the bias-tee) to the QDAC2 and two digital markers from the OPX to the
      QDAC2 external trigger ports.
    - (optional) Connect the OPX to the fast line of the plunger gates for playing the Coulomb pulse and calibrate the
      lever arm.

Before proceeding to the next node:
    - Identify the different charge occupation regions.
    - Update the config with the lever-arms.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.addons.variables import assign_variables_to_element
#from qdac2_driver import QDACII, load_voltage_list
import matplotlib.pyplot as plt
from macros import RF_reflectometry_macro, DC_current_sensing_macro
from datetime import datetime

import sys,json,time
import numpy as np
from datetime import datetime
sys.path.append('C:/PySemiQon')
import SemiQon_setups,SemiQon_microdevices
from SemiQon_setups import Probing,Cryostat
from SemiQon_microdevices import Microdevice,Quantum_Dot
from SemiQon_pins import Gate
import copy

# Current if RF_meas is false, reflectometry if RF_meas is true
RF_meas = True
# Channels swept
channels = [2,4]
n_avg = 1  # Number of averages
n_points_slow = 11
n_points_fast = 11  # Number of points for the fast axis

# Voltages in Volt
voltage_values_slow = np.linspace(1.042,1.067,n_points_slow).tolist()
voltage_values_fast = np.linspace(1.038,1.052,n_points_fast).tolist()

# DC integration time
total_integration_time = 0.02 # in seconds

pinout = {
'voltage_source':{
    'finger_gate_t1':'1',
    'finger_gate_t2':'2',
    'finger_gate_t3':'3',
    'finger_gate_t4':'4',
    'finger_gate_t5':'5',
    'finger_gate_b1':'6',
    'finger_gate_b2':'7',
    'finger_gate_b3':'8',
    'finger_gate_b4':'9',
    'finger_gate_b5':'10',
    'res_gate_source':'14',
    'res_gate_drain':'13',
    'source_PD_b':'11',
    "source_PD_t":'12',
},
'current_meter_1':{
    'drain_PD_t':'curr'
},
'current_meter_2':{
    'drain_PD_b':'curr'
},
}

settings = {
'device':Quantum_Dot,
'name':'2x1DQD_SP_Lg60GP120W230Sv60',
'reticle':'ret2_5',
'wafer':'Run3_S13',
'exclude':('matrix_module','current_meter'),
'pinout':pinout,
'direct_pinout':False,
}

setup = Cryostat(**settings)
device = Quantum_Dot(**settings,setup=setup,)
gates = Gate(pins=[__pin__ for __pin__ in device.pins if __pin__.__class__.__name__ == 'Gate'])

setup.voltage_source.set_channel(channel=[str(channels[0]),str(channels[1])],sweep_mode='fix')

res_gates = Gate(pins=[device.res_gate_source,device.res_gate_drain])
terminal_gates_t = Gate(pins=[__pin__ for __pin__ in gates.pins if device.source_PD_t in __pin__.source])
terminal_gates_b = Gate(pins=[__pin__ for __pin__ in gates.pins if device.source_PD_b in __pin__.source])
barrier_gates_b = Gate(pins=[device.finger_gate_b1,device.finger_gate_b3,device.finger_gate_b5])
plunger_gates_b = Gate(pins=[device.finger_gate_b2,device.finger_gate_b4])
barrier_gates_t = Gate(pins=[device.finger_gate_t1,device.finger_gate_t3,device.finger_gate_t5])
plunger_gates_t = Gate(pins=[device.finger_gate_t2,device.finger_gate_t4])

###################
#  Device tuning  #
###################

device.source_PD_t.set_voltage(1e-3)
device.source_PD_b.set_voltage(1e-3)
time.sleep(1)
terminal_gates_t.set_voltage(2.5)
terminal_gates_b.set_voltage(2.5)
time.sleep(1)
barrier_gates_b.set_voltage(-0.1)
barrier_gates_t.set_voltage(-0.1)
time.sleep(0.5)

###################
# The QUA program #
###################
n_readout = int(total_integration_time * 1e9 / readout_len)

if RF_meas:
    with program() as charge_stability_prog:
        n = declare(int)  # QUA integer used as an index for the averaging loop
        counter = declare(int)  # QUA integer used as an index for the Coulomb pulse
        i = declare(int)  # QUA integer used as an index to loop over the voltage points
        j = declare(int)  # QUA integer used as an index to loop over the voltage points
        n_st = declare_stream()  # Stream for the iteration number (progress bar)
        I = declare(fixed)
        Q = declare(fixed)
        ind1 = declare(int)
        value = declare(fixed)

        assign_variables_to_element("tank_circuit", I, Q)

        with for_(n, 0, n < n_avg, n + 1):  # The averaging loop
            with for_(i, 0, i < n_points_slow, i + 1):
                # Trigger the QDAC2 channel to output the next voltage level from the list
                play("trigger", "qdac_trigger2")
                with for_(j, 0, j < n_points_fast, j + 1):
                    # Trigger the QDAC2 channel to output the next voltage level from the list
                    play("trigger", "qdac_trigger1")
                    # Wait for the voltages to settle (depends on the channel bandwidth)
                    wait(300 * u.us, "tank_circuit")
                    # RF reflectometry: the voltage measured by the analog input 2 is recorded, demodulated at the readout
                    # frequency and the integrated quadratures are stored in "I" and "Q"
                    I, Q, I_st, Q_st = RF_reflectometry_macro(I=I, Q=Q)
                    # Wait at each iteration in order to ensure that the data will not be transferred faster than 1 sample
                    # per µs to the stream processing. Otherwise, the processor will receive the samples faster than it can
                    # process them which can cause the OPX to crash.
                    wait(1_000 * u.ns)  # in ns
            # Save the LO iteration to get the progress bar
            save(n, n_st)

        # Stream processing section used to process the data before saving it.
        with stream_processing():
            n_st.save("iteration")
            # Cast the data into a 2D matrix and performs a global averaging of the received 2D matrices together.
            # RF reflectometry
            I_st.buffer(n_points_fast).buffer(n_points_slow).average().save("I")
            Q_st.buffer(n_points_fast).buffer(n_points_slow).average().save("Q")

else:
    with program() as charge_stability_prog:
        n = declare(int)  # QUA integer used as an index for the averaging loop
        counter = declare(int)  # QUA integer used as an index for the Coulomb pulse
        i = declare(int)  # QUA integer used as an index to loop over the voltage points
        j = declare(int)  # QUA integer used as an index to loop over the voltage points
        n_st = declare_stream()  # Stream for the iteration number (progress bar)
        dc_signal = declare(fixed)
        ind1 = declare(int)
        value = declare(fixed)

        assign_variables_to_element("TIA_top", dc_signal)

        with for_(n, 0, n < n_avg, n + 1):  # The averaging loop
            with for_(i, 0, i < n_points_slow, i + 1):
                # Trigger the QDAC2 channel to output the next voltage level from the list
                play("trigger", "qdac_trigger2")
                with for_(j, 0, j < n_points_fast, j + 1):
                    # Trigger the QDAC2 channel to output the next voltage level from the list
                    play("trigger", "qdac_trigger1")
                    with for_(ind1,0,ind1 < n_readout/2, ind1 + 1):
                        # Wait for the voltages to settle (depends on the channel bandwidth)
                        wait(readout_len)
                    with for_(ind1,0,ind1 < n_readout, ind1 + 1):
                        dc_signal, dc_signal_st = DC_current_sensing_macro(element='TIA_top',dc_signal=dc_signal)
                        # Wait at each iteration in order to ensure that the data will not be transferred faster than 1 sample
                        # per µs to the stream processing. Otherwise, the processor will receive the samples faster than it can
                        # process them which can cause the OPX to crash.
                        wait(1_000 * u.ns)  # in ns
            # Save the LO iteration to get the progress bar
            save(n, n_st)

        # Stream processing section used to process the data before saving it.
        with stream_processing():
            n_st.save("iteration")
            # Cast the data into a 2D matrix and performs a global averaging of the received 2D matrices together.
            # DC current sensing
            dc_signal_st.buffer(n_readout).map(FUNCTIONS.average()).buffer(n_points_fast).buffer(n_points_slow).average().save("dc_signal")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

## QDAC2 section
#load the voltage list
setup.voltage_source.load_voltage_list(
    channel=channels[0],
    dwell=2e-6,
    slew_rate=2e7,
    trigger_port="ext1",
    output_range="high",
    output_filter="med",
    voltage_list=voltage_values_fast,
)

setup.voltage_source.load_voltage_list(
    channel=channels[1],
    dwell=2e-6,
    slew_rate=2e7,
    trigger_port="ext2",
    output_range="high",
    output_filter="med",
    voltage_list=voltage_values_slow,
)

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, charge_stability_prog, simulation_config)
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(charge_stability_prog)
    if RF_meas:
        results = fetching_tool(job, data_list=["I", "Q", "iteration"])#, mode="live")
        # Live plotting
        fig = plt.figure()
        interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
        # Fetch the data from the last OPX run corresponding to the current slow axis iteration
        I, Q, iteration = results.fetch_all()
        # Convert results into Volts
        S = u.demod2volts(I + 1j * Q, reflectometry_readout_length)
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        # Plot data
        plt.subplot(121)
        plt.cla()
        plt.title(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.pcolor(voltage_values_fast, voltage_values_slow, R)
        plt.xlabel("Fast voltage axis [V]")
        plt.ylabel("Slow voltage axis [V]")
        plt.subplot(122)
        plt.cla()
        plt.title("Phase [rad]")
        plt.pcolor(voltage_values_fast, voltage_values_slow, phase)
        plt.xlabel("Fast voltage axis [V]")
        plt.ylabel("Slow voltage axis [V]")
        plt.tight_layout()
        plt.pause(0.1)

    else:
        # Get results from QUA program and initialize live plotting
        results = fetching_tool(job, data_list=["dc_signal", "iteration"])#, mode="live")
        job.execution_report()
        # Live plotting
        fig = plt.figure()
        interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
        #while results.is_processing():
        # Fetch the data from the last OPX run corresponding to the current slow axis iteration
        DC_signal, iteration = results.fetch_all()
        # Convert results into Volts
        DC_signal = u.demod2volts(DC_signal, readout_len)
        print(DC_signal)
        # Progress bar
        #progress_counter(iteration, n_points_slow, start_time=results.start_time)
        # Plot data
        plt.cla()
        plt.title("Current")
        plt.pcolor(voltage_values_fast, voltage_values_slow, -DC_signal)
        plt.xlabel("Fast voltage axis [V]")
        plt.ylabel("Slow voltage axis [V]")
        plt.xlim(voltage_values_fast[0],voltage_values_fast[-1])
        plt.ylim(voltage_values_slow[0],voltage_values_slow[-1])
        plt.tight_layout()
        plt.pause(0.1)

try:
    amplitude = (-DC_signal).tolist()

    result_dict = {
        'finger_gate_t2-voltage_volt':list(voltage_values_fast),
        'finger_gate_t4-voltage_volt':list(voltage_values_slow),
        'drain_PD_t-current_ampere':amplitude,
    }
    setup.voltage_source.set_channel(channel=['2','4'],sweep_mode='fix')
    gates.set_voltage(0)
    device.source_PD_t.set_voltage(0)
    device.source_PD_b.set_voltage(0)
    setup.close_instruments()

    directory = 'C:/OPX_Evaluation/Results/'
    session_name = datetime.now().strftime('%m_%d_%Y-%H_%M_%S')+'_'+device.wafer+'_'+device.reticle+'_'+device.name
    plt.savefig(directory+session_name+'.pdf')
    with open(directory+session_name+'.json', 'w') as file: json.dump(result_dict,file,indent=2) 
    plt.show()
except:
    plt.show()



