import logging
from abc import ABCMeta
from typing import Any, List, Type, Tuple, Union, TypeVar, Optional, cast

from dependency_injector.wiring import Provide, inject

from qm.type_hinting import Value
from qm.exceptions import QmValueError
from qm.utils.async_utils import run_async
from qm.grpc.general_messages import Matrix
from qm.api.models.jobs import PendingJobData
from qm.grpc.qm_manager import GetRunningJobRequest
from qm.api.models.capabilities import ServerCapabilities
from qm.api.models.server_details import ConnectionDetails
from qm.utils.general_utils import create_input_stream_name
from qm.api.base_api import BaseApi, connection_error_handle
from qm.containers.capabilities_container import CapabilitiesContainer
from qm.api.stubs.deprecated_job_manager_stub import DeprecatedJobManagerServiceStub
from qm.grpc.job_manager import (
    JobManagerServiceStub,
    InsertInputStreamRequest,
    GetElementCorrectionRequest,
    SetElementCorrectionRequest,
)
from qm._QmJobErrors import (
    MissingJobError,
    MissingElementError,
    UnknownInputStreamError,
    ElementWithSingleInputError,
    InvalidElementCorrectionError,
    InvalidJobExecutionStatusError,
    ElementWithoutIntermediateFrequencyError,
    _handle_job_manager_error,
)
from qm.grpc.frontend import (
    HaltRequest,
    FrontendStub,
    ResumeRequest,
    JobQueryParams,
    QueryValueMatcher,
    JobExecutionStatus,
    IsJobRunningRequest,
    PausedStatusRequest,
    IsJobAcquiringDataRequest,
    GetJobExecutionStatusRequest,
    IsJobAcquiringDataResponseAcquiringStatus,
)

logger = logging.getLogger(__name__)


JobStubType = TypeVar("JobStubType", JobManagerServiceStub, DeprecatedJobManagerServiceStub)


@connection_error_handle()
class JobManagerBaseApi(BaseApi[JobStubType], metaclass=ABCMeta):
    def __init__(self, connection_details: ConnectionDetails):
        super().__init__(connection_details)
        self._frontend_stub = FrontendStub(self._channel)

    def set_element_correction(
        self, job_id: str, element_name: str, correction: Matrix
    ) -> Tuple[float, float, float, float]:
        request = SetElementCorrectionRequest(job_id=job_id, qe_name=element_name, correction=correction)

        response = run_async(self._stub.set_element_correction(request, timeout=self._timeout))

        valid_errors = (
            MissingElementError,
            ElementWithSingleInputError,
            InvalidElementCorrectionError,
            ElementWithoutIntermediateFrequencyError,
        )
        _handle_job_manager_error(request, response, valid_errors)
        return (
            response.correction.v00,
            response.correction.v01,
            response.correction.v10,
            response.correction.v11,
        )

    def get_element_correction(self, job_id: str, element_name: str) -> Tuple[float, float, float, float]:
        request = GetElementCorrectionRequest(job_id=job_id, qe_name=element_name)

        response = run_async(self._stub.get_element_correction(request, timeout=self._timeout))
        valid_errors = (
            MissingElementError,
            ElementWithSingleInputError,
            ElementWithoutIntermediateFrequencyError,
        )
        _handle_job_manager_error(request, response, valid_errors)
        return (
            response.correction.v00,
            response.correction.v01,
            response.correction.v10,
            response.correction.v11,
        )

    def insert_input_stream(self, job_id: str, stream_name: str, data: List[Value]) -> None:
        stream_name = create_input_stream_name(stream_name)
        request = InsertInputStreamRequest(job_id=job_id, stream_name=stream_name)

        if all(type(element) == bool for element in data):
            request.bool_stream_data.data.extend(cast(List[bool], data))
        elif all(type(element) == int for element in data):
            request.int_stream_data.data.extend(cast(List[int], data))
        elif all(type(element) == float for element in data):
            request.fixed_stream_data.data.extend(cast(List[float], data))
        else:
            raise QmValueError(
                f"Invalid type in data, type is '{set(type(el) for el in data)}', "
                f"excepted types are bool | int | float"
            )

        response = run_async(self._stub.insert_input_stream(request, timeout=self._timeout))

        valid_errors = (
            MissingJobError,
            InvalidJobExecutionStatusError,
            UnknownInputStreamError,
        )
        _handle_job_manager_error(request, response, valid_errors)

    def halt(self, job_id: str) -> bool:
        request = HaltRequest(job_id=job_id)
        response = run_async(self._frontend_stub.halt(request, timeout=self._timeout))
        return response.ok

    def resume(self, job_id: str) -> bool:
        request = ResumeRequest(job_id=job_id)
        run_async(self._frontend_stub.resume(request, timeout=self._timeout))
        return True

    def is_paused(self, job_id: str) -> bool:
        request = PausedStatusRequest(job_id=job_id)
        response = run_async(self._frontend_stub.paused_status(request, timeout=self._timeout))
        return response.is_paused

    def is_job_running(self, job_id: str) -> bool:
        request = IsJobRunningRequest(job_id=job_id)

        response = run_async(self._frontend_stub.is_job_running(request, timeout=self._timeout))
        return response.is_running

    def is_data_acquiring(self, job_id: str) -> IsJobAcquiringDataResponseAcquiringStatus:
        request = IsJobAcquiringDataRequest(job_id=job_id)
        response = run_async(self._frontend_stub.is_job_acquiring_data(request, timeout=self._timeout))
        return response.acquiring_status

    def get_job_execution_status(self, job_id: str, quantum_machine_id: str) -> JobExecutionStatus:
        request = GetJobExecutionStatusRequest(job_id=job_id, quantum_machine_id=quantum_machine_id)
        response = run_async(self._frontend_stub.get_job_execution_status(request, timeout=self._timeout))
        return response.status

    @staticmethod
    def _create_job_query_params(
        quantum_machine_id: str,
        job_id: Optional[str],
        position: Optional[int],
        user_id: Optional[str],
    ) -> JobQueryParams:
        request = JobQueryParams(quantum_machine_id=quantum_machine_id)

        if position is not None:
            request.position = position

        if job_id is not None:
            request.job_id = QueryValueMatcher(value=job_id)

        if user_id is not None:
            request.user_id = QueryValueMatcher(value=user_id)

        return request

    def remove_job(
        self,
        quantum_machine_id: str,
        job_id: Optional[str] = None,
        position: Optional[int] = None,
        user_id: Optional[str] = None,
    ) -> int:
        request = JobManagerBaseApi._create_job_query_params(quantum_machine_id, job_id, position, user_id)

        response = run_async(self._frontend_stub.remove_pending_jobs(request, timeout=self._timeout))
        return response.numbers_of_jobs_removed

    def get_pending_jobs(
        self,
        quantum_machine_id: str,
        job_id: Optional[str],
        position: Optional[int],
        user_id: Optional[str],
    ) -> List[PendingJobData]:
        request = JobManagerBaseApi._create_job_query_params(quantum_machine_id, job_id, position, user_id)
        response = run_async(self._frontend_stub.get_pending_jobs(request, timeout=self._timeout))
        return [
            PendingJobData(
                job_id=job_id,
                position_in_queue=status.position_in_queue,
                time_added=status.time_added,
                added_by=status.added_by,
            )
            for job_id, status in response.pending_jobs.items()
        ]

    def get_running_job(self, machine_id: str) -> Optional[str]:
        request = GetRunningJobRequest(machine_id=machine_id)
        response = run_async(self._frontend_stub.get_running_job(request, timeout=self._timeout))

        if response.job_id:
            return response.job_id
        return None


class JobManagerApi(JobManagerBaseApi[JobManagerServiceStub]):
    @property
    def _stub_class(self) -> Type[JobManagerServiceStub]:
        return JobManagerServiceStub


class DeprecatedJobManagerApi(JobManagerBaseApi[DeprecatedJobManagerServiceStub]):
    @property
    def _stub_class(self) -> Type[DeprecatedJobManagerServiceStub]:
        return DeprecatedJobManagerServiceStub


@inject
def create_job_manager_from_api(
    api: BaseApi[Any], capabilities: ServerCapabilities = Provide[CapabilitiesContainer.capabilities]
) -> Union[JobManagerApi, DeprecatedJobManagerApi]:
    if capabilities.supports_new_grpc_structure:
        return JobManagerApi(api.connection_details)
    return DeprecatedJobManagerApi(api.connection_details)
