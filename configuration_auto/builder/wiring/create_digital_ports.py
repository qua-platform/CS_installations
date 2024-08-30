from .paths import PORTS_BASE_JSON_PATH
from qualang_tools.wirer.instruments.instrument_channel import AnyInstrumentChannel

def create_digital_port(channel: AnyInstrumentChannel) -> (str, str):
    """
    Generates a key/JSON reference pair from which a QuAM port can be created
    for a single digital port.
    """
    key = f"digital_{channel.io_type}"

    reference = PORTS_BASE_JSON_PATH
    reference += f"/digital_{channel.io_type}s"
    if channel.instrument_id == "opx+":
        reference += f"/con{channel.con}"
    elif channel.instrument_id in ["lf-fem", "mw-fem"]:
        reference += f"/{channel.con}"
        reference += f"/{channel.slot}"
    else:
        raise NotImplementedError(f"Unhandled digital channel on instrument {channel.instrument_id}")
    reference += f"/{channel.port}"

    return key, reference
