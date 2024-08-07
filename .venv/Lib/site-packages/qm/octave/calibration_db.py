import time
import logging
from pathlib import Path
from dataclasses import asdict, dataclass
from typing import Dict, Tuple, Union, Optional, cast

import numpy as np
from tinydb.table import Document
from tinydb import Query, TinyDB, where
from tinydb.storages import JSONStorage

from qm.type_hinting.general import Number
from qm.octave.octave_mixer_calibration import MixerCalibrationResults

logger = logging.getLogger(__name__)
Correction = Tuple[float, float, float, float]


def convert_to_correction(gain: float, phase: float) -> Correction:
    s = phase
    c = np.polyval([-3.125, 1.5, 1], s**2)
    g_plus = np.polyval([0.5, 1, 1], gain)
    g_minus = np.polyval([0.5, -1, 1], gain)

    c00 = float(g_plus * c)
    c01 = float(g_plus * s)
    c10 = float(g_minus * s)
    c11 = float(g_minus * c)

    return c00, c01, c10, c11


@dataclass
class _Mode:
    octave_name: str
    octave_channel: int


@dataclass
class _LOMode:
    mode_id: int
    lo_freq: float
    gain: Optional[float]
    latest: int


@dataclass
class _IFMode:
    lo_mode_id: int
    if_freq: float
    latest: int


@dataclass
class LOCalibrationDBSchema:
    i0: float
    q0: float
    lo_mode_id: int
    dc_gain: float
    dc_phase: float
    temperature: float
    timestamp: float
    method: str

    @property
    def dc_correction(self) -> Correction:
        return convert_to_correction(self.dc_gain, self.dc_phase)


@dataclass
class IFCalibrationDBSchema:
    if_mode_id: int
    gain: float
    phase: float
    temperature: float
    timestamp: float
    method: str

    @property
    def correction(self) -> Correction:
        return convert_to_correction(self.gain, self.phase)


class ModeNotFoundError(KeyError):
    def __init__(self, query: Tuple[Union[str, Number], ...]):
        self._query = query

    def __str__(self) -> str:
        return f"Didn't find mode for {self._query}"


class CalibrationDB:
    def __init__(self, path: Union[Path, str]) -> None:
        self._file_path: Path = Path(path) / "calibration_db.json"
        self._db = TinyDB(self._file_path, indent=4, separators=(",", ": "), storage=JSONStorage)

    def __del__(self) -> None:
        self._db.close()

    def reset(self) -> None:
        self._db.close()

        self._file_path.unlink()
        self._db = TinyDB(self._file_path, indent=4, separators=(",", ": "), storage=JSONStorage)

    @property
    def file_path(self) -> str:
        return str(self._file_path)

    def _query_mode(self, octave_channel: Tuple[str, int]) -> Optional[Document]:
        return cast(
            Optional[Document],
            self._db.table("modes").get(
                (Query().octave_name == octave_channel[0]) & (Query().octave_channel == octave_channel[1])
            ),
        )

    def _get_timestamp(self, doc: Document) -> float:
        a = cast(Document, self._db.table("lo_cal").get(doc_id=doc["latest"]))
        return cast(float, a["timestamp"])

    def _query_lo_mode(self, mode_id: int, lo_freq: Number, gain: Optional[float]) -> Optional[Document]:
        if gain is not None:
            return cast(
                Optional[Document],
                self._db.table("lo_modes").get(
                    (Query().mode_id == mode_id) & (Query().lo_freq == lo_freq) & (Query().gain == gain)
                ),
            )

        lo_modes = self._db.table("lo_modes").search((Query().mode_id == mode_id) & (Query().lo_freq == lo_freq))
        if not lo_modes:
            return None

        return max(lo_modes, key=self._get_timestamp)

    def query_if_mode(self, lo_mode_id: int, if_freq: float) -> Optional[Document]:
        return cast(
            Optional[Document],
            self._db.table("if_modes").get((Query().lo_mode_id == lo_mode_id) & (Query().if_freq == if_freq)),
        )

    def _mode_id(self, octave_channel: Tuple[str, int], create: bool = False) -> int:
        query_result = self._query_mode(octave_channel)
        if query_result is None:
            if create:
                return self._db.table("modes").insert(asdict(_Mode(*octave_channel)))
            raise ModeNotFoundError(octave_channel)
        else:
            return query_result.doc_id

    def _lo_mode_id(self, mode_id: int, lo_freq: Number, gain: Optional[float], create: bool = False) -> int:
        query_result = self._query_lo_mode(mode_id, lo_freq, gain)
        if query_result is None:
            if create:
                return self._db.table("lo_modes").insert(asdict(_LOMode(mode_id, lo_freq, gain, 0)))
            else:
                raise ModeNotFoundError((mode_id, lo_freq))
        else:
            return query_result.doc_id

    def _if_mode_id(self, lo_mode_id: int, if_freq: float, create: bool = False) -> int:
        query_result = self.query_if_mode(lo_mode_id, if_freq)
        if query_result is None:
            if create:
                return self._db.table("if_modes").insert(asdict(_IFMode(lo_mode_id, if_freq, 0)))
            else:
                raise ModeNotFoundError((lo_mode_id, if_freq))
        else:
            return query_result.doc_id

    def update_lo_calibration(
        self,
        octave_channel: Tuple[str, int],
        lo_freq: float,
        gain: Optional[float],
        i0: float,
        q0: float,
        dc_gain: float,
        dc_phase: float,
        temperature: float,
        method: str = "",
    ) -> None:

        mode_id = self._mode_id(octave_channel, create=True)
        lo_mode_id = self._lo_mode_id(mode_id, lo_freq, gain, create=True)

        timestamp = time.time()

        lo_cal_id = self._db.table("lo_cal").insert(
            asdict(LOCalibrationDBSchema(i0, q0, lo_mode_id, dc_gain, dc_phase, temperature, timestamp, method))
        )

        self._db.table("lo_modes").update(asdict(_LOMode(mode_id, lo_freq, gain, lo_cal_id)), doc_ids=[lo_mode_id])

    def update_if_calibration(
        self,
        octave_channel: Tuple[str, int],
        lo_freq: float,
        output_gain: Optional[float],
        if_freq: float,
        gain: float,
        phase: float,
        temperature: float,
        method: str = "",
    ) -> None:

        mode_id = self._mode_id(octave_channel, create=True)
        lo_mode_id = self._lo_mode_id(mode_id, lo_freq, output_gain, create=True)
        if_mode_id = self._if_mode_id(lo_mode_id, if_freq, create=True)

        timestamp = time.time()
        if_cal_id = self._db.table("if_cal").insert(
            asdict(IFCalibrationDBSchema(if_mode_id, gain, phase, temperature, timestamp, method))
        )

        self._db.table("if_modes").update(asdict(_IFMode(lo_mode_id, if_freq, if_cal_id)), doc_ids=[if_mode_id])

    def get_lo_cal(
        self, octave_channel: Tuple[str, int], lo_freq: float, gain: Optional[float]
    ) -> Optional[LOCalibrationDBSchema]:
        try:
            mode_id = self._mode_id(octave_channel)
        except ModeNotFoundError:
            return None
        lo_mode = self._query_lo_mode(mode_id, lo_freq, gain)
        if lo_mode is None or lo_mode["latest"] == 0:
            return None

        lo_cal = cast(Optional[Document], self._db.table("lo_cal").get(doc_id=lo_mode["latest"]))
        if lo_cal is None:
            return None

        lo_cal_obj = LOCalibrationDBSchema(**lo_cal)

        return lo_cal_obj

    def get_if_cal(
        self, octave_channel: Tuple[str, int], lo_freq: Number, gain: Optional[float], if_freq: Number
    ) -> Optional[IFCalibrationDBSchema]:
        try:
            mode_id = self._mode_id(octave_channel, create=False)
            lo_mode_id = self._lo_mode_id(mode_id, lo_freq, gain, create=False)
            if_mode = self.query_if_mode(lo_mode_id, if_freq)
        except ModeNotFoundError:
            return None

        if if_mode is None or if_mode["latest"] == 0:
            return None

        if_cal = self._db.table("if_cal").get(doc_id=if_mode["latest"])
        if if_cal is None:
            return None
        assert isinstance(if_cal, dict)
        if_cal_obj = IFCalibrationDBSchema(**if_cal)

        return if_cal_obj

    def get_all_if_cal_for_lo(
        self, octave_channel: Tuple[str, int], lo_freq: float, gain: Optional[float]
    ) -> Dict[Number, IFCalibrationDBSchema]:
        try:
            mode_id = self._mode_id(octave_channel)
            lo_mode_id = self._lo_mode_id(mode_id, lo_freq, gain)
        except ModeNotFoundError:
            return {}

        if_modes = self._db.table("if_modes").search(where("lo_mode_id") == lo_mode_id)

        if if_modes is None:
            return {}

        if_dict: Dict[Number, IFCalibrationDBSchema] = {}
        for if_mode in if_modes:
            if_freq = if_mode["if_freq"]
            if_cal = self.get_if_cal(octave_channel, lo_freq, gain, if_freq)

            if if_cal:
                if_dict[if_freq] = if_cal

        return if_dict

    def update_calibration_result(
        self, result: MixerCalibrationResults, octave_channel: Tuple[str, int], method: str = ""
    ) -> None:

        for (lo_freq, output_gain), lo_cal in result.items():
            self.update_lo_calibration(
                octave_channel,
                lo_freq,
                output_gain,
                lo_cal.i0,
                lo_cal.q0,
                lo_cal.dc_gain,
                lo_cal.dc_phase,
                lo_cal.temperature,
                method,
            )

            for if_freq, if_cal in lo_cal.image.items():
                fine_cal = if_cal.fine
                self.update_if_calibration(
                    octave_channel,
                    lo_freq,
                    output_gain,
                    if_freq,
                    fine_cal.gain,
                    fine_cal.phase,
                    lo_cal.temperature,
                    method,
                )
