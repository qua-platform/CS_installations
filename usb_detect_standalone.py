# Requirements: pyserial, pyvisa, pyvisa-py

import sys
import pyvisa as visa
import serial.tools.list_ports as list_ports
import serial
import re
from dataclasses import dataclass
from typing import Sequence, Tuple, Optional
from platform import system as platform_system


@dataclass
class Device:
    kind: str
    signature: str
    baud_rate: int


devices = [
    # The order is important
    Device('QDAC-II', '0403:6014', 921600),
    Device('QSwitch', '04D8:00DD', 9600),
]


def find_qdac2_on_usb(backend='@py') -> visa.Resource:
    device = devices[0]
    handle = find_serial_device(device)
    if not handle:
        raise ValueError('No device found')
    if os_platform() == 'windows':
        if handle[:3].lower() == 'com':
            handle = handle[3:]
    return find_visa_device(f'ASRL{handle}::INSTR', 'QDAC-II')


def find_qswitch_on_usb(backend='@py') -> visa.Resource:
    device = devices[1]
    handle = find_serial_device(device)
    if not handle:
        raise ValueError('No device found')
    if os_platform() == 'windows':
        if handle[:3].lower() == 'com':
            handle = handle[3:]
    return find_visa_device(f'ASRL{handle}::INSTR', 'QSwitch')


def find_visa_device(address, description, backend='@py') -> visa.Resource:
    rm = resource_manager(backend)
    for tries in range(40):
        try:
            return rm.open_resource(address)
        except ValueError:
            break
        except visa.VisaIOError:
            print(f'Retrying connection to {address}')
    raise ValueError(f'{description} device with address {address} not found')


def resource_manager(backend=None) -> visa.ResourceManager:
    if backend:
        return visa.ResourceManager(backend)
    return visa.ResourceManager()  # Use default NI backend


def os_platform() -> str:
    os_type = platform_system()
    if os_type == 'Linux':
        return 'linux'
    if os_type == 'Darwin':
        return 'macos'
    if os_type == 'Windows':
        return 'windows'
    return 'unkown_os'


def find_serial_device(device: Device) -> Optional[str]:
    candidates = list(list_ports.grep(device.signature))
    if len(candidates) == 1:
        return candidates[0].device
    if len(candidates) > 1:
        raise ValueError('More than one device with signature '
                         f'{device.signature} found')
    return None


def find_serial_devices() -> Sequence[Tuple[Device, str]]:
    result = []
    for device in devices:
        handle = find_serial_device(device)
        if handle:
            result.append((device, handle))
    if not result:
        raise ValueError('No devices found')
    return result


def get_id(connection):
    raw = bytes('*idn?\n', 'utf8')
    connection.write(raw)
    data = connection.read(40)
    answer = data.decode('utf-8')
    match = re.search('[^\n]+', answer)
    return match[0]


def get_ip_addr(connection):
    raw = bytes('syst:comm:lan:ipad?\n', 'utf8')
    connection.write(raw)
    data = connection.read(30)
    answer = data.decode('utf-8')
    match = re.search('[0-9.]+', answer)
    return match[0]


def get_mac_addr(connection):
    raw = bytes('syst:comm:lan:mac?\n', 'utf8')
    connection.write(raw)
    data = connection.read(30)
    answer = data.decode('utf-8')
    match = re.search('[0-9A-F:]+', answer)
    return match[0]


def get_gateway(connection):
    raw = bytes('syst:comm:lan:gat?\n', 'utf8')
    connection.write(raw)
    data = connection.read(30)
    answer = data.decode('utf-8')
    match = re.search('[0-9.]+', answer)
    return match[0]


def get_mask(connection):
    raw = bytes('syst:comm:lan:smas?\n', 'utf8')
    connection.write(raw)
    data = connection.read(30)
    answer = data.decode('utf-8')
    match = re.search('[0-9.]+', answer)
    return match[0]


def get_name(connection):
    raw = bytes('syst:comm:lan:host?\n', 'utf8')
    connection.write(raw)
    data = connection.read(30)
    answer = data.decode('utf-8')
    match = re.search('[^"]+', answer)
    return match[0]


def get_dhcp(connection):
    raw = bytes('syst:comm:lan:dhcp?\n', 'utf8')
    connection.write(raw)
    data = connection.read(3)
    return (float(data.decode('utf-8')) == 1)


def report_device_info():
    for device, serial_info in find_serial_devices():
        print(f'Found: {device.kind}')
        print(f'Port: {serial_info}')
        connection = serial.Serial(serial_info, device.baud_rate, timeout=0.2)
        id = get_id(connection)
        print(f'identification: {id}')
        mac_addr = get_mac_addr(connection)
        print(f'MAC address: {mac_addr}')
        gateway = get_gateway(connection)
        print(f'Gateway: {gateway}')
        mask = get_mask(connection)
        print(f'Network mask: {mask}')
        ip_addr = get_ip_addr(connection)
        print(f'IP address: {ip_addr}')
        name = get_name(connection)
        print(f'Host name: {name}')
        dhcp = 'yes' if get_dhcp(connection) else 'no'
        print(f'DHCP enabled: {dhcp}')
        print('')

if __name__ == '__main__':
    try:
        report_device_info()
        sys.exit(0)
    except Exception as error:
        print(f'Error: {error}')
        sys.exit(1)
