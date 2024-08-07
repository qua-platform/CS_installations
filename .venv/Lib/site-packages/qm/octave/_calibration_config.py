from typing import Dict, Tuple

from qm.type_hinting import Number
from qm.type_hinting.config_types import DictQuaConfig, PortReferenceType, ControllerConfigType


def _prep_config(
    iq_channels: Tuple[PortReferenceType, PortReferenceType],
    adc_channels: Tuple[PortReferenceType, PortReferenceType],
    if_freq: Number,
    lo_freq: Number,
) -> DictQuaConfig:
    i_port = iq_channels[0]
    q_port = iq_channels[1]
    controller_names = set([ch[0] for ch in iq_channels] + [ch[0] for ch in adc_channels])
    controllers: Dict[str, ControllerConfigType] = {
        name: {
            "type": "opx1",
        }
        for name in controller_names
    }
    controllers[i_port[0]]["analog_outputs"] = {
        i_port[1]: {"offset": 0},
        q_port[1]: {"offset": 0},
    }
    for port in adc_channels:
        controllers[port[0]]["analog_inputs"] = {port[1]: {"offset": 0.0}}

    config: DictQuaConfig = {
        "version": 1,
        "controllers": controllers,
        "elements": {
            "to_calibrate": {
                "mixInputs": {
                    "I": i_port,
                    "Q": q_port,
                    "lo_frequency": lo_freq,
                    "mixer": "Correction_mixer",
                },
                "intermediate_frequency": if_freq,
                "operations": {},
                "digitalInputs": {},
            },
        },
        "pulses": {},
        "waveforms": {},
        "mixers": {
            "Correction_mixer": [
                {
                    "intermediate_frequency": if_freq,
                    "lo_frequency": lo_freq,
                    "correction": (1, 0, 0, 1),
                },
            ],
        },
    }

    return config
