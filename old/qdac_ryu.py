# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 16:42:27 2023

@author: Ryutaro Matsuoka, Tatsuya Matsuda
"""

from typing import Any
import pyvisa
from warnings import warn
from time import sleep
import signal
import numpy as np


class DelayedKeyboardInterrupt:
    def __enter__(self):
        self.signal_received = False
        #         self.old_handler = signal.signal(signal.SIGINT, self.handler)
        try:
            self.old_handler = signal.getsignal(signal.SIGINT)
            signal.signal(signal.SIGINT, self.handler)
        except:
            pass

    def handler(self, sig, frame):
        self.signal_received = (sig, frame)
        print("SIGINT received. Delaying KeyboardInterrupt.")

    def __exit__(self, type, value, traceback):
        #         signal.signal(signal.SIGINT, self.old_handler)
        try:
            signal.signal(signal.SIGINT, self.old_handler)
        except ValueError:
            pass
        if self.signal_received:
            self.old_handler(*self.signal_received)


class Qdac2Channel:
    def __init__(self, parent, channel: int, debug=False, name=None):
        self._parent = parent
        self._channel = channel
        if name is None:
            self.name = str(channel)
        self.channel = f"ch{channel:02}"
        self.parent_name = self._parent.name
        self.instr = parent.instr
        self.warn_comm_err = parent.warn_comm_err
        self._query = parent._query
        self._write = parent._write
        self._read = parent._read

        self.generator_mode = "FIX"
        self._voltage_range = self.voltage_range
        self._voltage_filter = self.voltage_filter
        self.voltage_offset = 0
        self._voltage = self.voltage
        if self._voltage:
            print(f"Caution: {self.name}({self.channel}) voltage is {self._voltage}!!!")
        # self.wait_time = 1e-3 #sec
        # self.step = 10e-3 #V
        self.slew_rate = 10
        # Read currnet setting
        # self._current_sens = self.current_sens
        # self._read_number = self.read_number
        self._current_range = "none"
        self._aperture = "none"
        self._nplc = "none"
        # self._opc = self.opc #None for Qdac2
        # Others
        self._voltage_limit = [-2, 2]
        self._list_voltage = None

    # def __setattr__(self, name, value):
    #     if name in self.set_list or isinstance(getattr(self.__class__, name, None), property):
    #         super().__setattr__(name, value)
    #     elif not hasattr(self, name):
    #         raise AttributeError(f'Cannot set attribute: {name}')
    #     else:
    #         raise AttributeError(f'Cannot set attribute: {name} (exception for {self.set_list})')

    @property
    def number(self):
        return self._channel

    @property
    def voltage_range(self):
        self._voltage_range = self._query(f"SOUR{self._channel}:RANG?")
        return self._voltage_range

    @voltage_range.setter
    def voltage_range(self, val):
        if val in ("H", "h", "High", "HIGH", "high", 10):
            self._write(f"SOUR{self._channel}:RANG HIGH ")
            self._voltage_range = "HIGH"
        elif val in ("L", "l", "Low", "LOW", "low", 2):
            if self.voltage > 2:
                raise Exception(
                    f"ch{self._channel} {self.name}: The current voltage setpoint {self.voltage} V is out of"
                    + f"the specified range (-2, 2) V!!!"
                )
            if np.max(self.voltage_limit) > 2 or np.min(self.voltage_limit) < -2:
                raise Exception(
                    f"ch{self._channel} {self.name}: The current voltage limit {self.voltage_limit} is out of"
                    + f"the specified range (-2, 2) V!!!"
                )
            self._write(f"SOUR{self._channel}:RANG LOW ")
            self._voltage_range = "LOW"
        else:
            raise Exception(
                f"ch{self._channel} {self.name}: Invalid voltage range: {val}!!!"
            )

    @property
    def voltage_limit(self):
        return self._voltage_limit

    @voltage_limit.setter
    def voltage_limit(self, vals: list):
        if not len(vals) == 2:
            raise Exception(
                f"ch{self._channel} {self.name}: Invalid voltage limit: {vals}"
            )
        voltage_limit_max = 10 if self.voltage_range == "HIGH" else 3
        if np.max([abs(val) for val in vals]) > voltage_limit_max:
            raise Exception(
                f"ch{self._channel} {self.name}:  The specified voltage limit {vals} is out of"
                + f"the current voltage range (-{voltage_limit_max}, {voltage_limit_max}) V!!!"
            )
        self._voltage_limit = vals

    @property
    def voltage_filter(self):
        self._voltage_filter = self._query(f"SOUR{self._channel}:FILT?")
        return self._voltage_filter

    @voltage_filter.setter
    def voltage_filter(self, filter_type):
        if filter_type in ("DC", "dc", "Low", "LOW", "low", 10):
            self._write(f"SOUR{self._channel}:FILT DC ")
            self._voltage_filter = "DC"
        elif filter_type in ("MED", "Med", "med", 10e3):
            self._write(f"SOUR{self._channel}:FILT MED ")
            self._voltage_filter = "MID"
        elif filter_type in ("High", "HIGH", "high", 100e3):
            self._write(f"SOUR{self._channel}:FILT HIGH ")
            self._voltage_filter = "HIGH"
        else:
            raise Exception(
                f"ch{self._channel} {self.name}: Invalid voltage filter: {filter_type}"
            )

    @property
    def generator_mode(self):
        self._generator_mode = self.instr.query(f"SOUR{self._channel}:DC:MODE? ")
        return self._generator_mode

    @generator_mode.setter
    def generator_mode(self, val: str):
        valid_modes = ("FIX", "SWE", "LIST")
        if val.upper() in valid_modes:
            self._write(f"SOUR{self._channel}:DC:MODE {val.upper()} ")
            self._generator_mode = val.upper()
        else:
            valid_modes_str = ", ".join(valid_modes)
            raise ValueError(
                f"ch{self._channel} {self.name}: Invalid generator_mode {val}."
                f"Valid values are: {valid_modes_str}"
            )

    # def _set_voltage(self, val):
    #     self._write(f'SOUR{self._channel}:VOLT {val}')
    #     # if not self.slew_rate == 'INF':
    #     #     sleep(abs(self._voltage-val)/self._slew_rate)
    #     return self._voltage
    # def _set_voltage(self, val):
    #     while abs(val - self._voltage) > self.step:
    #         self._voltage =  self._voltage + (2*(val>self._voltage)-1)*self.step
    #         self._write(f'SOUR{self._channel}:VOLT {self._voltage + self.voltage_offset}')
    #         # self._write(f'SOUR{self._channel}:VOLT {self._voltage}')
    #         sleep(self.wait_time)
    #     self._write(f'SOUR{self._channel}:VOLT {val}')
    # self._voltage = val

    @property
    def voltage(self):
        mode_tmp = self.generator_mode
        if not mode_tmp == "FIX":
            self.generator_mode = "FIX"
        self._voltage = (
            float(self.instr.query(f"SOUR{self._channel}:VOLT? ")) - self.voltage_offset
        )
        # self._voltage = float(self.instr.query(f'SOUR{self._channel}:VOLT? '))
        if not mode_tmp == "FIX":
            self.generator_mode = mode_tmp
        return self._voltage

    @voltage.setter
    def voltage(self, val: float):
        if not np.min(self.voltage_limit) <= val <= np.max(self.voltage_limit):
            raise Exception(
                f"ch{self._channel}{self.name}: The specified value {val} is out of"
                + f"the limit range ({self.voltage_limit})!!!"
            )
        if str(self._slew_rate) == "INF":
            raise Exception(f"ch{self._channel}{self.name}: The slew rate is INF!!!")
        # self._set_voltage(val)
        mode_tmp = self.generator_mode
        if not mode_tmp == "FIX":
            self.generator_mode = "FIX"
        self._write(f"SOUR{self._channel}:VOLT {val + self.voltage_offset}")
        self._voltage = val
        if not mode_tmp == "FIX":
            self.generator_mode = mode_tmp

    @property
    def slew_rate(self):
        self._slew_rate = float(self._query(f"SOUR{self._channel}:VOLT:SLEW?"))
        return self._slew_rate

    @slew_rate.setter
    def slew_rate(self, val):
        min = 0.01
        max = 2e7
        if isinstance(val, str):
            if val.upper() in ("INF", "Default", "default"):
                self._write(f"SOUR{self._channel}:VOLT:SLEW INF")
                self._slew_rate = "INF"
            else:
                raise Exception(f"{self.channel} {self.name}: Invalid command!!!")
        elif min <= float(val) <= max:
            self._write(f"SOUR{self._channel}:VOLT:SLEW {val}")
            self._slew_rate = val
        else:
            raise Exception(
                f"ch{self._channel}{self.name}: The specified value {val} is out of"
                + f"the limit range ({min}, {max}) V/sec!!!"
            )

    # -------List voltage context-------
    @property
    def list_count(self):
        return self._query(f"SOUR{self._channel}:LIST:COUN?")

    @list_count.setter
    def list_count(self, val):
        self.generator_mode = "LIST"
        self._write(f"SOUR{self._channel}:LIST:COUN {val}")

    @property
    def list_voltage(self):
        vals_str = self._query(f"SOUR{self._channel}:LIST:VOLT?")
        vals_float = [
            float(value.strip()) for value in vals_str.split(",") if value.strip()
        ]
        self._list_voltage = np.array(vals_float)
        return self._list_voltage

    @list_voltage.setter
    def list_voltage(self, vals: list):
        self.generator_mode = "LIST"
        if np.min(self.voltage_limit) > np.min(vals) or np.max(vals) > np.max(
            self.voltage_limit
        ):
            raise Exception(
                f"ch{self._channel}{self.name}: The specified value {np.min(vals)},{np.min(vals)} is out of"
                + f"the limit range ({self.voltage_limit})!!!"
            )
        if len(vals) > 1023:
            raise Exception(
                f"ch{self._channel}{self.name}: The specified number of values {len(vals)} is out of"
                + f"the limit range 1023!!!"
                + f"Use list_append() command to extend the list or use the binary format for large lists."
            )
        vals_str = ", ".join(map(str, vals))
        self._write(f"SOUR{self._channel}:LIST:VOLT {vals_str}")
        self._list_voltage = vals

    def list_append(self, vals: list):
        if self._list_voltage is None:
            raise ValueError(
                f"ch{self._channel}{self.name}: Specify the voltage list before this command."
            )
        if np.min(self.voltage_limit) > np.min(vals) or np.max(vals) > np.max(
            self.voltage_limit
        ):
            raise ValueError(
                f"ch{self._channel}{self.name}: The specified value {np.min(vals)},{np.min(vals)} is out of"
                + f"the limit range ({self.voltage_limit})!!!"
            )
        vals_str = ", ".join(map(str, vals))
        self._write(f"SOUR{self._channel}:LIST:VOLT:APP {vals_str}")
        self._list_voltage = self.list_voltage

    @property
    def list_dwell(self):
        self._list_dwell = self._query(f"SOUR{self._channel}:LIST:DWEL?")
        return self._list_dwell

    @list_dwell.setter
    def list_dwell(self, val):
        if self._list_voltage is None:
            raise Exception(
                f"ch{self._channel}{self.name}: Specify the voltage list before this command."
            )
        min = 2e-6
        max = 36000
        if not min <= float(val) <= max:
            raise Exception(
                f"ch{self._channel}{self.name}: The specified value {val} is out of"
                + f"the limit range ({min}, {max}) sec!!!"
            )
        if np.max(np.diff(self.list_voltage)) / val > self.slew_rate:
            raise Exception(
                f"ch{self._channel}{self.name}: The specified value {val} makes"
                + f"the list voltage sweep {np.max(np.diff(self.list_voltage))/val} V/sec"
                + f"faster than the slew rate {self.slew_rate} V/sec!!!"
            )
        self._write(f"SOUR{self._channel}:LIST:DWEL {val}")
        self._list_dwell = val

    @property
    def list_dirction(self):
        return self._query(f"SOUR{self._channel}:LIST:DIR?")

    @list_dirction.setter
    def list_dirction(self, val: str):
        if val in ("DOWN", "Down", "down"):
            self._write(f"SOUR{self._channel}:LIST:DIR DOWN")
        elif val in ("UP", "Up", "up"):
            self._write(f"SOUR{self._channel}:LIST:DIR UP")
        else:
            raise ValueError(
                f"ch{self._channel} {self.name}: Invalid list dirction: {val}"
            )

    @property
    def list_points(self):
        return self._query(f"SOUR{self._channel}:LIST:POIN?")

    @property
    def trigger_mode(self):
        self._trigger_mode = self._query(f"SOUR{self._channel}:LIST:TMODE?")
        return self._trigger_mode

    @trigger_mode.setter
    def trigger_mode(self, val):
        if val in ("STEP", "Step", "step"):
            self._write(f"SOUR{self._channel}:LIST:TMODE STEP")
            self._trigger_mode = "STEP"
        elif val in ("AUTO", "Auto", "auto"):
            self._write(f"SOUR{self._channel}:LIST:TMODE AUTO")
            self._trigger_mode = "AUTO"
        else:
            raise Exception(
                f"ch{self._channel} {self.name}: Invalid trigger mode: {val}"
            )

    # -------Trigger context-------
    def abort(self):
        self._write(f"SOUR{self._channel}:ALL:ABOR")

    @property
    def trigger_source(self):
        self._trigger_source = self._query(f"SOUR{self._channel}:DC:TRIG:SOUR?")
        return self._trigger_source

    @trigger_source.setter
    def trigger_source(self, val: str):
        if val in self._parent.trigger_list or val in ["HOLD", "BUS", "IMM"]:
            self._write(f"SOUR{self._channel}:DC:TRIG:SOUR {val}")
            self._trigger_source = val
        else:
            raise Exception(
                f"{self.channel} {self.name}: Invalid trigger source {val}!!!"
            )

    def fire_imm(self):
        if not self._trigger_source == "IMM":
            raise Exception(f"{self.channel} {self.name}: Trigger source is not IMM!!!")
        self._write(f"SOUR{self._channel}:DC:INIT")

    def standby(self):
        if self._trigger_source == "IMM":
            raise Exception(f"{self.channel} {self.name}: Trigger source is IMM!!!")
        self._write(f"SOUR{self._channel}:DC:INIT")

    @property
    def contuinuous(self):
        self._contuinuous = self._query(f"SOUR{self._channel}:DC:INIT:CONT?")
        return self._contuinuous

    @contuinuous.setter
    def contuinuous(self, val):
        val = str(val)
        if val in ("1", "ON", "on"):
            # if self._trigger_source == 'IMM':
            #     raise Exception(f"{self.channel} {self.name}: Trigger source is not IMM!!!")
            self._write(f"SOUR{self._channel}:DC:INIT:CONT ON")
            self._contuinuous = "ON"
        elif val in ("0", "OFF", "off"):
            self._write(f"SOUR{self._channel}:DC:INIT:CONT OFF")
            self._contuinuous = "OFF"
        else:
            raise Exception(f"ch{self._channel} {self.name}: Invalid value {val}")

    @property
    def trigger_delay(self):
        self._trigger_delay = self._query(f"SOUR{self._channel}:DC:DEL?")
        return self._trigger_delay

    @trigger_delay.setter
    def trigger_delay(self, val):
        min = 0
        max = 3600
        if min <= val <= max:
            self._write(f"SOUR{self._channel}:DC:DEL {val}")
            self._trigger_delay = val
        else:
            raise Exception(
                f"ch{self.channel} {self.name}: The specified triggrer delay {val} is out of"
                + f"the valid range (0, 3600) sec!!!"
            )

    def reset_trigger(self):
        self.abort()
        self.trigger_source = "IMM"
        self.contuinuous = "OFF"
        self.trigger_delay = 0
        self.start_marker = 0
        self.end_marker = 0
        self.pstart_marker = 0
        self.pend_marker = 0
        self.sstart_marker = 0
        self.send_marker = 0

    def trigger_setting(self):
        return {
            "source": self.trigger_source,
            "contuinuous": self.contuinuous,
            "delay": self.trigger_delay,
            "start_marker": self.start_marker,
            "end_marker": self.end_marker,
            "pstart_marker": self.pstart_marker,
            "pend_marker": self.pend_marker,
            "sstart_marker": self.sstart_marker,
            "send_marker": self.send_marker,
        }

    @property
    def start_marker(self):
        """
        The STARt MARKer occurs when the specified generator starts.
        """
        self._start_marker = self._query(f"SOUR{self._channel}:DC:MARK:STAR?")
        return self._start_marker

    @start_marker.setter
    def start_marker(self, intrig_num: int):
        max = 14
        min = 0
        if not max >= intrig_num >= min:
            raise Exception(
                f"ch{self._channel} {self.name}: Invalid internal trriger {intrig_num}"
            )
        self._write(f"SOUR{self._channel}:DC:MARK:STAR {intrig_num}")
        self._start_marker = intrig_num

    @property
    def end_marker(self):
        """
        The END MARKer occurs when the specified generator ENDs.
        (after completing its specified periods, COUNt, or when ABORted)
        """
        self._end_marker = self._query(f"SOUR{self._channel}:DC:MARK:END?")
        return self._end_marker

    @end_marker.setter
    def end_marker(self, intrig_num: int):
        max = 14
        min = 0
        if not max >= intrig_num >= min:
            raise Exception(
                f"ch{self._channel} {self.name}: Invalid internal trriger {intrig_num}"
            )
        self._write(f"SOUR{self._channel}:DC:MARK:END {intrig_num}")
        self._end_marker = intrig_num

    """
    PSTART & PEND don't work!!!!!
    """
    # @property
    # def pstart_marker(self):
    #     """
    #     The PSTart MARKer event occurs whenever a new cycle of one of the waveform generators begins.
    #     """
    #     self._pstart_marker = self._query(f'SOUR{self._channel}:DC:MARK:PST?')
    #     return self._pstart_marker
    # @pstart_marker.setter
    # def pstart_marker(self, intrig_num:int):
    #     max = 14
    #     min = 0
    #     if not max>=intrig_num>=min:
    #         raise Exception(f"ch{self._channel} {self.name}: Invalid internal trriger {intrig_num}")
    #     self._write(f'SOUR{self._channel}:DC:MARK:PST {intrig_num}')
    #     self._pstart_marker = intrig_num

    # @property
    # def pend_marker(self):
    #     """
    #     The PEND MARKer event occurs whenever a cycle of one of the waveform generators ends.
    #     """
    #     self._pend_marker = self._query(f'SOUR{self._channel}:DC:MARK:PEND?')
    #     return self._pend_marker
    # @pend_marker.setter
    # def pend_marker(self, intrig_num:int):
    #     max = 14
    #     min = 0
    #     if not max>=intrig_num>=min:
    #         raise Exception(f"ch{self._channel} {self.name}: Invalid internal trriger {intrig_num}")
    #     self._write(f'SOUR{self._channel}:DC:MARK:PEND {intrig_num}')
    #     self._pend_marker = intrig_num

    @property
    def sstart_marker(self):
        """
        The SSTart MARKer event occurs when a new value of the DC generator is set
        and is usually used in LIST or SWEep mode.
        """
        self._sstart_marker = self._query(f"SOUR{self._channel}:DC:MARK:SST?")
        return self._sstart_marker

    @sstart_marker.setter
    def sstart_marker(self, intrig_num: int):
        max = 14
        min = 0
        if not max >= intrig_num >= min:
            raise Exception(
                f"ch{self._channel} {self.name}: Invalid internal trriger {intrig_num}"
            )
        self._write(f"SOUR{self._channel}:DC:MARK:SST {intrig_num}")
        self._sstart_marker = intrig_num

    @property
    def send_marker(self):
        """
        The SEND MARKer event occurs when dwell time is reached for a DC generator
        iteration in LIST or SWEep mode
        """
        self._send_marker = self._query(f"SOUR{self._channel}:DC:MARK:SEND?")
        return self._send_marker

    @send_marker.setter
    def send_marker(self, intrig_num: int):
        max = 14
        min = 0
        if not max >= intrig_num >= min:
            raise Exception(
                f"ch{self._channel} {self.name}: Invalid internal trriger {intrig_num}"
            )
        self._write(f"SOUR{self._channel}:DC:MARK:SEND {intrig_num}")
        self._send_marker = intrig_num

    # -------Current sensing context-------
    @property
    def current_range(self):
        self._current_range = self._query(f"SENS{self._channel}:RANG?")
        return self._current_range

    @current_range.setter
    def current_range(self, val):
        if val in ("H", "h", "High", "HIGH", "high", 10e-3):
            self._write(f"SENS{self._channel}:RANG HIGH ")
            self._current_range = "HIGH"
        elif val in ("L", "l", "Low", "LOW", "low", 200e-9):
            self._write(f"SENS{self._channel}:RANG LOW ")
            self._current_range = "LOW"
        else:
            raise Exception(
                f"ch{self._channel} {self.name}: Invalid current range: {val}"
            )

    @property
    def aperture(self):
        self._aperture = self._query(f"SENS{self._channel}:APER?")
        return self._aperture

    @aperture.setter
    def aperture(self, val):
        min = 0.33e-3
        max = 2.0
        if not min <= val <= max:
            raise Exception(
                f"ch{self._channel}{self.name}: The specified value {val} is out of"
                + f"the limit range ({min}, {max}) sec!!!"
            )
        else:
            self._write(f"SENS{self._channel}:APER {val}")
            self._aperture = val

    @property
    def nplc(self):
        self._nplc = self._query(f"SENS{self._channel}:NPLC?")
        return self._nplc

    @nplc.setter
    def nplc(self, val):
        min = 0.01667
        max = 100
        if not min <= val <= max:
            raise Exception(
                f"ch{self._channel}{self.name}: The specified value {val} is out of"
                + f"the limit range ({min}, {max}) sec!!!"
            )
        self._nplc = self._write(f"SENS{self._channel}:NPLC {val}")

    def prep_readCurrent(self):
        self.current_range = "LOW"
        self.aperture = 0.02
        self.nplc = 1.0
        # print('Do not allow more than 200 nA of current to flow through the channel.')

    def readCurrent(self):
        return float(self._query(f"READ{self._channel}?"))

    @property
    def curr_cal_A(self):
        self._curr_cal_A = float(
            self._query(f"DIAG:ICAL{self._channel}:{self._current_range}:A?")
        )
        return self._curr_cal_A

    @curr_cal_A.setter
    def curr_cal_A(self, val):
        if val > 1 or val < -1 or val == 0:
            raise ValueError("Invalid value for curr_cal_A")
        self._write(f"DIAG:ICAL{self._channel}:{self._current_range}:A {val}")
        self._curr_cal_A = val
        # self._write(f'DIAG:CAL:UPD') #This command wll cause LED to flash red !!!

    @property
    def curr_cal_B(self):
        self._curr_cal_B = float(
            self._query(f"DIAG:ICAL{self._channel}:{self._current_range}:B?")
        )
        return self._curr_cal_B

    @curr_cal_B.setter
    def curr_cal_B(self, val):
        if val > 1 or val < -1:
            raise ValueError("Invalid value for curr_cal_B")
        self._write(f"DIAG:ICAL{self._channel}:{self._current_range}:B {val}")
        self._curr_cal_B = val
        # self._write(f'DIAG:CAL:UPD') #This command wll cause LED to flash red !!!

    # @property
    # def setting(self):
    #     return {key: getattr(self, key)
    #             for key in self.__dict__.keys()
    #             if key not in {'warn_comm_err', '_query', '_read', '_write', '_parent', 'instr', '_channel'}
    #             and getattr(self, key, 'none') != 'none'
    #             }

    @property
    def setting(self):
        settings = {}
        for key in self.__dict__.keys():
            # 特定の属性を除外する
            if key in {
                "warn_comm_err",
                "_query",
                "_read",
                "_write",
                "_parent",
                "instr",
                "_channel",
            }:
                continue
            value = getattr(self, key)
            # 属性の値が配列である場合の処理
            if isinstance(value, np.ndarray):
                if value.any():  # 配列のいずれかの要素がTrueの場合
                    settings[key] = value.tolist()  # 配列をリストに変換して追加
            else:
                settings[key] = value  # 配列以外の場合はそのまま追加
        return settings


class Qdac2Trigger:
    def __init__(self, parent, channel: str, debug=False, name=None):
        self.parent = parent
        self.channel = channel
        self.name = channel if name is None else name
        self.connection = []

        self.instr = parent.instr
        self.warn_comm_err = parent.warn_comm_err
        self._query = parent._query
        self._write = parent._write
        self._read = parent._read

        if self.channel.startswith("EXT"):
            """
            Note that the trigger output pulses appear approximately 1µs
            before the marker position of the voltage generator output
            due to different delays (phase shifts) in the analogue circuits.
            """
            self.delay = 1e-6
            self._width = self.width
            self._polarity = self.polarity
            self._source = self.source

    def reset_trigger(self):
        if not self.channel.startswith("INT"):
            self.source = "HOLD"
            self.width = 10e-6
            self.polarity = "NORM"
            self.delay = 1e-6
        self.connection = []

    def trigger_setting(self):
        return {
            "source": self.source,
            "delay": self.delay,
            "width": self.width,
            "polarity": self.polarity,
            "delay": self.delay,
        }

    def fire(self):
        if not self.channel.startswith("INT"):
            raise Exception(f"{self.channel} {self.name}: Invalid command!!!")
        self._write(f"TINT {int(self.name[3:])}")

    @property
    def source(self):
        if self.channel.startswith("INT"):
            raise Exception(f"{self.channel} {self.name}: Invalid command!!!")
        self._source = self._query(f"OUTP:TRIG{int(self.name[3:])}:SOUR?")
        return self._source

    @source.setter
    def source(self, val):
        if self.channel.startswith("INT"):
            raise Exception(f"{self.channel} {self.name}: Invalid command!!!")
        if val in self.parent.trigger_list or val in ["HOLD", "BUS"]:
            self._write(f"OUTP:TRIG{int(self.name[3:])}:SOUR {val}")
            self._source = val
            self.connection.append(val)
        else:
            raise Exception(f"{self.channel} {self.name}: Invalid source {val}!!!")

    @property
    def width(self):
        if self.channel.startswith("INT"):
            raise Exception(f"{self.channel} {self.name}: Invalid command!!!")
        self._width = self._query(f"OUTP:TRIG{int(self.name[3:])}:WIDTH?")
        return self._width

    @width.setter
    def width(self, val):
        if self.channel.startswith("INT"):
            raise Exception(f"{self.channel} {self.name}: Invalid command!!!")
        min = 1e-6
        max = 3600
        if min <= val <= max:
            self._write(f"OUTP:TRIG{int(self.name[3:])}:WIDTH {val}")
            self._width = val
        else:
            raise Exception(
                f"ch{self.channel} {self.name}: The specified triggrer width {val} is out of"
                + f"the valid range (1e-6, 3600) sec!!!"
            )

    @property
    def polarity(self):
        if self.channel.startswith("INT"):
            raise Exception(f"{self.channel} {self.name}: Invalid command!!!")
        self._polarity = self._query(f"OUTP:TRIG{int(self.name[3:])}:POL?")
        return self._polarity

    @polarity.setter
    def polarity(self, val):
        if self.channel.startswith("INT"):
            raise Exception(f"{self.channel} {self.name}: Invalid command!!!")
        if val in ("NORM", "Norm", "norm", "NORMAL", "Normal", "normal"):
            self._write(f"OUTP:TRIG{int(self.name[3:])}:POL NORM")
            self._polarity = "NORM"
        elif val in ("INV", "Inv", "inv"):
            self._write(f"OUTP:TRIG{int(self.name[3:])}:POL INV")
            self._polarity = "INV"
        else:
            raise Exception(
                f"{self.channel} {self.name}: Invalid trigger polarity {val}!!!"
            )

    @property
    def delay(self):
        if self.channel.startswith("INT"):
            raise Exception(f"{self.channel} {self.name}: Invalid command!!!")
        self._delay = self._query(f"OUTP:TRIG{int(self.name[3:])}:DEL?")
        return self._delay

    @delay.setter
    def delay(self, val):
        if self.channel.startswith("INT"):
            raise Exception(f"{self.channel} {self.name}: Invalid command!!!")
        min = 0
        max = 3600
        if min <= val <= max:
            self._write(f"OUTP:TRIG{int(self.name[3:])}:DEL {val}")
            self._delay = val
        else:
            raise Exception(
                f"ch{self.channel} {self.name}: The specified triggrer delay {val} is out of"
                + f"the valid range (0, 3600) sec!!!"
            )


class Qdac2:
    def __init__(self, addr: str, name: str, channelnum=24, debug=False):
        rm = pyvisa.ResourceManager("")
        self._debug = debug
        self.addr = addr
        self.name = name
        self.channelnum = channelnum
        self.instr = rm.open_resource(
            self.addr, write_termination="\n", read_termination="\n"
        )
        # Set baudrate and stuff for serial communication only
        if self.addr.find("ASRL") != -1:
            self.instr.baud_rate = 921600
            self.instr.send_end = False

        # for ch in range(self.channelnum):
        #     self.f'ch{ch:02}' = Qdac2Channel(self, f'ch{ch:02}', ch)

        # self._channel = {f'ch{ch:02}':Qdac2Channel(self, f'ch{ch:02}', ch) for ch in range(1, 24+1)}
        self._channel = {}
        self.set_list = []
        self.warn_comm_err("check before init")
        self.trigger_list = {}

    # @property
    # def opc(self):
    #     with DelayedKeyboardInterrupt():
    #         self._opc = int(self.instr.query('*OPC?'))
    #     return self._opc

    # def wait_for_opc(self, max_wait = 1):
    #     interval, count = 1e-3, 0
    #     while self.opc!=1 and interval*count < max_wait:
    #         sleep(interval)
    #         count += 1

    def warn_comm_err(self, command):
        if command == "check before init":
            i = 0
            try:
                while True:
                    with DelayedKeyboardInterrupt():
                        print(self.instr.read())  # Receive all unread replies.
                        # print(self.instr.query('*IDN?'))
            except pyvisa.VisaIOError:
                with DelayedKeyboardInterrupt():
                    self.instr.query("SYST:ERR?")  # Should raise -420 error
        # self.wait_for_opc(1.)
        while True:
            with DelayedKeyboardInterrupt():
                err = self.instr.query("SYST:ERR?")
            # if err != '0,"No error"':
            if not err.find("No error") == -1:
                break
            else:
                print(f"SYST:ERR? -> {err}")
                warn(f"{self.name} reported {err} for {command}.")

    def _query(self, command):
        with DelayedKeyboardInterrupt():
            ans = self.instr.query(command)
        if self._debug:
            print(f"{command} -> {ans}")
            self.warn_comm_err(command)
        return ans

    def _write(self, command):
        with DelayedKeyboardInterrupt():
            self.instr.write(command)
        if self._debug:
            print(command)
            self.warn_comm_err(command)

    def _read(self):
        with DelayedKeyboardInterrupt():
            ans = self.instr.read()
        if self._debug:
            print(f"-> {ans}")
            self.warn_comm_err("read")
        return ans

    # def channel(self, ch: int):
    #     return self._channel[f'ch{ch:02}']

    # def __getattr__(self, name):
    #     if name in self._channel:
    #         return self._channel[name]
    #     else:
    #         raise AttributeError
    #         (f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def __getattr__(self, name):
        if name in self._channel:
            return self._channel[name]
        elif name in self.trigger_list:
            return self.trigger_list[name]
        elif name.startswith("ch") and name[2:].isdigit():
            ch = int(name[2:])
            if 1 <= ch <= 24:
                return self._channel.setdefault(
                    f"ch{ch:02}", Qdac2Channel(self, ch, f"ch{ch:02}")
                )
            raise Exception(
                f"The specified value {name} is out of" + "the range (1, 24) ch!!!"
            )
        elif name.startswith("INT") and name[3:].isdigit():
            ch = int(name[3:])
            if 1 <= ch <= 14:
                return self.trigger_list.setdefault(
                    f"INT{ch}", Qdac2Trigger(self, f"INT{ch}", f"INT{ch}")
                )
            raise Exception(
                f"The specified value {name} is out of" + "the range (1, 14) ch!!!"
            )
        elif name.startswith("EXT") and name[3:].isdigit():
            ch = int(name[3:])
            if 1 <= ch <= 5:
                return self.trigger_list.setdefault(
                    f"EXT{ch}", Qdac2Trigger(self, f"EXT{ch}", f"EXT{ch}")
                )
            raise Exception(
                f"The specified value {name} is out of" + "the range (1, 5) ch!!!"
            )
        else:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )

    # def __setattr__(self, name, value):
    #     if name in self.set_list or isinstance(getattr(self.__class__, name, None), property):
    #         super().__setattr__(name, value)
    #     elif not hasattr(self, name):
    #         raise AttributeError(f'Cannot set attribute: {name}')
    #     else:
    #         raise AttributeError(f'Cannot set attribute: {name} (exception for {self.set_list})')
    # -------Multich operation context-------
    @property
    def all_voltages(self):
        voltages = {f"{ch.name} ({i}) ": ch.voltage for i, ch in self._channel.items()}
        return voltages

    @all_voltages.setter
    def all_voltages(self, voltage):
        for ch_name in self._channel:
            self._channel[ch_name].voltage = voltage

    def set_multiCh(self, settings_dict):
        """
        Args:
            settings_dict (dict):
                ex: {'ch01': {'voltage': 2.0, 'voltage_range': 'LOW'},
                     'ch02': {'voltage': 3.5, 'voltage_range': 'HIGH'}}
        """
        for ch_name, settings in settings_dict.items():
            if ch_name not in self._channel:
                raise ValueError(f"Invalid channel name: {ch_name}")
            channel = self._channel[ch_name]
            for key, value in settings.items():
                if not hasattr(channel, key):
                    raise ValueError(f"Invalid setting: {key}")
                setattr(channel, key, value)

    def multich_voltage(self, voltage_dict):
        """
        Args:
            voltage_dict (dict):
                ex: {'ch01': 0.1,'ch02': 0.3}
        """
        for ch_name, val in voltage_dict.items():
            channel_names = {value.name: value for key, value in self._channel.items()}
            if ch_name in self._channel:
                channel = self._channel[ch_name]
            elif ch_name in channel_names:
                channel = channel_names[ch_name]
            else:
                raise ValueError(f"Invalid channel name: {ch_name}")
            channel.voltage = val

    def read_multich(self, ch_list):
        channels = ",".join(f"@{ch}" for ch in ch_list)
        response = self._query(f"READ?({channels})")
        currents = {
            f"ch{ch:02}": float(value)
            for ch, value in zip(ch_list, response.strip().split(","))
        }
        return currents

    # -------Trigger context-------
    def reset_trigger(self):
        for ch_name, ch in self._channel.items():
            ch.reset_trigger()
        for trig_name, trig in self.trigger_list.items():
            trig.reset_trigger()

    # -------Others-------
    def settings(self, ch_list="all"):
        """
        Args:
            ch_name (str): ex: 'ch01', 'ch02' or "all"
        Returns:
            dict or dict of dicts:
        """
        if ch_list == "all":
            return {
                ch_name: {
                    k: getattr(self._channel[ch_name].setting, k)
                    for k in self._channel[ch_name].__dict__.keys()
                }
                for ch_name in self._channel.keys()
            }
        elif isinstance(ch_list, list):
            return {
                ch_name: {
                    k: getattr(self._channel[ch_name].setting, k)
                    for k in self._channel[ch_name].__dict__.keys()
                }
                for ch_name in ch_list
            }
        else:
            raise ValueError(
                "Invalid input for ch_names. Use 'all' or a list of channel names."
            )

    def reset(self) -> None:
        self._write("*rst")
        sleep(5.0)

    def errors(self) -> str:
        return self._query("syst:err:all?")

    def close(self) -> None:
        self.instr.close()

    # def sweep_1D(self, vals: list, gate: list, sweep_freq: float, ext_trigger:str, int_trigger:str, n_rep = 1, tigger_voltage = 1, ):
    #     slew_list = [g.slew_rate for g in gate]
    #     voltage_lim_list = [np.max([np.min(g.voltage_limit) for g in gate]), np.min([np.man(g.voltage_limit) for g in gate])]
    #     for g in gate:
    #         g.generator_mode = 'LIST'
    #         g.list_count = n_rep
    #         g.list_voltage = vals
    #         g.list_dwell = 1/sweep_freq*len(vals)
    #         g.list_dirction = 'UP'
    #         g.trriger_mode = 'AUTO'
    #         g.contuinuous = 'OFF'

    # def sweep_2D(self, x_vals: list, y_vals:list, x_gate: list, y_gate: list, sweep_freq: float, outer_trigger:str, n_rep = 1, tigger_voltage = 1, ):
    #     for g in x_gate:
    #         g.generator_mode = 'LIST'
    #         g.list_count = n_rep
    #         g.list_voltage = x_vals
    #         g.list_dwell = 1/sweep_freq*len(x_vals)
    #         g.list_dirction = 'UP'
    #         g.trriger_mode = 'AUTO'
    # g.contuinuous = 'ON'

    #     for g in x_gate:
    #         g.generator_mode = 'LIST'
    #         g.list_count = n_rep
    #         g.list_voltage = y_vals
    #         g.list_dwell = g.
    #         g.list_dirction = 'UP'
    #         g.trriger_mode = 'STEP'
