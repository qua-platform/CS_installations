from pathlib import Path
import numpy as np
from scipy.signal.windows import gaussian
from qualang_tools.units import unit


#######################
# AUXILIARY FUNCTIONS #
#######################

# IQ imbalance matrix
def IQ_imbalance(g, phi):
    """
    Creates the correction matrix for the mixer imbalance caused by the gain and phase imbalances, more information can
    be seen here:
    https://docs.qualang.io/libs/examples/mixer-calibration/#non-ideal-mixer

    :param g: relative gain imbalance between the I & Q ports (unit-less). Set to 0 for no gain imbalance.
    :param phi: relative phase imbalance between the I & Q ports (radians). Set to 0 for no phase imbalance.
    """
    c = np.cos(phi)
    s = np.sin(phi)
    N = 1 / ((1 - g**2) * (2 * c**2 - 1))
    return [float(N * x) for x in [(1 - g) * c, (1 + g) * s, (1 - g) * s, (1 + g) * c]]


######################
# Network parameters #
######################

u = unit(coerce_to_integer=True)
qop_ip = "127.0.0.1"  # Write the QM router IP address
cluster_name = "my_cluster"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220
octave_config = None

##################
# Data save path #
##################

base_dir = Path().absolute()
save_dir = base_dir / 'QM' / 'Data'


##############
# Parameters #
##############

time_of_flight = 24

reflectometry_IF = 123 * u.MHz
reflectometry_amp = 0.1
reflectometry_len = 200 * u.ns # 1 * u.us

qubit_LO = 8.0 * u.GHz
qubit_IF = 10 * u.MHz
qubit_g = 0.0
qubit_phi = 0.0 

cw_amp = 0.125 # in V
cw_len = 40 # in ns

P1_step_amp = 0.125
P2_step_amp = 0.125
sensor_step_amp = 0.125
step_len = 16
hold_offset_duration = 4
bias_tee_cut_off_frequency = 10 * u.kHz

pi_amp = 0.125 # in V 
pi_len = 40 # in ns

pi_half_amp = 0.0625 # in V 
pi_half_len = 40 # in ns

gaussian_amp = 0.1
gaussian_len = 40
gaussian_sigma = gaussian_len / 5
gaussian_samples = list(gaussian_amp * gaussian(gaussian_len, gaussian_sigma))

## Section defining the points from the charge stability map - can be done in the config
# Relevant points in the charge stability map as ["P1", "P2"] in V
level_init = [-0.12, -0.1]
level_interim = [0.0, 0.02]
level_manip = [0.1, 0.12]
level_readout = [-0.08, -0.06] # level_init

# Duration of each step in ns
readout_len = reflectometry_len
duration_init = 100
duration_interim = 100
duration_manip = 100
duration_readout = readout_len + 20
duration_compensation_pulse = 1 * u.us


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0}, # P1 IF I
                2: {"offset": 0.0}, # P1 IF Q
                3: {"offset": 0.0}, # P1 LF
                4: {"offset": 0.0}, # P2 LF
                5: {"offset": 0.0}, # sensor gate
                6: {"offset": 0.0}, # RF Reflectometry
            },
            "digital_outputs": {
                1: {}, # TTL for 
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0} # RF Reflectometry
            },
        },
    },
    "elements": {
        "qubit": {
            "mixInputs": {
                "I": ("con1", 1),
                "Q": ("con1", 2),
                "lo_frequency": qubit_LO,
                "mixer": "mixer_qubit",
            },
            "intermediate_frequency": qubit_IF,
            "operations": {
                "cw": "const_pulse",
                "pi": "pi_pulse",
                "pi_half": "pi_half_pulse",
                "gauss": "gaussian_pulse",
            }
        },
        "P1": {
            "singleInput": {
                "port": ("con1", 3),
            },
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "P1_sticky": {
            "singleInput": {
                "port": ("con1", 3),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "P2": {
            "singleInput": {
                "port": ("con1", 4),
            },
            "operations": {
                "step": "P2_step_pulse",
            },
        },
        "P2_sticky": {
            "singleInput": {
                "port": ("con1", 4),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "sensor_gate": {
            "singleInput": {
                "port": ("con1", 5),
            },
            "operations": {
                "step": "sensor_step_pulse",
            },
        },
        "sensor_gate_sticky": {
            "singleInput": {
                "port": ("con1", 5),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "sensor_step_pulse",
            },
        },
        "tank_circuit": {
            "singleInput": {
                "port": ("con1", 6)
            },
            "intermediate_frequency": reflectometry_IF,
            "operations": {
                "readout": "reflectometry_pulse",
            },
            "outputs": {
                "out1": ("con1", 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
    },
    "pulses": {
        "P1_step_pulse": {
            "operation": "control",
            "length": step_len,
            "waveforms": {
                "single": "P1_step_wf",
            },
        },
        "P2_step_pulse": {
            "operation": "control",
            "length": step_len,
            "waveforms": {
                "single": "P2_step_wf",
            },
        },
        "sensor_step_pulse": {
            "operation": "control",
            "length": step_len,
            "waveforms": {
                "single": "sensor_step_wf",
            },
        },
        "const_pulse": {
            "operation": "control",
            "length": cw_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "gaussian_pulse": {
            "operation": "control",
            "length": gaussian_len,
            "waveforms": {
                "I": "gaussian_wf",
                "Q": "zero_wf",
            },
        },
        "pi_pulse": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "pi_wf",
                "Q": "zero_wf",
            },
        },
        "pi_half_pulse": {
            "operation": "control",
            "length": pi_half_len,
            "waveforms": {
                "I": "pi_half_wf",
                "Q": "zero_wf",
            },
        },
        "reflectometry_pulse": {
            "operation": "measurement",
            "length": reflectometry_len,
            "waveforms": {
                "single": "reflectometry_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "P1_step_wf": {"type": "constant", "sample": P1_step_amp},
        "P2_step_wf": {"type": "constant", "sample": P2_step_amp},
        "sensor_step_wf": {"type": "constant", "sample": sensor_step_amp},
        "pi_wf": {"type": "constant", "sample": pi_amp},
        "pi_half_wf": {"type": "constant", "sample": pi_half_amp},
        "gaussian_wf": {"type": "arbitrary", "samples": gaussian_samples},
        "reflectometry_wf": {"type": "constant", "sample": reflectometry_amp},
        "const_wf": {"type": "constant", "sample": cw_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, reflectometry_len)],
            "sine": [(0.0, reflectometry_len)],
        },
        "sine_weights": {
            "cosine": [(0.0, reflectometry_len)],
            "sine": [(1.0, reflectometry_len)],
        },
    },
    "mixers": {
        "mixer_qubit": [
            {
                "intermediate_frequency": qubit_IF,
                "lo_frequency": qubit_LO,
                "correction": IQ_imbalance(qubit_g, qubit_phi)
            }
        ],
    },
}



from qm.qua._dsl import _Variable, QuaExpression
from qm.qua import declare, assign, play, fixed, Cast, amp, wait, ramp, ramp_to_zero


class OPX_virtual_gate_sequence:
    def __init__(self, configuration: dict, elements: list):
        """Framework allowing to design an arbitrary pulse sequence using virtual gates and pre-defined point from the
        charge stability map. TODO better docstring explaining how it works

        :param configuration: The OPX configuration.
        :param elements: List containing the elements taking part in the virtual gate.
        """
        # List of the elements involved in the virtual gates
        self._elements = elements
        # The OPX configuration
        self._config = configuration
        # Initialize the current voltage level for sticky elements
        self.current_level = [0.0 for _ in self._elements]
        # Relevant voltage points in the charge stability diagram
        self._voltage_points = {}
        # Keep track of the averaged voltage played for defining the compensation pulse at the end of the sequence
        self.average_power = [0 for _ in self._elements]
        self._expression = None
        self._expression2 = None
        # Add to the config the step operation (length=16ns & amp=0.25V)
        for el in self._elements:
            self._config["elements"][el]["operations"]["step"] = "step_pulse"
        self._config["pulses"]["step_pulse"] = {
            "operation": "control",
            "length": 16,
            "waveforms": {"single": "step_wf"},
        }
        self._config["waveforms"]["step_wf"] = {"type": "constant", "sample": 0.25}

    def _check_name(self, name, key):
        if name in key:
            return self._check_name(name + "%", key)
        else:
            return name

    def _add_op_to_config(self, el: str, name: str, amplitude: float, length: int) -> str:
        """Add an operation to an element when the amplitude is fixed to release the number of real-time operations on
        the OPX.

        :param el: the element to which we want to add the operation.
        :param name: name of the operation.
        :param amplitude: Amplitude of the pulse in V.
        :param length: Duration of the pulse in ns.
        :return : The name of the created operation.
        """
        op_name = self._check_name(name, self._config["elements"][el]["operations"])
        pulse_name = self._check_name(f"{el}_{op_name}_pulse", self._config["pulses"])
        wf_name = self._check_name(f"{el}_{op_name}_wf", self._config["waveforms"])
        self._config["elements"][el]["operations"][op_name] = pulse_name
        self._config["pulses"][pulse_name] = {
            "operation": "control",
            "length": length,
            "waveforms": {"single": wf_name},
        }
        self._config["waveforms"][wf_name] = {"type": "constant", "sample": amplitude}
        return op_name

    @staticmethod
    def _check_duration(duration: int):
        if duration is not None and not isinstance(duration, (_Variable, QuaExpression)):
            assert duration >= 4, "The duration must be a larger than 16 ns."

    def _update_averaged_power(self, level, duration, ramp_duration=None, current_level=None):
        if self.is_QUA(level):
            self._expression = declare(fixed)
            assign(self._expression, level)
            new_average = Cast.mul_int_by_fixed(duration, self._expression)
        elif self.is_QUA(duration):
            new_average = Cast.mul_int_by_fixed(duration, level)
        else:
            new_average = int(np.round(level * duration))

        if ramp_duration is not None:
            if not self.is_QUA(ramp_duration):
                if self.is_QUA(level):
                    self._expression2 = declare(fixed)
                    assign(self._expression2, (self._expression + current_level) >> 1)
                    new_average += Cast.mul_int_by_fixed(ramp_duration, self._expression2)
                elif self.is_QUA(current_level):
                    expression2 = declare(fixed)
                    assign(expression2, (level + current_level) >> 1)
                    new_average += Cast.mul_int_by_fixed(ramp_duration, expression2)
                elif self.is_QUA(duration):
                    new_average += Cast.mul_int_by_fixed(ramp_duration, (level + current_level) / 2)
                else:
                    new_average += int(np.round((level + current_level) * ramp_duration / 2))

            else:
                pass
        return new_average

    @staticmethod
    def is_QUA(var):
        return isinstance(var, (_Variable, QuaExpression))

    def add_step(
        self,
        level: list = None,
        duration: int = None,
        voltage_point_name: str = None,
        ramp_duration: int = None,
    ) -> None:
        """Add a voltage level to the pulse sequence.
        The voltage level is either identified by its voltage_point_name if added to the voltage_point dict beforehand, or by its level and duration.
        A ramp_duration can be used to ramp to the desired level instead of stepping to it.

        :param level: Desired voltage level of the different gates composing the virtual gate in Volt.
        :param duration: How long the voltage level should be maintained in clock cycles (4ns). Must be larger than 4 clock cycles.
        :param voltage_point_name: Name of the voltage level if added to the list of relevant points in the charge stability map.
        :param ramp_duration: Duration in clock cycles (4ns) of the ramp if the voltage should be ramped to the desired level instead of stepped. Must be larger than 4 clock cycles.
        """
        self._check_duration(duration)
        self._check_duration(ramp_duration)

        if voltage_point_name is not None and duration is None:
            _duration = self._voltage_points[voltage_point_name]["duration"]
        elif duration is not None:
            _duration = duration
        else:
            raise RuntimeError(
                "Either the voltage_point_name or the duration and desired voltage level must be provided."
            )

        for i, gate in enumerate(self._elements):
            if voltage_point_name is not None and level is None:
                voltage_level = self._voltage_points[voltage_point_name]["coordinates"][i]
            elif level is not None:
                voltage_point_name = "unregistered_value"
                voltage_level = level[i]
            else:
                raise RuntimeError(
                    "Either the voltage_point_name or the duration and desired voltage level must be provided."
                )
            # Play a step
            if ramp_duration is None:
                self.average_power[i] += self._update_averaged_power(voltage_level, _duration)

                # Dynamic amplitude change...
                if self.is_QUA(voltage_level) or self.is_QUA(self.current_level[i]):
                    # if dynamic duration --> play step and wait
                    if self.is_QUA(_duration):
                        play("step" * amp((voltage_level - self.current_level[i]) * 4), gate)
                        wait((_duration - 16) >> 2, gate)
                    # if constant duration --> new operation and play(*amp(..))
                    else:
                        operation = self._add_op_to_config(
                            gate,
                            "step",
                            amplitude=0.25,
                            length=_duration,
                        )
                        play(operation * amp((voltage_level - self.current_level[i]) * 4), gate)

                # Fixed amplitude but dynamic duration --> new operation and play(duration=..)
                elif isinstance(_duration, (_Variable, QuaExpression)):
                    operation = self._add_op_to_config(
                        gate,
                        voltage_point_name,
                        amplitude=voltage_level - self.current_level[i],
                        length=16,
                    )
                    play(operation, gate, duration=_duration >> 2)

                # Fixed amplitude and duration --> new operation and play()
                else:
                    operation = self._add_op_to_config(
                        gate,
                        voltage_point_name,
                        amplitude=voltage_level - self.current_level[i],
                        length=_duration,
                    )
                    play(operation, gate)

            # Play a ramp
            else:
                self.average_power[i] += self._update_averaged_power(
                    voltage_level, _duration, ramp_duration, self.current_level[i]
                )

                if not self.is_QUA(ramp_duration):
                    ramp_rate = 1 / ramp_duration
                    play(ramp((voltage_level - self.current_level[i]) * ramp_rate), gate, duration=ramp_duration >> 2)
                    wait(_duration >> 2, gate)

            self.current_level[i] = voltage_level

    def add_compensation_pulse(self, duration: int) -> None:
        """Add a compensation pulse of the specified duration whose amplitude is derived from the previous operations.

        :param duration: Duration of the compensation pulse in clock cycles (4ns). Must be larger than 4 clock cycles.
        """
        self._check_duration(duration)
        for i, gate in enumerate(self._elements):
            if not self.is_QUA(self.average_power[i]):
                compensation_amp = -self.average_power[i] / duration
                operation = self._add_op_to_config(
                    gate, "compensation", amplitude=compensation_amp - self.current_level[i], length=duration
                )
                play(operation, gate)
            else:
                operation = self._add_op_to_config(gate, "compensation", amplitude=0.25, length=duration)
                compensation_amp = declare(fixed)
                eval_average_power = declare(int)
                assign(eval_average_power, self.average_power[i])
                assign(compensation_amp, -Cast.mul_fixed_by_int(1 / duration, eval_average_power))
                play(operation * amp((compensation_amp - self.current_level[i]) * 4), gate)
            self.current_level[i] = compensation_amp

    def ramp_to_zero(self, duration: int = None):
        """Ramp all the gate voltages down to zero Volt and reset the averaged voltage derived for defining the compensation pulse.

        :param duration: How long will it take for the voltage to ramp down to 0V in clock cycles (4ns). If not
            provided, the default pulse duration defined in the configuration will be used.
        """
        for i, gate in enumerate(self._elements):
            ramp_to_zero(gate, duration)
            self.current_level[i] = 0
            self.average_power[i] = 0
        if self._expression is not None:
            assign(self._expression, 0)
        if self._expression2 is not None:
            assign(self._expression2, 0)

    def add_points(self, name: str, coordinates: list, duration: int) -> None:
        """Register a relevant voltage point.

        :param name: Name of the voltage point.
        :param coordinates: Voltage value of each gate involved in the virtual gate in V.
        :param duration: How long should the voltages be maintained at this level in ns. Must be larger than 16ns and a multiple of 4ns.
        """
        self._voltage_points[name] = {}
        self._voltage_points[name]["coordinates"] = coordinates
        self._voltage_points[name]["duration"] = duration
