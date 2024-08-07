import time
import logging
from typing import Any, Dict, Generic, TypeVar, Callable

SERVICE_HEADER_NAME = "x-grpc-service"

T = TypeVar("T")


def create_input_stream_name(name: str) -> str:
    return f"input_stream_{name}"


def run_until_with_timeout(
    on_iteration_callback: Callable[[], bool],
    # The type ignore can be removed in 3.12 with `T = TypeVar("T", default=None)`
    on_complete_callback: Callable[[], T] = lambda: None,  # type: ignore[assignment, return-value]
    timeout: float = float("infinity"),
    loop_interval: float = 0.1,
    timeout_message: str = "Timeout Exceeded",
) -> T:
    """

    :param on_iteration_callback: A callback that returns bool that is called every loop iteration.
     If True is returned, the loop is complete and on_complete_callback is called.

    :param on_complete_callback: A callback that is called when the loop is completed.
    This function returns the return value of on_complete_callback

    :param timeout: The timeout in seconds for on_iteration_callback to return True,
    on Zero the loop is executed once.

    :param loop_interval: The interval (in seconds) between each loop execution.

    :param timeout_message: The message of the TimeoutError exception.
    raise TimeoutError: When the timeout is exceeded
    """
    if timeout < 0:
        raise ValueError("timeout cannot be smaller than 0")

    start = time.time()
    end = start + timeout

    while True:
        if on_iteration_callback():
            return on_complete_callback()

        time.sleep(loop_interval)

        if time.time() >= end:
            raise TimeoutError(timeout_message)


_T = TypeVar("_T")


class Singleton(type, Generic[_T]):
    _instances: Dict["Singleton[_T]", _T] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> _T:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


def is_debug() -> bool:
    return logging.getLogger("qm").level <= logging.DEBUG
