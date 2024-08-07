import logging

from qm.jobs.qm_job import QmJob
from qm.jobs.base_job import QmBaseJob
from qm.utils import run_until_with_timeout
from qm.grpc.frontend import JobExecutionStatus
from qm.exceptions import JobCancelledError, ErrorJobStateError, UnknownJobStateError

logger = logging.getLogger(__name__)

INVALID_QUEUE_POSITION = -1


class QmPendingJob(QmBaseJob):
    """A Class describing a job in the execution queue"""

    def position_in_queue(self) -> int:
        """Returns the current position of the job in the queue, returns -1 on if the job is not pending anymore

        Returns:
            The position in the queue

        Example:
            ```python
            pending_job.position_in_queue()
            ```
        """
        status = self._job_manager.get_job_execution_status(self._id, self._machine_id)
        if status.pending:
            return status.pending.position_in_queue

        logger.warning(f"Job {self.id} is not pending, therefor it does not have a position in queue")
        return INVALID_QUEUE_POSITION

    def wait_for_execution(self, timeout: float = float("infinity")) -> QmJob:
        """Waits for the job to be executed (start running) or until the timeout has elapsed.
        On zero and negative timeout, the job is checked once.

        Args:
            timeout: Timeout (in seconds) for this operation

        Raises:
            TimeoutError: When timeout is elapsed

        Returns:
            The running ``QmJob``
        """

        def on_iteration() -> bool:
            status: JobExecutionStatus = self._job_manager.get_job_execution_status(self._id, self._machine_id)
            if status.running or status.completed:
                return True

            if status.pending or status.loading:
                return False

            if status.error:
                raise ErrorJobStateError(
                    f"job {self._id} encountered an error",
                    error_list=[value.string_value for value in status.error.error_messages.values],
                )

            elif status.canceled:
                raise JobCancelledError(f"job {self._id} was cancelled")

            else:
                raise UnknownJobStateError(f"job {self._id} has unknown job state")

        def on_complete() -> QmJob:
            return QmJob(
                job_id=self._id,
                machine_id=self._machine_id,
                frontend_api=self._frontend,
                capabilities=self._capabilities,
                store=self._store,
            )

        return run_until_with_timeout(
            on_iteration_callback=on_iteration,
            on_complete_callback=on_complete,
            timeout=timeout,
            loop_interval=0.01,
            timeout_message=f"job {self._id} was not started in time. "
            f"Check the QMApp for errors and try reloading the version. "
            f"Please also inform QM about this issue. ",
        )

    def cancel(self) -> bool:
        """Removes the job from the queue

        Returns:
            true if the operation was successful

        Example:
            ```python
            pending_job.cancel()
            ```
        """
        return self._job_manager.remove_job(self._machine_id, job_id=self._id) > 0
