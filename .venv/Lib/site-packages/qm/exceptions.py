from pprint import pformat
from collections import defaultdict
from collections.abc import Collection
from typing import Any, List, Tuple, Generic, TypeVar

import betterproto
from marshmallow import ValidationError

from qm.StreamMetadata import StreamMetadataError


class QmQuaException(Exception):
    def __init__(self, message: str, *args: Any):
        self.message = message
        super().__init__(message, *args)


class QmmException(QmQuaException):
    pass


class OctaveConfigDeprecationException(QmmException):
    def __init__(self) -> None:
        super().__init__(
            "Received a response from the QM-app that includes octaves, please remove the OctaveConfig "
            "and move the configuration to the QUA-config."
        )


class OpenQmException(QmQuaException):
    def __init__(self, message: str, *args: Any, errors: List[Tuple[str, str, str]]):
        super().__init__(message, *args)
        self.errors = errors


class FailedToExecuteJobException(QmQuaException):
    pass


class FailedToAddJobToQueueException(QmQuaException):
    pass


class CompilationException(QmQuaException):
    pass


class JobCancelledError(QmQuaException):
    pass


class ErrorJobStateError(QmQuaException):
    def __init__(self, *args: Any, error_list: List[str]):
        super().__init__(*args)
        self._error_list = error_list if error_list else []

    def __str__(self) -> str:
        errors_string = "\n".join(error for error in self._error_list)
        return f"{super().__str__()}\n{errors_string}"


class UnknownJobStateError(QmQuaException):
    pass


class InvalidStreamMetadataError(QmQuaException):
    def __init__(self, stream_metadata_errors: List[StreamMetadataError], *args: Any):
        stream_errors_message = "\n".join(f"{e.error} at: {e.location}" for e in stream_metadata_errors)
        message = f"Error creating stream metadata:\n{stream_errors_message}"
        super().__init__(message, *args)


class ConfigValidationException(QmQuaException):
    pass


def _format_validation_error(curr_error: object) -> object:
    if isinstance(curr_error, defaultdict):
        to_return = {}
        for k, v in curr_error.items():
            for error in v.values():
                to_return[k] = _format_validation_error(error)
                # There is a hidden assumption here of a single error per entry
                break
        return to_return
    elif isinstance(curr_error, dict):
        to_return = {}
        for k, v in curr_error.items():
            to_return[k] = _format_validation_error(v)
        return to_return
    elif isinstance(curr_error, Collection):
        if all(isinstance(i, str) for i in curr_error):
            return curr_error
        else:
            return [_format_validation_error(i) for i in curr_error]
    raise ValueError(f"Unexpected type {type(curr_error)} in validation error")


class ConfigSchemaError(ConfigValidationException):
    def __init__(self, data: ValidationError) -> None:
        self.data = data
        self.formatted_dict = _format_validation_error(data.messages)
        super().__init__(pformat(self.formatted_dict, width=120))


class NoInputsOrOutputsError(ConfigValidationException):
    def __init__(self) -> None:
        super().__init__("An element must have either outputs or inputs. Please specify at least one.")


class ConfigSerializationException(QmQuaException):
    pass


class UnsupportedCapabilityError(QmQuaException):
    pass


class InvalidConfigError(QmQuaException):
    pass


class QMHealthCheckError(QmQuaException):
    pass


class QMFailedToGetQuantumMachineError(QmQuaException):
    pass


class QMSimulationError(QmQuaException):
    pass


class QmFailedToCloseQuantumMachineError(QmQuaException):
    pass


class QMFailedToCloseAllQuantumMachinesError(QmFailedToCloseQuantumMachineError):
    pass


class QMRequestError(QmQuaException):
    pass


class QMConnectionError(QmQuaException):
    pass


class QMTimeoutError(QmQuaException):
    pass


class QMRequestDataError(QmQuaException):
    pass


class QmServerDetectionError(QmQuaException):
    pass


class QmValueError(QmQuaException, ValueError):
    pass


class QmInvalidSchemaError(QmQuaException):
    pass


class QmInvalidResult(QmQuaException):
    pass


class QmNoResultsError(QmQuaException):
    pass


class FunctionInputError(QmQuaException):
    pass


class AnotherJobIsRunning(QmQuaException):
    def __init__(self) -> None:
        super().__init__("Another job is running on the QM. Halt it first")


class CalibrationException(QmQuaException):
    pass


class CantCalibrateElementError(CalibrationException):
    pass


class OctaveConnectionError(QmQuaException):
    pass


class OctaveLoopbackError(OctaveConnectionError):
    def __init__(self) -> None:
        super().__init__("lo loopback between different octave devices are not supported.")


class OctaveCableSwapError(OctaveConnectionError):
    def __init__(self) -> None:
        super().__init__("Cable swap detected. Please check your connections.")


class ElementUpconverterDeclarationError(OctaveConnectionError):
    def __init__(self) -> None:
        super().__init__(
            "Element declaration error, the I and Q connections are not connected to the same upconverter."
        )


class LOFrequencyMismatch(ConfigValidationException):
    def __init__(self) -> None:
        super().__init__(
            "LO frequency mismatch. The frequency stated in the element is different from "
            "the one stated in the Octave, remove the one in the element."
        )


class OctaveConnectionAmbiguity(ConfigValidationException):
    def __init__(self) -> None:
        super().__init__(
            "It is not allowed to override the default connection of the Octave. You should either state the "
            "default connection to Octave in the controller level, or set each port separately in the port level."
        )


class InvalidOctaveParameter(ConfigValidationException):
    pass


class ElementOutputConnectionAmbiguity(ConfigValidationException):
    pass


class QmRedirectionError(QmQuaException):
    pass


class QmLocationParsingError(QmQuaException):
    pass


class ElementInputConnectionAmbiguity(ConfigValidationException):
    pass


class StreamProcessingDataLossError(QmQuaException):
    pass


ErrorType = TypeVar("ErrorType", bound=betterproto.Message)


class QopResponseError(Exception, Generic[ErrorType]):
    def __init__(self, error: ErrorType):
        self._error = error

    @property
    def error(self) -> ErrorType:
        return self._error

    def __str__(self) -> str:
        details = getattr(self._error, "details", "")
        to_return = f"Error from QOP, details:\n{details}." if details else f"Error from QOP: {self._error}"
        return to_return
