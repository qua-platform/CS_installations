from typing import List

from octave_sdk.grpc.quantummachines.octave.api.v1 import (
    SynthUpdate,
    SingleUpdate,
    RfUpConvUpdate,
    RfDownConvUpdate,
    IfDownConvUpdate,
    ClockUpdate,
)


class _BuilderList:
    def __init__(self) -> None:
        super().__init__()
        self._items = {}

    def get_items(self) -> List:
        return list(self._items.values())


class _SynthBuilderList(_BuilderList):
    def __init__(self) -> None:
        super().__init__()

    def __getitem__(self, item) -> SynthUpdate:
        if item not in self._items:
            self._items[item] = SingleUpdate(synth=SynthUpdate(index=item))
        return self._items[item].synth


class _DownBuilderList(_BuilderList):
    def __init__(self) -> None:
        super().__init__()

    def __getitem__(self, item) -> RfDownConvUpdate:
        if item not in self._items:
            self._items[item] = SingleUpdate(rf_down_conv=RfDownConvUpdate(index=item))
        return self._items[item].rf_down_conv


class _UpBuilderList(_BuilderList):
    def __init__(self) -> None:
        super().__init__()

    def __getitem__(self, item) -> RfUpConvUpdate:
        if item not in self._items:
            self._items[item] = SingleUpdate(rf_up_conv=RfUpConvUpdate(index=item))
        return self._items[item].rf_up_conv


class _IFBuilderList(_BuilderList):
    def __init__(self) -> None:
        super().__init__()

    def __getitem__(self, item) -> IfDownConvUpdate:
        if item not in self._items:
            self._items[item] = SingleUpdate(if_down_conv=IfDownConvUpdate(index=item))
        return self._items[item].if_down_conv


class _ClockBuilderList(_BuilderList):
    def __init__(self) -> None:
        super().__init__()

    def __getitem__(self, item) -> ClockUpdate:
        if item not in self._items:
            self._items[item] = SingleUpdate(clock=ClockUpdate())
        return self._items[item].clock_dist


class ClientRequestBuilder:
    def __init__(self) -> None:
        super().__init__()
        self._synth_builder_list = _SynthBuilderList()
        self._up_builder_list = _UpBuilderList()
        self._down_builder_list = _DownBuilderList()
        self._if_builder_list = _IFBuilderList()
        self._clock_builder_list = _ClockBuilderList()
        self._updates = []

    def __getattr__(self, item):
        if item == "synth":
            return self._synth_builder_list
        if item == "up":
            return self._up_builder_list
        if item == "down":
            return self._down_builder_list
        if item == "ifconv":
            return self._if_builder_list
        if item == "clk":
            return self._clock_builder_list

    def get_updates(self):
        return (
            self._synth_builder_list.get_items()
            + self._down_builder_list.get_items()
            + self._up_builder_list.get_items()
            + self._if_builder_list.get_items()
            + self._clock_builder_list.get_items()
        )
