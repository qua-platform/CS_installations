import requests

class HttpLocalOscillator():
    def __init__(self, host: str, port: int):
        if host == "None":
            self.address = None
        else:
            self.address = f"{host}:{port}"

    def _send_get_request(self, cmd: str):
        if self.address is not None:
            send = f'http://{self.address}/PWD?;{cmd}'
            return requests.post(send).content.decode()
        else:
            return ""

    def _send_set_request(self, cmd: str):
        if self.address is not None:
            send = f'http://{self.address}/PWD;{cmd}'
            return requests.post(send).content.decode()
        else:
            return ""

    # ________________Get Functions________________

    def get_SN(self):
        return self._send_get_request(':SN?').strip()

    def get_frequency(self):
        return print(float(self._send_get_request(':FREQ?')), ' MHz')

    def get_max_frequency(self):
        return float(self._send_get_request(':FREQ:MAX?'))

    def get_min_frequency(self):
        return float(self._send_get_request(':FREQ:MIN?'))

    def get_frequency_step(self):
        return float(self._send_get_request(':FREQ:STEP?'))

    def get_power(self):
        return float(self._send_get_request(':PWR?'))

    def get_max_power(self):
        return float(self._send_get_request(':PWR:MAX?'))

    def get_min_power(self):
        return float(self._send_get_request(':PWR:MIN?'))

    def get_rf_state(self):
        return self._send_get_request(':PWR:RF?').strip()

    def get_internal_temperature(self):
        return float(self._send_get_request(':TSENDOR?'))

    # ________________Set Functions________________

    def set_frequency(self, freq: float, units='HZ'):
        return self._send_set_request(f':FREQ:{freq}{units}')

    def set_power_dbm(self, gain: float):
        return self._send_set_request(f':PWR:{gain}')

    def set_rf_state(self, state: str):
        if (state != 'ON') and (state != 'OFF'):
            raise ValueError("State must be 'ON' or 'OFF'")
        return self._send_set_request(f':PWR:RF:{state}')

    # ________________Check Functions________________

    def check_frequency(self, freq: float):
        is_correct = freq == self.get_frequency()
        while not is_correct:
            self.set_frequency(freq)
            is_correct = freq == self.get_frequency()
        return is_correct

    def check_power(self, power: float):
        is_correct = power == self.get_power()
        while not is_correct:
            self.set_power(power)
            is_correct = power == self.get_power()
        return is_correct

    def check_rf_state(self):
        is_correct = 'ON' == self.get_rf_state()
        while not is_correct:
            self.set_rf_state('ON')
            is_correct = 'ON' == self.get_rf_state()
        return is_correct
