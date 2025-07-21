# %%
"""
octave_introduction.py: shows the basic commands to control the octave's clock, synthesizers, up-converters, triggers,
down-converters and calibration
"""

from qm import QuantumMachinesManager
from qm.octave import *
from qm.octave.octave_manager import ClockMode
from qm.qua import *
import os
import time
import matplotlib.pyplot as plt
from qualang_tools.units import unit
from qm import SimulationConfig

from configuration_octave import *

###################################
# Open Communication with the QOP #
###################################
qmm = QuantumMachinesManager(
    host=qop_ip, cluster_name=cluster_name, octave_calibration_db_path=os.getcwd()
)
qm = qmm.open_qm(config)

simulate = False


# wrapper
def run(qua_prog, sleep_time=None):
    if simulate:
        simulation_config = SimulationConfig(duration=400)  # in clock cycles
        job_sim = qmm.simulate(config, qua_prog, simulation_config)
        job_sim.get_simulated_samples().con1.plot()
    else:
        job = qm.execute(qua_prog)
        if sleep_time:
            time.sleep(sleep_time)
            job.halt()


###################
# The QUA program #
###################
elements = list(config["elements"].keys())
with program() as hello_octave:
    with infinite_loop_():
        for el in elements:
            play("cw", el)

# %%
###########################
# Step 1 : clock settings #
###########################
external_clock = False
if external_clock:
    # Change to the relevant external frequency
    qm.octave.set_clock(octave, clock_mode=ClockMode.External_10MHz)
else:
    qm.octave.set_clock(octave, clock_mode=ClockMode.Internal)
    # You can connect clock out from rear panel to a spectrum analyzer  to see the 1GHz signal

# %%
#######################################
# Step 2 : checking the up-converters #
#######################################
print("-" * 37 + " Checking up-converters")
run(hello_octave, sleep_time=60)
# You can connect RF1, RF2, RF3, RF4, RF5 to a spectrum analyzer and check the 3 peaks before calibration:
# 1. LO-IF, 2. LO, 3. LO+IF

# %%
##################################
# Step 3 : checking the triggers #
##################################
print("-" * 37 + " Checking triggers")
# Connect RF1, RF2, RF3, RF4, RF5 to a spectrum analyzer and check that you get a signal for 4sec then don't get a signal fo 4 sec and so on.
for el in elements:
    # set the behaviour of the RF switch to be on only when triggered
    qm.octave.set_rf_output_mode(el, RFOutputMode.trig_normal)

with program() as hello_octave_trigger:
    with infinite_loop_():
        for el in elements:
            play("cw", el, duration=1e9)
            play("cw_w_trig", el, duration=1e9)
run(hello_octave_trigger, sleep_time=60)

# %%
#########################################
# Step 4 : checking the down-converters #
#########################################
print("-" * 37 + " Checking down-converters")
# Connect RF1 -> RF1In, RF2 -> RF2In
# Connect IFOUT1 -> AI1 , IFOUT2 -> AI2
check_down_converter_1 = True
check_down_converter_2 = False
u = unit()
if check_down_converter_1:
    # Reduce the Octave gain to avoid saturating the OPX ADC or add a 20dB attenuator
    qm.octave.set_rf_output_gain(elements[0], -10)
    with program() as hello_octave_readout_1:
        raw_ADC_1 = declare_stream(adc_trace=True)
        measure("readout", elements[0], raw_ADC_1)
        with stream_processing():
            raw_ADC_1.input1().save("adc_1")
            raw_ADC_1.input2().save("adc_2")
    # Execute the program
    job = qm.execute(hello_octave_readout_1)
    res = job.result_handles
    res.wait_for_all_values()
    # Plot the results
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle("Inputs from down conversion 1")
    adc_1 = u.raw2volts(res.get("adc_1").fetch_all())
    ax1.plot(adc_1, label="Input 1")
    ax1.set_title("amp VS time Input 1")
    ax1.set_xlabel("Time [ns]")
    ax1.set_ylabel("Signal amplitude [V]")

    adc_2 = u.raw2volts(res.get("adc_2").fetch_all())
    ax2.plot(adc_2, label="Input 2")
    ax2.set_title("amp VS time Input 2")
    ax2.set_xlabel("Time [ns]")
    ax2.set_ylabel("Signal amplitude [V]")
    plt.tight_layout()

if check_down_converter_2:
    # Reduce the Octave gain to avoid saturating the OPX ADC or add a 20dB attenuator
    qm.octave.set_rf_output_gain(elements[1], -10)

    with program() as hello_octave_readout_2:
        raw_ADC_2 = declare_stream(adc_trace=True)
        measure("readout", elements[1], raw_ADC_2)
        with stream_processing():
            raw_ADC_2.input1().save("adc_1")
            raw_ADC_2.input2().save("adc_2")
    # Execute the program
    job = qm.execute(hello_octave_readout_2)
    res = job.result_handles
    res.wait_for_all_values()
    # Plot the results
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle("Inputs from down conversion 2")
    adc_1 = u.raw2volts(res.get("adc_1").fetch_all())
    ax1.plot(adc_1, label="Input 1")
    ax1.set_title("amp VS time Input 1")
    ax1.set_xlabel("Time [ns]")
    ax1.set_ylabel("Signal amplitude [V]")

    adc_2 = u.raw2volts(res.get("adc_2").fetch_all())
    ax2.plot(adc_2, label="Input 2")
    ax2.set_title("amp VS time Input 2")
    ax2.set_xlabel("Time [ns]")
    ax2.set_ylabel("Signal amplitude [V]")
    plt.tight_layout()

# %%
#################################
# Step 5 : checking calibration #
#################################
print("-" * 37 + " Play before calibration")
# Step 5.1: Connect RF1 and run these lines in order to see the uncalibrated signal first
job = qm.execute(hello_octave)
time.sleep(10)  # The program will run for 10 seconds
job.halt()
# Step 5.2: Run this in order to calibrate
for element in [elements[1]]:  # Only calibrate the qubit
    print("-" * 37 + f" Calibrates {element}")
    qm.calibrate_element(element, {qubit_LO: (qubit_IF,)})
    # can provide many IFs for specific LO
    # If no frequencies are given calibration will occur according to LO & IF declared in the element
# Step 5.3: Run these and look at the spectrum analyzer and check if you get 1 peak at LO+IF (i.e. 6.05GHz)
print("-" * 37 + " Play after calibration")
job = qm.execute(hello_octave)
time.sleep(30)  # The program will run for 30 seconds
job.halt()

# %%
