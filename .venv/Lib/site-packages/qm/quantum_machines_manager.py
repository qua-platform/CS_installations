import ssl
import json
import logging
import warnings
from dataclasses import dataclass
from typing import Any, Dict, List, Union, Iterable, Optional, TypedDict

import marshmallow

from qm.api.v2.qm_api import QmApi
from qm.octave import QmOctaveConfig
from qm.user_config import UserConfig
from qm.grpc.qua_config import QuaConfig
from qm.utils import deprecation_message
from qm.api.frontend_api import FrontendApi
from qm.program import Program, load_config
from qm.utils.general_utils import is_debug
from qm.api.v2.job_api.job_api import JobData
from qm.quantum_machine import QuantumMachine
from qm.results import StreamingResultFetcher
from qm.api.models.debug_data import DebugData
from qm.jobs.simulated_job import SimulatedJob
from qm.logging_utils import set_logging_level
from qm.api.v2.job_api import JobApi, JobStatus
from qm.api.server_detector import detect_server
from qm.simulate.interface import SimulationConfig
from qm.api.job_result_api import JobResultServiceApi
from qm.persistence import BaseStore, SimpleFileStore
from qm.api.models.server_details import ServerDetails
from qm.type_hinting.config_types import DictQuaConfig
from qm.api.v2.qmm_api import Controller, OldQmmApiMock
from qm.program._qua_config_to_pb import load_config_pb
from qm.api.v2.job_api.simulated_job_api import SimulatedJobApi
from qm._octaves_container import load_config_from_calibration_db
from qm.program._qua_config_schema import validate_config_capabilities
from qm.api.simulation_api import SimulationApi, create_simulation_request
from qm.containers.capabilities_container import create_capabilities_container
from qm.octave.octave_manager import OctaveManager, prep_config_for_calibration
from qm.exceptions import QmmException, ConfigSchemaError, ConfigValidationException
from qm.api.models.compiler import CompilerOptionArguments, standardize_compiler_params

logger = logging.getLogger(__name__)

Version = TypedDict(
    "Version",
    {"qm-qua": str, "QOP": str, "OPX": str, "client": str, "server": str},
    total=False,
)


@dataclass
class DevicesVersion:
    gateway: str
    controllers: Dict[str, str]
    qm_qua: str
    octaves: Dict[str, str]


SERVER_TO_QOP_VERSION_MAP = {
    "2.40-144e7bb": "2.0.0",
    "2.40-82d4afc": "2.0.1",
    "2.40-8521884": "2.0.2",
    "2.40-3a0d7f1": "2.0.3",
    "2.50-1a24163": "2.1.3",
    "2.60-5ba458f": "2.2.0",
    "2.60-b62e6b6": "2.2.1",
    "2.60-0b17cac": "2.2.2",
    "2.70-7abf0e0": "2.4.0",
}


@dataclass
class OctaveDetails:
    host: str
    port: int


@dataclass
class Devices:
    controllers: Dict[str, Controller]
    octaves: Dict[str, OctaveDetails]


class QuantumMachinesManager:
    def __init__(
        self,
        host: Optional[str] = None,
        port: Optional[int] = None,
        *,
        cluster_name: Optional[str] = None,
        timeout: Optional[float] = None,
        log_level: int = logging.INFO,
        connection_headers: Optional[Dict[str, str]] = None,
        add_debug_data: bool = False,
        credentials: Optional[ssl.SSLContext] = None,
        store: Optional[BaseStore] = None,
        file_store_root: str = ".",
        octave: Optional[QmOctaveConfig] = None,
    ):
        """
        Args:
            host (string): Host where to find the QM orchestrator. If
                ``None``, local settings are used
            port: Port where to find the QM orchestrator. If None, local
                settings are used
        """
        set_logging_level(log_level)
        self._user_config = UserConfig.create_from_file()
        self._port = port
        host = host or self._user_config.manager_host or ""
        if host is None:
            message = "Failed to connect to QuantumMachines server. No host given."
            logger.error(message)
            raise QmmException(message)

        self._cluster_name = cluster_name
        self._store = store if store else SimpleFileStore(file_store_root)
        self._server_details = self._initialize_connection(
            host=host,
            port=port,
            timeout=timeout,
            add_debug_data=add_debug_data,
            connection_headers=connection_headers,
            credentials=credentials,
        )
        if self._server_details.octaves:
            if octave is None:
                octave = QmOctaveConfig()
            if octave.get_devices():
                warnings.warn(
                    "QMM was opened with OctaveConfig. Please note that from QOP2.4.0 the octave devices "
                    "are managed by the cluster setting in the QM-app. It is recommended to remove the "
                    "OctaveConfig from the QMM instantiation.",
                    category=DeprecationWarning,
                )
            else:
                for name, info in self._server_details.octaves.items():
                    octave.add_device(name, info)
        elif octave is not None:
            opx_headers = self._server_details.connection_details.headers
            for _, device in octave.get_devices().items():
                device.headers = {**opx_headers, **device.headers}

        self._caps = self._server_details.capabilities
        self._frontend = FrontendApi(self._server_details.connection_details)
        self._simulation_api = SimulationApi(self._server_details.connection_details)
        self._octave_config = octave
        self._octave_manager = OctaveManager(self._octave_config, self, self._caps)
        self._api = None
        if self._caps.supports_api_v2:
            self._api = OldQmmApiMock(
                self._server_details.connection_details,
                store=self._store,
                capabilities=self._caps,
                octave_config=self._octave_config,
                octave_manager=self._octave_manager,
            )

        raise_on_error = self._user_config.strict_healthcheck is not False
        self.perform_healthcheck(raise_on_error)

    def _initialize_connection(
        self,
        host: str,
        port: Optional[int],
        timeout: Optional[float],
        add_debug_data: bool,
        credentials: Optional[ssl.SSLContext],
        connection_headers: Optional[Dict[str, str]],
    ) -> ServerDetails:
        server_details = detect_server(
            cluster_name=self._cluster_name,
            user_token=self._user_config.user_token,
            ssl_context=credentials,
            host=host,
            port_from_user_config=self._user_config.manager_port,
            user_provided_port=port,
            add_debug_data=add_debug_data,
            timeout=timeout,
            extra_headers=connection_headers,
        )
        create_capabilities_container(server_details.qua_implementation)
        return server_details

    @property
    def store(self) -> BaseStore:
        return self._store

    @property
    def octave_manager(self) -> OctaveManager:
        # warnings.warn(
        #     "Do not use OctaveManager, it will be removed in the next version", DeprecationWarning, stacklevel=2
        # )
        return self._octave_manager

    @property
    def cluster_name(self) -> str:
        return self._cluster_name or "any"

    def perform_healthcheck(self, strict: bool = True) -> None:
        """Perform a health check against the QM server.

        Args:
            strict: Will raise an exception if health check failed
        """
        if self._api:
            self._api.perform_healthcheck()
        else:
            self._frontend.healthcheck(strict)
        if self._octave_config is not None:
            for octave in self._octave_config.get_devices():
                self._octave_manager.get_client(octave)

    def version_dict(self) -> Version:
        """
        Returns:
            A dictionary with the qm-qua and QOP versions
        """
        from qm.version import __version__

        output_dict: Version = {}
        server_version = self._server_details.server_version
        output_dict["qm-qua"] = __version__
        if server_version in SERVER_TO_QOP_VERSION_MAP:
            output_dict["QOP"] = SERVER_TO_QOP_VERSION_MAP[server_version]
        else:
            output_dict["OPX"] = server_version
        if is_debug():
            logger.debug(f"OPX version: {server_version}")

        return output_dict

    def version(self) -> Union[Version, DevicesVersion]:
        """
        Returns:
            A dictionary with the qm-qua and QOP versions
        """
        if self._api is None:
            warnings.warn(
                deprecation_message(
                    "QuantumMachineManager.version()",
                    "1.1.4",
                    "1.2.0",
                    "QuantumMachineManager.version() will have a different return type in 1.2.0. Use `QuantumMachineManager.version_dict()` instead",
                ),
                category=DeprecationWarning,
                stacklevel=2,
            )
            output_dict = self.version_dict()

            output_dict["client"] = output_dict["qm-qua"]
            output_dict["server"] = self._server_details.server_version
            return output_dict
        else:
            from qm.version import __version__

            response = self._api.get_version()
            octaves = {}
            if self._octave_config is not None:
                for octave_name in self._octave_config.get_devices():
                    octaves[octave_name] = self._octave_manager.get_client(octave_name).get_version()
            return DevicesVersion(
                gateway=response.gateway,
                controllers=response.controllers,
                qm_qua=__version__,
                octaves=octaves,
            )

    def reset_data_processing(self) -> None:
        """Stops current data processing for ALL running jobs"""
        if self._api:
            self._api.reset_data_processing()
        else:
            self._frontend.reset_data_processing()

    def close(self) -> None:
        """Closes the Quantum machine manager"""
        warnings.warn(
            deprecation_message("QuantumMachineManager.close()", "1.1.0", "1.2.0", "close will be removed."),
            category=DeprecationWarning,
            stacklevel=2,
        )
        pass

    def open_qm(
        self,
        config: DictQuaConfig,
        close_other_machines: bool = True,
        validate_with_protobuf: bool = False,
        add_calibration_elements_to_config: bool = True,
        use_calibration_data: bool = True,
        **kwargs: Any,
    ) -> Union[QuantumMachine, QmApi]:
        """Opens a new quantum machine. A quantum machine can use multiple OPXes, and a
        single OPX can also be used by multiple quantum machines as long as they do not
        share the same physical resources (input/output ports) as defined in the config.

        Args:
            config: The config that will be used by the quantum machine
            close_other_machines: When set to true (default) any open
                quantum machines will be closed. This simplifies the
                workflow, but does not enable opening more than one
                quantum machine.
            validate_with_protobuf (bool): Validates config with
                protobuf instead of marshmallow. It is usually faster
                when working with large configs. Defaults to False.

        Returns:
            A quantum machine obj that can be used to execute programs
        """
        if kwargs:
            logger.warning(f"unused kwargs: {list(kwargs)}, please remove them.")

        loaded_config = self._load_config(config, disable_marshmallow_validation=validate_with_protobuf)

        if use_calibration_data and self._octave_config is not None:
            if self._octave_config.calibration_db is not None:
                loaded_config = load_config_from_calibration_db(
                    loaded_config, self._octave_config.calibration_db, self._octave_config, self._caps
                )
            else:
                logger.warning("No calibration_db set in octave config, skipping loading calibration data")

        if add_calibration_elements_to_config and self._octave_config is not None:
            loaded_config = prep_config_for_calibration(loaded_config, self._octave_config, self._caps)

        self._octave_manager.set_octaves_from_qua_config(loaded_config.v1_beta.octaves)
        if self._api:
            return self._api.open_qm(loaded_config, close_other_machines)

        machine_id = self._frontend.open_qm(loaded_config, close_other_machines)

        return QuantumMachine(
            machine_id=machine_id,
            pb_config=loaded_config,
            frontend_api=self._frontend,
            capabilities=self._caps,
            store=self.store,
            octave_config=self._octave_config,
            octave_manager=self._octave_manager,
        )

    def _load_config(self, qua_config: DictQuaConfig, *, disable_marshmallow_validation: bool = False) -> QuaConfig:
        try:
            if disable_marshmallow_validation:
                loaded_config = load_config_pb(qua_config)
            else:
                loaded_config = load_config(qua_config)
            validate_config_capabilities(loaded_config, self._caps)
            return loaded_config
        except KeyError as key_error:
            raise ConfigValidationException(f"Missing key {key_error} in config") from key_error
        except marshmallow.exceptions.ValidationError as validation_error:
            raise ConfigSchemaError(validation_error) from validation_error

    def validate_qua_config(self, qua_config: DictQuaConfig) -> None:
        """
        Validates a qua config based on the connected server's capabilities.
        Raises an exception if the config is invalid.

        Args:
            qua_config: A python dict containing the qua config to validate
        """
        self._load_config(qua_config)

    def open_qm_from_file(self, filename: str, close_other_machines: bool = True) -> Union[QuantumMachine, QmApi]:
        """Opens a new quantum machine with config taken from a file on the local file system

        Args:
            filename: The path to the file that contains the config
            close_other_machines: Flag whether to close all other
                running machines

        Returns:
            A quantum machine obj that can be used to execute programs
        """
        warnings.warn(
            deprecation_message(
                "qmm.open_qm_from_file",
                "1.1.8",
                "1.2.0",
                "This method is going to be removed.",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        with open(filename) as json_file:
            json1_str = json_file.read()

            def remove_nulls(d: Dict[Any, Any]) -> Dict[Any, Any]:
                return {k: v for k, v in d.items() if v is not None}

            config = json.loads(json1_str, object_hook=remove_nulls)
        return self.open_qm(config, close_other_machines)

    def simulate(
        self,
        config: DictQuaConfig,
        program: Program,
        simulate: SimulationConfig,
        compiler_options: Optional[CompilerOptionArguments] = None,
        *,
        strict: Optional[bool] = None,
        flags: Optional[List[str]] = None,
    ) -> Union[SimulatedJob, SimulatedJobApi]:
        """Simulate the outputs of a deterministic QUA program.

        The following example shows a simple execution of the simulator, where the
        associated config object is omitted for brevity.

        Example:
            ```python
            from qm.qua import *
            from qm import SimulationConfig, QuantumMachinesManager

            qmm = QuantumMachinesManager()

            with program() as prog:
                play('pulse1', 'qe1')

            job = qmm.simulate(config, prog, SimulationConfig(duration=100))
            ```
        Args:
            config: A QM config
            program: A QUA ``program()`` object to execute
            simulate: A ``SimulationConfig`` configuration object
            compiler_options: additional parameters to pass to execute
            strict: a deprecated option for the compiler
            flags: deprecated way to provide flags to the compiler

        Returns:
            a ``QmJob`` object (see QM Job API).
        """
        standardized_options = standardize_compiler_params(compiler_options, strict, flags)
        pb_config = load_config(config)

        if self._api:
            request = create_simulation_request(pb_config, program, simulate, standardized_options)
            simulated_job = self._api.simulate(
                request.config, request.high_level_program, request.simulate, request.controller_connections
            )
            return simulated_job
        else:
            job_id, simulated_response_part = self._simulation_api.simulate(
                pb_config, program, simulate, standardized_options
            )
            return SimulatedJob(
                job_id=job_id,
                frontend_api=self._frontend,
                capabilities=self._server_details.capabilities,
                store=self.store,
                simulated_response=simulated_response_part,
            )

    def list_open_qms(self) -> List[str]:
        """Return a list of open quantum machines. (Returns only the ids, use ``get_qm(...)`` to get the machine object)

        Returns:
            The ids list
        """
        if self._api:
            return self._api.list_open_qms()
        else:
            return self._frontend.list_open_quantum_machines()

    def list_open_quantum_machines(self) -> List[str]:
        warnings.warn(
            deprecation_message(
                "qmm.list_open_quantum_machines",
                "1.1.8",
                "1.2.0",
                "This method was renamed to `qmm.list_open_qms()`",
            )
        )
        return self.list_open_qms()

    def get_qm(self, machine_id: str) -> Union[QuantumMachine, QmApi]:
        """Gets an open quantum machine object with the given machine id

        Args:
            machine_id: The id of the open quantum machine to get

        Returns:
            A quantum machine obj that can be used to execute programs
        """
        if self._api:
            return self._api.get_qm(machine_id)

        qm_data = self._frontend.get_quantum_machine(machine_id)
        machine_id = qm_data.machine_id
        pb_config = qm_data.config

        return QuantumMachine(
            machine_id=machine_id,
            pb_config=pb_config,
            frontend_api=self._frontend,
            capabilities=self._caps,
            store=self.store,
            octave_manager=self.octave_manager,
        )

    def get_job_result_handles(self, job_id: str) -> StreamingResultFetcher:
        """
        Returns the result handles for a job.
        :param job_id: The job id
        :return: The handles that this job generated
        """
        if self._api is not None:
            raise NotImplementedError(
                "This method is not available in the current QOP version, "
                "please use `qmm.get_job(job_id).result_handles`"
            )
        return StreamingResultFetcher(
            job_id,
            JobResultServiceApi(self._server_details.connection_details, job_id),
            self._store,
            self._caps,
        )

    def close_all_qms(self) -> None:
        """Closes ALL open quantum machines"""
        if self._api:
            self._api.close_all_qms()
        else:
            self._frontend.close_all_quantum_machines()

    def close_all_quantum_machines(self) -> None:
        warnings.warn(
            deprecation_message(
                "qmm.close_all_quantum_machines",
                "1.1.8",
                "1.2.0",
                "This function is going to change its name to `qmm.close_all_qms()`",
            ),
            category=DeprecationWarning,
            stacklevel=2,
        )
        self.close_all_qms()

    def get_controllers(self) -> List[Controller]:
        """Returns a list of all the controllers that are available"""
        if self._api:
            warnings.warn(
                deprecation_message(
                    "get_controllers",
                    "1.1.8",
                    "1.2.0",
                    "This will have a different return type",
                ),
                category=DeprecationWarning,
                stacklevel=2,
            )
            new_response = self._api.get_controllers()
            return list(new_response.values())
        else:
            old_response = self._frontend.get_controllers()
            return [Controller.build_from_message(message) for message in old_response]

    def _get_controllers_as_dict(self) -> Dict[str, Controller]:
        if self._api:
            return self._api.get_controllers()
        else:
            old_response = self._frontend.get_controllers()
            return {message.name: Controller.build_from_message(message) for message in old_response}

    def get_devices(self) -> Devices:
        controllers = self._get_controllers_as_dict()
        octaves = {}
        if self._octave_config is not None:
            octaves = {k: OctaveDetails(v.host, v.port) for k, v in self._octave_config.get_devices().items()}
        return Devices(controllers=controllers, octaves=octaves)

    def clear_all_job_results(self) -> None:
        """Deletes all data from all previous jobs"""
        if self._api:
            warnings.warn(
                deprecation_message(
                    "clear_all_job_results",
                    "1.1.8",
                    "1.2.0",
                    "This method is going to be removed.",
                ),
                category=DeprecationWarning,
                stacklevel=1,
            )
            self._api.clear_all_job_results()
        else:
            self._frontend.clear_all_job_results()

    def get_jobs(
        self,
        qm_ids: Iterable[str] = tuple(),
        job_ids: Iterable[str] = tuple(),
        user_ids: Iterable[str] = tuple(),
        description: str = "",
        status: Iterable[JobStatus] = tuple(),
    ) -> List[JobData]:
        if self._api is None:
            raise NotImplementedError("This method is not available in the current QOP version")
        return self._api.get_jobs(
            qm_ids=qm_ids, job_ids=job_ids, user_ids=user_ids, description=description, status=status
        )

    def get_job(self, job_id: str) -> JobApi:
        if self._api is None:
            raise NotImplementedError("This method is not available in the current QOP version")
        return self._api.get_job(job_id)

    @property
    def _debug_data(self) -> Optional[DebugData]:
        return self._server_details.connection_details.debug_data
