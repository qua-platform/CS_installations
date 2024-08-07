import abc
from collections import defaultdict
from typing import Callable, Dict, Hashable, Tuple

from octave_sdk.grpc.quantummachines.octave.api.v1 import SingleUpdate
from octave_sdk.singleton import Singleton


class BatchSingleton(metaclass=Singleton):
    def __init__(self):
        self._batch_mode = False
        self._start_batch_callbacks: Dict[Hashable, Callable[[], None]] = {}
        self._end_batch_callbacks: Dict[Hashable, Callable[[], None]] = {}

        self._cached_updates: Dict[int, Dict[Tuple[int, str], SingleUpdate]] = defaultdict(dict)
        self._cached_modules: Dict[int, Dict[Tuple[int, str], SingleUpdate]] = defaultdict(dict)

    @property
    def is_batch_mode(self):
        return self._batch_mode

    def start_batch_mode(self):
        if not self._batch_mode:
            for callback in self._start_batch_callbacks.values():
                callback()
        self._batch_mode = True

    def end_batch_mode(self):
        if self._batch_mode:
            for callback in self._end_batch_callbacks.values():
                callback()
            self._cached_updates = defaultdict(dict)
            self._cached_modules = defaultdict(dict)
        self._batch_mode = False

    def set_cached_modules(self, obj: Hashable, modules: Dict[Tuple[int, str], SingleUpdate]):
        self._cached_modules[hash(obj)] = modules

    def set_cached_updates(self, obj: Hashable, modules: Dict[Tuple[int, str], SingleUpdate]):
        self._cached_updates[hash(obj)] = modules

    def get_cached_updates(self, obj: Hashable) -> Dict[Tuple[int, str], SingleUpdate]:
        return self._cached_updates[hash(obj)]

    def get_cached_modules(self, obj: Hashable) -> Dict[Tuple[int, str], SingleUpdate]:
        return self._cached_modules[hash(obj)]

    def register_start_batch_callback(self, obj: Hashable, callback: Callable[[], None]):
        self._start_batch_callbacks[hash(obj)] = callback

    def register_end_batch_callback(self, obj: Hashable, callback: Callable[[], None]):
        self._end_batch_callbacks[hash(obj)] = callback

    def unregister_start_batch_callback(self, obj: Hashable):
        self._start_batch_callbacks.pop(hash(obj))

    def unregister_end_batch_callback(self, obj: Hashable):
        self._end_batch_callbacks.pop(hash(obj))


class Batched(metaclass=abc.ABCMeta):
    def __init__(self):
        BatchSingleton().register_start_batch_callback(self, self._start_batch_callback)
        BatchSingleton().register_end_batch_callback(self, self._end_batch_callback)

    def __del__(self):
        BatchSingleton().unregister_start_batch_callback(self)
        BatchSingleton().unregister_end_batch_callback(self)

    @abc.abstractmethod
    def _start_batch_callback(self):
        pass

    @abc.abstractmethod
    def _end_batch_callback(self):
        pass

    @abc.abstractmethod
    def __hash__(self) -> int:
        pass
