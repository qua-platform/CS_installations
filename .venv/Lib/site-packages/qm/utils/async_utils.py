import sys
import asyncio
import selectors
import threading
from typing import Any, TypeVar, Coroutine

from qm.utils.general_utils import Singleton


class EventLoopThread(metaclass=Singleton):
    def __init__(self) -> None:
        if sys.platform == "win32":
            loop = asyncio.SelectorEventLoop(selectors.SelectSelector())
        else:
            loop = asyncio.new_event_loop()
        self.loop = loop
        self._thread = threading.Thread(target=self.loop.run_forever)
        self._thread.daemon = True
        self._thread.start()

    def stop(self) -> None:
        self.loop.stop()
        self._thread.join()


T = TypeVar("T")


# TODO: in 3.9, remove the typing ignore


# In 3.9 future is generic: asyncio.Future[T]
def create_future(coroutine: Coroutine[Any, Any, T]) -> asyncio.Future:  # type: ignore[type-arg]
    return asyncio.run_coroutine_threadsafe(coroutine, loop=EventLoopThread().loop)  # type: ignore[return-value]


def run_async(coroutine: Coroutine[Any, Any, T]) -> T:
    return create_future(coroutine).result()  # type: ignore[no-any-return]
