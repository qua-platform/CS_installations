"""
        RAW ADC TRACES
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
import matplotlib.pyplot as plt
import numpy as np
from qualang_tools.units import unit


######################
# Network parameters #
######################
qop_ip = "172.16.33.107"  # Write the QM router IP address
cluster_name = "Beta_8"  # Write your cluster_name if version >= QOP220
qop_port = 9510  # Write the QOP port if version < QOP220

#####################
# OPX configuration #
#####################
con = "con1"
mw_fem = 1

#############################################
#                  Qubits                   #
#############################################
u = unit(coerce_to_integer=True)

sampling_rate = int(1e9)  # or, int(2e9)

#############################################
#                Resonators                 #
#############################################
resonator_LO = 5.5 * u.GHz
resonator_IF = 60 * u.MHz
resonator_power = 1  # power in dBm at waveform amp = 1

# Note: amplitudes can be -1..1 and are scaled up to `resonator_power` at amp=1
readout_len = 5000
readout_amp = 0.6

time_of_flight = 24
depletion_time = 2 * u.us

#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1000",
            "fems": {
                mw_fem: {
                    "type": "MW",
                    "analog_outputs": {
                        1: {
                            "full_scale_power_dbm": resonator_power,
                            "band": 2,
                            "upconverter_frequency": resonator_LO,
                        },  # resonator
                    },
                    "digital_outputs": {},
                    "analog_inputs": {
                        1: {"band": 2, "downconverter_frequency": resonator_LO},  # I from down-conversion
                    },
                },
            },
        },
    },
    "elements": {
        "resonator": {
            "MWInput": {
                "port": (con, mw_fem, 1),
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "readout": "readout_pulse",
            },
            "MWOutput": {
                "port": (con, mw_fem, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
    },
    "pulses": {
        "readout_pulse": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf",
                "Q": "zero_wf",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "zero_wf": {"type": "constant", "sample": 0.0},
        "readout_wf": {"type": "constant", "sample": readout_amp},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
}

###################
# The QUA program #
###################
n_avg = 100  # The number of averages

with program() as raw_trace_prog:
    n = declare(int)  # QUA variable for the averaging loop
    adc_st = declare_stream(adc_trace=True)  # The stream to store the raw ADC trace

    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        # Make sure that the readout pulse is sent with the same phase so that the acquired signal does not average out
        reset_phase("resonator")
        # Measure the resonator (send a readout pulse and record the raw ADC trace)
        measure("readout", "resonator", adc_st)
        # Wait for the resonator to deplete
        wait(depletion_time * u.ns, "resonator")

    with stream_processing():
        # Will save average:
        adc_st.input1().average().save("adc")
        # Will save only last run:
        adc_st.input1().save("adc_single_run")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, raw_trace_prog, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(raw_trace_prog)
    # Creates a result handle to fetch data from the OPX
    res_handles = job.result_handles
    # Waits (blocks the Python console) until all results have been acquired
    res_handles.wait_for_all_values()
    # Fetch the raw ADC traces and convert them into Volts
    adc = u.raw2volts(res_handles.get("adc").fetch_all())
    adc_single_run = u.raw2volts(res_handles.get("adc_single_run").fetch_all())
    # Plot data
    plt.figure()
    plt.subplot(121)
    plt.title("Single run, FEM 1, CH 1")
    plt.plot(adc_single_run.real, label="I")
    plt.plot(adc_single_run.imag, label="Q")
    plt.xlabel("Time [ns]")
    plt.ylabel("Signal amplitude [V]")
    plt.legend()

    plt.subplot(122)
    plt.title("Averaged run, FEM 1, CH 1")
    plt.plot(adc.real, label="I")
    plt.plot(adc.imag, label="Q")
    plt.xlabel("Time [ns]")
    plt.legend()
    plt.tight_layout()
plt.show()