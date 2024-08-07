import asyncio
import copy
import dataclasses
import logging
import time
from pprint import PrettyPrinter
from typing import Optional, List, Dict

from grpclib.client import Channel, Configuration
from grpclib.events import SendRequest, listen
import betterproto
from octave_sdk.octave_async_thread import EventLoopThread, ConnectionDetails

from octave_sdk.batch import Batched, BatchSingleton
from octave_sdk.grpc.quantummachines.octave.api.v1 import (
    OctaveServiceStub,
    OctaveModule,
    ModuleReference,
    ControlRequest,
    UpdateRequest,
    SaveRequest,
    AquireRequest,
    RecallRequest,
    ListRequest,
    GetVersionRequest,
    MonitorRequest,
    ExploreRequest,
    IdentifyRequest,
    MonitorResponse,
    SingleUpdate,
    MonitorResponseModuleStatusError,
    ResetRequest,
    AquireResponse,
    ControlResponseRdataDebug,
)

logger = logging.getLogger("qm")

"""
# OctaveClient
#
#   This is a gRPC based Octave. The standard setup is the whole Octave product.
#   Namely, we access the SOM on its motherboard via ethernet and from there
#   communicate with all the boards via the main PIC.
#
#   A temporary alternative is using a mini SOM eval board which is connected
#   to a mini motherboard, directly into the serial lines of its PIC.
#
#   The specific variation is passed to the constructor.
"""


module_type_to_class = {
    OctaveModule.OCTAVE_MODULE_RF_UPCONVERTER: "rf_up_conv",
    OctaveModule.OCTAVE_MODULE_RF_DOWNCONVERTER: "rf_down_conv",
    OctaveModule.OCTAVE_MODULE_SYNTHESIZER: "synth",
    OctaveModule.OCTAVE_MODULE_IF_DOWNCONVERTER: "if_down_conv",
    OctaveModule.OCTAVE_MODULE_MOTHERBOARD: "motherboard",
}


class DebugSetException(Exception):
    pass


def _build_grpclib_channel(host, port, octave_name: Optional = None, credentials: Optional = None) -> Channel:
    channel = Channel(
        host=host,
        port=port,
        ssl=credentials is not None,
        config=Configuration(),
    )

    if octave_name is not None:

        async def send_request(event: SendRequest):
            event.metadata["x-grpc-service"] = octave_name

        listen(channel, SendRequest, send_request)

    return channel


@dataclasses.dataclass
class MonitorData:
    temp: float
    errors: List[MonitorResponseModuleStatusError]


class MonitorResult:
    def __init__(self, results_pb: MonitorResponse):
        self.modules: Dict[OctaveModule, List[MonitorData]] = {}
        self.modules = {
            OctaveModule.OCTAVE_MODULE_RF_UPCONVERTER: [None for _ in range(5)],
            OctaveModule.OCTAVE_MODULE_RF_DOWNCONVERTER: [None for _ in range(2)],
            OctaveModule.OCTAVE_MODULE_IF_DOWNCONVERTER: [None for _ in range(2)],
            OctaveModule.OCTAVE_MODULE_SYNTHESIZER: [None for _ in range(6)],
            OctaveModule.OCTAVE_MODULE_SOM: [None],
        }
        for module in results_pb.modules:
            self.modules[module.module.type][module.module.index - 1] = MonitorData(
                temp=module.temperature, errors=module.errors
            )

    def __repr__(self):
        pp = PrettyPrinter(width=150)
        return pp.pformat(self.modules)

    def __eq__(self, other):
        # Basically compare all elements except temp
        self_copy = copy.deepcopy(self)
        self._clear_temp_values(self_copy)
        other_copy = copy.deepcopy(other)
        self._clear_temp_values(other_copy)

        return self_copy.modules == other_copy.modules

    def _clear_temp_values(self, monitor_result):
        for module_list in monitor_result.modules.values():
            for monitor_data in module_list:
                if monitor_data is not None:
                    monitor_data.temp = 0


class ExploreResult:
    def __init__(self, results_pb):
        self.modules = {
            OctaveModule.OCTAVE_MODULE_RF_UPCONVERTER: [None for _ in range(5)],
            OctaveModule.OCTAVE_MODULE_RF_DOWNCONVERTER: [None for _ in range(2)],
            OctaveModule.OCTAVE_MODULE_IF_DOWNCONVERTER: [None for _ in range(2)],
            OctaveModule.OCTAVE_MODULE_SYNTHESIZER: [None for _ in range(6)],
            OctaveModule.OCTAVE_MODULE_MOTHERBOARD: [None for _ in range(1)],
        }
        for module in results_pb.modules:
            self.modules[module.module.type][module.module.index - 1] = module.id

    def __repr__(self):
        module_types = [
            OctaveModule.OCTAVE_MODULE_RF_UPCONVERTER,
            OctaveModule.OCTAVE_MODULE_RF_DOWNCONVERTER,
            OctaveModule.OCTAVE_MODULE_IF_DOWNCONVERTER,
            OctaveModule.OCTAVE_MODULE_SYNTHESIZER,
        ]

        m_id = self.modules[OctaveModule.OCTAVE_MODULE_MOTHERBOARD][0]
        if m_id is None or m_id == "":
            res = "MOTHERBOARD [\x1b[38;5;208m???\x1b[0m]\n"
        else:
            res = f"MOTHERBOARD [\x1b[38;5;154m{m_id}\x1b[0m]\n"

        res += "    RF_UPCONVs          RF_DOWNCONVs        IF_DOWNCONVs        " "SYNTHESIZERs\n"
        for index in range(6):
            res += "     "
            for t in module_types:
                if index < len(self.modules[t]):
                    m_id = self.modules[t][index]
                    if m_id is None:
                        res += f"\x1b[38;5;241m{index + 1}. {'---':17s}\x1b[0m"
                    elif m_id == "":
                        res += f"{index + 1}. \x1b[38;5;208m{'???':17s}\x1b[0m"
                    else:
                        res += f"{index + 1}. \x1b[38;5;154m{m_id:17s}\x1b[0m"
                else:
                    res += f"{'':20s}"
            res += "\n"
        return res


async def create_channel(details: ConnectionDetails) -> Channel:
    return Channel(
        host=details.host,
        port=details.port,
        ssl=details.credentials is not None,
        config=Configuration(
            http2_connection_window_size=details.max_message_size,
            http2_stream_window_size=details.max_message_size,
        ),
    )


class OctaveClient(Batched):
    def __init__(
        self, host: str, port: int, octave_name: str = None, connection_headers: Optional[Dict[str, str]] = None
    ) -> None:
        self._host = host
        self._port = port
        self._octave_name = octave_name
        self._event_loop = EventLoopThread().loop
        self._headers = connection_headers or {}
        super().__init__()

        self._channel = asyncio.run_coroutine_threadsafe(
            create_channel(ConnectionDetails(host, port)), loop=self._event_loop
        ).result()
        self._create_add_headers_event()
        self._service = OctaveServiceStub(self._channel)

    def _create_add_headers_event(self) -> None:
        async def add_headers(event: SendRequest) -> None:
            event.metadata.update(self._headers)

        listen(self._channel, SendRequest, add_headers)

    def __hash__(self) -> int:
        return hash((self._octave_name, self._host, self._port) + tuple(sorted(self._headers.items())))

    @property
    def name(self) -> str:
        return self._octave_name

    def __del__(self):
        self._service = None
        self._channel.close()

    def _control(self, w_data=b"", r_length=0):
        control_request = ControlRequest(w_data=w_data, r_length=r_length)
        future = asyncio.run_coroutine_threadsafe(self._service.control(control_request), loop=self._event_loop)
        return future.result()

    def _format_cached_modules(self, modules: AquireResponse):
        cached_modules = {}
        for update in modules.state.updates:
            module_type, message = betterproto.which_one_of(update, "update")

            if module_type not in ("clock", "motherboard"):
                update_id = message.index
            else:
                update_id = 0

            cache_key = (update_id, module_type)
            cached_modules[cache_key] = update
        BatchSingleton().set_cached_modules(self, cached_modules)

    def _start_batch_callback(self):
        self._format_cached_modules(self.aquire_modules([]))

    def _end_batch_callback(self):
        self._send_update(list(BatchSingleton().get_cached_updates(self).values()))

    def update(self, updates: List[SingleUpdate]):
        if BatchSingleton().is_batch_mode:
            for update in updates:
                self._cache_update(update)
        else:
            self._send_update(updates)

    def _cache_update(self, update: SingleUpdate):
        module_type, message = betterproto.which_one_of(update, "update")

        if module_type not in ("clock", "motherboard"):
            update_id = message.index
        else:
            update_id = 0

        cache_key = (update_id, module_type)
        current_updates = BatchSingleton().get_cached_updates(self)
        if current_updates.get(cache_key):
            previous_cached_update = getattr(current_updates.get(cache_key), module_type).to_dict()
        else:
            previous_cached_update = {}

        previous_cached_update.update(message.to_dict())
        message.from_dict(previous_cached_update)

        new_update = SingleUpdate()
        setattr(new_update, module_type, message)
        current_updates[cache_key] = new_update
        BatchSingleton().set_cached_updates(self, current_updates)

    def _send_update(self, updates: List[SingleUpdate]):
        update_request = UpdateRequest(updates=updates)
        future = asyncio.run_coroutine_threadsafe(self._service.update(update_request), loop=self._event_loop)
        response = future.result()
        if not response.success:
            raise Exception(f"Octave update failed: {response.error_message}")
        return response

    def debug_request_clock_print(self):
        self._control(
            w_data=bytes([0xFF, 0xB9]),
            r_length=1,
        )

    def debug_set(
        self,
        monitor_enabled: bool = None,
        monitor_timeout: int = None,
        monitor_print_rate: int = None,
        monitor_update_fan: bool = None,
        uart_debug_mode: bool = None,
        print_updates: bool = None,
        min_fan_speed: bool = None,
        min_temp: int = None,
        max_temp_modules: int = None,
        max_temp_fpga: int = None,
    ):
        if monitor_timeout is not None:
            if monitor_timeout < 1 or monitor_timeout > 15:
                print("OctaveClientBase.debug_set   ERROR    monitor_timeout should be" " 1..15")
                return
        else:
            monitor_timeout = 0x00

        if monitor_print_rate is not None:
            if monitor_print_rate < 0 or monitor_print_rate > 255:
                print(
                    "OctaveClientBase.debug_set   ERROR    monitor_print_rate should either 0 (no printings) or 1..255"
                )
                return

        activate = 0x00
        state = 0x00

        if monitor_enabled is not None:
            activate |= 0x01
            state |= 0x01 if monitor_enabled else 0x00

        if uart_debug_mode is not None:
            activate |= 0x02
            state |= 0x02 if uart_debug_mode else 0x00

        if print_updates is not None:
            activate |= 0x04
            state |= 0x04 if print_updates else 0x00

        if monitor_print_rate is not None:
            activate |= 0x08
        else:
            monitor_print_rate = 0

        if monitor_update_fan is not None:
            activate |= 0x10
            state |= 0x10 if monitor_update_fan else 0x00

        if min_fan_speed is not None:
            activate |= 0x20
            min_fan_speed = min(int(min_fan_speed), 31)
            state |= (min_fan_speed & 1) << 5
            monitor_timeout |= (min_fan_speed & 0x1E) << 3

        if min_temp is not None:
            if min_temp < 1 or min_temp > 60:
                print("OctaveClientBase.debug_set   ERROR    min_temp should be between 1 to 60")
                return
            activate |= 0x40
        else:
            min_temp = 0x00

        if (max_temp_modules and not max_temp_fpga) or (max_temp_fpga and not max_temp_modules):
            logger.error("max_temp_modules and max_temp_fpga must come in paris")
            return

        if max_temp_modules and max_temp_fpga:
            if max_temp_modules < 1 or max_temp_modules > 65:
                print("OctaveClientBase.debug_set   ERROR    max_temp_modlues should be between 1 to 65")
                return
            if max_temp_fpga < 1 or max_temp_fpga > 75:
                print("OctaveClientBase.debug_set   ERROR    max_temp_fpga should be between 1 to 75")
                return
            activate |= 0x80
        else:
            max_temp_modules = 0
            max_temp_fpga = 0

        control_payload_old: bytes = bytes(
            [
                0xFF,
                0xFF,
                activate,
                state,
                monitor_timeout,
                monitor_print_rate,
            ]
        )

        control_payload_new = control_payload_old + bytes(
            [
                min_temp,
                max_temp_modules,
                max_temp_fpga,
            ]
        )

        # Try new format
        res = (
            self._control(
                w_data=control_payload_new,
                r_length=1,
            )
        ).r_data
        res_int = int.from_bytes(res, "little")
        if res_int == ControlResponseRdataDebug.RDATA_DEBUG_SUCCESS_RESPONSE:
            return

        # Fall back to old format
        res = (
            self._control(
                w_data=control_payload_old,
                r_length=1,
            )
        ).r_data
        res_int = int.from_bytes(res, "little")
        if res_int != ControlResponseRdataDebug.RDATA_DEBUG_SUCCESS_RESPONSE:
            raise DebugSetException("Failed to set debug params")

    def save_modules(self, m_id: str = None, module_refs=None, overwrite=True):
        module_id = m_id or "default"
        module_references = module_refs if module_refs else []
        save_request = SaveRequest(
            id=module_id, modules=module_references, overwrite=overwrite, timestamp=int(time.time())
        )

        future = asyncio.run_coroutine_threadsafe(self._service.save(save_request), loop=self._event_loop)
        return future.result()

    def _fetch_aquire_from_cache(self, modules: List[ModuleReference]):
        res = AquireResponse(state=UpdateRequest(updates=[]))
        for module in modules:
            module_type = module_type_to_class[module.type]
            if module_type != "motherboard":
                update_id = module.index
            else:
                update_id = 0

            cache_key = (update_id, module_type)
            cached_modules = BatchSingleton().get_cached_modules(self)
            cached_updates = BatchSingleton().get_cached_updates(self)
            if cache_key in cached_modules:
                cached_module = cached_modules[cache_key].to_dict()
                cached_update = cached_updates.get(cache_key, SingleUpdate()).to_dict()

                cached_module.update(cached_update)
                new_update = SingleUpdate().from_dict(cached_module)
                res.state.updates.append(new_update)
        return res

    def aquire_modules(self, modules: List[ModuleReference], use_cache=True):
        if BatchSingleton().is_batch_mode:
            res = self._fetch_aquire_from_cache(modules)

        else:
            aquire_request = AquireRequest(modules=modules, use_cache=use_cache)
            future = asyncio.run_coroutine_threadsafe(self._service.aquire(aquire_request), loop=self._event_loop)
            res = future.result()

        if len(modules) == 1 and len(res.state.updates) == 1:
            return res.state.updates[0]

        return res

    def recall(self, m_id: str = None):
        recall_request = RecallRequest(id="default" if m_id is None else m_id)
        future = asyncio.run_coroutine_threadsafe(self._service.recall(recall_request), loop=self._event_loop)
        return future.result()

    def configs(self):
        future = asyncio.run_coroutine_threadsafe(self._service.list(ListRequest()), loop=self._event_loop)
        return future.result().save_infos

    def version(self):
        future = asyncio.run_coroutine_threadsafe(self._service.get_version(GetVersionRequest()), loop=self._event_loop)
        return future.result()

    def monitor(self, sense_only=True) -> MonitorResult:
        monitor_request = MonitorRequest(sense_only=sense_only)

        future = asyncio.run_coroutine_threadsafe(self._service.monitor(monitor_request), loop=self._event_loop)
        return MonitorResult(future.result())

    def explore(self):
        future = asyncio.run_coroutine_threadsafe(self._service.explore(ExploreRequest()), loop=self._event_loop)
        return ExploreResult(future.result())

    def identify(self):
        future = asyncio.run_coroutine_threadsafe(self._service.identify(IdentifyRequest()), loop=self._event_loop)
        return future.result()

    def reset(self) -> bool:
        future = asyncio.run_coroutine_threadsafe(self._service.reset(ResetRequest()), loop=self._event_loop)
        return future.result()

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def octave_name(self):
        return self._octave_name
