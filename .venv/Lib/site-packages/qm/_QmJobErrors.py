from typing import Dict, Type, Tuple, Union, cast

from qm.exceptions import QmQuaException
from qm.grpc.errors import JobManagerErrorTypes, ConfigQueryErrorTypes, JobOperationSpecificErrorTypes
from qm.grpc.job_manager import (
    InsertInputStreamRequest,
    JobManagerResponseHeader,
    InsertInputStreamResponse,
    GetElementCorrectionRequest,
    SetElementCorrectionRequest,
    GetElementCorrectionResponse,
    SetElementCorrectionResponse,
)

ResponseType = Union[InsertInputStreamResponse, SetElementCorrectionResponse, GetElementCorrectionResponse]

RequestType = Union[InsertInputStreamRequest, SetElementCorrectionRequest, GetElementCorrectionRequest]


class QmApiError(QmQuaException):
    @staticmethod
    def build_from_response(request: RequestType, response: ResponseType) -> "QmApiError":
        return QmApiError(0, str(response))

    def __init__(self, code: int, message: str = "") -> None:
        super().__init__(message)
        self.message = message
        self.code = code


class UnspecifiedError(QmApiError):
    @staticmethod
    def build_from_response(request: RequestType, response: ResponseType) -> "UnspecifiedError":
        return UnspecifiedError("Unspecified operation specific error")

    def __init__(self, message: str) -> None:
        super().__init__(0, message)


class _QmJobError(QmApiError):
    """Base class for exceptions in this module."""

    pass


class MissingJobError(_QmJobError):
    """if the job isn't recognized by the server (can happen if it never ran or if it was already deleted)"""

    def __init__(self) -> None:
        super().__init__(1000)


class InvalidJobExecutionStatusError(_QmJobError):
    def __init__(self) -> None:
        super().__init__(1001)


class InvalidOperationOnSimulatorJobError(_QmJobError):
    def __init__(self) -> None:
        super().__init__(1002)


class InvalidOperationOnRealJobError(_QmJobError):
    def __init__(self) -> None:
        super().__init__(1003)


class UnknownInputStreamError(_QmJobError):
    def __init__(self) -> None:
        super().__init__(1006)


class ConfigQueryError(QmApiError):
    pass


class MissingElementError(ConfigQueryError):
    """"""

    @staticmethod
    def build_from_response(request: RequestType, response: ResponseType) -> "MissingElementError":
        return MissingElementError(response.job_manager_response_header.job_error_details.message)

    def __init__(self, message: str):
        super().__init__(4001, message)


class MissingDigitalInputError(ConfigQueryError):
    """"""

    @staticmethod
    def _build_from_response(request: RequestType, response: ResponseType) -> "MissingDigitalInputError":
        return MissingDigitalInputError(response.job_manager_response_header.job_error_details.message)

    def __init__(self, message: str):
        super().__init__(4002, message)


class _InvalidConfigChangeError(QmApiError):
    pass


class ElementWithSingleInputError(_InvalidConfigChangeError):
    @staticmethod
    def build_from_response(request: RequestType, response: ResponseType) -> "ElementWithSingleInputError":
        return ElementWithSingleInputError(
            cast(Union[SetElementCorrectionRequest, GetElementCorrectionRequest], request).qe_name
        )

    def __init__(self, element_name: str):
        super().__init__(3000)
        self.element_name = element_name


class InvalidElementCorrectionError(_InvalidConfigChangeError):
    """If the correction values are invalid"""

    @staticmethod
    def build_from_response(request: RequestType, response: ResponseType) -> "InvalidElementCorrectionError":
        return InvalidElementCorrectionError(
            response.job_manager_response_header.job_error_details.message,
            cast(Union[SetElementCorrectionRequest, GetElementCorrectionRequest], request).qe_name,
            (
                cast(Union[SetElementCorrectionRequest, GetElementCorrectionRequest], request).correction.v00,
                cast(Union[SetElementCorrectionRequest, GetElementCorrectionRequest], request).correction.v01,
                cast(Union[SetElementCorrectionRequest, GetElementCorrectionRequest], request).correction.v10,
                cast(Union[SetElementCorrectionRequest, GetElementCorrectionRequest], request).correction.v11,
            ),
        )

    def __init__(
        self,
        message: str,
        element_name: str,
        correction: Tuple[float, float, float, float],
    ) -> None:
        super().__init__(3001, message)
        self.element_name = element_name
        self.correction = correction


class ElementWithoutIntermediateFrequencyError(_InvalidConfigChangeError):
    @staticmethod
    def build_from_response(request: RequestType, response: ResponseType) -> "ElementWithoutIntermediateFrequencyError":
        return ElementWithoutIntermediateFrequencyError(
            cast(Union[SetElementCorrectionRequest, GetElementCorrectionRequest], request).qe_name
        )

    def __init__(self, element_name: str):
        super().__init__(3002)
        self.element_name = element_name


class InvalidDigitalInputThresholdError(_InvalidConfigChangeError):
    @staticmethod
    def build_from_response(request: RequestType, response: ResponseType) -> "InvalidDigitalInputThresholdError":
        return InvalidDigitalInputThresholdError(response.job_manager_response_header.job_error_details.message)

    def __init__(self, message: str):
        super().__init__(3003)
        self.message = message


class InvalidDigitalInputDeadtimeError(_InvalidConfigChangeError):
    @staticmethod
    def build_from_response(request: RequestType, response: ResponseType) -> "InvalidDigitalInputDeadtimeError":
        return InvalidDigitalInputDeadtimeError(response.job_manager_response_header.job_error_details.message)

    def __init__(self, message: str):
        super().__init__(3004)
        self.message = message


class InvalidDigitalInputPolarityError(_InvalidConfigChangeError):
    @staticmethod
    def build_from_response(request: RequestType, response: ResponseType) -> "InvalidDigitalInputPolarityError":
        return InvalidDigitalInputPolarityError(response.job_manager_response_header.job_error_details.message)

    def __init__(self, message: str):
        super().__init__(3005)
        self.message = message


def _handle_job_manager_error(
    request: RequestType,
    response: ResponseType,
    valid_errors: Tuple[Type[QmQuaException], ...],
) -> None:
    api_response: JobManagerResponseHeader = response.job_manager_response_header
    if not api_response.success:
        error_type = api_response.job_manager_error_type

        if error_type == JobManagerErrorTypes.MissingJobError:
            raise MissingJobError()
        elif error_type == JobManagerErrorTypes.InvalidJobExecutionStatusError:
            raise InvalidJobExecutionStatusError()
        elif error_type == JobManagerErrorTypes.InvalidOperationOnSimulatorJobError:
            raise InvalidOperationOnSimulatorJobError()
        elif error_type == JobManagerErrorTypes.InvalidOperationOnRealJobError:
            raise InvalidOperationOnRealJobError()
        elif error_type == JobManagerErrorTypes.JobOperationSpecificError:
            exception_to_raise = _get_handle_job_operation_error(request, response)
            if exception_to_raise is not None and type(exception_to_raise) in valid_errors:
                raise exception_to_raise
            else:
                raise UnspecifiedError("Unspecified operation specific error")
        elif error_type == JobManagerErrorTypes.ConfigQueryError:
            exception_to_raise = _get_handle_config_query_error(request, response)
            if exception_to_raise is not None and type(exception_to_raise) in valid_errors:
                raise exception_to_raise
            else:
                raise UnspecifiedError("Unspecified operation specific error")
        elif error_type == JobManagerErrorTypes.UnknownInputStreamError:
            raise UnknownInputStreamError()
        else:
            raise UnspecifiedError("Unspecified operation error")


def _get_handle_config_query_error(request: RequestType, response: ResponseType) -> QmApiError:
    error_type = response.job_manager_response_header.job_error_details.config_query_error_type
    errors: Dict[int, Type[QmApiError]] = {
        ConfigQueryErrorTypes.MissingElementError: MissingElementError,
        ConfigQueryErrorTypes.MissingDigitalInputError: MissingDigitalInputError,
    }

    return errors.get(error_type, UnspecifiedError).build_from_response(request, response)


def _get_handle_job_operation_error(request: RequestType, response: ResponseType) -> QmApiError:
    error_type = response.job_manager_response_header.job_error_details.job_operation_specific_error_type
    errors: Dict[int, Type[QmApiError]] = {
        JobOperationSpecificErrorTypes.SingleInputElementError: ElementWithSingleInputError,
        JobOperationSpecificErrorTypes.InvalidCorrectionMatrixError: InvalidElementCorrectionError,
        JobOperationSpecificErrorTypes.ElementWithoutIntermediateFrequencyError: ElementWithoutIntermediateFrequencyError,
        JobOperationSpecificErrorTypes.InvalidDigitalInputThresholdError: InvalidDigitalInputThresholdError,
        JobOperationSpecificErrorTypes.InvalidDigitalInputDeadtimeError: InvalidDigitalInputDeadtimeError,
        JobOperationSpecificErrorTypes.InvalidDigitalInputPolarityError: InvalidDigitalInputPolarityError,
    }

    return errors.get(error_type, UnspecifiedError).build_from_response(request, response)
