COMMON_OCTAVE_PREFIX = "__oct__"


class SavedVariablesNames:
    n_lo = "n_lo"
    n_image = "n_image"
    i_scan = "i_scan"
    q_scan = "q_scan"
    lo = "lo"
    g_scan = "g_scan"
    p_scan = "p_scan"
    image = "image"


class CalibrationElementsNames:
    def __init__(self, device_name: str, channel_index: int):
        self._device_name = device_name
        self._channel_index = channel_index

    @property
    def _element_prefix(self) -> str:
        return f"{COMMON_OCTAVE_PREFIX}{self._device_name}_{self._channel_index}_"

    @property
    def iq_mixer(self) -> str:
        return self._element_prefix + "IQmixer"

    @property
    def i_offset(self) -> str:
        return self._element_prefix + "I_offset"

    @property
    def q_offset(self) -> str:
        return self._element_prefix + "Q_offset"

    @property
    def signal_analyzer(self) -> str:
        return self._element_prefix + "signal_analyzer"

    @property
    def lo_analyzer(self) -> str:
        return self._element_prefix + "lo_analyzer"

    @property
    def image_analyzer(self) -> str:
        return self._element_prefix + "image_analyzer"
