import re
import logging
from typing import Dict, Tuple

import httpx
from betterproto.lib.google.protobuf import Empty

from qm.api.models.server_details import ResponseConnectionDetails
from qm.exceptions import QmRedirectionError, QmLocationParsingError

logger = logging.getLogger(__name__)


def _parse_location(location_header: str) -> Tuple[str, int]:
    match = re.match("(?P<host>[^:]*):(?P<port>[0-9]*)(/(?P<url>.*))?", location_header)
    if match is None:
        raise QmLocationParsingError(f"Could not parse new host and port (location header: {location_header})")
    host, port, _, __ = match.groups()
    if not port.isdigit() or not host:
        raise QmLocationParsingError(f"Could not parse new port (location header: {location_header})")
    return str(host), int(port)


def parse_octaves(raw_response: str) -> Dict[str, Tuple[str, int]]:
    octaves = {}
    for octave_details in raw_response.split(";"):
        if octave_details:
            name_and_location = octave_details.split(",")
            if len(name_and_location) != 2:
                raise QmLocationParsingError(
                    f"Could not parse octave name and location from '{octave_details}' (raw response: {raw_response})"
                )
            octaves[name_and_location[0]] = _parse_location(name_and_location[1])
    return octaves


async def send_redirection_check(
    host: str, port: int, headers: Dict[str, str], timeout: float
) -> ResponseConnectionDetails:
    extended_headers = {"content-type": "application/grpc", "te": "trailers", **headers}
    async with httpx.AsyncClient(http2=True, follow_redirects=False, http1=False, timeout=timeout) as client:
        response = await client.post(f"http://{host}:{port}", headers=extended_headers, content=bytes(Empty()))
    if response.status_code == 400:
        if headers.get("any_cluster", "false") == "false":
            cluster_name = f"cluster '{headers['cluster_name']}'"
        else:
            cluster_name = "any cluster"
        raise QmRedirectionError(f"Connected to server at in {host}:{port}. Could not find {cluster_name}.")
    if response.status_code != 302:
        return ResponseConnectionDetails(host, port, {})

    new_host, new_port = _parse_location(response.headers["location"])
    octaves = parse_octaves(response.headers.get("octaves", ""))

    return ResponseConnectionDetails(new_host, new_port, octaves)
