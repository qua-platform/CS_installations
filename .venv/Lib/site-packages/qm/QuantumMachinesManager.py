from qm.utils.deprecation_utils import throw_warning
from qm.quantum_machines_manager import QuantumMachinesManager  # noqa

throw_warning(
    "'qm.QuantumMachinesManager.QuantumMachinesManager' is moved as of 1.1.2 and will be removed in 1.2.0. "
    "use 'qm.QuantumMachinesManager' instead",
    category=DeprecationWarning,
    stacklevel=2,
)
