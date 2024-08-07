from qm.utils.deprecation_utils import throw_warning
from qm.jobs.job_queue_old_api import QmQueue  # noqa

throw_warning(
    "'qm.QmQueue.QmQueue' is moved as of 1.1.0 and will be removed in 1.2.0. " "use 'qm.QmQueue' instead",
    category=DeprecationWarning,
    stacklevel=2,
)
