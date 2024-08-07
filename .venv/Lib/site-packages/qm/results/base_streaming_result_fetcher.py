import abc
import json
import logging
import warnings
from io import BytesIO
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple, Union, BinaryIO, Optional, Protocol, cast

import numpy
import numpy.typing
from numpy.lib import format as _format

from qm.persistence import BaseStore
from qm.utils import deprecation_message
from qm.utils.async_utils import run_async
from qm.type_hinting.general import PathLike
from qm.api.v2.job_result_api import JobResultApi
from qm.api.job_result_api import JobResultServiceApi
from qm.api.models.capabilities import ServerCapabilities
from qm.utils.general_utils import run_until_with_timeout
from qm.StreamMetadata import StreamMetadata, StreamMetadataError
from qm.grpc.results_analyser import GetJobNamedResultHeaderResponse
from qm.exceptions import InvalidStreamMetadataError, StreamProcessingDataLossError

logger = logging.getLogger(__name__)

DtypeType = List[List[str]]


class JobStreamingStateProtocol(Protocol):
    done: bool
    closed: bool
    has_dataloss: bool


def _parse_dtype(simple_dtype: str) -> DtypeType:
    def hinted_tuple_hook(obj: Any) -> Any:
        if "__tuple__" in obj:
            return tuple(obj["items"])
        else:
            return obj

    dtype = json.loads(simple_dtype, object_hook=hinted_tuple_hook)
    return cast(DtypeType, dtype)


@dataclass
class JobResultItemSchema:
    name: str
    dtype: DtypeType
    shape: Tuple[int, ...]
    is_single: bool
    expected_count: int


@dataclass
class JobResultSchema:
    items: Dict[str, JobResultItemSchema]


@dataclass
class NamedJobResultHeader:
    count_so_far: int
    is_single: bool
    output_name: str
    job_id: str
    d_type: DtypeType
    shape: Tuple[int, ...]
    has_dataloss: bool


@dataclass
class JobStreamingState:
    job_id: str
    done: bool
    closed: bool
    has_dataloss: bool


class BaseStreamingResultFetcher(metaclass=abc.ABCMeta):
    def __init__(
        self,
        schema: JobResultItemSchema,
        service: Union[JobResultServiceApi, JobResultApi],
        store: BaseStore,
        stream_metadata_errors: List[StreamMetadataError],
        stream_metadata: Optional[StreamMetadata],
        capabilities: ServerCapabilities,
    ) -> None:
        self._schema = schema
        self._service = service
        self._store = store
        self._stream_metadata_errors = stream_metadata_errors
        self._stream_metadata = stream_metadata
        self._count_data_written = 0
        self._capabilities = capabilities

        self._validate_schema()

    @property
    def _job_id(self) -> str:
        return self._service.id

    @abc.abstractmethod
    def _validate_schema(self) -> None:
        pass

    @property
    def name(self) -> str:
        """The name of result this handle is connected to"""
        return self._schema.name

    @property
    def job_id(self) -> str:
        """The job id this result came from"""
        return self._job_id

    @property
    def expected_count(self) -> int:
        return self._schema.expected_count

    @property
    def numpy_dtype(self) -> DtypeType:
        return self._schema.dtype

    @property
    def stream_metadata(self) -> Optional[StreamMetadata]:
        """Provides the StreamMetadata of this stream.

        Metadata currently includes the values and shapes of the automatically identified loops
        in the program.

        """
        if len(self._stream_metadata_errors) > 0:
            logger.error("Error creating stream metadata:")
            for e in self._stream_metadata_errors:
                logger.error(f"{e.error} at: {e.location}")
            raise InvalidStreamMetadataError(self._stream_metadata_errors)
        return self._stream_metadata

    def save_to_store(
        self,
        writer: Optional[Union[BinaryIO, str]] = None,
        flat_struct: bool = False,
    ) -> int:
        """Saving to persistent store the NPY data of this result handle

        Args:
            writer: An optional writer to override the store defined in
                [QuantumMachinesManager][qm.quantum_machines_manager.QuantumMachinesManager]
            flat_struct: results will have a flat structure - dimensions
                will be part of the shape and not of the type

        Returns:
            The number of items saved
        """
        warnings.warn(
            deprecation_message(
                method="StreamingResultFetcher.save_to_store",
                deprecated_in="1.1.1",
                removed_in="1.2.0",
                details="function no longer supported, will be removed.",
            ),
            DeprecationWarning,
            stacklevel=2,
        )
        writer_opened = False
        if writer is None or isinstance(writer, str):
            writer_opened = True
            writer = self._open_bytes_writer(writer)
        try:
            header = self._get_named_header(flat_struct=flat_struct)
            return self._save_to_file(header, writer)
        finally:
            if writer_opened:
                writer.close()

    def _open_bytes_writer(self, path: Optional[PathLike]) -> BinaryIO:
        if path is not None:
            return open(path, "wb+")
        else:
            return self._store.job_named_result(self._job_id, self._schema.name).for_writing()

    def wait_for_values(self, count: int = 1, timeout: float = float("infinity")) -> None:
        """Wait until we know at least `count` values were processed for this named result

        Args:
            count: The number of items to wait for
            timeout: Timeout for waiting in seconds

        Returns:

        """
        run_until_with_timeout(
            lambda: self.count_so_far() >= count,
            timeout=timeout,
            timeout_message=f"result {self.name} was not done in time",
        )

    def wait_for_all_values(self, timeout: float = float("infinity")) -> bool:
        """Wait until we know all values were processed for this named result

        Args:
            timeout: Timeout for waiting in seconds

        Returns:
            True if job finished successfully and False if job has
            closed before done
        """
        if timeout is None:
            timeout = float("infinity")
            warnings.warn(
                "Parameter `timeout` can only be float since 1.1.0, please use `wait_for_all_values()` instead",
                category=DeprecationWarning,
                stacklevel=2,
            )

        def on_iteration() -> bool:
            header = self.get_job_state()
            return header.done or header.closed

        def on_finish() -> bool:
            header = self.get_job_state()
            return header.done

        return run_until_with_timeout(
            on_iteration_callback=on_iteration,
            on_complete_callback=on_finish,
            timeout=timeout,
            timeout_message=f"result {self.name} was not done in time",
        )

    def is_processing(self) -> bool:
        header = self.get_job_state()
        return not (header.done or header.closed)

    def count_so_far(self) -> int:
        """also `len(handle)`

        Returns:
            The number of values this result has so far
        """
        header = self._get_named_header()
        return header.count_so_far

    def __len__(self) -> int:
        return self.count_so_far()

    def has_dataloss(self) -> bool:
        """Returns:
        if there was data loss during job execution
        """
        state = self.get_job_state()
        return state.has_dataloss

    def _write_header(
        self,
        writer: BinaryIO,
        shape: Tuple[int, ...],
        d_type: object,
    ) -> None:
        _format.write_array_header_2_0(
            writer, {"descr": d_type, "fortran_order": False, "shape": shape}
        )  # type: ignore[no-untyped-call]

    async def _add_results_to_writer(self, data_writer: BinaryIO, start: int, stop: int) -> None:
        async for result in self._service.get_job_named_result(self._schema.name, start, stop - start):
            self._count_data_written += result.count_of_items
            data_writer.write(result.data)

    def _save_to_file(self, header: NamedJobResultHeader, writer: BinaryIO) -> int:
        self._count_data_written = 0

        final_shape = self._get_final_shape(header.count_so_far, header.shape)
        self._write_header(writer, final_shape, header.d_type)

        run_async(self._add_results_to_writer(writer, 0, header.count_so_far))
        return self._count_data_written

    def get_job_state(self) -> JobStreamingState:
        response: JobStreamingStateProtocol
        if self._capabilities.has_job_streaming_state:
            response = self._service.get_job_state()
        else:
            # This is just for backward compatibility
            response = cast(GetJobNamedResultHeaderResponse, self._service.get_named_header(self.name, False))
        return JobStreamingState(
            job_id=self._job_id,
            done=response.done,
            closed=response.closed,
            has_dataloss=response.has_dataloss,
        )

    def _get_named_header(self, check_for_errors: bool = True, flat_struct: bool = False) -> NamedJobResultHeader:
        response = self._service.get_named_header(self.name, flat_struct)
        dtype = _parse_dtype(response.simple_d_type)

        if check_for_errors and response.has_execution_errors:
            logger.error(
                "Runtime errors were detected. Please fetch the execution report using job.execution_report() for "
                "more information"
            )

        return NamedJobResultHeader(
            count_so_far=response.count_so_far,
            is_single=response.is_single,
            output_name=self.name,
            job_id=self.job_id,
            d_type=dtype,
            shape=tuple(response.shape),
            has_dataloss=response.has_dataloss,
        )

    def fetch_all(
        self, *, check_for_errors: bool = True, flat_struct: bool = False
    ) -> Optional[numpy.typing.NDArray[numpy.generic]]:
        """Fetch a result from the current result stream saved in server memory.
        The result stream is populated by the save() and save_all() statements.
        Note that if save_all() statements are used, calling this function twice
        may give different results.

        Args:
            check_for_errors: If true, the function would also check whether run-time errors happened during the
                program execution and would write to the logger an error message.
            flat_struct: results will have a flat structure - dimensions will be part of the shape and not of the type

        Returns:
            all result of current result stream
        """
        return self.fetch(
            slice(0, self.count_so_far()),
            check_for_errors=check_for_errors,
            flat_struct=flat_struct,
        )

    def fetch(
        self,
        item: Union[int, slice],
        *,
        check_for_errors: bool = True,
        flat_struct: bool = False,
    ) -> Optional[numpy.typing.NDArray[numpy.generic]]:
        """Fetch a single result from the current result stream saved in server memory.
        The result stream is populated by the save().

        Args:
            item: ignored
            check_for_errors: If true, the function would also check whether run-time errors happened during the
                program execution and would write to the logger an error message.
            flat_struct: results will have a flat structure - dimensions will be part of the shape and not of the type

        Returns:
            the current result

        Example:
            ```python
            res.fetch() # return the item in the top position
            ```
        """
        return self.strict_fetch(item, check_for_errors=check_for_errors, flat_struct=flat_struct)

    def strict_fetch(
        self,
        item: Union[int, slice],
        *,
        check_for_errors: bool = True,
        flat_struct: bool = False,
    ) -> numpy.typing.NDArray[numpy.generic]:
        """Fetch a result from the current result stream saved in server memory.
        The result stream is populated by the save() and save_all() statements.
        Note that if save_all() statements are used, calling this function twice
        with the same item index may give different results.

        Args:
            item: The index of the result in the saved results stream.
            check_for_errors: If true, the function would also check whether run-time errors happened during the
                program execution and would write to the logger an error message.
            flat_struct: results will have a flat structure - dimensions will be part of the shape and not of the type

        Returns:
            a single result if item is integer or multiple results if item is Python slice object.

        Example:
            ```python
            res.fetch(0)         #return the item in the top position
            res.fetch(1)         #return the item in position number 2
            res.fetch(slice(1,6))# return items from position 1 to position 6 (exclusive)
                                 # same as res.fetch_all()[1:6]
            ```
        """
        if type(item) is int:
            start = item
            stop = item + 1
            step = None
        elif type(item) is slice:
            start = item.start
            stop = item.stop
            step = item.step
        else:
            raise Exception("fetch supports only int or slice")

        if step != 1 and step is not None:
            raise Exception("fetch supports step=1 or None in slices")

        header = self._get_named_header(check_for_errors=check_for_errors, flat_struct=flat_struct)

        if stop is None:
            stop = header.count_so_far
        if start is None:
            start = 0

        writer = self._fetch_all_job_results(header, start, stop)

        if header.has_dataloss:
            raise StreamProcessingDataLossError(f"Data loss detected in data for job: {self._job_id}")

        return cast(numpy.typing.NDArray[numpy.generic], numpy.load(writer))

    def _fetch_all_job_results(self, header: NamedJobResultHeader, start: int, stop: int) -> BinaryIO:
        self._count_data_written = 0
        writer = BytesIO()
        data_writer = BytesIO()

        run_async(self._add_results_to_writer(data_writer, start, stop))

        final_shape = self._get_final_shape(self._count_data_written, header.shape)

        self._write_header(writer, final_shape, header.d_type)

        data_writer.seek(0)
        for d in data_writer:
            writer.write(d)

        writer.seek(0)
        return writer

    @staticmethod
    def _get_final_shape(count: int, shape: Tuple[int, ...]) -> Tuple[int, ...]:
        if count == 1:
            final_shape = shape
        else:
            if len(shape) == 1 and shape[0] == 1:
                final_shape = (count,)
            else:
                final_shape = (count,) + shape
        return final_shape
