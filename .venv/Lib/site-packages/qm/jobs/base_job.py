import datetime
import warnings
from typing import List, Optional, Protocol

import betterproto

from qm.type_hinting import Value
from qm.persistence import BaseStore
from qm.exceptions import QmQuaException
from qm.api.frontend_api import FrontendApi
from qm.grpc.frontend import JobExecutionStatus
from qm.api.models.capabilities import ServerCapabilities
from qm.api.job_manager_api import create_job_manager_from_api
from qm.utils import deprecation_message, deprecate_to_property


class JobStateProtocol(Protocol):
    added_by: Optional[str]
    time_added: Optional[datetime.datetime]


class QmBaseJob:
    def __init__(
        self,
        job_id: str,
        machine_id: str,
        frontend_api: FrontendApi,
        capabilities: ServerCapabilities,
        store: BaseStore,
    ):
        self._id = job_id
        self._machine_id = machine_id
        self._frontend = frontend_api
        self._capabilities = capabilities
        self._store = store

        self._job_manager = create_job_manager_from_api(frontend_api)

        self._added_user_id: Optional[str] = None
        self._time_added: Optional[datetime.datetime] = None
        self._initialize_from_job_status()

    def _initialize_from_job_status(self) -> None:
        status: JobExecutionStatus = self._job_manager.get_job_execution_status(self._id, self._machine_id)
        name, one_of = betterproto.which_one_of(status, "status")

        if name in ("pending", "running", "completed", "loading") and one_of is not None:
            job_state: JobStateProtocol = one_of
            self._added_user_id = job_state.added_by
            self._time_added = job_state.time_added

    @property
    def status(self) -> str:
        """Returns the status of the job, one of the following strings:
        "unknown", "pending", "running", "completed", "canceled", "loading", "error"
        """
        status: JobExecutionStatus = self._job_manager.get_job_execution_status(self._id, self._machine_id)
        name, _ = betterproto.which_one_of(status, "status")
        return name

    @property
    def id(self) -> str:
        """Returns:
        The id of the job
        """
        class_name = self.__class__.__name__
        return deprecate_to_property(
            self._id,
            f"{class_name}.id()",
            "1.1.0",
            "1.2.0",
            f"id moved to be property, use '{class_name}.id' instead",
        )

    @property
    def user_added(self) -> Optional[str]:
        return self._added_user_id

    @property
    def time_added(self) -> Optional[datetime.datetime]:
        return self._time_added

    def insert_input_stream(
        self,
        name: str,
        data: List[Value],
    ) -> None:
        warnings.warn(
            deprecation_message(
                method="job.insert_input_stream",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method was renamed to `job.push_to_input_stream`.",
            ),
            DeprecationWarning,
            stacklevel=2,
        )
        self.push_to_input_stream(name, data)

    def push_to_input_stream(self, name: str, data: List[Value]) -> None:
        """Insert data to the input stream declared in the QUA program.
        The data is then ready to be read by the program using the advance
        input stream QUA statement.

        Multiple data entries can be inserted before the data is read by the program.

        See [Input streams](/qm-qua-sdk/docs/Guides/features/#input-streams) for more information.

        -- Available from QOP 2.0 --

        Args:
            name: The input stream name the data is to be inserted to.
            data: The data to be inserted. The data's size must match
                the size of the input stream.
        """
        if not self._capabilities.supports_input_stream:
            raise QmQuaException("`insert_input_stream()` is not supported by the QOP version.")

        if not isinstance(data, list):
            data = [data]

        self._job_manager.insert_input_stream(self.id, name, data)
