import base64
import logging
import os.path
import datetime
import dataclasses
from copy import deepcopy
from dataclasses import dataclass
from collections import defaultdict
from abc import ABCMeta, abstractmethod
from typing import (
    Any,
    Set,
    Dict,
    List,
    Type,
    Tuple,
    Union,
    Mapping,
    TypeVar,
    Callable,
    Optional,
    Protocol,
    Sequence,
    cast,
)

import numpy as np
import plotly.colors  # type: ignore[import-untyped]
import plotly.graph_objects as go  # type: ignore[import-untyped]

from qm.results.simulator_samples import SimulatorSamples, SimulatorControllerSamples
from qm.type_hinting.simulator_types import (
    IqInfoType,
    ChirpInfoType,
    AdcAcquisitionType,
    PlayedWaveformType,
    PulserLocationType,
    WaveformReportType,
    PlayedAnalogWaveformType,
)


class HasPortsProtocol(Protocol):
    @property
    def ports(self) -> List[int]:
        raise NotImplementedError

    @property
    def controller(self) -> str:
        raise NotImplementedError

    @property
    def fem(self) -> int:
        raise NotImplementedError

    @property
    def element(self) -> str:
        raise NotImplementedError


T = TypeVar("T", bound="PlayedWaveform")


@dataclass(frozen=True)
class PlayedWaveform(metaclass=ABCMeta):
    waveform_name: str
    pulse_name: str
    length: int
    timestamp: int
    iq_info: IqInfoType
    element: str
    output_ports: List[int]
    controller: str
    pulser: Dict[str, Any]
    fem: int

    @staticmethod
    def _build_initialization_dict(
        dict_description: PlayedWaveformType, formatted_attribute_dict: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        attribute_dict: Dict[str, Any]
        if formatted_attribute_dict is None:
            attribute_dict = {}
        else:
            attribute_dict = deepcopy(formatted_attribute_dict)

        attribute_dict.update(
            pulse_name=dict_description["pulseName"],
            waveform_name=dict_description["waveformName"],
            timestamp=int(dict_description["timestamp"]),
            length=int(dict_description["length"]),
            iq_info=dict_description["iqInfo"],
            element=dict_description["quantumElements"],
            output_ports=[int(p) for p in dict_description["outputPorts"]],
            pulser=dict_description["pulser"],
            controller=dict_description["pulser"]["controllerName"],
            fem=int(dict_description["pulser"].get("femId", 0)) + 1,
        )
        return attribute_dict

    @classmethod
    def from_job_dict(cls: Type[T], dict_description: PlayedWaveformType) -> T:
        return cls(**cls._build_initialization_dict(dict_description))

    @property
    def ports(self) -> List[int]:
        return self.output_ports

    @property
    def is_iq(self) -> bool:
        return self.iq_info["isPartOfIq"]

    @property
    def is_I_pulse(self) -> bool:
        return self.iq_info["isI"]

    @property
    def get_iq_association(self) -> str:
        if not self.is_iq:
            return ""
        return "I" if self.is_I_pulse else "Q"

    @property
    def ends_at(self) -> int:
        return self.timestamp + self.length

    @abstractmethod
    def to_string(self) -> str:
        return ""

    def __str__(self) -> str:
        return self.to_string()

    def to_dict(self) -> Dict[str, Any]:
        return dataclasses.asdict(self)

    def _common_attributes_to_printable_str_list(self) -> List[str]:
        waveform_type_string = "Type="
        if self.is_iq:
            waveform_type_string += f"IQ Type ({'I' if self.iq_info['isI'] else 'Q'})"
        else:
            waveform_type_string += "Single"
        return [
            f"Waveform Name={self.waveform_name}",
            f"Pulse name={remove_prefix(self.pulse_name, 'OriginPulseName=')}",
            f"Start Time={self.timestamp} ns",
            f"Length={self.length} ns",
            f"Element={self.element}",
            f"Output Ports={self.output_ports}",
            waveform_type_string,
        ]


# str.removeprefix exists only for python 3.9+, this is here for backward compatibility
def remove_prefix(text: str, prefix: str) -> str:
    if text.startswith(prefix):
        return text[len(prefix) :]
    return text


def format_float(f: float) -> str:
    return "{:.3f}".format(f)


def pretty_string_freq(f: float) -> str:
    if f < 1000:
        div, units = 1.0, "Hz"
    elif 1000 <= f < 1_000_000:
        div, units = 1000.0, "kHz"
    else:
        div, units = 1e6, "MHz"
    return f"{format_float(f / div).rstrip('0').rstrip('.')}{units}"


@dataclass(frozen=True)
class PlayedAnalogWaveform(PlayedWaveform):
    current_amp_elements: List[float]
    current_dc_offset_by_port: Dict[str, float]
    current_intermediate_frequency: float
    current_frame: List[float]
    current_correction_elements: List[float]
    chirp_info: Optional[ChirpInfoType]
    current_phase: float

    @classmethod
    def from_job_dict(cls: Type[T], dict_description: PlayedWaveformType) -> T:
        dict_description = cast(PlayedAnalogWaveformType, dict_description)
        pulse_chirp_info = dict_description["chirpInfo"]
        is_pulse_have_chirp = len(pulse_chirp_info["units"]) > 0 or len(pulse_chirp_info["rate"]) > 0
        formatted_attribute_list = dict(
            current_amp_elements=dict_description["currentGMatrixElements"],
            current_dc_offset_by_port=dict_description["currentDCOffsetByPort"],
            current_intermediate_frequency=dict_description["currentIntermediateFrequency"],
            current_frame=dict_description["currentFrame"],
            current_correction_elements=dict_description["currentCorrectionElements"],
            chirp_info=pulse_chirp_info if is_pulse_have_chirp else None,
            current_phase=dict_description.get("currentPhase", 0),
        )
        return cls(**cls._build_initialization_dict(dict_description, formatted_attribute_list))

    def to_custom_string(self, show_chirp: bool = True) -> str:
        _attributes = super()._common_attributes_to_printable_str_list()
        _attributes += (
            [
                f"{k}={v if self.is_iq else v[0]}"
                for k, v in [
                    ("Amplitude Values", [format_float(f) for f in self.current_amp_elements]),
                    ("Frame Values", [format_float(f) for f in self.current_frame]),
                    ("Correction Values", [format_float(f) for f in self.current_correction_elements]),
                ]
            ]
            + [
                f"Intermediate Frequency={pretty_string_freq(self.current_intermediate_frequency)}",
                f"Current DC Offset (By output ports)={ {k: format_float(v) for k, v in self.current_dc_offset_by_port.items()} }",
                f"Current Phase={format_float(self.current_phase)},",
            ]
            + ([] if (self.chirp_info is None or not show_chirp) else [f"chirp_info={self.chirp_info}"])
        )
        s = "AnalogWaveform(" + ("\n" + len("AnalogWaveform(") * " ").join(_attributes) + ")"
        return s

    def to_string(self) -> str:
        return self.to_custom_string()


@dataclass(frozen=True)
class PlayedDigitalWaveform(PlayedWaveform):
    @classmethod
    def from_job_dict(cls: Type[T], dict_description: PlayedWaveformType) -> T:
        return cls(**cls._build_initialization_dict(dict_description))

    def to_string(self) -> str:
        s = (
            "DigitalWaveform("
            + ("\n" + len("DigitalWaveform(") * " ").join(self._common_attributes_to_printable_str_list())
            + ")"
        )
        return s


@dataclass(frozen=True)
class AdcAcquisition:
    start_time: int
    end_time: int
    process: str
    pulser: PulserLocationType
    quantum_element: str
    adc_ports: List[int]
    controller: str
    fem: int
    element: str

    @classmethod
    def from_job_dict(cls, dict_description: AdcAcquisitionType) -> "AdcAcquisition":
        return cls(
            start_time=int(dict_description["startTime"]),
            end_time=int(dict_description["endTime"]),
            process=dict_description["process"],
            pulser=dict_description["pulser"],
            quantum_element=dict_description["quantumElement"],
            adc_ports=[int(p) + 1 for p in dict_description["adc"]],
            controller=dict_description["pulser"]["controllerName"],
            fem=int(dict_description["pulser"].get("femId", 0)) + 1,
            element=dict_description["quantumElement"],
        )

    @property
    def ports(self) -> List[int]:
        return self.adc_ports

    def to_string(self) -> str:
        return (
            "AdcAcquisition("
            + ("\n" + len("AdcAcquisition(") * " ").join(
                [
                    f"start_time={self.start_time}",
                    f"end_time={self.end_time}",
                    f"process={self.process}",
                    f"element={self.quantum_element}",
                    f"input_ports={self.adc_ports}",
                ]
            )
            + ")"
        )

    def to_dict(self) -> Dict[str, Any]:
        return dataclasses.asdict(self)


@dataclass
class FemToWaveformMap:
    analog_out: Dict[int, List[PlayedAnalogWaveform]]
    digital_out: Dict[int, List[PlayedDigitalWaveform]]
    analog_in: Dict[int, List[AdcAcquisition]]


class _SingleControllerMapping(Dict[int, FemToWaveformMap]):
    @property
    def num_analog_out_ports(self) -> int:
        return len(self.flat_analog_out)

    @property
    def num_digital_out_ports(self) -> int:
        return len(self.flat_digital_out)

    @property
    def num_analog_in_ports(self) -> int:
        return len(self.flat_analog_in)

    @property
    def flat_analog_out(self) -> Dict[str, List[PlayedAnalogWaveform]]:
        return {f"{fem_idx}-{port_idx}": v for fem_idx, fem in self.items() for port_idx, v in fem.analog_out.items()}

    @property
    def flat_digital_out(self) -> Dict[str, List[PlayedDigitalWaveform]]:
        return {f"{fem_idx}-{port_idx}": v for fem_idx, fem in self.items() for port_idx, v in fem.digital_out.items()}

    @property
    def flat_analog_in(self) -> Dict[str, List[AdcAcquisition]]:
        return {f"{fem_idx}-{port_idx}": v for fem_idx, fem in self.items() for port_idx, v in fem.analog_in.items()}


@dataclass(frozen=True)
class WaveformReport:
    job_id: Union[int, str]
    analog_waveforms: List[PlayedAnalogWaveform]
    digital_waveforms: List[PlayedDigitalWaveform]
    adc_acquisitions: List[AdcAcquisition]

    @classmethod
    def from_dict(cls, d: WaveformReportType, job_id: Union[int, str] = -1) -> "WaveformReport":
        return cls(
            analog_waveforms=[PlayedAnalogWaveform.from_job_dict(awf) for awf in d["analogWaveforms"]],
            digital_waveforms=[PlayedDigitalWaveform.from_job_dict(dwf) for dwf in d["digitalWaveforms"]],
            adc_acquisitions=[AdcAcquisition.from_job_dict(acq) for acq in d.get("adcAcquisitions", [])],
            job_id=job_id,
        )

    @property
    def waveforms(self) -> Sequence[PlayedWaveform]:
        return cast(List[PlayedWaveform], self.analog_waveforms) + cast(List[PlayedWaveform], self.digital_waveforms)

    @property
    def controllers_in_use(self) -> Sequence[str]:
        return sorted(self.fems_in_use_by_controller)

    @property
    def elements_in_report(self) -> Sequence[str]:
        wf_elements = {wf.element for wf in self.waveforms}
        adc_elements = {adc.element for adc in self.adc_acquisitions}
        return sorted(wf_elements | adc_elements)

    @property
    def fems_in_use_by_controller(self) -> Mapping[str, Sequence[int]]:
        fems_in_use = defaultdict(set)
        for ap in self.waveforms:
            fems_in_use[ap.controller].add(ap.fem)
        for adc in self.adc_acquisitions:
            fems_in_use[adc.controller].add(adc.fem)
        return {k: sorted(v) for k, v in fems_in_use.items()}

    @property
    def num_controllers_in_use(self) -> int:
        return len(self.controllers_in_use)

    def to_string(self) -> str:
        """
        Dumps the report into a (pretty-print) string.

        return: str
        """
        waveforms_str = [wf.to_string() for wf in self.waveforms]
        adc_string = [adc.to_string() for adc in self.adc_acquisitions]
        return "\n".join(waveforms_str + adc_string)

    def _transform_report_by_func(self, func: Callable[[HasPortsProtocol], bool]) -> "WaveformReport":
        return WaveformReport(
            analog_waveforms=list(filter(func, self.analog_waveforms)),
            digital_waveforms=list(filter(func, self.digital_waveforms)),
            adc_acquisitions=list(filter(func, self.adc_acquisitions)),
            job_id=self.job_id,
        )

    def report_by_controllers(self) -> Mapping[str, "WaveformReport"]:
        def create_filter_func(controller: str) -> Callable[[HasPortsProtocol], bool]:
            return lambda r: r.controller == controller

        by_controller_map: Dict[str, "WaveformReport"] = {}
        for con_name in self.controllers_in_use:
            con_filter = create_filter_func(con_name)
            by_controller_map[con_name] = self._transform_report_by_func(con_filter)

        return by_controller_map

    def report_by_elements(self) -> Mapping[str, "WaveformReport"]:
        def create_filter_func(_element: str) -> Callable[[HasPortsProtocol], bool]:
            return lambda r: r.element == _element

        by_element_map: Dict[str, "WaveformReport"] = {}
        for element in self.elements_in_report:
            element_filter = create_filter_func(element)
            by_element_map[element] = self._transform_report_by_func(element_filter)

        return by_element_map

    def report_by_controller_and_fems(self) -> Mapping[str, Mapping[int, "WaveformReport"]]:
        def create_filter_func(controller: str, _fem: int) -> Callable[[HasPortsProtocol], bool]:
            return lambda r: r.controller == controller and r.fem == _fem

        by_controller_fem_map: Dict[str, Dict[int, "WaveformReport"]] = {}
        for con_name in self.controllers_in_use:
            by_controller_fem_map[con_name] = {}
            for fem in self.fems_in_use_by_controller[con_name]:
                fem_filter = create_filter_func(con_name, fem)
                by_controller_fem_map[con_name][fem] = self._transform_report_by_func(fem_filter)

        return by_controller_fem_map

    def to_dict(self) -> Dict[str, Any]:
        """
        Dumps the report to a dictionary containing three keys:
            "analog_waveforms", "digital_waveforms", "acd_acquisitions".
        Each key holds the list of all the associate data.

        Returns:
            dict
        """
        return {
            "analog_waveforms": [awf.to_dict() for awf in self.analog_waveforms],
            "digital_waveforms": [dwf.to_dict() for dwf in self.digital_waveforms],
            "adc_acquisitions": [acq.to_dict() for acq in self.adc_acquisitions],
        }

    def _strict_get_report_by_output_ports(self) -> Mapping[str, _SingleControllerMapping]:
        report_by_controller_and_fem = self.report_by_controller_and_fems()
        result = {}
        for controller, fem_to_report_map in report_by_controller_and_fem.items():
            per_controller = {}
            for fem, report in fem_to_report_map.items():
                analog_out, digital_out, analog_in = defaultdict(list), defaultdict(list), defaultdict(list)
                for awf in report.analog_waveforms:
                    for p in awf.output_ports:
                        analog_out[p].append(awf)
                for dwf in report.digital_waveforms:
                    for p in dwf.output_ports:
                        digital_out[p].append(dwf)
                for adc in report.adc_acquisitions:
                    for p in adc.adc_ports:
                        analog_in[p].append(adc)
                per_controller[fem] = FemToWaveformMap(
                    analog_out=dict(analog_out), digital_out=dict(digital_out), analog_in=dict(analog_in)
                )
            result[controller] = _SingleControllerMapping(per_controller)
        return result

    def get_report_by_output_ports(
        self, on_controller: Optional[str] = None
    ) -> Union[Mapping[str, _SingleControllerMapping], _SingleControllerMapping]:
        result = self._strict_get_report_by_output_ports()
        if on_controller is None:
            if self.num_controllers_in_use == 1:
                return result[self.controllers_in_use[0]]
            else:
                return result
        else:
            return result[on_controller]

    def create_plot(
        self,
        samples: Optional[SimulatorSamples] = None,
        controllers: Optional[Sequence[str]] = None,
        plot: bool = True,
        save_path: Optional[str] = None,
    ) -> None:
        """Creates a plot describing the pulses from each element to each port.
        See arguments description for further options.

        Args:
            samples: The raw samples as generated from the simulator. If not given, the plot will be generated without it.
            controllers: list of controllers to generate the plot. Each controller output will be saved as a different
                        file. If not given, take all the controllers who participate in the program.
            plot: Show the plot at the end of this function call.
            save_path: Save the plot to the given location. None for not saving.

        Returns:
            None
        """
        if controllers is None:
            controllers = self.controllers_in_use

        report_by_controllers = self.report_by_controllers()
        for con_name, report in report_by_controllers.items():
            if con_name not in controllers:
                continue

            if samples is None:
                con_builder = _WaveformPlotBuilder(report, self.job_id)
            else:
                con_builder = _WaveformPlotBuilderWithSamples(report, samples[con_name], self.job_id)

            if save_path is not None:
                dirname = os.path.dirname(save_path)
                filename = f"waveform_report_{con_name}_{self.job_id}"
                con_builder.save(dirname, filename)
            if plot:
                con_builder.plot()


@dataclass
class _MaxParallelTracesPerRow:
    analog: Dict[str, int]
    digital: Dict[str, int]


class _WaveformPlotBuilder:
    def __init__(self, wf_report: WaveformReport, job_id: Union[int, str] = -1):
        self._report = wf_report
        if wf_report.num_controllers_in_use > 1:
            raise RuntimeError(
                f"Plot Builder does not support plotting more than 1 controllers, yet. {os.linesep}"
                "Please provide a report containing a single controller."
            )
        self._job_id = job_id
        self._figure = go.Figure()
        self._already_registered_qe: Set[str] = set()
        self._colormap = self._get_qe_colorscale(wf_report.elements_in_report)
        report_by_output_ports = cast(_SingleControllerMapping, wf_report.get_report_by_output_ports())
        self._max_parallel_traces_per_row = self._calculate_max_parallel_traces_per_row(report_by_output_ports)
        self._num_rows = self._get_num_rows(report_by_output_ports)

        self._report_by_output_ports = report_by_output_ports
        self._setup_figure(self._num_rows)
        self._add_data()
        self._update_extra_features()

    @property
    def _samples_factor(self) -> int:
        return 1

    @staticmethod
    def _get_qe_colorscale(qe_in_use: Sequence[str]) -> Dict[str, str]:
        n_colors = len(qe_in_use)
        samples = plotly.colors.qualitative.Pastel + plotly.colors.qualitative.Safe
        if n_colors > len(samples):
            samples += plotly.colors.sample_colorscale(
                "turbo",
                [n / (n_colors - len(samples)) for n in range(n_colors - len(samples))],
            )
        return dict(zip(qe_in_use, samples))

    @staticmethod
    def _calculate_max_parallel_traces_per_row(
        report_by_output_port: _SingleControllerMapping,
    ) -> _MaxParallelTracesPerRow:
        def calc_row(_waveform_list: Sequence[PlayedWaveform]) -> int:
            max_in_row = 0
            functional_ts = sorted(
                [(r.timestamp, 1) for r in _waveform_list] + [(r.ends_at, -1) for r in _waveform_list],
                key=lambda t: t[0],
            )
            for _, f in functional_ts:
                max_in_row = max(max_in_row, max_in_row + f)
            return max_in_row

        analog_traces_per_row = {}
        digital_traces_per_row = {}
        for fem_idx, report in report_by_output_port.items():
            for output_port, waveform_list in report.analog_out.items():
                analog_traces_per_row[f"{fem_idx}-{output_port}"] = calc_row(waveform_list)
            for output_port, digital_waveform_list in report.digital_out.items():
                digital_traces_per_row[f"{fem_idx}-{output_port}"] = calc_row(digital_waveform_list)

        return _MaxParallelTracesPerRow(analog=analog_traces_per_row, digital=digital_traces_per_row)

    def _get_num_rows(self, report_by_output_ports: _SingleControllerMapping) -> int:
        num_rows = report_by_output_ports.num_analog_out_ports + report_by_output_ports.num_digital_out_ports
        num_rows *= self._samples_factor
        num_rows += report_by_output_ports.num_analog_in_ports
        return num_rows

    @property
    def _num_output_rows(self) -> int:
        return self._num_rows - self._report_by_output_ports.num_analog_in_ports

    @property
    def _num_analog_rows(self) -> int:
        return self._report_by_output_ports.num_analog_out_ports * self._samples_factor

    @property
    def _num_digital_rows(self) -> int:
        return self._report_by_output_ports.num_digital_out_ports * self._samples_factor

    def _is_row_analog(self, r: int) -> bool:
        return 1 <= r <= self._num_analog_rows

    def _is_row_digital(self, r: int) -> bool:
        return self._num_analog_rows < r <= self._num_output_rows

    def _is_row_analog_input(self, r: int) -> bool:
        return self._num_output_rows < r <= self._num_rows

    @property
    def _xrange(self) -> int:
        return max(self._report.waveforms, key=lambda x: x.ends_at).ends_at + 100

    @staticmethod
    def _is_intersect(r1: Tuple[int, int], r2: Tuple[int, int]) -> bool:
        return (r1[0] <= r2[0] <= r1[1]) or (r1[0] <= r2[1] <= r1[1]) or (r2[0] < r1[0] and r2[1] > r1[1])

    @staticmethod
    def _get_hover_text(played_waveform: PlayedWaveform) -> str:
        waveform_desc = played_waveform.to_string()
        if isinstance(played_waveform, PlayedAnalogWaveform):
            if played_waveform.chirp_info is not None:
                waveform_desc = played_waveform.to_custom_string(False)
                s = (
                    f"rate={played_waveform.chirp_info['rate']},units={played_waveform.chirp_info['units']},"
                    f" times={played_waveform.chirp_info['times']}\n"
                    + f"start_freq={pretty_string_freq(played_waveform.chirp_info['startFrequency'])}, "
                    + f"end_freq={pretty_string_freq(played_waveform.chirp_info['endFrequency'])}"
                )

                waveform_desc = f"<b>Chirp Pulse</b>\n({s})\n" + waveform_desc
        return "%{x}ns<br>" + waveform_desc.replace("\n", "</br>") + "<extra></extra>"

    def _get_output_port_waveform_plot_data(
        self, port_played_waveforms: Sequence[PlayedWaveform], x_axis_name: str, max_in_row: int
    ) -> List[go.Scatter]:
        graph_data: List[go.Scatter] = []
        levels: List[Tuple[int, int]] = []
        diff_between_traces, start_y = (0.2, 1.2) if max_in_row <= 7 else (1.4 / max_in_row, 1.45)
        y_level = [start_y] * 3
        for wf in port_played_waveforms:
            x_axis_points = (wf.timestamp, wf.ends_at)
            num_intersections = len([l for l in levels if self._is_intersect(l, x_axis_points)])
            levels.append(x_axis_points)
            prev_y = start_y if num_intersections == 0 else y_level[0]
            y_level = [prev_y - diff_between_traces] * 3
            graph_data.append(
                go.Scatter(
                    x=[x_axis_points[0], sum(x_axis_points) // 2, x_axis_points[1]],
                    y=y_level,
                    mode="lines+markers+text",
                    text=[
                        "",
                        f"{remove_prefix(wf.pulse_name, 'OriginPulseName=')}"
                        + (f"({wf.get_iq_association})" if wf.is_iq else ""),
                        "",
                    ],
                    hovertemplate=self._get_hover_text(wf),
                    textfont=dict(size=10),
                    xaxis=x_axis_name,
                    name=wf.element,
                    legendgroup=wf.element,
                    showlegend=not (wf.element in self._already_registered_qe),
                    marker=dict(
                        line=dict(width=2, color=self._colormap[wf.element]),
                        symbol=["line-ns", "line-ew", "line-ns"],
                    ),
                    line=dict(color=self._colormap[wf.element], width=5),
                )
            )
            self._already_registered_qe.add(wf.element)

        return graph_data

    def _add_plot_data_for_analog_output_port(
        self, figure_row_number: int, output_port: str, port_waveforms: Sequence[PlayedWaveform]
    ) -> None:
        self._add_plot_data_for_port(
            figure_row_number, self._max_parallel_traces_per_row.analog[output_port], port_waveforms
        )

    def _add_plot_data_for_port(
        self, figure_row_number: int, _max_parallel_traces_per_row: int, port_waveforms: Sequence[PlayedWaveform]
    ) -> None:
        if len(port_waveforms) == 0:
            return

        x_axis_name = self._get_x_axis_name(figure_row_number)
        port_wf_plot = self._get_output_port_waveform_plot_data(
            port_waveforms,
            x_axis_name,
            max_in_row=_max_parallel_traces_per_row,
        )
        row_number = figure_row_number * self._samples_factor
        self._figure.add_traces(port_wf_plot, rows=row_number, cols=1)

    @staticmethod
    def _get_x_axis_name(figure_row_number: int) -> str:
        return f"x{figure_row_number}"

    def _add_plot_data_for_digital_output_port(
        self, figure_row_number: int, output_port: str, port_waveforms: Sequence[PlayedWaveform]
    ) -> None:
        self._add_plot_data_for_port(
            figure_row_number, self._max_parallel_traces_per_row.digital[output_port], port_waveforms
        )

    def _add_plot_data_for_adc_port(
        self,
        figure_row_number: int,
        adc_port_acquisitions: List[AdcAcquisition],
    ) -> None:
        graph_data: List[go.Scatter] = []
        levels: List[Tuple[int, int]] = []
        y_level = [1.2] * 3
        for adc in adc_port_acquisitions:
            x_axis_points = (adc.start_time, adc.end_time)
            num_intersections = len([l for l in levels if self._is_intersect(l, x_axis_points)])
            levels.append(x_axis_points)
            prev_y = 1.2 if num_intersections == 0 else y_level[0]
            y_level = [prev_y - 0.2] * 3
            graph_data.append(
                go.Scatter(
                    x=[x_axis_points[0], sum(x_axis_points) // 2, x_axis_points[1]],
                    y=y_level,
                    mode="lines+markers+text",
                    text=["", f"{adc.process}", ""],
                    textfont=dict(size=10),
                    hovertemplate="%{x}ns<br>" + adc.to_string().replace("\n", "</br>") + "<extra></extra>",
                    name=adc.quantum_element,
                    legendgroup=adc.quantum_element,
                    showlegend=not (adc.quantum_element in self._already_registered_qe),
                    marker=dict(
                        line=dict(width=2, color=self._colormap[adc.quantum_element]),
                        symbol=["line-ns", "line-ew", "line-ns"],
                    ),
                    line=dict(color=self._colormap[adc.quantum_element], width=5),
                )
            )
            self._already_registered_qe.add(adc.quantum_element)

        self._figure.add_traces(graph_data, rows=figure_row_number, cols=1)

    def _add_data(self) -> None:
        for figure_row_number, (output_port, port_waveforms_list) in enumerate(
            self._report_by_output_ports.flat_analog_out.items()
        ):
            self._add_plot_data_for_analog_output_port(figure_row_number + 1, output_port, port_waveforms_list)

        for (figure_row_number, (output_port, digital_port_waveforms_list)) in enumerate(
            self._report_by_output_ports.flat_digital_out.items()
        ):
            self._add_plot_data_for_digital_output_port(
                figure_row_number + self._report_by_output_ports.num_analog_out_ports + 1,
                output_port,
                digital_port_waveforms_list,
            )

        for figure_row_number, adc_acquisition_list in enumerate(self._report_by_output_ports.flat_analog_in.values()):
            self._add_plot_data_for_adc_port(figure_row_number + self._num_output_rows + 1, adc_acquisition_list)

    def _update_extra_features(self) -> None:
        all_x_axis_names = sorted(
            [a for a in self._figure.layout.__dir__() if a.startswith("xaxis")],
            key=lambda s: int(s.removeprefix("xaxis")) if s.removeprefix("xaxis").isnumeric() else 0,
        )
        all_xaxis_names_short = {
            k: "x" + k.removeprefix("xaxis") if k.removeprefix("xaxis").isnumeric() else "" for k in all_x_axis_names
        }
        bottommost_x_axis = all_x_axis_names[-1]
        self._figure.update_layout(
            updatemenus=[
                dict(
                    type="buttons",
                    direction="left",
                    active=0,
                    buttons=list(
                        [
                            dict(
                                args=[
                                    {k + ".matches": all_xaxis_names_short[bottommost_x_axis] for k in all_x_axis_names}
                                ],
                                label="Shared",
                                method="relayout",
                            ),
                            dict(
                                args=[{k + ".matches": v for k, v in all_xaxis_names_short.items()}],
                                label="Distinct",
                                method="relayout",
                            ),
                        ]
                    ),
                    showactive=True,
                    x=1,
                    xanchor="right",
                    y=1,
                    yanchor="bottom",
                    font=dict(size=10),
                ),
            ]
        )
        self._figure.add_annotation(
            dict(
                text="X-Axis scrolling method:",
                showarrow=False,
                x=1,
                y=1,
                yref="paper",
                yshift=40,
                yanchor="bottom",
                xref="paper",
                align="left",
            )
        )
        self._figure.update_layout(
            modebar_remove=[
                "autoscale",
                "autoscale2d",
                "lasso",
            ]
        )

        source_path = os.path.join(os.path.dirname(__file__), "sources", "logo_qm_square.png")

        im = base64.b64encode(open(source_path, "rb").read())
        self._figure.add_layout_image(
            source="data:image/png;base64,{}".format(im.decode()),
            xref="paper",
            yref="paper",
            x=0,
            y=1,
            sizex=0.1,
            sizey=0.1,
            xanchor="center",
            yanchor="bottom",
        )

    @property
    def _subplot_titles(self) -> Sequence[Union[str, Sequence[str]]]:
        titles = (
            [f"Analog-Out-{a}" for a in self._report_by_output_ports.flat_analog_out]
            + [f"Digital-Out-{d}" for d in self._report_by_output_ports.flat_digital_out]
            + [f"Analog-In-{ai}" for ai in self._report_by_output_ports.flat_analog_in]
        )
        return titles

    def _get_subplot_specs(self, num_rows: int) -> List[List[Dict[str, float]]]:
        return [[{"t": 1 / (num_rows * 4)}]] * num_rows

    def _setup_figure(self, num_rows: int, minimum_number_of_rows: int = 4) -> None:
        num_rows = max(num_rows, minimum_number_of_rows)
        self._figure.set_subplots(
            rows=num_rows,
            cols=1,
            subplot_titles=self._subplot_titles,
            vertical_spacing=0.1 / num_rows,
            specs=self._get_subplot_specs(num_rows),
        )

        self._figure.update_layout(
            hovermode="closest",
            hoverdistance=5,
            height=160 * num_rows,
            title=dict(
                text=(
                    f"Waveform Report (connection: {self._report.controllers_in_use[0]})"
                    + (" for job: {}".format(self._job_id) if self._job_id != -1 else "")
                ),
                x=0.5,
                xanchor="center",
                yanchor="auto",
                xref="paper",
            ),
            legend=dict(title="Elements", y=0.98, yanchor="top"),
        )
        self._figure.add_annotation(
            dict(
                text=f"Created at {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
                showarrow=False,
                x=0.5,
                y=1,
                yref="paper",
                yshift=20,
                yanchor="bottom",
                xref="paper",
                xanchor="center",
            )
        )

        for idx in range(1, num_rows + 1):
            self._figure.update_xaxes(range=[0, self._xrange], row=idx, col=1)

        self._update_axes_for_samples()

        inc = self._samples_factor
        input_rows_first_idx = self._num_output_rows + 1
        output_rows_indices = list(range(inc, input_rows_first_idx, inc))
        input_rows_indices = list(
            range(input_rows_first_idx, input_rows_first_idx + self._report_by_output_ports.num_analog_in_ports)
        )
        for idx in output_rows_indices + input_rows_indices:
            self._figure.update_yaxes(
                range=[-0.5, 1.5],
                showticklabels=False,
                tickvals=[-0.5],
                ticklen=50,
                tickcolor="#000000",
                showgrid=False,
                zeroline=False,
                row=idx,
                col=1,
            )
            self._figure.update_xaxes(title=dict(text="Time(ns)", standoff=5, font=dict(size=9)), row=idx, col=1)

    def _update_axes_for_samples(self) -> None:
        return

    def plot(self) -> None:
        self._figure.show(renderer="browser")

    def save(self, basedir: str = "", filename: str = "") -> None:
        os.makedirs(basedir, exist_ok=True)
        if filename == "":
            filename = f"waveform_report_{self._job_id}"
        if not os.path.splitext(filename)[1] == "html":
            filename += ".html"

        path = os.path.join(basedir, filename)
        with open(path, "w", encoding="UTF-8") as f:
            self._figure.write_html(f)


class _WaveformPlotBuilderWithSamples(_WaveformPlotBuilder):
    def __init__(self, wf_report: WaveformReport, samples: SimulatorControllerSamples, job_id: Union[int, str] = -1):
        self._samples = samples
        super().__init__(wf_report, job_id)

    @property
    def _samples_factor(self) -> int:
        return 2

    @property
    def _xrange(self) -> int:
        first_key = next(iter(self._samples.analog.keys()))
        return len(self._samples.analog[first_key])

    def _add_plot_data_for_analog_output_port(
        self, figure_row_number: int, output_port: str, port_waveforms: Sequence[PlayedWaveform]
    ) -> None:
        if len(port_waveforms) == 0:
            return

        self._add_plot_data_for_port(
            figure_row_number, self._max_parallel_traces_per_row.analog[output_port], port_waveforms
        )

        port_samples = self._samples.analog[output_port]
        sampling_rate = self._samples.analog_sampling_rate[output_port] / 1e9
        t = list(x / sampling_rate for x in range(len(port_samples)))
        self._add_trace_to_figure(figure_row_number, t, np.real(port_samples).tolist())
        if isinstance(port_samples[0], complex):
            self._add_trace_to_figure(figure_row_number, t, np.imag(port_samples).tolist())

    def _add_plot_data_for_digital_output_port(
        self, figure_row_number: int, output_port: str, port_waveforms: Sequence[PlayedWaveform]
    ) -> None:
        if len(port_waveforms) == 0:
            return

        self._add_plot_data_for_port(
            figure_row_number, self._max_parallel_traces_per_row.digital[output_port], port_waveforms
        )

        port_samples = self._fetch_digital_samples(output_port)
        t = list(range(len(port_samples)))  # here we assume 1ns sampling rate
        self._add_trace_to_figure(figure_row_number, t, port_samples)

    def _fetch_digital_samples(self, output_port: Union[int, str]) -> Sequence[int]:
        port_samples = self._samples.digital.get(str(output_port))
        if port_samples is None:
            logging.log(logging.WARNING, f"Could not find digital samples for output port {output_port}")
            return [0] * self._xrange
        return [int(_x) for _x in port_samples]

    def _add_trace_to_figure(
        self, figure_row_number: int, t: Sequence[float], port_samples: Union[Sequence[int], Sequence[float]]
    ) -> None:
        self._figure.add_trace(
            go.Scatter(
                x=t,
                y=port_samples,
                showlegend=False,
                xaxis=self._get_x_axis_name(figure_row_number),
                hovertemplate="%{x}ns, %{y}v<extra></extra>",
            ),
            row=figure_row_number * 2 - 1,
            col=1,
        )

    @property
    def _subplot_titles(self) -> Sequence[Union[str, Sequence[str]]]:
        _titles = [f"Analog-Out-{a}" for a in self._report_by_output_ports.flat_analog_out] + [
            f"Digital-Out-{d}" for d in self._report_by_output_ports.flat_digital_out
        ]
        zipped: Sequence[Tuple[str, Sequence[str]]] = list(zip(_titles, [[]] * len(_titles)))
        titles: Sequence[Union[str, Sequence[str]]] = [item for z in zipped for item in z] + [
            f"Analog-In-{a}" for a in self._report_by_output_ports.flat_analog_in
        ]
        return titles

    def _get_subplot_specs(self, num_rows: int) -> List[List[Dict[str, float]]]:
        specs = ([[{"t": 1.2 / (num_rows * 5)}]] + [[{"b": 1.2 / (num_rows * 5)}]]) * (self._num_output_rows // 2) + [
            [{"t": 1 / (num_rows * 4)}]
        ] * self._report_by_output_ports.num_analog_in_ports
        if len(specs) < num_rows:
            specs += [[{}]] * (num_rows - len(specs))
        return specs

    def _update_axes_for_samples(self) -> None:
        for r in range(1, self._num_output_rows, 2):
            sample_y_range = [-0.1, 1.1] if self._is_row_digital(r) else [-0.6, 0.6]
            self._figure.update_yaxes(range=sample_y_range, row=r, col=1)
            self._figure.update_xaxes(showticklabels=False, row=r, col=1)
            self._figure.update_yaxes(title=dict(text="Voltage(v)", standoff=5, font=dict(size=9)), row=r, col=1)
