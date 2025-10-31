#%%
from pathlib import Path
import numpy as np
import plotly.io as pio
from qualang_tools.units import unit
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from tools import visualize_opx1000_config, get_band
import os
from datetime import datetime

pio.renderers.default = "browser"
u = unit(coerce_to_integer=True)

out1_band = out1_power = out1_up1_LO = out2_band = out2_power = out2_up1_LO \
= out3_band = out3_power = out3_up1_LO = out4_band = out4_power = out4_up1_LO \
= out5_band = out5_power = out5_up1_LO = out6_band = out6_power = out6_up1_LO \
= out7_band = out7_power = out7_up1_LO = out8_band = out8_power = out8_up1_LO \
= in1_band = in1_LO = in2_band = in2_LO = in1_gain_db = in2_gain_db = 1

######################
# Network parameters #
###################### 	
qop_ip = "192.168.88.253"  # Write the QM router IP address
cluster_name = "Cluster_1"  # Write your cluster_name if version >= QOP220
# qop_ip = "IP adress"  # Write the QM router IP address
# cluster_name = "cluster name"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220
con = "con1"

# #####################################
# #  Open Communication with the QOP  #
# #####################################
qmm = QuantumMachinesManager(host=qop_ip, 
                             port=qop_port, 
                             cluster_name=cluster_name)
# qmm.close_all_qms()
#%%

"""
QUA-Config supporting OPX1000 w/ LF-FEM
"""
from pathlib import Path
import numpy as np
import plotly.io as pio
from qualang_tools.units import unit
from qualang_tools.voltage_gates import VoltageGateSequence

pio.renderers.default = "browser"

#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)

#####################
# OPX configuration #
#####################
con = "con1"
fem = 1  # Should be the LF-FEM index, e.g., 1
# Set octave_config to None if no octave are present
octave_config = None

#############################################
#              OPX PARAMETERS               #
#############################################
sampling_rate = int(1e9)  # or, int(2e9)

######################
#       READOUT      #
######################
u = unit(coerce_to_integer=True)

# DC readout parameters
readout_len = 1 * u.us
readout_amp = 0.0
IV_scale_factor = 0.5e-9  # in A/V

# Reflectometry
resonator_IF = 151 * u.MHz
reflectometry_readout_length = 1 * u.us
reflectometry_readout_amp = 30 * u.mV

# Time of flight
time_of_flight = 28

######################
#      DC GATES      #
######################

## Section defining the points from the charge stability map - can be done in the config
# Relevant points in the charge stability map as ["P1", "P2"] in V
level_init = [0.1, -0.1]
level_manip = [0.2, -0.2]
level_readout = [0.12, -0.12]

# Duration of each step in ns
duration_init = 2500
duration_manip = 1000
duration_readout = readout_len + 100
duration_compensation_pulse = 4 * u.us

# Step parameters
coulomb_step_length = 60  # in ns
step_length = 16  # in ns
P1_step_amp = 0.25  # in V
P2_step_amp = 0.25  # in V
charge_sensor_amp = 0.25  # in V

# Time to ramp down to zero for sticky elements in ns
hold_offset_duration = 4

bias_tee_cut_off_frequency = 10 * u.kHz

######################
#    QUBIT PULSES    #
######################
# Durations in ns
pi_length = 10000
pi_half_length = 16
# Amplitudes in V
pi_amps = [0.27, -0.27]
pi_half_amps = [0.27, -0.27]


#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1000",
            "fems": {
                fem: {
                    "type": "LF",
                    "analog_outputs": {
                        # P1
                        1: {
                            # DC Offset applied to the analog output at the beginning of a program.
                            "offset": 0.0,
                            # The "output_mode" can be used to tailor the max voltage and frequency bandwidth, i.e.,
                            #   "direct":    1Vpp (-0.5V to 0.5V), 750MHz bandwidth (default)
                            #   "amplified": 5Vpp (-2.5V to 2.5V), 330MHz bandwidth
                            # Note, 'offset' takes absolute values, e.g., if in amplified mode and want to output 2.0 V, then set "offset": 2.0
                            "output_mode": "direct",
                            # The "sampling_rate" can be adjusted by using more FEM cores, i.e.,
                            #   1 GS/s: uses one core per output (default)
                            #   2 GS/s: uses two cores per output
                            # NOTE: duration parameterization of arb. waveforms, sticky elements and chirping
                            #       aren't yet supported in 2 GS/s.
                            "sampling_rate": sampling_rate,
                            # At 1 GS/s, use the "upsampling_mode" to optimize output for
                            #   modulated pulses (optimized for modulated pulses):      "mw"    (default)
                            #   unmodulated pulses (optimized for clean step response): "pulse"
                            "upsampling_mode": "mw",
                        },
                        # P2
                        3: {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                    },
                    "digital_outputs": {
                        1: {},  # TTL for QDAC
                        2: {},  # TTL for QDAC
                    },
                    "analog_inputs": {
                        1: {"offset": 0.0, "gain_db": 0, "sampling_rate": sampling_rate},  # RF reflectometry input
                        2: {"offset": 0.0, "gain_db": 0, "sampling_rate": sampling_rate},  # DC readout input
                    },
                }
            },
        }
    },
    "elements": {
        "LF_demo_dc_1": {
            "singleInput": {
                "port": (con, fem, 1),
            },
            "operations": {
                "cw": "cw_pulse",
            },
        },
        "LF_demo_sine_1": {
            "singleInput": {
                "port": (con, fem, 1),
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "cw": "cw_pulse",
                "readout": "reflectometry_readout_pulse",
            },
            "outputs": {
                "out1": (con, fem, 1),
                "out2": (con, fem, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "LF_demo_sine_2": {
            "singleInput": {
                "port": (con, fem, 3),
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "cw": "cw_pulse",
                "readout": "reflectometry_readout_pulse",
            },
            "outputs": {
                "out1": (con, fem, 1),
                "out2": (con, fem, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "sticky_line_1": {
            "singleInput": {
                "port": (con, fem, 1),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "qdac_trigger1": {
            "digitalInputs": {
                "trigger": {
                    "port": (con, fem, 1),
                    "delay": 0,
                    "buffer": 0,
                }
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
    },
    "pulses": {
        "cw_pulse": {
            "operation": "measurement",
            "length": 10000,
            "waveforms": {
                "single": "reflect_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            # "digital_marker": "ON",
        },
        "P1_step_pulse": {
            "operation": "control",
            "length": step_length,
            "waveforms": {
                "single": "P1_step_wf",
            },
        },
        "trigger_pulse": {
            "operation": "control",
            "length": 1000,
            "digital_marker": "ON",
        },
        "reflectometry_readout_pulse": {
            "operation": "measurement",
            "length": reflectometry_readout_length,
            "waveforms": {
                "single": "reflect_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "digital_marker": "ON",
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "single": "readout_pulse_wf",
            },
            "integration_weights": {
                "constant": "constant_weights",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "cw_pulse_wf": {"type": "constant", "sample": 1.0},
        "readout_pulse_wf": {"type": "constant", "sample": readout_amp},
        "reflect_wf": {"type": "constant", "sample": reflectometry_readout_amp},
        "P1_step_wf": {"type": "constant", "sample": P1_step_amp}
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "constant_weights": {
            "cosine": [(1, readout_len)],
            "sine": [(0.0, readout_len)],
        },
        "cosine_weights": {
            "cosine": [(1.0, reflectometry_readout_length)],
            "sine": [(0.0, reflectometry_readout_length)],
        },
        "sine_weights": {
            "cosine": [(0.0, reflectometry_readout_length)],
            "sine": [(1.0, reflectometry_readout_length)],
        },
    },
}

#%%
with program() as cw_prog: 
    n = declare(int) 
    with for_(n, 0, n < 10_000_000, n + 1): 
        play("cw", "LF_demo_sine_1") 
        play("cw"*amp(0.25), "LF_demo_sine_2") 
# %%
#######################
# Simulate or execute #
#######################
simulate = False
if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=2000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, cw_prog, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()

    # Visualize and save the waveform report
    timestamp = datetime.now().strftime('%y%m%d_%H%M')
    script_name = 'continueous_wave'
    save_dir = os.path.join("./Data", script_name, timestamp)
    os.makedirs(save_dir, exist_ok=True)
    filename_cfg = f"{timestamp}_cfg_ToF.png"
    filename_sim = f"{timestamp}_sim_ToF.png"

    print(f"Figure saved to: {save_dir}") 
    visualize_opx1000_config(config, save_path=os.path.join(save_dir, filename_cfg)) 
    waveform_report.create_plot(samples, plot=True, save_path=os.path.join(save_dir, filename_sim)) 

else: 
    # Open a quantum machine to execute the QUA program 
    qm = qmm.open_qm(config) 
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python! 
    job = qm.execute(cw_prog) 



