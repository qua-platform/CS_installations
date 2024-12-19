# %%
import matplotlib.pyplot as plt
import numpy as np
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from qualang_tools.units import unit
from scipy.special import i0  # Zeroth-order modified Bessel function of the first kind


def generate_kaiser_wwaveform(
    amplitude: float, length: int, alpha: float
) -> np.ndarray:
    """
    Generate a Kaiser window for digital signal processing.

    :param T: Length of the window (number of points - 1).
    :param alpha: Shape parameter that determines the trade-off between main lobe width and side lobe level.
    :return: A numpy array of the Kaiser window values.
    """
    # Compute the normalized indices
    x = np.linspace(-1, 1, length)

    # Calculate the Kaiser window using the zeroth-order modified Bessel function
    wf = i0(np.pi * alpha * np.sqrt(1 - x**2)) / i0(np.pi * alpha)
    wf *= amplitude / wf.max()
    return wf


#############
# VARIABLES #
#############
u = unit(coerce_to_integer=True)
qop_ip = "172.16.33.101"  # QOP IP address
qop_port = None  # Write the QOP port if version < QOP220
cluster_name = "Cluster_83"  # Name of the cluster

qubit_if_freq = 50 * u.MHz

const_amp = 0.1
const_len_ns = 1000

kaiser_amp = 0.1
kaiser_len_ns = 300  # ensure it's multiple of 4ns

gauss_amp = kaiser_amp
gauss_len_ns = kaiser_len_ns


kaiser_wf = generate_kaiser_wwaveform(
    amplitude=kaiser_amp,
    length=kaiser_len_ns,
    alpha=2.0,  # rise or fall
)

gauss_wf, _ = drag_gaussian_pulse_waveforms(
    amplitude=gauss_amp,
    length=gauss_len_ns,
    sigma=gauss_len_ns / 5,
    alpha=0.0,
    anharmonicity=0.0,
)


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0, "delay": 0.0},
            },
            "digital_outputs": {},
            "analog_inputs": {},
        }
    },
    "elements": {
        "qubit": {
            "singleInput": {"port": ("con1", 1)},
            "intermediate_frequency": qubit_if_freq,
            "operations": {
                "const": "const_pulse",
                "kaiser": "kaiser_pulse",
                "gauss": "gauss_pulse",
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": const_len_ns,
            "waveforms": {"single": "const_wf"},
        },
        "kaiser_pulse": {
            "operation": "control",
            "length": kaiser_len_ns,
            "waveforms": {"single": "kaiser_wf"},
        },
        "gauss_pulse": {
            "operation": "control",
            "length": gauss_len_ns,
            "waveforms": {"single": "gauss_wf"},
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "gauss_wf": {"type": "arbitrary", "samples": gauss_wf},
        "kaiser_wf": {"type": "arbitrary", "samples": kaiser_wf},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},  # [(on/off, ns)]
    },
}


from qualang_tools.voltage_gates import VoltageGateSequence

###################
# The QUA program #
###################

with program() as PROGRAM:
    play("kaiser", "qubit")
    wait(100 * u.ns)
    play("gauss", "qubit")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)


###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=300)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, PROGRAM, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()
    plt.show()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(PROGRAM)

# %%
