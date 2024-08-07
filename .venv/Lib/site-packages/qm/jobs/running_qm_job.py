import warnings
from enum import Enum
from typing import Tuple

from qm.jobs.base_job import QmBaseJob
from qm.utils import deprecation_message
from qm.grpc.general_messages import Matrix
from qm.results import StreamingResultFetcher
from qm.api.job_result_api import JobResultServiceApi
from qm._report import ExecutionError, ExecutionReport


class AcquiringStatus(Enum):
    AcquireStopped = 0
    NoDataToAcquire = 1
    HasDataToAcquire = 2


class RunningQmJob(QmBaseJob):
    @property
    def manager(self) -> None:
        """The QM object where this job lives

        Returns:

        """
        warnings.warn(
            deprecation_message(
                method="RunningQmJob.manager",
                deprecated_in="1.1.0",
                removed_in="1.2.0",
                details="QMJob no longer has 'manager' property",
            ),
            DeprecationWarning,
            stacklevel=2,
        )
        return None

    @property
    def result_handles(self) -> StreamingResultFetcher:
        """:type: qm._results.JobResults

        Returns:
            The handles that this job generated
        """
        return StreamingResultFetcher(
            self._id,
            JobResultServiceApi(self._frontend.connection_details, self._id),
            self._store,
            self._capabilities,
        )

    def cancel(self) -> bool:
        return self.halt()

    def halt(self) -> bool:
        """Halts the job on the opx"""
        return self._job_manager.halt(self._id)

    def resume(self) -> bool:
        """Resumes a program that was halted using the [qm.qua._dsl.pause][] statement"""
        return self._job_manager.resume(self._id)

    def is_paused(self) -> bool:
        """Returns:
            Returns ``True`` if the job is in a paused state.

        see also:

            ``resume()``
        """
        return self._job_manager.is_paused(self._id)

    def _is_job_running(self) -> bool:
        """Returns:
        Returns ``True`` if the job is running
        """
        return self._job_manager.is_job_running(self._id)

    def _is_data_acquiring(self) -> AcquiringStatus:
        """Returns the data acquiring status.
        The possible statuses are: AcquireStopped, NoDataToAcquire,  HasDataToAcquire

        Returns:
            An AcquiringStatus enum object
        """
        status = self._job_manager.is_data_acquiring(self._id)
        return AcquiringStatus(status.value)

    def execution_report(self) -> ExecutionReport:
        """Get runtime errors report for this job. See [Runtime errors](../../Guides/error/#runtime-errors).

        Returns:
            An object holding the errors that this job generated.
        """
        errors = [
            ExecutionError.create_from_grpc_message(item)
            for item in JobResultServiceApi(self._frontend.connection_details, self.id).get_job_errors()
        ]
        return ExecutionReport(self._id, errors)

    def set_element_correction(
        self, element: str, correction: Tuple[float, float, float, float]
    ) -> Tuple[float, float, float, float]:
        r"""Sets the correction matrix for correcting gain and phase imbalances
        of an IQ mixer associated with a element.

        Changes will only be done to the current job!

        Values will be rounded to an accuracy of $2^{-16}$.
        Valid values for the correction values are between $-2$ and $(2 - 2^{-16})$.

        Warning - the correction matrix can increase the output voltage which might result in an
        overflow.

        Args:
            element (str): the name of the element to update the
                correction for
            correction (tuple):

                tuple is of the form (v00, v01, v10, v11) where
                the matrix is
                $\begin{pmatrix} v_{00} & v_{01} \\ v_{10} & v_{11}\end{pmatrix}$

        Returns:
            The correction matrix, after rounding to the OPX resolution.
        """
        correction_matrix = Matrix(v00=correction[0], v01=correction[1], v10=correction[2], v11=correction[3])

        return self._job_manager.set_element_correction(self._id, element, correction_matrix)

    def get_element_correction(self, element: str) -> Tuple[float, float, float, float]:
        """Gets the correction matrix for correcting gain and phase imbalances
        of an IQ mixer associated with a element.

        Args:
            element (str): the name of the element to update the
                correction for

        Returns:
            The current correction matrix
        """
        return self._job_manager.get_element_correction(self._id, element)
