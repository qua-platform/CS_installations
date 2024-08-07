import asyncio
import dataclasses
import threading
from typing import Optional

from octave_sdk.singleton import Singleton

MAX_MESSAGE_SIZE = 1024 * 1024 * 100  # 100 mb in bytes
BASE_TIMEOUT = 60


@dataclasses.dataclass
class ConnectionDetails:
    host: str
    port: int
    credentials: Optional[str] = dataclasses.field(default=None)
    max_message_size: int = dataclasses.field(default=MAX_MESSAGE_SIZE)
    timeout: float = dataclasses.field(default=BASE_TIMEOUT)


class EventLoopThread(metaclass=Singleton):
    def __init__(self):
        self.loop = asyncio.new_event_loop()
        self._thread = threading.Thread(target=self.loop.run_forever)
        self._thread.daemon = True
        self._thread.start()

    def stop(self):
        self.loop.stop()
        self._thread.join()
