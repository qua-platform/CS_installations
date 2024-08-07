from qm.utils.deprecation_utils import throw_warning
from qm.results import StreamingResultFetcher, SingleStreamingResultFetcher, MultipleStreamingResultFetcher  # noqa

# Backward compatible names
JobResults = StreamingResultFetcher
SingleNamedJobResult = SingleStreamingResultFetcher
MultipleNamedJobResult = MultipleStreamingResultFetcher

throw_warning(
    "'qm._results.JobResults' is moved as of 1.1.0 and will be removed in 1.2.0. "
    "use 'qm.results.JobResults' instead",
    category=DeprecationWarning,
    stacklevel=2,
)
