from typing import Dict, Any, Union, Optional, Literal, Tuple
from dataclasses import field
from logging import getLogger

from quam.core import quam_dataclass
from quam.components.channels import IQChannel, MWChannel, Pulse
from quam import QuamComponent
from .components import TankCircuit, XYDrive, QDAC_trigger, PlungerGate

from qm import QuantumMachine, logger
from qm.qua import (
    save,
    align,
    declare,
    fixed,
    assign,
    wait,
    while_,
    StreamType,
    if_,
    update_frequency,
    Math,
    Cast,
)

try:
    from qm.qua.type_hints import QuaVariable

    QuaVariableBool = QuaVariable[bool]
except ImportError:
    from qm.qua._dsl import QuaVariableType as QuaVariableBool

__all__ = ["Qubit"]


@quam_dataclass
class Qubit(QuamComponent):
    """
    Example QUAM component for a transmon qubit.

    Attributes:
        id (Union[int, str]): The id of the Transmon, used to generate the name.
            Can be a string, or an integer in which case it will add `Channel._default_label`.
        xy (Union[MWChannel, IQChannel]): The xy drive component.
        resonator (Union[ReadoutResonatorIQ, ReadoutResonatorMW]): The readout resonator component.
        f_01 (float): The 0-1 transition frequency in Hz.
        f_12 (float): The 1-2 transition frequency in Hz.
        anharmonicity (int): The transmon anharmonicity in Hz. Default is 150e6.
        T1 (float): The transmon T1 in seconds. Default is 10e-6.
        T2ramsey (float): The transmon T2* in seconds.
        T2echo (float): The transmon T2 in seconds.
        thermalization_time_factor (int): Thermalization time in units of T1. Default is 5.
        sigma_time_factor (int): Sigma time factor for pulse shaping. Default is 5.
        GEF_frequency_shift (int): The frequency shift for the GEF states. Default is 10.
        chi (float): The dispersive shift in Hz. Default is 0.0.
        grid_location (str): Qubit location in the plot grid as "(column, row)".
        extras (Dict[str, Any]): Additional attributes for the transmon.

    Methods:
        name: Returns the name of the transmon.
        inferred_f_12: Returns the 0-2 (e-f) transition frequency in Hz, derived from f_01 and anharmonicity.
        inferred_anharmonicity: Returns the transmon anharmonicity in Hz, derived from f_01 and f_12.
        sigma: Returns the sigma value for a given pulse.
        thermalization_time: Returns the transmon thermalization time in ns.
        calibrate_octave: Calibrates the Octave channels (xy and resonator) linked to this transmon.
        set_gate_shape: Sets the shape of the single qubit gates.
        readout_state: Performs a readout of the qubit state using the specified pulse.
        reset_qubit: Reset the qubit to the ground state ('g') with the specified method.
        reset_qubit_thermal: Reset the qubit to the ground state ('g') using thermalization.
        reset_qubit_active: Reset the qubit to the ground state ('g') using active reset.
        reset_qubit_active_gef: Reset the qubit to the ground state ('g') using active reset with GEF state readout.
        readout_state_gef: Perform a GEF state readout using the specified pulse and update the state variable.
    """

    id: Union[int, str]

    xy: XYDrive = None
    qdac_trigger: QDAC_trigger = None
    resonator: TankCircuit = None
    p1: PlungerGate = None
    p2: PlungerGate = None

    f_01: float = None
    f_12: float = None
    anharmonicity: float = None

    T1: float = None
    T2ramsey: float = None
    T2echo: float = None
    thermalization_time_factor: int = 5
    sigma_time_factor: int = 5

    grid_location: str = None
    gate_fidelity: Dict[str, Any] = field(default_factory=dict)
    extras: Dict[str, Any] = field(default_factory=dict)

    @property
    def name(self):
        """The name of the transmon"""
        return self.id if isinstance(self.id, str) else f"q{self.id}"

    @property
    def thermalization_time(self):
        """The transmon thermalization time in ns."""
        if self.T1 is not None:
            return int(self.thermalization_time_factor * self.T1 * 1e9 / 4) * 4
        else:
            return int(self.thermalization_time_factor * 10e-6 * 1e9 / 4) * 4

    def readout_state(
        self, state, pulse_name: str = "readout", threshold: float = None
    ):
        """
        Perform a readout of the qubit state using the specified pulse.

        This function measures the qubit state using the specified readout pulse and assigns the result to the given state variable.
        If no threshold is provided, the default threshold for the specified pulse is used.

        Args:
            state: The variable to assign the readout result to.
            pulse_name (str): The name of the readout pulse to use. Default is "readout".
            threshold (float, optional): The threshold value for the readout. If None, the default threshold for the pulse is used.

        Returns:
            None

        The function declares fixed variables I and Q, measures the qubit state using the specified pulse, and assigns the result to the state variable based on the threshold.
        It then waits for the resonator depletion time.
        """
        I = declare(fixed)
        Q = declare(fixed)
        if threshold is None:
            threshold = self.resonator.operations[pulse_name].threshold
        self.resonator.measure(pulse_name, qua_vars=(I, Q))
        assign(state, Cast.to_int(I > threshold))
        wait(self.resonator.depletion_time // 4, self.resonator.name)

    def reset_qubit_thermal(self):
        """
        Perform a thermal reset of the qubit.

        This function waits for a duration specified by the thermalization time
        to allow the qubit to return to its ground state through natural thermal
        relaxation.
        """
        self.wait(self.thermalization_time // 4)

    def align(self):
        align(self.resonator.name, self.xy.name)
