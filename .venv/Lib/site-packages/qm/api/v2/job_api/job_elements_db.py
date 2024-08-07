from typing import Dict, cast

import betterproto

from qm.grpc.qua_config import QuaConfigElementDec
from qm.api.models.server_details import ConnectionDetails
from qm.api.v2.job_api.element_api import ElementApi, JobElement
from qm.api.v2.job_api.element_input_api import InputConfigType, create_element_input_class
from qm.api.v2.job_api.element_port_api import MwOutputApi, AnalogOutputApi, DigitalInputApi


class JobElementNotFound(KeyError):
    def __init__(self, key: str):
        self._key = key

    def __str__(self) -> str:
        return f"Element with the key {self._key} was not found."


class JobElementsDB(Dict[str, JobElement]):
    def __missing__(self, key: str) -> None:
        raise JobElementNotFound(key)

    @classmethod
    def init_from_data(
        cls, elements: Dict[str, QuaConfigElementDec], connection_details: ConnectionDetails, job_id: str
    ) -> "JobElementsDB":
        res = {
            element_name: cls._create_single_element(element_name, element_config, connection_details, job_id)
            for element_name, element_config in elements.items()
        }
        return cls(res)

    @staticmethod
    def _create_single_element(
        element_name: str, element_config: QuaConfigElementDec, connection_details: ConnectionDetails, job_id: str
    ) -> JobElement:
        input_config = cast(InputConfigType, betterproto.which_one_of(element_config, "element_inputs_one_of")[1])
        input_api_class = create_element_input_class(input_config)
        output_names = list(element_config.multiple_outputs.port_references) or list(element_config.outputs)
        outputs_apis = {
            output_name: AnalogOutputApi(connection_details, job_id, element_name, output_name)
            for output_name in output_names
        }
        digital_inputs_apis = {
            input_name: DigitalInputApi(connection_details, job_id, element_name, input_name)
            for input_name in element_config.digital_inputs
        }
        mw_output_api = (
            MwOutputApi(connection_details, job_id, element_name)
            if (betterproto.serialized_on_wire(element_config.microwave_output))
            else None
        )
        return JobElement(
            api=ElementApi(connection_details, job_id, element_name),
            input_api=input_api_class(connection_details, job_id, element_name),
            outputs_apis=outputs_apis,
            digital_inputs_apis=digital_inputs_apis,
            microwave_output_api=mw_output_api,
        )
