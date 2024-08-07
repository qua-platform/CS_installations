from collections import defaultdict
from typing import Dict, List, Union, Optional, Sequence

import betterproto

from qm.api.v2.job_api import JobApi
from qm.persistence import BaseStore
from qm.utils.async_utils import run_async
from qm.exceptions import QMSimulationError
from qm.waveform_report import WaveformReport
from qm.utils.config_utils import get_fem_config
from qm.grpc.frontend import SimulatedResponsePart
from qm.api.v2.job_api.job_api import OldJobApiMock
from qm.jobs.simulated_job import extract_struct_value
from qm.api.models.capabilities import ServerCapabilities
from qm.api.models.server_details import ConnectionDetails
from qm.results.simulator_samples import SimulatorSamples, SimulatorControllerSamples
from qm.grpc.qua_config import (
    QuaConfigControllerDec,
    QuaConfigOctoDacFemDec,
    QuaConfigMicrowaveFemDec,
    QuaConfigAdcPortReference,
)
from qm.grpc.v2 import (
    PullSamplesRequest,
    PullSamplesResponsePullSamplesResponseSuccess,
    PullSamplesResponsePullSamplesResponseSuccessMode,
)


class SimulatedJobApi(JobApi):
    def __init__(
        self,
        connection_details: ConnectionDetails,
        job_id: str,
        store: BaseStore,
        simulated_response: SimulatedResponsePart,
        capabilities: ServerCapabilities,
    ) -> None:
        super().__init__(connection_details, job_id, store, capabilities)
        self._simulated_response = simulated_response

        self._waveform_report = WaveformReport.from_dict(
            extract_struct_value(simulated_response.waveform_report), self.id
        )

    def get_simulated_waveform_report(self) -> Optional[WaveformReport]:
        return self._waveform_report

    async def _pull_simulator_samples(
        self, include_analog: bool, include_digital: bool
    ) -> Dict[str, List[PullSamplesResponsePullSamplesResponseSuccess]]:
        request = PullSamplesRequest(self._id, include_analog, include_digital)
        bare_results = defaultdict(list)
        async for result in self._stub.pull_samples(request, timeout=self._timeout):
            _, response = betterproto.which_one_of(result, "response_oneof")
            if isinstance(response, PullSamplesResponsePullSamplesResponseSuccess):
                bare_results[response.controller].append(response)
            else:
                raise QMSimulationError("Error while pulling samples")
        return dict(bare_results)

    def get_simulated_samples(self, include_analog: bool = True, include_digital: bool = True) -> SimulatorSamples:
        config = self._get_pb_config()

        results_by_controller = run_async(self._pull_simulator_samples(include_analog, include_digital))
        controller_to_samples = {}
        for controller, responses in results_by_controller.items():
            analog: Dict[str, Sequence[Union[float, complex]]] = {}
            digital = {}
            analog_sampling_rate = {}
            for response in responses:
                fem_config = get_fem_config(
                    config,
                    QuaConfigAdcPortReference(controller=controller, fem=response.fem_id, number=response.port_id),
                )
                key = f"{response.fem_id}-{response.port_id}"
                if response.mode == PullSamplesResponsePullSamplesResponseSuccessMode.ANALOG:
                    if isinstance(fem_config, QuaConfigControllerDec):
                        analog_sampling_rate[key] = 1e9
                    elif isinstance(fem_config, QuaConfigOctoDacFemDec):
                        analog_sampling_rate[key] = 2e9
                    elif isinstance(fem_config, QuaConfigMicrowaveFemDec):
                        analog_sampling_rate[key] = fem_config.analog_outputs[response.port_id].sampling_rate
                    else:
                        raise QMSimulationError(f"Unknown FEM type: {fem_config}")

                    samples = response.double_data
                    if len(samples.data) == 2:
                        analog[key] = [x + 1j * y for x, y in zip(samples.data[0].item, samples.data[1].item)]
                    else:
                        analog[key] = samples.data[0].item
                else:
                    digital[key] = response.boolean_data.data[0].item
            controller_to_samples[controller] = SimulatorControllerSamples(
                analog, digital, analog_sampling_rate=analog_sampling_rate
            )
        return SimulatorSamples(controller_to_samples)

    def plot_waveform_report_with_simulated_samples(self) -> None:
        self._waveform_report.create_plot(self.get_simulated_samples())

    def plot_waveform_report_without_samples(self) -> None:
        self._waveform_report.create_plot()


class OldSimulatedJobApiMock(OldJobApiMock, SimulatedJobApi):
    pass
