import logging
from typing import List, Tuple, Optional

from qm.persistence import BaseStore
from qm.program.program import Program
from qm.grpc.qua_config import QuaConfig
from qm.api.frontend_api import FrontendApi
from qm.jobs.pending_job import QmPendingJob
from qm.api.models.capabilities import ServerCapabilities
from qm.api.models.compiler import CompilerOptionArguments
from qm.api.job_manager_api import create_job_manager_from_api
from qm.api.models.jobs import PendingJobData, InsertDirection
from qm.jobs.job_queue_base import QmQueueBase, JobNotFoundError
from qm.type_hinting.exceution_overrides import ExecutionOverridesType
from qm.program._execution_overrides_schema import ExecutionOverridesSchema

logger = logging.getLogger(__name__)


class QmQueue(QmQueueBase[QmPendingJob]):
    def __init__(
        self,
        config: QuaConfig,
        quantum_machine_id: str,
        frontend_api: FrontendApi,
        capabilities: ServerCapabilities,
        store: BaseStore,
    ):
        super().__init__(store, capabilities)
        self.machine_id = quantum_machine_id
        self._config = config
        self._frontend: FrontendApi = frontend_api
        self._job_manager = create_job_manager_from_api(self._frontend)

    def _get_pending_jobs(
        self, job_id: Optional[str] = None, position: Optional[int] = None, user_id: Optional[str] = None
    ) -> Tuple[QmPendingJob, ...]:
        jobs: List[PendingJobData] = self._job_manager.get_pending_jobs(self.machine_id, job_id, position, user_id)
        jobs.sort(key=lambda it: it.job_id)
        result = tuple(
            QmPendingJob(
                job_id=job.job_id,
                machine_id=self.machine_id,
                frontend_api=self._frontend,
                capabilities=self._capabilities,
                store=self._store,
            )
            for job in jobs
        )
        return result

    def add(
        self,
        program: Program,
        compiler_options: Optional[CompilerOptionArguments] = None,
    ) -> QmPendingJob:
        """Adds a QmJob to the queue.
        Programs in the queue will play as soon as possible.

        Args:
            program: A QUA program
            compiler_options: Optional arguments for compilation

        Example:
            ```python
            qm.queue.add(program)  # adds at the end of the queue
            qm.queue.insert(program, position)  # adds at position
            ```
        """
        if compiler_options is None:
            compiler_options = CompilerOptionArguments()

        job = self._insert(program, InsertDirection.end, compiler_options)
        return job

    def add_compiled(self, program_id: str, overrides: Optional[ExecutionOverridesType] = None) -> QmPendingJob:
        """Adds a compiled QUA program to the end of the queue, optionally
        overriding the values of analog waveforms defined in the program.
        Programs in the queue will play as soon as possible.
        For a detailed explanation see
        [Precompile Jobs](../../Guides/features/#precompile-jobs).

        Args:
            program_id: A QUA program ID returned from the compile
                function
            overrides: Object containing Waveforms to run the program
                with

        Example:
            ```python
            program_id = qm.compile(...)
            pending_job = qm.queue.add_compiled(program_id, overrides={
                'waveforms': {
                    'my_arbitrary_waveform': [0.1, 0.2, 0.3],
                    'my_constant_waveform': 0.2
                }
            })
            job = pending_job.wait_for_execution()
            ```
        """
        execution_overrides = overrides or {}

        job_id = self._frontend.add_compiled_to_queue(
            machine_id=self.machine_id,
            program_id=program_id,
            execution_overrides=ExecutionOverridesSchema().load(execution_overrides),
        )
        return QmPendingJob(
            job_id=job_id,
            machine_id=self.machine_id,
            frontend_api=self._frontend,
            capabilities=self._capabilities,
            store=self._store,
        )

    def add_to_start(
        self,
        program: Program,
        compiler_options: Optional[CompilerOptionArguments] = None,
    ) -> QmPendingJob:
        """Adds a QMJob to the start of the queue.
        Programs in the queue will play as soon as possible.

        Args:
            program: A QUA program
            compiler_options: Optional arguments for compilation

        """
        return self._insert(program, InsertDirection.start, compiler_options)

    def _insert(
        self,
        program: Program,
        insert_direction: InsertDirection,
        compiler_options: Optional[CompilerOptionArguments],
    ) -> QmPendingJob:
        """Inner function to insert a program to the queue by a given insert direction (start, end)"""
        if compiler_options is None:
            compiler_options = CompilerOptionArguments()

        job_id = self._frontend.add_to_queue(
            machine_id=self.machine_id,
            program=program.qua_program,
            compiler_options=compiler_options,
            insert_direction=insert_direction,
        )

        return QmPendingJob(
            job_id=job_id,
            machine_id=self.machine_id,
            frontend_api=self._frontend,
            capabilities=self._capabilities,
            store=self._store,
        )

    def get_at(self, position: int) -> QmPendingJob:
        """Gets the pending job object at the given position in the queue

        Args:
            position: An integer position in queue

        Returns:
            The pending job

        Example:
            ```python
            qm.queue.get(job_id)
            ```
        """
        jobs = self._get_pending_jobs(None, position)
        if len(jobs) == 0:
            raise JobNotFoundError()
        return jobs[0]

    def remove_by_id(self, job_id: str) -> int:
        """Removes the pending job object with a specific job id

        Args:
            job_id: a QMJob id

        Returns:
            The number of jobs removed

        Example:
            ```python
            qm.queue.remove_by_id(job_id)
            ```
        """
        if job_id is None or job_id == "":
            raise ValueError("job_id can not be empty")

        return self._job_manager.remove_job(
            quantum_machine_id=self.machine_id,
            job_id=job_id,
            position=None,
            user_id=None,
        )

    def remove_by_position(self, position: int) -> int:
        """Remove the PendingQmJob object by position in queue

        Args:
            position: position in queue

        Returns:
            The number of jobs removed

        Example:
            ```python
            qm.queue.remove_by_position(position)
            ```python
        """
        if position is None or position <= 0:
            raise ValueError("position must be positive")

        return self._job_manager.remove_job(
            quantum_machine_id=self.machine_id,
            job_id=None,
            position=position,
            user_id=None,
        )

    def remove_by_user_id(self, user_id: str) -> int:
        return self._job_manager.remove_job(
            quantum_machine_id=self.machine_id,
            job_id=None,
            position=None,
            user_id=user_id,
        )

    def clear(self) -> int:
        """Empties the queue from all pending jobs

        Returns:
            The number of jobs removed
        """
        return self._job_manager.remove_job(self.machine_id)
