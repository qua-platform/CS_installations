import logging
from typing import TYPE_CHECKING, Tuple, Generic, TypeVar, Optional

from qm.persistence import BaseStore
from qm.program.program import Program
from qm.api.v2.job_api.job_api import JobApi
from qm.jobs.pending_job import QmPendingJob
from qm.api.models.capabilities import ServerCapabilities
from qm.api.models.compiler import CompilerOptionArguments

if TYPE_CHECKING:
    pass

logger = logging.getLogger(__name__)


class JobNotFoundError(Exception):
    pass


JobTypeVar = TypeVar("JobTypeVar", JobApi, QmPendingJob)


class QmNewApiNotImplementedError(NotImplementedError):
    pass


class QmQueueBase(Generic[JobTypeVar]):
    def __init__(self, store: BaseStore, capabilities: ServerCapabilities):
        self._store = store
        self._capabilities = capabilities

    def _get_pending_jobs(
        self,
        job_id: Optional[str] = None,
        position: Optional[int] = None,
        user_id: Optional[str] = None,
    ) -> Tuple[JobTypeVar, ...]:
        raise QmNewApiNotImplementedError

    def add(
        self,
        program: Program,
        compiler_options: Optional[CompilerOptionArguments] = None,
    ) -> JobTypeVar:
        raise QmNewApiNotImplementedError

    def add_compiled(self, program_id: str) -> JobTypeVar:
        raise QmNewApiNotImplementedError

    def add_to_start(
        self,
        program: Program,
        compiler_options: Optional[CompilerOptionArguments] = None,
    ) -> JobTypeVar:
        """Adds a QMJob to the start of the queue.
        Programs in the queue will play as soon as possible.

        Args:
            program: A QUA program
            compiler_options: Optional arguments for compilation

        """
        raise QmNewApiNotImplementedError

    @property
    def count(self) -> int:
        """Get the number of jobs currently on the queue

        Returns:
            The number of jobs in the queue

        Example:
            ```python
            qm.queue.count
            ```
        """
        return len(self._get_pending_jobs())

    def __len__(self) -> int:
        return self.count

    @property
    def pending_jobs(self) -> Tuple[JobTypeVar, ...]:
        """Returns all currently pending jobs

        Returns:
            A list of all the currently pending jobs
        """
        return self._get_pending_jobs()

    def get(self, job_id: str) -> JobTypeVar:
        """Get a pending job object by job_id

        Args:
            job_id: a QMJob id

        Returns:
            The pending job

        Example:
            ```python
            qm.queue.get(job_id)
            ```
        """
        jobs = self._get_pending_jobs(job_id)
        if len(jobs) == 0:
            raise JobNotFoundError()
        return jobs[0]

    def get_at(self, position: int) -> JobTypeVar:
        raise QmNewApiNotImplementedError

    def get_by_user_id(self, user_id: str) -> Tuple[JobTypeVar, ...]:
        return self._get_pending_jobs(user_id=user_id)

    def remove_by_id(self, job_id: str) -> int:
        raise QmNewApiNotImplementedError

    def remove_by_position(self, position: int) -> int:
        raise QmNewApiNotImplementedError

    def remove_by_user_id(self, user_id: str) -> int:
        raise QmNewApiNotImplementedError

    def __getitem__(self, position: int) -> JobTypeVar:
        return self.get_at(position)

    def clear(self) -> int:
        raise QmNewApiNotImplementedError
