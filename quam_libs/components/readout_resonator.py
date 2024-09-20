from quam.core import quam_dataclass
from quam.components.channels import InOutIQChannel, InOutMWChannel
from qualang_tools.units import unit
import numpy as np

__all__ = ["ReadoutResonator", "ReadoutResonatorIQ", "ReadoutResonatorMW"]


@quam_dataclass
class ReadoutResonatorBase:
    """QuAM component for a readout resonator

    Args:
        depletion_time (int): the resonator depletion time in ns.
        frequency_bare (int, float): the bare resonator frequency in Hz.
    """

    depletion_time: int = 5000
    frequency_bare: float = None

    f_01: float = None
    f_12: float = None
    confusion_matrix: list = None
    
    gef_centers : list = None
    gef_confusion_matrix : list = None


@quam_dataclass
class ReadoutResonatorIQ(InOutIQChannel, ReadoutResonatorBase):
    time_of_flight = 28  # smallest deviation from default (24ns) to work with Qualibrate

    @property
    def upconverter_frequency(self):
        return self.LO_frequency

    def set_output_power(self, operation, power_dBm, amplitude=None, gain_or_full_scale_power_dbm=None, Z=50):
        u = unit(coerce_to_integer=True)
        if amplitude is not None:
            self.operations[operation].amplitude = amplitude
            if not -0.5 <= self.operations[operation].amplitude < 0.5:
                raise ValueError("The OPX+ pulse amplitude must be within [-0.5, 0.5) V.")
            self.frequency_converter_up.gain = round((power_dBm - u.volts2dBm(amplitude, Z=Z)) * 2) / 2
            print(f"Setting the Octave gain to {self.frequency_converter_up.gain} dB")
            if not -20 <= self.frequency_converter_up.gain <= 20:
                raise ValueError("The Octave gain must be within [-20:0.5:20] dB.")
        elif gain_or_full_scale_power_dbm is not None:
            self.frequency_converter_up.gain = gain_or_full_scale_power_dbm
            if not -20 <= self.frequency_converter_up.gain <= 20:
                raise ValueError("The Octave gain must be within [-20:0.5:20] dB.")
            self.operations[operation].amplitude = u.dBm2volts(power_dBm - self.frequency_converter_up.gain)
            print(f"Setting the {operation} amplitude to {self.operations[operation].amplitude} V")
            if not -0.5 <= self.operations[operation].amplitude < 0.5:
                raise ValueError("The OPX+ pulse amplitude must be within [-0.5, 0.5) V.")
        else:
            raise RuntimeError("Either amplitude or gain_or_full_scale_power_dbm must be specified.")

    def get_output_power(self, operation, Z=50) -> float:
        u = unit(coerce_to_integer=True)
        amplitude = self.operations[operation].amplitude
        return self.frequency_converter_up.gain + u.volts2dBm(amplitude, Z=Z)

@quam_dataclass
class ReadoutResonatorMW(InOutMWChannel, ReadoutResonatorBase):
    time_of_flight = 28

    @property
    def upconverter_frequency(self):
        return self.opx_output.upconverter_frequency

    def set_output_power(self, operation, power_dBm, amplitude=None, gain_or_full_scale_power_dbm=None):
        if amplitude is not None:
            self.operations[operation].amplitude = amplitude
            if not -0.5 <= self.operations[operation].amplitude < 0.5:
                raise ValueError("The OPX1000 pulse amplitude must be within [-1, 1] V.")
            self.opx_output.full_scale_power_dbm = round(power_dBm - 20*np.log10(amplitude))
            print(f"Setting the full_scale_power_dbm {self.opx_output.full_scale_power_dbm} dBm")
            if not -41 <= self.opx_output.full_scale_power_dbm <= 10:
                raise ValueError("The OPX1000 full_scale_power_dbm must be within [-41:3:10] dB.")
        elif gain_or_full_scale_power_dbm is not None:
            self.opx_output.full_scale_power_dbm = gain_or_full_scale_power_dbm
            if not -41 <= self.opx_output.full_scale_power_dbm <= 10:
                raise ValueError("The OPX1000 full_scale_power_dbm must be within [-41:3:10] dB.")
            self.operations[operation].amplitude = 10**((power_dBm - self.opx_output.full_scale_power_dbm) / 20)
            print(f"Setting the {operation} amplitude to {self.operations[operation].amplitude} V")
            if not -0.5 <= self.operations[operation].amplitude < 0.5:
                raise ValueError("The OPX1000 pulse amplitude must be within [-1, 1] V.")
        else:
            raise RuntimeError("Either amplitude or gain_or_full_scale_power_dbm must be specified.")

    def get_output_power(self, operation, Z=50) -> float:
        amplitude = self.operations[operation].amplitude
        power = self.opx_output.full_scale_power_dbm
        x_mw = 10 ** (power / 10)
        x_v = amplitude * np.sqrt(2 * Z * x_mw / 1000)
        return 10 * np.log10(((x_v / np.sqrt(2)) ** 2 * 1000) / Z)

ReadoutResonator = ReadoutResonatorIQ

