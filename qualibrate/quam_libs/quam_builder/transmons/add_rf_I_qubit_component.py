from typing import Dict
from quam.components.channels import SingleChannel
from quam_libs.quam_builder.transmons.get_digital_outputs import get_digital_outputs

from quam_libs.components import RF_Transmon


def add_rf_I_qubit_component(transmon: RF_Transmon, wiring_path: str, ports: Dict[str, str]):
    digital_outputs = get_digital_outputs(wiring_path, ports)
    if "opx_output" in ports:
        transmon.I = SingleChannel(
            opx_output=f"{wiring_path}/opx_output",
            opx_output_offset=0.0,
            intermediate_frequency=50e6,
            digital_outputs=digital_outputs,
        )
    else:
        raise ValueError(f"Unimplemented mapping of port keys to channel for ports: {ports}")
