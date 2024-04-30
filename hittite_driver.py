import socket

class HittiteHMCT2220:
    def __init__(self, ip_address, port=56789):
        self.ip_address = ip_address
        self.port = port
        self.sock = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip_address, self.port))
        self.sock.settimeout(5)

    def disconnect(self):
        if self.sock:
            self.sock.close()
            self.sock = None

    def send_command(self, command):
        command += "\n"
        self.sock.send(command.encode())

    def query(self, command):
        self.send_command(command)
        response = self.sock.recv(1024).decode().strip()
        return response

    def set_frequency(self, freq, unit="Hz"):
        command = f":FREQ {freq}{unit}"
        self.send_command(command)

    def get_frequency(self):
        return float(self.query(":FREQ?"))

    def set_power(self, power):
        command = f":PWR {power}"
        self.send_command(command)

    def get_power(self):
        return float(self.query(":PWR?"))

    def set_output_state(self, state):
        state_str = "ON" if state else "OFF"
        command = f":OUTP {state_str}"
        self.send_command(command)

    def get_output_state(self):
        return self.query(":OUTP?") == "ON"

    def set_frequency_mode(self, mode):
        if mode.upper() not in ["CW", "FIXED", "SWEEP", "LIST"]:
            raise ValueError("Invalid frequency mode")
        command = f":FREQ:MODE {mode}"
        self.send_command(command)

    def get_frequency_mode(self):
        return self.query(":FREQ:MODE?")

    def set_power_mode(self, mode):
        if mode.upper() not in ["FIX", "SWEEP", "LIST"]:
            raise ValueError("Invalid power mode")
        command = f":POW:MODE {mode}"
        self.send_command(command)

    def get_power_mode(self):
        return self.query(":POW:MODE?")

    def set_sweep_dwell_time(self, dwell_time):
        command = f":SWE:DWEL {dwell_time}"
        self.send_command(command)

    def get_sweep_dwell_time(self):
        return float(self.query(":SWE:DWEL?"))

    def set_sweep_direction(self, direction):
        if direction.upper() not in ["UP", "DOWN"]:
            raise ValueError("Invalid sweep direction")
        command = f":SWE:DIR {direction}"
        self.send_command(command)

    def get_sweep_direction(self):
        return self.query(":SWE:DIR?")

    def set_frequency_sweep_start(self, start_freq):
        command = f":FREQ:STAR {start_freq}"
        self.send_command(command)

    def set_frequency_sweep_stop(self, stop_freq):
        command = f":FREQ:STOP {stop_freq}"
        self.send_command(command)

    def set_frequency_sweep_step(self, step_freq):
        command = f":FREQ:STEP {step_freq}"
        self.send_command(command)

    def set_power_sweep_start(self, start_power):
        command = f":POW:STAR {start_power}"
        self.send_command(command)

    def set_power_sweep_stop(self, stop_power):
        command = f":POW:STOP {stop_power}"
        self.send_command(command)

    def set_power_sweep_step(self, step_power):
        command = f":POW:STEP {step_power}"
        self.send_command(command)

    def initiate_sweep(self):
        self.send_command(":INIT")

    def abort_sweep(self):
        self.send_command(":ABOR")
# class HittiteWrapper(GPIBDeviceWrapper):
#     async def initialize(self) -> None:
#         pass

#     async def get_frequency(self) -> Value:
#         frequency_Hz_str = await self.query("SOUR:FREQ?", retry=True)
#         return float(frequency_Hz_str) * Hz

#     async def set_frequency(self, f: Value) -> None:
#         await self.write(f"SOUR:FREQ:FIX {f[Hz]:f}", retry=True)

#     async def get_amplitude(self) -> Value:
#         amplitude_dBm_str = await self.query("SOUR:POW:LEV:AMPL?", retry=True)
#         return float(amplitude_dBm_str) * dBm

#     async def set_amplitude(self, a: Value) -> None:
#         await self.write(f"SOUR:POW:LEV:IMM:AMPL {a[dBm]:f}", retry=True)

#     async def get_output(self) -> bool:
#         output_str = await self.query("OUTP:STAT?", retry=True)
#         return int(output_str) == 1

#     async def set_output(self, out: bool) -> None:
#         await self.write(f"OUTP:STAT {int(out):d}", retry=True)

#     async def get_status(self) -> int:
#         status_str = await self.query("*STB?", retry=True)
#         return int(status_str)

#     async def ext_ref_detected(self) -> bool:
#         return "EXT" == await self.query("SOUR:ROSC:SOUR?", retry=True)