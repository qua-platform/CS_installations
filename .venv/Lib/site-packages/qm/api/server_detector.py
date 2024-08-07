import ssl
import logging
import traceback
from typing import Set, Dict, List, Tuple, Optional

from qm.utils import SERVICE_HEADER_NAME
from qm.utils.async_utils import run_async
from qm.api.frontend_api import FrontendApi
from qm.api.models.info import QuaMachineInfo
from qm.api.models.debug_data import DebugData
from qm.exceptions import QmServerDetectionError
from qm.api.info_service_api import InfoServiceApi
from qm.communication.http_redirection import send_redirection_check
from qm.api.models.server_details import BASE_TIMEOUT, MAX_MESSAGE_SIZE, ServerDetails, ConnectionDetails

logger = logging.getLogger(__name__)

DEFAULT_PORTS = (80,)


def detect_server(
    cluster_name: Optional[str],
    user_token: str,
    ssl_context: Optional[ssl.SSLContext],
    host: str,
    port_from_user_config: Optional[int],
    user_provided_port: Optional[int],
    add_debug_data: bool,
    timeout: Optional[float] = None,
    max_message_size: Optional[int] = None,
    extra_headers: Optional[Dict[str, str]] = None,
) -> ServerDetails:
    ports_to_try = _get_ports(port_from_user_config, user_provided_port)
    extra_headers = extra_headers or {}
    headers = _create_headers(extra_headers, "gateway", cluster_name, user_token)
    errors: List[Tuple[str, str]] = []

    for port in ports_to_try:
        dst = f"{host}:{port}"
        logger.debug(f"Probing gateway at: {dst}")
        debug_data = DebugData()

        connection_details = ConnectionDetails(
            host=host,
            port=port,
            user_token=user_token,
            ssl_context=ssl_context,
            max_message_size=max_message_size if max_message_size else MAX_MESSAGE_SIZE,
            headers=headers,
            timeout=timeout if timeout else BASE_TIMEOUT,
            debug_data=debug_data if add_debug_data else None,
        )

        try:
            connection_details, octaves = _redirect(connection_details)
            info, server_version = _connect(connection_details)
        except Exception as e:
            errors.append((dst, f"{e}\n{traceback.format_exc()}"))
            continue

        if not server_version:
            errors.append((dst, "could not get server version"))
            continue

        logger.debug(f"Gateway discovered at: {dst}")
        return ServerDetails(
            port=port,
            host=host,
            server_version=server_version,
            qua_implementation=info,
            connection_details=connection_details,
            octaves={
                name: ConnectionDetails(
                    octave_host, octave_port, headers=_create_headers(extra_headers, name, cluster_name, user_token)
                )
                for name, (octave_host, octave_port) in octaves.items()
            },
        )

    targets = ",".join([f"{host}:{port}" for port in ports_to_try])
    cluster_str = f"cluster '{cluster_name}'" if cluster_name else "a cluster"
    message = (
        f"Failed to detect to QuantumMachines server, failed to connect to {cluster_str}. "
        f"Tried connecting to {targets}."
    )
    errors_msgs = "\n".join([f"{dst}: {error}" for dst, error in errors])
    logger.error(f"{message}\nErrors:\n{errors_msgs}.")
    raise QmServerDetectionError(message)


def _redirect(connection_details: ConnectionDetails) -> Tuple[ConnectionDetails, Dict[str, Tuple[str, int]]]:
    response_details = run_async(
        send_redirection_check(
            connection_details.host, connection_details.port, connection_details.headers, connection_details.timeout
        )
    )
    octaves = {}
    if response_details.host != connection_details.host or response_details.port != connection_details.port:
        logger.debug(
            f"Connection redirected from '{connection_details.host}:{connection_details.port}' to "
            f"'{response_details.host}:{response_details.port}'"
        )
        connection_details.host = response_details.host
        connection_details.port = response_details.port
        octaves = response_details.octaves
        if octaves:
            logger.debug(f"Detected octaves: {octaves}")

    return connection_details, octaves


def _connect(
    connection_details: ConnectionDetails,
) -> Tuple[Optional[QuaMachineInfo], Optional[str]]:
    frontend = FrontendApi(connection_details)
    info_service = InfoServiceApi(connection_details)

    info = info_service.get_info()
    if info.implementation.version:
        server_version = info.implementation.version
    else:
        server_version = frontend.get_version()

    logger.debug(f"Established connection to {connection_details.host}:{connection_details.port}")

    return info, server_version


def _get_ports(port_from_config: Optional[int], user_provided_port: Optional[int]) -> Set[int]:
    if user_provided_port is not None:
        return {user_provided_port}

    ports = set()
    if port_from_config is not None:
        ports.add(int(port_from_config))

    ports.update({int(port) for port in DEFAULT_PORTS})
    return ports


def _create_headers(
    base_headers: Dict[str, str], device_identity: str, cluster_name: Optional[str], user_token: Optional[str]
) -> Dict[str, str]:
    headers = {}
    headers.update(base_headers if base_headers is not None else {})
    headers[SERVICE_HEADER_NAME] = device_identity
    if user_token:
        headers["authorization"] = f"Bearer {user_token}"
    headers.update(_create_cluster_headers(cluster_name))
    return headers


def _create_cluster_headers(cluster_name: Optional[str]) -> Dict[str, str]:
    if cluster_name and cluster_name != "any":
        return {"cluster_name": cluster_name}
    return {"cluster_name": "any", "any_cluster": "true"}
