import logging
import zipfile
from collections.abc import Mapping
from typing import Dict, List, Tuple, Union, BinaryIO, KeysView, Optional, Generator, ItemsView, ValuesView, cast

from qm.persistence import BaseStore
from qm.api.v2.job_result_api import JobResultApi
from qm.api.job_result_api import JobResultServiceApi
from qm.api.models.capabilities import ServerCapabilities
from qm.utils.general_utils import run_until_with_timeout
from qm.StreamMetadata import StreamMetadata, StreamMetadataError
from qm.results.single_streaming_result_fetcher import SingleStreamingResultFetcher
from qm.results.multiple_streaming_result_fetcher import MultipleStreamingResultFetcher
from qm.results.base_streaming_result_fetcher import (
    JobResultSchema,
    JobResultItemSchema,
    BaseStreamingResultFetcher,
    _parse_dtype,
)

logger = logging.getLogger(__name__)


class StreamingResultFetcher(Mapping):
    """Access to the results of a QmJob

    This object is created by calling [QmJob.result_handles][qm.jobs.running_qm_job.RunningQmJob.result_handles]

    Assuming you have an instance of StreamingResultFetcher:
    ```python
        job_results: StreamingResultFetcher
    ```
    This object is iterable:

    ```python
        for name, handle in job_results:
            print(name)
    ```

    Can detect if a name exists:

    ```python
    if "somename" in job_results:
        print("somename exists!")
        handle = job_results.get("somename")
    ```
    """

    def __init__(
        self,
        job_id: str,
        service: Union[JobResultServiceApi, JobResultApi],
        store: BaseStore,
        capabilities: ServerCapabilities,
    ) -> None:
        self._job_id = job_id
        self._service = service
        self._store = store
        self._schema = JobResultSchema({})
        self._capabilities = capabilities

        self._all_results: Dict[str, BaseStreamingResultFetcher] = {}
        self._add_job_results()

    def _add_job_results(self) -> None:
        self._schema = StreamingResultFetcher._load_schema(self._service)
        stream_metadata_errors, stream_metadata_dict = self._get_stream_metadata()
        for name, item_schema in self._schema.items.items():
            stream_metadata = stream_metadata_dict.get(name)
            result: BaseStreamingResultFetcher
            if item_schema.is_single:
                result = SingleStreamingResultFetcher(
                    schema=item_schema,
                    service=self._service,
                    store=self._store,
                    stream_metadata_errors=stream_metadata_errors,
                    stream_metadata=stream_metadata,
                    capabilities=self._capabilities,
                )
            else:
                result = MultipleStreamingResultFetcher(
                    job_results=self,
                    schema=item_schema,
                    service=self._service,
                    store=self._store,
                    stream_metadata_errors=stream_metadata_errors,
                    stream_metadata=stream_metadata,
                    capabilities=self._capabilities,
                )
            self._all_results[name] = result

    def __len__(self) -> int:
        return len(self._all_results)

    def __getitem__(self, item: str) -> Optional[BaseStreamingResultFetcher]:
        return self.get(item)

    def __getattr__(self, item: str) -> Optional[BaseStreamingResultFetcher]:
        if item == "shape" or item == "__len__":
            return (
                None  # this is here because of a bug in pycharm debugger: ver: 2022.3.2 build #PY-223.8617.48 (24/1/23)
            )
        return self.get(item)

    def _get_stream_metadata(self) -> Tuple[List[StreamMetadataError], Dict[str, StreamMetadata]]:
        return self._service.get_program_metadata()

    def __iter__(self) -> Generator[Tuple[str, Optional[BaseStreamingResultFetcher]], None, None]:
        for item in self._schema.items.values():
            yield item.name, self.get(item.name)

    def keys(self) -> KeysView[str]:
        """
        Returns a view of the names of the results
        """
        return self._all_results.keys()

    def items(self) -> ItemsView[str, BaseStreamingResultFetcher]:
        """
        Returns a view, in which the first item is the name of the result and the second is the result
        """
        return self._all_results.items()

    def values(self) -> ValuesView[BaseStreamingResultFetcher]:
        """
        Returns a view of the results
        """
        return self._all_results.values()

    def is_processing(self) -> bool:
        """Check if the job is still processing results

        Returns:
            True if results are still being processed, False otherwise
        """
        key = list(self._all_results.keys())[0]
        return self._all_results[key].is_processing()

    def save_to_store(
        self,
        writer: Optional[BinaryIO] = None,
        flat_struct: bool = False,
    ) -> None:
        """Save all results to store (file system by default) in a single NPZ file

        Args:
            writer: An optional writer to be used instead of the pre-populated
            store passed to [qm.quantum_machines_manager.QuantumMachinesManager][]
            flat_struct: results will have a flat structure - dimensions
                will be part of the shape and not of the type

        """
        own_writer = False
        if writer is None:
            own_writer = True
            writer = self._store.all_job_results(self._job_id).for_writing()
        zipf = None
        try:
            zipf = zipfile.ZipFile(writer, allowZip64=True, mode="w", compression=zipfile.ZIP_DEFLATED)
            for name, result in self:
                if result is not None:
                    with zipf.open(f"{name}.npy", "w") as entry:
                        result.save_to_store(cast(BinaryIO, entry), flat_struct)
        finally:
            if zipf is not None:
                zipf.close()
            if own_writer:
                writer.close()

    @staticmethod
    def _load_schema(service: Union[JobResultServiceApi, JobResultApi]) -> JobResultSchema:
        response = service.get_job_result_schema()
        return JobResultSchema(
            {
                item.name: JobResultItemSchema(
                    item.name,
                    _parse_dtype(item.simple_d_type),
                    tuple(item.shape),
                    item.is_single,
                    item.expected_count,
                )
                for item in response.items
            }
        )

    def get(self, name: str, /) -> Optional[BaseStreamingResultFetcher]:
        """Get a handle to a named result from [stream_processing][qm.qua._dsl.stream_processing]

        Args:
            name: The named result using in [stream_processing][qm.qua._dsl.stream_processing]


        Returns:
            A handle object to the results `MultipleNamedJobResult` or `SingleNamedJobResult` or None if the named results in unknown
        """
        return self._all_results.get(name)

    def __contains__(self, name: object) -> bool:
        if not isinstance(name, str):
            return False
        return name in self._all_results

    def wait_for_all_values(self, timeout: Optional[float] = None) -> bool:
        """Wait until we know all values were processed for all named results

        Args:
            timeout: Timeout for waiting in seconds

        Returns:
            True if all finished successfully, False if any result was closed before done
        """

        def on_iteration() -> bool:
            all_job_states = [result.get_job_state() for result in self._all_results.values()]
            all_done = all(state.done for state in all_job_states)
            any_closed = any(state.closed for state in all_job_states)
            return all_done or any_closed

        def on_complete() -> bool:
            return all(result.get_job_state().done for result in self._all_results.values())

        return run_until_with_timeout(
            on_iteration_callback=on_iteration,
            on_complete_callback=on_complete,
            timeout=timeout if timeout else float("infinity"),
            timeout_message="Job was not done in time",
        )
