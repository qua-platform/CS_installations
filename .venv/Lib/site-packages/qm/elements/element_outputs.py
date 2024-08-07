from typing import Optional

from octave_sdk.octave import RFInput
from octave_sdk import IFMode, RFInputLOSource, RFInputRFSource


class ElementOutput:
    pass


class NoOutput(ElementOutput):
    pass


class DownconvertedOutput(ElementOutput):
    def __init__(self, client: RFInput):
        self._client = client

    def set_downconversion(
        self,
        lo_source: RFInputLOSource,
        lo_frequency: Optional[float] = None,
        if_mode_i: IFMode = IFMode.direct,
        if_mode_q: IFMode = IFMode.direct,
    ) -> None:
        """
        Sets the LO source for the downconverters.
        The LO source will be the one associated with the upconversion of element

        :param lo_source:
        :param lo_frequency:
        :param if_mode_i:
        :param if_mode_q:
        """
        self._set_downconversion_lo(lo_source, lo_frequency)
        self._set_downconversion_if_mode(if_mode_i, if_mode_q)

    def _set_downconversion_lo(
        self,
        lo_source: RFInputLOSource,
        lo_frequency: Optional[float] = None,
    ) -> None:
        """
        Sets the LO source for the downconverters.
        If no value is given the LO source will be the one associated with the
        upconversion of element

        :param lo_frequency:
        :param lo_source:
        """
        self._client.set_lo_source(lo_source, ignore_shared_errors=True)
        self._client.set_rf_source(RFInputRFSource.RF_in)
        is_internal = lo_source in {RFInputLOSource.Internal, RFInputLOSource.Analyzer}

        if lo_frequency is not None and is_internal:
            self._client.set_lo_frequency(source_name=lo_source, frequency=lo_frequency)

    def _set_downconversion_if_mode(self, if_mode_i: IFMode = IFMode.direct, if_mode_q: IFMode = IFMode.direct) -> None:
        self._client.set_if_mode_i(if_mode_i)
        self._client.set_if_mode_q(if_mode_q)
