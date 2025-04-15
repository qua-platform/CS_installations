from pathlib import Path
from qm.octave import QmOctaveConfig
from qualibrate_config.resolvers import get_qualibrate_config_path
from quam.components import FrequencyConverter
from quam.core import QuamRoot, quam_dataclass
from quam.components.octave import Octave
from quam.components.ports import FEMPortsContainer, OPXPlusPortsContainer
from .qubit import Qubit
from qm import QuantumMachinesManager, QuantumMachine
from qualang_tools.results.data_handler import DataHandler
from qm.qua._dsl import _ResultSource
from qm.qua._expressions import QuaVariable
from qm.qua import declare_stream, declare, fixed
from dataclasses import field
from typing import List, Dict, ClassVar, Optional, Sequence, Union

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:
    import tomli as tomllib

__all__ = ["Quam"]


@quam_dataclass
class Quam(QuamRoot):
    """Example QUAM root component."""

    qubits: Dict[str, Qubit] = field(default_factory=dict)
    wiring: dict = field(default_factory=dict)
    network: dict = field(default_factory=dict)

    active_qubit_names: List[str] = field(default_factory=list)

    ports: Union[FEMPortsContainer, OPXPlusPortsContainer] = None

    _data_handler: ClassVar[DataHandler] = None
    qmm: ClassVar[Optional[QuantumMachinesManager]] = None

    @classmethod
    def get_quam_state_path(cls) -> Optional[Path]:
        qualibrate_config_path = get_qualibrate_config_path()

        if qualibrate_config_path.exists():
            config = tomllib.loads(qualibrate_config_path.read_text())
            quam_state_path = config.get("quam", {}).get("state_path", None)
            if quam_state_path is not None:
                quam_state_path = Path(quam_state_path)
            return quam_state_path
        else:
            return None

    @classmethod
    def load(cls, *args, **kwargs) -> "Quam":
        if not args:
            quam_state_path = cls.get_quam_state_path()
            if quam_state_path is None:
                raise ValueError(
                    "No path argument provided to load the QUAM state. "
                    "Please set the quam_state_path in the QUAlibrate config. "
                    "See the README for instructions."
                )

            args = (quam_state_path,)

        return super().load(*args, **kwargs)

    def save(
        self,
        path: Union[Path, str] = None,
        content_mapping: Dict[Union[Path, str], Sequence[str]] = None,
        include_defaults: bool = False,
        ignore: Sequence[str] = None,
    ):
        if path is None:
            path = self.get_quam_state_path()
            if path is None:
                raise ValueError(
                    "No path argument provided to save the QUAM state. "
                    "Please provide a path or set the 'QUAM_STATE_PATH' environment variable. "
                    "See the README for instructions."
                )

        super().save(path, content_mapping, include_defaults, ignore)

    def connect(self) -> QuantumMachinesManager:
        """Open a Quantum Machine Manager with the credentials ("host" and "cluster_name") as defined in the network file.

        Returns: the opened Quantum Machine Manager.
        """
        settings = dict(
            host=self.network["host"],
            cluster_name=self.network["cluster_name"],
            octave=None,
        )
        if "port" in self.network:
            settings["port"] = self.network["port"]
        self.qmm = QuantumMachinesManager(**settings)
        return self.qmm

    @property
    def data_handler(self) -> DataHandler:
        """Return the existing data handler or open a new one to conveniently handle data saving."""
        if self._data_handler is None:
            self._data_handler = DataHandler(
                root_data_folder=self.network["data_folder"]
            )
            DataHandler.node_data = {"quam": "./state.json"}
        return self._data_handler

    @property
    def active_qubits(self) -> List[Qubit]:
        """Return the list of active qubits."""
        return [self.qubits[q] for q in self.active_qubit_names]

    @property
    def depletion_time(self) -> int:
        """Return the longest depletion time amongst the active qubits."""
        return max(q.resonator.depletion_time for q in self.active_qubits)

    @property
    def thermalization_time(self) -> int:
        """Return the longest thermalization time amongst the active qubits."""
        return max(q.thermalization_time for q in self.active_qubits)

    def qua_declaration(
        self,
    ) -> tuple[
        list[QuaVariable],
        list[_ResultSource],
        list[QuaVariable],
        list[_ResultSource],
        QuaVariable,
        _ResultSource,
    ]:
        """Macro to declare the necessary QUA variables"""

        n = declare(int)
        n_st = declare_stream()
        I = [declare(fixed) for _ in range(len(self.qubits))]
        Q = [declare(fixed) for _ in range(len(self.qubits))]
        I_st = [declare_stream() for _ in range(len(self.qubits))]
        Q_st = [declare_stream() for _ in range(len(self.qubits))]
        return I, I_st, Q, Q_st, n, n_st

    def initialize_qpu(self, **kwargs):
        pass
