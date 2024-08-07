import dataclasses
from typing import List


@dataclasses.dataclass
class ImplementationInfo:
    name: str
    version: str
    url: str


@dataclasses.dataclass
class QuaMachineInfo:
    capabilities: List[str]
    implementation: ImplementationInfo
