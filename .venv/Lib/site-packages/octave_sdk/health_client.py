import asyncio
import logging
import threading
from typing import Callable, Optional

import grpclib.exceptions
from grpclib.exceptions import StreamTerminatedError

from octave_sdk.octave_async_thread import EventLoopThread
from octave_sdk.grpc.quantummachines.octave.api.v1 import HealthRequest, GetVersionRequest

from octave_sdk._octave_client import OctaveClient, ExploreResult, MonitorResult

logger = logging.getLogger("qm")


NUM_CONNECTION_RETRIES = 3


class HealthClient:
    # Creates a constant gRPC stream to the Server, will call the "health_update_callback" on new health result
    # health_update_callback args should be (ExploreResult, MonitorResult)
    def __init__(
        self,
        interval: int,
        client: OctaveClient,
        health_update_callback: Callable[[ExploreResult, MonitorResult], None],
    ):
        self._interval = interval
        self._client = client
        self._callback = health_update_callback
        self._stream_running = False
        self._grace_stop = False
        self._connection_lost = 0

        self._future: Optional[asyncio.Task] = None

        self._stop_event = threading.Event()
        self._event_loop = EventLoopThread().loop

    def start(self):
        self._future = asyncio.run_coroutine_threadsafe(self._health_loop(), loop=self._event_loop)

    def stop(self):
        self._grace_stop = True
        self._stop_event.set()
        if self._future:
            self._future.cancel()

    async def _health_loop(self):
        while not self._stop_event.is_set():
            try:
                await self._health_monitor()
            except (asyncio.CancelledError, StreamTerminatedError, ConnectionRefusedError):
                pass
            except grpclib.exceptions.GRPCError as e:
                if e.status == grpclib.const.Status.UNIMPLEMENTED:
                    # In case of health monitor not implemented, we do not want to print messages of disconnection
                    logger.warning(f'Octave "{self._client.octave_name}" does not support live monitoring')
                    self._stream_running = False
                    return
            finally:
                if not self._grace_stop and self._stream_running:
                    self._connection_lost += 1
                    logger.error(f'Octave "{self._client.octave_name}" lost monitor connection')
                    if self._connection_lost == NUM_CONNECTION_RETRIES:
                        logger.error(f"Failed {NUM_CONNECTION_RETRIES} times to connect Octave aborting")

    async def _health_monitor(self):
        self._stream_running = False
        try:
            await self._client._service.get_version(GetVersionRequest())
            self._health_answers = self._client._service.health(
                HealthRequest(monitor_interval_seconds=self._interval, stop_stream=False)
            )
            self._stream_running = True
            if self._connection_lost:
                self._connection_lost = 0
                logger.info(f'Octave "{self._client.octave_name}" restored monitor connection')

            # FYI infinite loop here until server stream ends or task cancel
            async for response in self._health_answers:
                self._callback(ExploreResult(response.explore), MonitorResult(response.monitor))
        except (asyncio.CancelledError, StreamTerminatedError, ConnectionRefusedError):
            pass

    def run_once(self):
        explore_result = self._client.explore()
        monitor_result = self._client.monitor()
        self._callback(explore_result, monitor_result)
