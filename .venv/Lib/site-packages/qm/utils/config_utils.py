from typing import Union

import betterproto

from qm.exceptions import InvalidConfigError
from qm.grpc.qua_config import (
    QuaConfig,
    QuaConfigFemTypes,
    QuaConfigControllerDec,
    QuaConfigOctoDacFemDec,
    QuaConfigPortReference,
    QuaConfigMicrowaveFemDec,
    QuaConfigAdcPortReference,
    QuaConfigDacPortReference,
)

FemTypes = Union[QuaConfigControllerDec, QuaConfigOctoDacFemDec, QuaConfigMicrowaveFemDec]


def get_fem_config_instance(fem_ref: QuaConfigFemTypes) -> FemTypes:
    _, config = betterproto.which_one_of(fem_ref, "fem_type_one_of")
    if not isinstance(config, (QuaConfigControllerDec, QuaConfigOctoDacFemDec, QuaConfigMicrowaveFemDec)):
        raise InvalidConfigError(f"FEM type {type(config)} is not supported")
    return config


def get_fem_config(
    pb_config: QuaConfig, port: Union[QuaConfigDacPortReference, QuaConfigAdcPortReference, QuaConfigPortReference]
) -> FemTypes:
    if port.controller not in pb_config.v1_beta.control_devices:
        raise InvalidConfigError("Controller not found")
    controller = pb_config.v1_beta.control_devices[port.controller]
    if port.fem not in controller.fems:
        raise InvalidConfigError("FEM not found")

    fem_ref = controller.fems[port.fem]
    config = get_fem_config_instance(fem_ref)
    return config


def get_simulation_sampling_rate(pb_config: QuaConfig) -> float:
    """
    This function is for the simulation, for OPX1000 we simulate with 2e9Hz sampling rate,
    for OPX we simulate with 1e9Hz sampling rate. To see whether it is OPX or OPX1000, we check the config.
    """
    for controller in pb_config.v1_beta.control_devices.values():
        for fem in controller.fems.values():
            _, fem_config = betterproto.which_one_of(fem, "fem_type_one_of")
            if isinstance(fem_config, QuaConfigOctoDacFemDec):
                return 2e9
    return 1e9
