from collections import defaultdict
from typing import Dict, List, Union, Literal, Mapping, Optional, Sequence, TypedDict, cast

import numpy as np


def _standardize_port(port: Union[str, int]) -> str:
    # Since we moved to a notation of <fem>-<port>, we want to keep backwards compatibility
    if isinstance(port, int) or "-" not in port:
        port = f"1-{port}"
    return port


class _PortsWaveformsContainer(Dict[str, Sequence[float]]):
    def __init__(self, ports: Mapping[str, Sequence[Union[float, complex]]]):
        data = {}
        for k, v in ports.items():
            standard_port = _standardize_port(k)
            data[standard_port] = np.array(v)  # This is a foul, but we want to keep the same behavior as before.
        super().__init__(data)  # type: ignore[arg-type]

    def __getitem__(self, port: Union[str, int]) -> Sequence[float]:
        return super().__getitem__(_standardize_port(port))

    def __contains__(self, item: object) -> bool:
        if not isinstance(item, (int, str)):
            return False
        return super().__contains__(_standardize_port(item))


class SimulatorControllerSamples:
    def __init__(
        self,
        analog: Mapping[str, Sequence[Union[float, complex]]],
        digital: Mapping[str, Sequence[bool]],
        analog_sampling_rate: Optional[Mapping[str, float]] = None,
    ):
        self.analog = _PortsWaveformsContainer(analog)
        self.digital = _PortsWaveformsContainer(digital)
        self._analog_sampling_rate = (
            analog_sampling_rate if analog_sampling_rate is not None else defaultdict(lambda: 1e9)
        )

    @property
    def analog_sampling_rate(self) -> Mapping[str, float]:
        return self._analog_sampling_rate

    def plot(
        self,
        analog_ports: Optional[Union[str, int, List[Union[str, int]]]] = None,
        digital_ports: Optional[Union[str, int, List[Union[str, int]]]] = None,
    ) -> None:
        """Plots the simulated output of the OPX in the given ports.
        If no ports are given, all active ports are plotted.

        Args:
            analog_ports: Union[None, str, list[str]]
            digital_ports: Union[None, str, list[str]]
        """
        import matplotlib.pyplot as plt

        def calc_t_axis(_samples: Sequence[float], _sampling_rate: float) -> np.typing.NDArray[np.float64]:
            return np.arange(len(_samples)) / _sampling_rate * 1e9

        if isinstance(analog_ports, (str, int)):
            analog_ports = [analog_ports]
        if isinstance(digital_ports, (str, int)):
            digital_ports = [digital_ports]

        analog_to_plot = self.analog.keys() if analog_ports is None else analog_ports
        digital_to_plot = self.digital.keys() if digital_ports is None else digital_ports

        for analog_port in analog_to_plot:
            analog_samples = self.analog[analog_port]
            t_axis = calc_t_axis(analog_samples, self._analog_sampling_rate[str(analog_port)])
            if isinstance(analog_samples[0], complex):
                plt.plot(t_axis, np.real(analog_samples), label=f"Analog {analog_port} I")
                plt.plot(t_axis, np.imag(analog_samples), label=f"Analog {analog_port} Q")
            else:
                plt.plot(t_axis, analog_samples, label=f"Analog {analog_port}")
        for digital_port in digital_to_plot:
            digital_samples = self.digital[digital_port]
            plt.plot(calc_t_axis(digital_samples, 1e9), digital_samples, label=f"Digital {digital_port}")
        plt.xlabel("Time [ns]")
        plt.ylabel("Output")
        plt.legend()


class SimulatorSamplesDictType(TypedDict):
    analog: Dict[str, Sequence[float]]
    digital: Dict[str, Sequence[bool]]


class SimulatorSamples(Dict[str, SimulatorControllerSamples]):
    def __getattr__(self, item: str) -> SimulatorControllerSamples:
        return self[item]

    @property
    def __dict__(self) -> Dict[str, SimulatorControllerSamples]:  # type: ignore[override]
        """
        This property is here for backwards compatibility.
        We didn't put a deprecation message because it's annoying.
        In any case, this object is already a dict, so no need to convert it to a dict.
        """
        return {k: v for k, v in self.items()}

    @staticmethod
    def from_np_array(arr: np.typing.NDArray[np.generic]) -> "SimulatorSamples":
        controllers: Dict[str, SimulatorSamplesDictType] = {}
        assert arr.dtype.names is not None
        for col in arr.dtype.names:
            controller_name, output, key = col.split(":")
            output = cast(Literal["analog", "digital"], output)
            controller = controllers.setdefault(controller_name, {"analog": {}, "digital": {}})
            controller[output][key] = arr[col]  # type: ignore[call-overload]
        res = {}
        for controller_name, samples in controllers.items():
            res[controller_name] = SimulatorControllerSamples(samples["analog"], samples["digital"])
        return SimulatorSamples(res)
