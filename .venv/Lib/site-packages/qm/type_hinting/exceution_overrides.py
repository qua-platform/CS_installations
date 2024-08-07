from typing import Dict, List, Union, TypedDict


class ExecutionOverridesType(TypedDict, total=False):
    waveforms: Dict[str, Union[float, List[float]]]
