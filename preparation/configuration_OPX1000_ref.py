# %%
import os
from pathlib import Path
import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from qualang_tools.units import unit
import copy

#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)

######################
# Network parameters #
######################
qop_ip = "192.168.88.252"  # Write the QM router IP address
cluster_name = 'Cluster_2'  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

# Path to save data
save_dir = Path().absolute() / "QM" / "INSTALLATION" / "data"

#####################
# OPX configuration #
#####################
# CW pulse parameter
const_len = 1000
const_amp = 125 * u.mV

# PORT DELAYS
ports = [1,2,3,4,5,6,7,8]
delays = [[7, 7, 7, 7, 7, 7, 7, 7], [4, 4, 4, 4, 4, 4, 4, 4], [0, 0, 0, 0, 0, 0, 0, 0]]

# MARK: QUBITS
#############################################
#                  Qubits                   #
#############################################
qubit_rotation_keys = ["x180", "x180_flux_spec", "x90", "minus_x90", "y180", "y90", "minus_y90"]

# Constants for Pi Pulse
PI_LENGTH = 48
PI_SIGMA = PI_LENGTH / 5
PI_LENGTH_FLUX_SPEC = 48
PI_SIGMA_FLUX_SPEC = PI_LENGTH_FLUX_SPEC / 5

# Constants for each qubit (replace example values with actual values)
QUBIT_CONSTANTS = {
    "q1_xy": {
        "amplitude": 0.208432, 
        "pi_len": PI_LENGTH,
        "pi_sigma": PI_SIGMA,
        "pi_len_flux_spec": PI_LENGTH_FLUX_SPEC,
        "pi_sigma_flux_spec": PI_SIGMA_FLUX_SPEC,
        "anharmonicity": -200 * u.MHz,
        "drag_coefficient": 0.5,
        "ac_stark_shift": 0.0 * u.MHz,
        "LO": 4.146 * u.GHz,  # Example LO frequency
        "IF": 0 * u.MHz,    # Example IF frequency
        "con": "con1",
        "fem": 2,
        "ao": 4,
        "band": 1,
        "full_scale_power_dbm": -20,
        "delay": delays[1][3],
        # NOTE: twin q3_xy
        "fem_twin": 1,
        "ao_twin": 4
    },
    "q2_xy": {
        "amplitude": 0.194518,
        "pi_len": PI_LENGTH,
        "pi_sigma": PI_SIGMA, 
        "pi_len_flux_spec": PI_LENGTH_FLUX_SPEC,
        "pi_sigma_flux_spec": PI_SIGMA_FLUX_SPEC,
        "anharmonicity": -180 * u.MHz,
        "drag_coefficient": 0.5,
        "ac_stark_shift": 0.0 * u.MHz,
        "LO": 4.222 * u.GHz,  
        "IF": 0 * u.MHz,
        "con": "con1",
        "fem": 2,
        "ao": 5,
        "band": 1,
        "full_scale_power_dbm": -20,
        "delay": delays[1][4],
        # NOTE: twin q4_xy
        "fem_twin": 1,
        "ao_twin": 5
    },
    "q3_xy": {
        "amplitude": 0.192296,
        "pi_len": PI_LENGTH,
        "pi_sigma": PI_SIGMA, 
        "pi_len_flux_spec": PI_LENGTH_FLUX_SPEC,
        "pi_sigma_flux_spec": PI_SIGMA_FLUX_SPEC,
        "anharmonicity": -190 * u.MHz,
        "drag_coefficient": 0.5,
        "ac_stark_shift": 0.0 * u.MHz,
        "LO": 4.44 * u.GHz,  
        "IF": 0 * u.MHz,
        "con": "con1",
        "fem": 1,
        "ao": 4,
        "band": 1,
        "full_scale_power_dbm": -20,
        "delay": delays[0][3],
        # NOTE: twin q1_xy
        "fem_twin": 2,
        "ao_twin": 4
    },
    "q4_xy": {
        "amplitude": 0.175370,
        "pi_len": PI_LENGTH,
        "pi_sigma": PI_SIGMA, 
        "pi_len_flux_spec": PI_LENGTH_FLUX_SPEC,
        "pi_sigma_flux_spec": PI_SIGMA_FLUX_SPEC,
        "anharmonicity": -185 * u.MHz,
        "drag_coefficient": 0.5,
        "ac_stark_shift": 0.0 * u.MHz,
        "LO": 4.247 * u.GHz,  
        "IF": 0 * u.MHz,
        "con": "con1",
        "fem": 1,
        "ao": 5,
        "band": 1,
        "full_scale_power_dbm": -20,
        "delay": delays[0][4],
        # NOTE: twin q2_xy
        "fem_twin": 2,
        "ao_twin": 5    
    },
    "q5_xy": {
        "amplitude": 0.21329,
        "pi_len": PI_LENGTH,
        "pi_sigma": PI_SIGMA, 
        "pi_len_flux_spec": PI_LENGTH_FLUX_SPEC,
        "pi_sigma_flux_spec": PI_SIGMA_FLUX_SPEC,
        "anharmonicity": -195 * u.MHz,
        "drag_coefficient": 0.5,
        "ac_stark_shift": 0.0 * u.MHz,
        "LO": 6.022 * u.GHz,
        "IF": 0 * u.MHz,
        "con": "con1",
        "fem": 1,
        "ao": 6,
        "band": 2,
        "full_scale_power_dbm": -8,
        "delay": delays[0][5],
        # NOTE: twin q7_xy
        "fem_twin": 2,
        "ao_twin": 6
    },
    "q6_xy": {
        "amplitude": 0.20604,
        "pi_len": PI_LENGTH,
        "pi_sigma": PI_SIGMA, 
        "pi_len_flux_spec": PI_LENGTH_FLUX_SPEC,
        "pi_sigma_flux_spec": PI_SIGMA_FLUX_SPEC,
        "anharmonicity": -175 * u.MHz,
        "drag_coefficient": 0.5,
        "ac_stark_shift": 0.0 * u.MHz,
        "LO": 5.916 * u.GHz,  
        "IF": 0 * u.MHz,
        "con": "con1",
        "fem": 1,
        "ao": 7,
        "band": 2,
        "full_scale_power_dbm": -8,
        "delay": delays[0][6],
        # NOTE: twin empty analog output
        "fem_twin": 2,
        "ao_twin": 7
    },
    "q7_xy": {
        "amplitude": 0.1655625,
        "pi_len": PI_LENGTH,
        "pi_sigma": PI_SIGMA, 
        "pi_len_flux_spec": PI_LENGTH_FLUX_SPEC,
        "pi_sigma_flux_spec": PI_SIGMA_FLUX_SPEC,
        "anharmonicity": -170 * u.MHz,
        "drag_coefficient": 0.5,
        "ac_stark_shift": 0.0 * u.MHz,
        "LO": 5.932 * u.GHz,  
        "IF": 0 * u.MHz,
        "con": "con1",
        "fem": 2,
        "ao": 6,
        "band": 2,
        "full_scale_power_dbm": -8,
        "delay": delays[1][5],
        # NOTE: twin q5_xy
        "fem_twin": 1,
        "ao_twin": 6
    }
}

for qubit_key in QUBIT_CONSTANTS.keys():
    assert QUBIT_CONSTANTS[qubit_key]['amplitude'] <= 0.499, f"{qubit_key} amplitude needs to be less than 0.499"

# MARK: TWIN INFO

TWIN_QUBIT = "q7_xy"
TWIN_RESONATOR = TWIN_QUBIT[0:3] + "rr"
TWIN_DEACTIVATED = False

if TWIN_DEACTIVATED == False:
    print("TWIN is deactivated, meaning is not in the config")
else:
    print("TWIN is activated, meaning is in the config")

# Relaxation time
qb_reset_time = 50_000

# Saturation_pulse
saturation_len = 30 * u.us
saturation_amp = 0.45

def generate_waveforms(rotation_keys):
    """ Generate all necessary waveforms for a set of rotation types across all qubits. """
    
    if not isinstance(rotation_keys, list):
        raise ValueError("rotation_keys must be a list")

    waveforms = {}

    for qubit_key, constants in QUBIT_CONSTANTS.items():
        amp = constants["amplitude"]
        pi_len = constants["pi_len"]
        pi_sigma = constants["pi_sigma"]
        pi_len_flux_spec = constants["pi_len_flux_spec"]
        pi_sigma_flux_spec = constants["pi_sigma_flux_spec"]
        drag_coef = constants["drag_coefficient"]
        ac_stark_shift = constants["ac_stark_shift"]
        anharmonicity = constants["anharmonicity"]

        for rotation_key in rotation_keys:
            if rotation_key in ["x180", "x180_flux_spec", "y180"]:
                wf_amp = amp
            elif rotation_key in ["x90", "y90"]:
                wf_amp = amp / 2
            elif rotation_key in ["minus_x90", "minus_y90"]:
                wf_amp = -amp / 2
            else:
                continue

            wf, der_wf = np.array(drag_gaussian_pulse_waveforms(wf_amp, pi_len, pi_sigma, drag_coef, anharmonicity, ac_stark_shift))

            if rotation_key == "x180_flux_spec":
                wf, der_wf = np.array(drag_gaussian_pulse_waveforms(wf_amp, pi_len_flux_spec, pi_sigma_flux_spec, drag_coef, anharmonicity, ac_stark_shift))
                I_wf = wf
                Q_wf = der_wf
            elif rotation_key.startswith("x") or rotation_key == "minus_x90":
                I_wf = wf
                Q_wf = der_wf
            else:  # y rotations
                I_wf = (-1) * der_wf
                Q_wf = wf

            waveforms[f"{qubit_key}_{rotation_key}_I"] = I_wf
            waveforms[f"{qubit_key}_{rotation_key}_Q"] = Q_wf

    return waveforms
waveforms = generate_waveforms(qubit_rotation_keys)

# MARK: FLUXES
##########################################
#               Flux line                #
##########################################
FLUX_CONSTANTS = {
    "q1_z": {
        "idle_point": 0.4, # 1.6e-3 * 50 * 1/2 * 10
        "con": "con1",
        "fem": 3,
        "ao": 1,
        "iir": [],
        "fir": [],
        "delay": delays[2][0],
        "unipolar_flux_len": 200,
        "unipolar_flux_amp": 0.11,
        "output_mode": "amplified"
    },
    "q2_z": {
        "idle_point": 0.425,
        "con": "con1",
        "fem": 3,
        "ao": 2,
        "iir": [],
        "fir": [],
        "delay": delays[2][1],
        "unipolar_flux_len": 200,
        "unipolar_flux_amp": 0.12,
        "output_mode": "amplified"
    },
    "q3_z": {
        "idle_point": 0.425,
        "con": "con1",
        "fem": 3,
        "ao": 3,
        "iir": [],
        "fir": [],
        "delay": delays[2][2],
        "unipolar_flux_len": 200,
        "unipolar_flux_amp": 0.13,
        "output_mode": "amplified"
    },
    "q4_z": {
        "idle_point": 0.4,
        "con": "con1",
        "fem": 3,
        "ao": 4,
        "iir": [],
        "fir": [],
        "delay": delays[2][3],
        "unipolar_flux_len": 200,
        "unipolar_flux_amp": 0.14,
        "output_mode": "amplified"
    },
    "q5_z": {
        "idle_point": 0.04,
        "con": "con1",
        "fem": 3,
        "ao": 5,
        "iir": [],
        "fir": [],
        "delay": delays[2][4],
        "unipolar_flux_len": 200,
        "unipolar_flux_amp": 0.15,
        "output_mode": "amplified"
    },
    "q6_z": {
        "idle_point": 0.04,
        "con": "con1",
        "fem": 3,
        "ao": 6,
        "iir": [],
        "fir": [],
        "delay": delays[2][5],
        "unipolar_flux_len": 200,
        "unipolar_flux_amp": 0.16,
        "output_mode": "amplified"
    },
    "q7_z": {
        "idle_point": 0.04,
        "con": "con1",
        "fem": 3,
        "ao": 7,
        "iir": [],
        "fir": [],
        "delay": delays[2][6],
        "unipolar_flux_len": 200,
        "unipolar_flux_amp": 0.17,
        "output_mode": "amplified"
    },
}

flux_settle_time = 200

# MARK: RESONATORS
#############################################
#                Resonators                 #
#############################################
readout_len = 800
rr_reset_time = 4_000
pump_len = 200

pump_amp = {
    "TWPA1": 0.5623,
    "TWPA2": 0.5623
}

RL_CONSTANTS = {
    "rl1": {
        "LO": 7.64 * u.GHz,
        "RESONATORS": ["q1_rr", "q2_rr", "q7_rr"],
        "TWPA": "TWPA1",
        "TWPA_LO": 9.0357 * u.GHz,
        "TWPA_IF": 0.0e6, # NOT USED
        "TOF": 28,
        "rl_con": "con1",
        "rl_fem": 2,
        "rl_ao": 2,
        "rl_ai": 1,
        "twpa_con": "con1",
        "twpa_fem": 2,
        "twpa_ao": 8,
        "band": 3,
        "full_scale_power_dbm": -12,  # q3 -25, q4 -41, q5 -21, q6 -21
        "delay": delays[1][1]
    },   
    "rl2": {
        "LO": 7.54 * u.GHz,
        "RESONATORS": ["q3_rr", "q4_rr", "q5_rr", "q6_rr"],
        "TWPA": "TWPA2",
        "TWPA_LO": 9.0357 * u.GHz,
        "TWPA_IF": 0.0e6, # NOT USED
        "TOF": 28,
        "rl_con": "con1",
        "rl_fem": 1,
        "rl_ao": 2,
        "rl_ai": 1,
        "twpa_con": "con1",
        "twpa_fem": 1,
        "twpa_ao": 8,
        "band": 3,
        "full_scale_power_dbm": -12,  # q1 -24, q2 -28, q7 -21
        "delay": delays[0][1]
    }   
}

RR_CONSTANTS = {
    "q1_rr": {
        "amplitude": 0.125590,  # 10^(-DdB/20) where DdB is the difference in dB from full_scale
        "midcircuit_amplitude": 0.2511, 
        "IF": -313 * u.MHz,    # Example IF frequency
        "rotation_angle": (0.0 / 180) * np.pi,
        "ge_threshold": 0.0,
        "midcircuit_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_ge_threshold": 0.0
    },
    "q2_rr": {
        "amplitude": 0.07924, 
        "midcircuit_amplitude": 0.1585, 
        "IF": -126 * u.MHz,    # Example IF frequency
        "rotation_angle": (0.0 / 180) * np.pi,
        "ge_threshold": 0.0,
        "midcircuit_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_ge_threshold": 0.0,
    },
    "q3_rr": {
        "amplitude": 0.11193,
        "midcircuit_amplitude": 0.2238, 
        "IF": -114 * u.MHz,    # Example IF frequency
        "rotation_angle": (0.0 / 180) * np.pi,
        "ge_threshold": 0.0,
        "midcircuit_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_ge_threshold": 0.0,
    },
    "q4_rr": {
        "amplitude": 0.01774, 
        "midcircuit_amplitude": 0.0355, 
        "IF": -307 * u.MHz,    # Example IF frequency
        "rotation_angle": (0.0 / 180) * np.pi,
        "ge_threshold": 0.0,
        "midcircuit_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_ge_threshold": 0.0
    },
    "q5_rr": {
        "amplitude": 0.17740, 
        "midcircuit_amplitude": 0.3548, 
        "IF": 303 * u.MHz,    # Example IF frequency
        "rotation_angle": (0.0 / 180) * np.pi,
        "ge_threshold": 0.0,
        "midcircuit_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_ge_threshold": 0.0,
    },
    "q6_rr": {
        "amplitude": 0.17740, 
        "midcircuit_amplitude": 0.3548, 
        "IF": 103 * u.MHz,    # Example IF frequency
        "rotation_angle": (0.0 / 180) * np.pi,
        "ge_threshold": 0.0,
        "midcircuit_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_ge_threshold": 0.0
    },
    "q7_rr": {
        "amplitude": 0.17740, 
        "midcircuit_amplitude": 0.3548, 
        "IF": 110 * u.MHz,    # Example IF frequency
        "rotation_angle": (0.0 / 180) * np.pi,
        "ge_threshold": 0.0,
        "midcircuit_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_ge_threshold": 0.0,
    },
}

for rr_key in RR_CONSTANTS.keys():
    assert RR_CONSTANTS[rr_key]['amplitude'] <= 0.499, f"{rr_key} amplitude needs to be less than 0.499"

for rl_key in RL_CONSTANTS.keys():
    total_amp = 0
    for rr in RL_CONSTANTS[rl_key]['RESONATORS']:
        total_amp += RR_CONSTANTS[rr]['amplitude']
    assert total_amp <= 0.499, f"the sum of {rl_key} resonators is larger than 0.499"
    print(f'Total power on {rl_key}', RL_CONSTANTS[rl_key]['full_scale_power_dbm'])

# # add twin
# if TWIN_RESONATOR in RL_CONSTANTS["rl1"]["RESONATORS"]:
#     RL_CONSTANTS["rl2"]["RESONATORS"].append(TWIN_RESONATOR+ "_twin")
# else:
#     RL_CONSTANTS["rl1"]["RESONATORS"].append(TWIN_RESONATOR+ "_twin")

# RR_CONSTANTS[TWIN_RESONATOR+ "_twin"] = copy.deepcopy(RR_CONSTANTS[TWIN_RESONATOR[0:3]+"rr"])
# RR_CONSTANTS[TWIN_RESONATOR+ "_twin"]["amplitude"] = 0.0
# RR_CONSTANTS[TWIN_RESONATOR+ "_twin"]["midcircuit_rotation_angle"] = ( 0.0 / 180 ) * np.pi
# RR_CONSTANTS[TWIN_RESONATOR+ "_twin"]["midcircuit_ge_threshold"] = 0.0

opt_weights = False

if opt_weights:

    current_file_path = os.path.dirname(os.path.abspath(__file__))
    weights_q1_rr = np.load(os.path.join(current_file_path, "optimal_weights_q1_rr.npz"))
    weights_q2_rr = np.load(os.path.join(current_file_path, "optimal_weights_q2_rr.npz"))
    weights_q3_rr = np.load(os.path.join(current_file_path, "optimal_weights_q3_rr.npz"))
    weights_q4_rr = np.load(os.path.join(current_file_path, "optimal_weights_q4_rr.npz"))
    weights_q5_rr = np.load(os.path.join(current_file_path, "optimal_weights_q5_rr.npz"))
    weights_q6_rr = np.load(os.path.join(current_file_path, "optimal_weights_q6_rr.npz"))
    weights_q7_rr = np.load(os.path.join(current_file_path, "optimal_weights_q7_rr.npz"))

    OPT_WEIGHTS = {
        "q1_rr": {
            "real": [(x, weights_q1_rr['division_length'] * 4) for x in weights_q1_rr["weights_real"]],
            "minus_imag": [(x, weights_q1_rr['division_length'] * 4) for x in weights_q1_rr["weights_minus_imag"]],
            "imag": [(x, weights_q1_rr['division_length'] * 4) for x in weights_q1_rr["weights_imag"]] ,
            "minus_real": [(x, weights_q1_rr['division_length'] * 4) for x in weights_q1_rr["weights_minus_real"]] 
        },
        "q2_rr": {
            "real": [(x, weights_q2_rr['division_length'] * 4) for x in weights_q2_rr["weights_real"]],
            "minus_imag": [(x, weights_q2_rr['division_length'] * 4) for x in weights_q2_rr["weights_minus_imag"]],
            "imag": [(x, weights_q2_rr['division_length'] * 4) for x in weights_q2_rr["weights_imag"]] ,
            "minus_real": [(x, weights_q2_rr['division_length'] * 4) for x in weights_q2_rr["weights_minus_real"]] 
        },
        "q3_rr": {
            "real": [(x, weights_q3_rr['division_length'] * 4) for x in weights_q3_rr["weights_real"]],
            "minus_imag": [(x, weights_q3_rr['division_length'] * 4) for x in weights_q3_rr["weights_minus_imag"]],
            "imag": [(x, weights_q3_rr['division_length'] * 4) for x in weights_q3_rr["weights_imag"]] ,
            "minus_real": [(x, weights_q3_rr['division_length'] * 4) for x in weights_q3_rr["weights_minus_real"]] 
        },
        "q4_rr": {
            "real": [(x, weights_q4_rr['division_length'] * 4) for x in weights_q4_rr["weights_real"]],
            "minus_imag": [(x, weights_q4_rr['division_length'] * 4) for x in weights_q4_rr["weights_minus_imag"]],
            "imag": [(x, weights_q4_rr['division_length'] * 4) for x in weights_q4_rr["weights_imag"]] ,
            "minus_real": [(x, weights_q4_rr['division_length'] * 4) for x in weights_q4_rr["weights_minus_real"]] 
        },
        "q5_rr": {
            "real": [(x, weights_q5_rr['division_length'] * 4) for x in weights_q5_rr["weights_real"]],
            "minus_imag": [(x, weights_q5_rr['division_length'] * 4) for x in weights_q5_rr["weights_minus_imag"]],
            "imag": [(x, weights_q5_rr['division_length'] * 4) for x in weights_q5_rr["weights_imag"]] ,
            "minus_real": [(x, weights_q5_rr['division_length'] * 4) for x in weights_q5_rr["weights_minus_real"]] 
        },
        "q6_rr": {
            "real": [(x, weights_q6_rr['division_length'] * 4) for x in weights_q6_rr["weights_real"]],
            "minus_imag": [(x, weights_q6_rr['division_length'] * 4) for x in weights_q6_rr["weights_minus_imag"]],
            "imag": [(x, weights_q6_rr['division_length'] * 4) for x in weights_q6_rr["weights_imag"]] ,
            "minus_real": [(x, weights_q6_rr['division_length'] * 4) for x in weights_q6_rr["weights_minus_real"]] 
        },
        "q7_rr": {
            "real": [(x, weights_q7_rr['division_length'] * 4) for x in weights_q7_rr["weights_real"]],
            "minus_imag": [(x, weights_q7_rr['division_length'] * 4) for x in weights_q7_rr["weights_minus_imag"]],
            "imag": [(x, weights_q7_rr['division_length'] * 4) for x in weights_q7_rr["weights_imag"]] ,
            "minus_real": [(x, weights_q7_rr['division_length'] * 4) for x in weights_q7_rr["weights_minus_real"]] 
        },
    }

    OPT_WEIGHTS[TWIN_RESONATOR+"_twin"] = copy.deepcopy(OPT_WEIGHTS[TWIN_RESONATOR[0:3]+"rr"])
else:
    OPT_WEIGHTS = {
        "q1_rr": {
            "real": [(1.0, readout_len)],
            "minus_imag": [(0.0, readout_len)],
            "imag": [(0.0, readout_len)],
            "minus_real": [(1.0, readout_len)]
        },
        "q2_rr": {
            "real": [(1.0, readout_len)],
            "minus_imag": [(0.0, readout_len)],
            "imag": [(0.0, readout_len)],
            "minus_real": [(1.0, readout_len)]
        },
        "q3_rr": {
            "real": [(1.0, readout_len)],
            "minus_imag": [(0.0, readout_len)],
            "imag": [(0.0, readout_len)],
            "minus_real": [(1.0, readout_len)]
        },
        "q4_rr": {
            "real": [(1.0, readout_len)],
            "minus_imag": [(0.0, readout_len)],
            "imag": [(0.0, readout_len)],
            "minus_real": [(1.0, readout_len)]
        },
        "q5_rr": {
            "real": [(1.0, readout_len)],
            "minus_imag": [(0.0, readout_len)],
            "imag": [(0.0, readout_len)],
            "minus_real": [(1.0, readout_len)]
        },
        "q6_rr": {
            "real": [(1.0, readout_len)],
            "minus_imag": [(0.0, readout_len)],
            "imag": [(0.0, readout_len)],
            "minus_real": [(1.0, readout_len)]
        },
        "q7_rr": {
            "real": [(1.0, readout_len)],
            "minus_imag": [(0.0, readout_len)],
            "imag": [(0.0, readout_len)],
            "minus_real": [(1.0, readout_len)]
        },
    }
    OPT_WEIGHTS[TWIN_RESONATOR+"_twin"] = copy.deepcopy(OPT_WEIGHTS[TWIN_RESONATOR[0:3]+"rr"])

#######################
# Terminal Flux Pulse #
#######################

terminal_flux_len = 500
terminal_flux_amp = 0.125

##################
# DELAYS PER FEM #
##################

DELAY_FEM_1 = 0
DELAY_FEM_2 = 0
DELAY_FEM_3 = 0
DELAY_FEM_3_CH_8 = 0

# %%

# MARK: CONFIGURATION
#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                1: {
                    "type": "MW",
                    "analog_outputs": {
                        2: {"sampling_rate": 1e9, "full_scale_power_dbm": RL_CONSTANTS['rl2']['full_scale_power_dbm'], "band": RL_CONSTANTS["rl2"]['band'], "delay": DELAY_FEM_1 + RL_CONSTANTS['rl2']['delay']}, # RL2  0.5V => 4dbm +[+6, -45] 3db spacing  
                        4: {"sampling_rate": 1e9, "full_scale_power_dbm": QUBIT_CONSTANTS["q3_xy"]['full_scale_power_dbm'], "band": QUBIT_CONSTANTS["q3_xy"]['band'], "delay": DELAY_FEM_1 + QUBIT_CONSTANTS["q3_xy"]['delay']}, # q3 XY
                        5: {"sampling_rate": 1e9, "full_scale_power_dbm": QUBIT_CONSTANTS['q4_xy']['full_scale_power_dbm'], "band": QUBIT_CONSTANTS['q4_xy']['band'], "delay": DELAY_FEM_1 + QUBIT_CONSTANTS["q4_xy"]['delay']}, # q4 XY
                        6: {"sampling_rate": 1e9, "full_scale_power_dbm": QUBIT_CONSTANTS['q5_xy']['full_scale_power_dbm'], "band": QUBIT_CONSTANTS['q5_xy']['band'], "delay": DELAY_FEM_1 + QUBIT_CONSTANTS["q5_xy"]['delay']}, # q5 XY 
                        7: {"sampling_rate": 1e9, "full_scale_power_dbm": QUBIT_CONSTANTS['q6_xy']['full_scale_power_dbm'], "band": QUBIT_CONSTANTS["q6_xy"]['band'], "delay": DELAY_FEM_1 + QUBIT_CONSTANTS["q6_xy"]['delay']}, # q6 XY
                        # 8: {"sampling_rate": 1e9, "full_scale_power_dbm": +3, "band": 3} # TWPA
                    },
                    "analog_inputs": {
                        # TODO: gain_db
                        1: {"sampling_rate": 1e9, "band": RL_CONSTANTS["rl2"]['band'], "gain_db": 0},  # RL2, gain_db resolution is 1
                    },
                },
                2: {
                    "type": "MW",
                    "analog_outputs": {
                        2: {"sampling_rate": 1e9, "full_scale_power_dbm": RL_CONSTANTS["rl1"]['full_scale_power_dbm'], "band": RL_CONSTANTS['rl1']['band'], "delay": DELAY_FEM_2 + RL_CONSTANTS['rl1']['delay']}, # RL1  0.5V => 4dbm +[+6, -45] 3db spacing  
                        4: {"sampling_rate": 1e9, "full_scale_power_dbm": QUBIT_CONSTANTS['q1_xy']['full_scale_power_dbm'], "band": QUBIT_CONSTANTS["q1_xy"]['band'], "delay": DELAY_FEM_2 + QUBIT_CONSTANTS["q1_xy"]['delay']}, # q1 XY (for active reset between FEMs)
                        5: {"sampling_rate": 1e9, "full_scale_power_dbm": QUBIT_CONSTANTS["q2_xy"]["full_scale_power_dbm"], "band": QUBIT_CONSTANTS["q2_xy"]["band"], "delay": DELAY_FEM_2 + QUBIT_CONSTANTS["q2_xy"]['delay']}, # q2 XY
                        6: {"sampling_rate": 1e9, "full_scale_power_dbm": QUBIT_CONSTANTS['q7_xy']['full_scale_power_dbm'], "band": QUBIT_CONSTANTS['q7_xy']['band'], "delay": DELAY_FEM_2 + QUBIT_CONSTANTS["q7_xy"]['delay']}, # q7 XY
                        # 8: {"sampling_rate": 1e9, "full_scale_power_dbm": +3, "band": 3} # TWPA
                    },
                    "analog_inputs": {
                        # TODO: gain_db
                        1: {"sampling_rate": 1e9, "band": RL_CONSTANTS['rl1']['band'], "gain_db": 0},  # RL1, gain_db resolution is 1
                    },
                },
                3: {
                    "type": "LF",
                    "analog_outputs": {
                        ** {FLUX_CONSTANTS[qz]["ao"]: {"offset": FLUX_CONSTANTS[qz]["idle_point"], "sampling_rate": 1e9, "output_mode": FLUX_CONSTANTS[qz]["output_mode"], "upsampling_mode": "pulse", "filter": {"feedforward": FLUX_CONSTANTS[qz]["fir"], "feedback": FLUX_CONSTANTS[qz]["iir"]}, "delay": FLUX_CONSTANTS[qz]["delay"] + DELAY_FEM_3} for qz in FLUX_CONSTANTS.keys()},
                        8: {"offset": 0.0, "sampling_rate": 1e9, "output_mode": "amplified", "upsampling_mode": "pulse", "delay": DELAY_FEM_3 + DELAY_FEM_3_CH_8},
                    },
                },
            },
        },
    },
    "elements": {

        # readout line 1
        **{rr: {
            "MWInput": {
                "port": (RL_CONSTANTS["rl1"]["rl_con"], RL_CONSTANTS["rl1"]["rl_fem"], RL_CONSTANTS["rl1"]["rl_ao"]),
                "oscillator_frequency": RL_CONSTANTS["rl1"]["LO"],  # in Hz [6-8e9]
            },
            "intermediate_frequency": RR_CONSTANTS[rr]["IF"],  # in Hz [-350e6, +350e6]
            "MWOutput": {
                "port": (RL_CONSTANTS["rl1"]["rl_con"], RL_CONSTANTS["rl1"]["rl_fem"], RL_CONSTANTS["rl1"]["rl_ai"]),
            },
			'time_of_flight': RL_CONSTANTS["rl1"]["TOF"],
            'smearing': 0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_"+rr,
                "midcircuit_readout": "midcircuit_readout_pulse_"+rr,
            },
        } for rr in RL_CONSTANTS["rl1"]["RESONATORS"]},

        # readout line 2
        **{rr: {
            "MWInput": {
                "port": (RL_CONSTANTS["rl2"]["rl_con"], RL_CONSTANTS["rl2"]["rl_fem"], RL_CONSTANTS["rl2"]["rl_ao"]),
                "oscillator_frequency": RL_CONSTANTS["rl2"]["LO"],  # in Hz [6-8e9]
            },
            "intermediate_frequency": RR_CONSTANTS[rr]["IF"],  # in Hz [-350e6, +350e6]
            "MWOutput": {
                "port": (RL_CONSTANTS["rl2"]["rl_con"], RL_CONSTANTS["rl2"]["rl_fem"], RL_CONSTANTS["rl2"]["rl_ai"]),
            },
			'time_of_flight': RL_CONSTANTS["rl2"]["TOF"],
            'smearing': 0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_"+rr,
                "midcircuit_readout": "midcircuit_readout_pulse_"+rr,
            },
        } for rr in RL_CONSTANTS['rl2']['RESONATORS']},
        
        # xy drives
        **{qubit_key: {
            "MWInput": {
                "port": (QUBIT_CONSTANTS[qubit_key]["con"], QUBIT_CONSTANTS[qubit_key]["fem"], QUBIT_CONSTANTS[qubit_key]["ao"]),
                "oscillator_frequency": QUBIT_CONSTANTS[qubit_key]["LO"],  # in Hz
            },
            "intermediate_frequency": QUBIT_CONSTANTS[qubit_key]["IF"],  # in Hz
            "operations": {
                "zero": "zero_pulse",
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": f"x180_pulse_{qubit_key}",
                "x180_flux_spec": f"x180_flux_spec_pulse_{qubit_key}",
                "x90": f"x90_pulse_{qubit_key}",
                "-x90": f"-x90_pulse_{qubit_key}",
                "y90": f"y90_pulse_{qubit_key}",
                "y180": f"y180_pulse_{qubit_key}",
                "-y90": f"-y90_pulse_{qubit_key}",
            },
        } for qubit_key in QUBIT_CONSTANTS.keys()},

        # flux lines
        **{flux_key: {
            "singleInput": {
                "port": (FLUX_CONSTANTS[flux_key]["con"], FLUX_CONSTANTS[flux_key]["fem"], FLUX_CONSTANTS[flux_key]["ao"]),
            },
            "operations": {
                "unipolar": f"unipolar_flux_pulse_{flux_key}",
                "netzero": f"netzero_flux_pulse_{flux_key}",
            },
        } for flux_key in FLUX_CONSTANTS.keys()},

        # repeatl unstil success flux lines
        "rus_z": {
            "singleInput": {
                "port": ("con1", 3, 8),
            },
            "operations": {
                "flux": "flux_pulse",
            },
        },
    }, 
    "pulses": {
        "flux_pulse": {
            "operation": "control",
            "length": terminal_flux_len,
            "waveforms": {
                "single": "terminal_flux_wf",
            },
        },
        **{f"unipolar_flux_pulse_{key}":
            {
                "operation": "control",
                "length": FLUX_CONSTANTS[key]["unipolar_flux_len"],
                "waveforms": {
                    "single": f"unipolar_flux_wf_{key}",
                }
            }
            for key in FLUX_CONSTANTS.keys()
        },
        **{f"netzero_flux_pulse_{key}":
            {
                "operation": "control",
                "length": FLUX_CONSTANTS[key]["unipolar_flux_len"],
                "waveforms": {
                    "single": f"netzero_flux_wf_{key}",
                }
            }
            for key in FLUX_CONSTANTS.keys()
        },
        "const_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "zero_pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "zero_wf",
                "Q": "zero_wf",
            },
        },
        "saturation_pulse": {
            "operation": "control",
            "length": saturation_len,
            "waveforms": {
                "I": "saturation_wf",
                "Q": "zero_wf",
            },
        },
        **{f"x90_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LENGTH,
                "waveforms": {
                    "I": f"x90_I_wf_{key}",
                    "Q": f"x90_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{f"x180_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LENGTH,
                "waveforms": {
                    "I": f"x180_I_wf_{key}",
                    "Q": f"x180_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{f"x180_flux_spec_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LENGTH_FLUX_SPEC,
                "waveforms": {
                    "I": f"x180_flux_spec_I_wf_{key}",
                    "Q": f"x180_flux_spec_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{f"-x90_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LENGTH,
                "waveforms": {
                    "I": f"minus_x90_I_wf_{key}",
                    "Q": f"minus_x90_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{f"y90_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LENGTH,
                "waveforms": {
                    "I": f"y90_I_wf_{key}",
                    "Q": f"y90_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{f"y180_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LENGTH,
                "waveforms": {
                    "I": f"y180_I_wf_{key}",
                    "Q": f"y180_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{f"-y90_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LENGTH,
                "waveforms": {
                    "I": f"minus_y90_I_wf_{key}",
                    "Q": f"minus_y90_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },

        **{
            f"readout_pulse_{key}": {
                "operation": "measurement",
                "length": readout_len,
                "waveforms": {
                    "I": f"readout_wf_{key}",
                    "Q": "zero_wf"
                },
                "integration_weights": {
                    "cos": "cosine_weights",
                    "sin": "sine_weights",
                    "minus_sin": "minus_sine_weights",
                    "rotated_cos": f"rotated_cosine_weights_{key}",
                    "rotated_sin": f"rotated_sine_weights_{key}",
                    "rotated_minus_sin": f"rotated_minus_sine_weights_{key}",
                    "opt_cos": f"opt_cosine_weights_{key}",
                    "opt_sin": f"opt_sine_weights_{key}",
                    "opt_minus_sin": f"opt_minus_sine_weights_{key}",
                },
                "digital_marker": "ON",
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_readout_pulse_{key}": {
                "operation": "measurement",
                "length": readout_len,
                "waveforms": {
                    "I": f"midcircuit_readout_wf_{key}",
                    "Q": "zero_wf"
                },
                "integration_weights": {
                    "cos": "cosine_weights",
                    "sin": "sine_weights",
                    "minus_sin": "minus_sine_weights",
                    "rotated_cos": f"midcircuit_rotated_cosine_weights_{key}",
                    "rotated_sin": f"midcircuit_rotated_sine_weights_{key}",
                    "rotated_minus_sin": f"midcircuit_rotated_minus_sine_weights_{key}",
                    "opt_cos": f"midcircuit_opt_cosine_weights_{key}",
                    "opt_sin": f"midcircuit_opt_sine_weights_{key}",
                    "opt_minus_sin": f"midcircuit_opt_minus_sine_weights_{key}",
                },
                "digital_marker": "ON",
            } for key in RR_CONSTANTS.keys()
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp},
        "saturation_wf": {"type": "constant", "sample": saturation_amp},
        "terminal_flux_wf": {"type": "constant", "sample": terminal_flux_amp},
        **{f"unipolar_flux_wf_{key}": {"type": "constant", "sample": FLUX_CONSTANTS[key]["unipolar_flux_amp"]} for key in FLUX_CONSTANTS.keys()},
        **{f"netzero_flux_wf_{key}": {"type": "arbitrary", "samples": [FLUX_CONSTANTS[key]["unipolar_flux_amp"]] * int(FLUX_CONSTANTS[key]["unipolar_flux_len"] / 2) + [-FLUX_CONSTANTS[key]["unipolar_flux_amp"]] * int(FLUX_CONSTANTS[key]["unipolar_flux_len"] / 2)} for key in FLUX_CONSTANTS.keys()},
        "zero_wf": {"type": "constant", "sample": 0.0},
        **{f"x90_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_x90_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"x90_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_x90_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"x180_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_x180_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"x180_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_x180_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"x180_flux_spec_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_x180_flux_spec_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"x180_flux_spec_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_x180_flux_spec_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"minus_x90_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_minus_x90_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"minus_x90_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_minus_x90_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"y90_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_y90_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"y90_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_y90_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"y180_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_y180_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"y180_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_y180_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"minus_y90_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_minus_y90_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"minus_y90_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_minus_y90_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"readout_wf_{key}": {"type": "constant", "sample": RR_CONSTANTS[key]["amplitude"]} for key in RR_CONSTANTS.keys()},
        **{f"midcircuit_readout_wf_{key}": {"type": "constant", "sample": RR_CONSTANTS[key]["midcircuit_amplitude"]} for key in RR_CONSTANTS.keys()},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, readout_len)],
            "sine": [(0.0, readout_len)],
        },
        "sine_weights": {
            "cosine": [(0.0, readout_len)],
            "sine": [(1.0, readout_len)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, readout_len)],
            "sine": [(-1.0, readout_len)],
        },
        **{
            f"rotated_cosine_weights_{key}": {
                "cosine": [(np.cos(RR_CONSTANTS[key]["rotation_angle"])), readout_len],
                "sine": [(np.sin(RR_CONSTANTS[key]["rotation_angle"])), readout_len]
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"rotated_sine_weights_{key}": {
                "cosine": [(-np.sin(RR_CONSTANTS[key]["rotation_angle"])), readout_len],
                "sine": [(np.cos(RR_CONSTANTS[key]["rotation_angle"])), readout_len]
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"rotated_minus_sine_weights_{key}": {
                "cosine": [(np.sin(RR_CONSTANTS[key]["rotation_angle"])), readout_len],
                "sine": [(-np.cos(RR_CONSTANTS[key]["rotation_angle"])), readout_len]
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"opt_cosine_weights_{key}": {
                "cosine": OPT_WEIGHTS[key]['real'],
                "sine": OPT_WEIGHTS[key]['minus_imag']
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"opt_sine_weights_{key}": {
                "cosine": OPT_WEIGHTS[key]['imag'],
                "sine": OPT_WEIGHTS[key]['real']
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"opt_minus_sine_weights_{key}": {
                "cosine": OPT_WEIGHTS[key]['minus_imag'],
                "sine": OPT_WEIGHTS[key]['minus_real']
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_rotated_cosine_weights_{key}": {
                "cosine": [(np.cos(RR_CONSTANTS[key]["midcircuit_rotation_angle"])), readout_len],
                "sine": [(np.sin(RR_CONSTANTS[key]["midcircuit_rotation_angle"])), readout_len]
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_rotated_sine_weights_{key}": {
                "cosine": [(-np.sin(RR_CONSTANTS[key]["midcircuit_rotation_angle"])), readout_len],
                "sine": [(np.cos(RR_CONSTANTS[key]["midcircuit_rotation_angle"])), readout_len]
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_rotated_minus_sine_weights_{key}": {
                "cosine": [(np.sin(RR_CONSTANTS[key]["midcircuit_rotation_angle"])), readout_len],
                "sine": [(-np.cos(RR_CONSTANTS[key]["midcircuit_rotation_angle"])), readout_len]
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_opt_cosine_weights_{key}": {
                "cosine": OPT_WEIGHTS[key]['real'],
                "sine": OPT_WEIGHTS[key]['minus_imag']
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_opt_sine_weights_{key}": {
                "cosine": OPT_WEIGHTS[key]['imag'],
                "sine": OPT_WEIGHTS[key]['real']
            } for key in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_opt_minus_sine_weights_{key}": {
                "cosine": OPT_WEIGHTS[key]['minus_imag'],
                "sine": OPT_WEIGHTS[key]['minus_real']
            } for key in RR_CONSTANTS.keys()
        },
    },
}

if TWIN_DEACTIVATED:
    config['elements'][TWIN_QUBIT + "_twin"] = {
                "MWInput": {
                    "port": (QUBIT_CONSTANTS[TWIN_QUBIT]["con"], QUBIT_CONSTANTS[TWIN_QUBIT]["fem_twin"], QUBIT_CONSTANTS[TWIN_QUBIT]["ao_twin"]),
                    "oscillator_frequency": QUBIT_CONSTANTS[TWIN_QUBIT]["LO"],  # in Hz
                },
                "intermediate_frequency": QUBIT_CONSTANTS[TWIN_QUBIT]["IF"],  # in Hz
                "operations": {
                    "cw": "const_pulse",
                    "saturation": "saturation_pulse",
                    "x180": "x180_pulse_q1_xy",
                    "x90": "x90_pulse_q1_xy",
                    "-x90": "-x90_pulse_q1_xy",
                    "y90": "y90_pulse_q1_xy",
                    "y180": "y180_pulse_q1_xy",
                    "-y90": "-y90_pulse_q1_xy",
                },
            },      

# %%
