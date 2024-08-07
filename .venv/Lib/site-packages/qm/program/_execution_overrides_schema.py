from typing import Any, List, Sized, Union

from marshmallow import Schema, ValidationError, fields, post_load
from marshmallow_polyfield import PolyField  # type: ignore[import-untyped]

from qm.grpc.frontend import WaveformOverride, ExecutionOverrides
from qm.type_hinting.exceution_overrides import ExecutionOverridesType


def _non_empty(v: Sized) -> None:
    if len(v) == 0:
        raise ValidationError("List must be non-empty")


def _waveforms_schema_deserialization_disambiguation(
    data: Union[float, List[float]], _o: Any
) -> Union[fields.List, fields.Float]:
    if isinstance(data, list):
        return fields.List(fields.Float(), required=True, validate=_non_empty)
    else:
        return fields.Float(required=True)


class ExecutionOverridesSchema(Schema):
    waveforms = fields.Dict(
        keys=fields.String(),
        values=PolyField(
            deserialization_schema_selector=_waveforms_schema_deserialization_disambiguation,
            required=True,
        ),
    )

    @post_load(pass_many=False)
    def build(self, data: ExecutionOverridesType, **kwargs: Any) -> ExecutionOverrides:
        result = {}

        waveforms = data.get("waveforms", {})

        for k, v in waveforms.items():
            samples = v if isinstance(v, list) else [v]
            result[k] = WaveformOverride(samples=samples)

        return ExecutionOverrides(waveforms=result)
