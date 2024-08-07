from qm.jobs.qm_job import QmJob  # noqa
from qm.utils.deprecation_utils import throw_warning

throw_warning(
    "'qm.QmJob.QmJob' is moved as of 1.1.0 and will be removed in 1.2.0. " "use 'qm.QmJob' instead",
    category=DeprecationWarning,
    stacklevel=2,
)
