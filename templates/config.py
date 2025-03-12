from typing import Any

from qcodes_contrib_drivers.drivers.QDevil import QDAC2



def get_probe_from_electrode(d: dict[int, str], electrode: str) -> int:
    """Return the probe number corresponding to the electrode.

    Parameters
    ----------
    d : dict[int, str]
        The dictionary mapping probe number to electrode.
    electrode : str
        The electrode name.

    """
    keys = [k for k, v in d.items() if v == electrode]
    if len(keys) != 1:
        raise ValueError(
            f"Unique electrode '{electrode}' not found in the dictionary: {d}"
        )
    return keys[0]


# Give for each probe the corresponding QDAC channel
probe_to_QDAC: dict[int, Any] = {
    1: qdac2.channel(1),
    2: qdac2.channel(12),
    3: qdac1.channel(12),
    4: qdac3.channel(20),
}

# Give for each probe the corresponding electrode (specific to each scribe !)
probe_to_electrode: dict[int, str] = {
    1: "gate_1",
    2: "gate_2",
    3: "gate_3",
    4: "gate_4",
}
