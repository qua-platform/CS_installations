"""
QDAC-II LAN Setup & Smoke Test
================================
Purpose:
- An end-to-end script to connect the QDAC-II via Ethernet (LAN), verify communication with PyVISA, and then transition to the QCoDeS driver. Detailed comments are provided for customer delivery.

Prerequisites (Mandatory):
1) Python 3.9+ recommended
2) Package installation:
    pip install pyvisa
    # If using the NI-VISA backend (recommended): Install NI-VISA driver (https://www.ni.com/visa)
    # If using the pure Python backend (@py):
    pip install pyvisa-py
    # If using the QCoDeS driver as well:
    pip install qcodes qcodes_contrib_drivers

Network/Equipment Notes:
- The Ethernet cable can be connected (hot-plugged) even when the instrument power is on (port galvanic isolation design).
  However, if using DHCP, the instrument might not automatically obtain an IP "after connecting the cable," potentially requiring a restart (or SCPI 'SYST:REStart').
- While Labber might be connected via USB (ASRLx), this script connects only via LAN.
  Avoid "simultaneous control" from two clients (risk of global command collision).
- The default TCP/IP SCPI port for the QDAC-II is socket 5025.

Usage Examples:
python qdac2_lan_setup_and_test.py --ip 192.168.8.17 --backend @py
python qdac2_lan_setup_and_test.py --ip 192.168.8.17 --backend @ni --qcodes

Options:
--ip        : QDAC-II IP Address (Mandatory)
--backend   : Select PyVISA backend. '@ni' (NI-VISA) or '@py' (pyvisa-py). Default: @py
--qcodes    : Flag to also connect the QCoDeS driver and run a simple example
--timeout   : VISA timeout (ms), default 10000
--idn-only  : Check connection/IDN/errors only, skip waveform examples
--static-ip : Attempt to set a static IP instead of DHCP (e.g., --static-ip 192.168.8.17 --mask 255.255.255.0 --gw 192.168.8.1)
--mask      : Subnet mask when using --static-ip
--gw        : Gateway when using --static-ip

Safety Guide:
- This script uses safe DC levels of about 0.2 V and a short sine wave for testing on the output channels.
- If experimental apparatus is connected, **always verify circuit safety** before executing output commands.
"""

import argparse
import time
import socket

# --- PyVISA ---
import pyvisa

# QCoDeS is optionally imported (only when flag is used)
try:
    from qcodes_contrib_drivers.drivers.QDevil import QDAC2 as QDAC2_driver
    QCODeS_AVAILABLE = True
except Exception:
    QCODeS_AVAILABLE = False


def make_tcpip_socket_visa_address(ip: str) -> str:
    """Generates the QDAC-II LAN (VISA SOCKET) address format."""
    return f"TCPIP0::{ip}::5025::SOCKET"


def ping_host_quick(ip: str, timeout=2.0) -> bool:
    """A very simple check for TCP 5025 port openness (instead of ICMP ping).
        Since VISA may connect even if this fails depending on router policy, it is for 'reference' only."""
    try:
        with socket.create_connection((ip, 5025), timeout=timeout):
            return True
    except Exception:
        return False


def connect_pyvisa(ip: str, backend: str, timeout_ms: int):
    """Connects to QDAC-II LAN with PyVISA and returns the session handle."""
    visa_addr = make_tcpip_socket_visa_address(ip)
    rm = pyvisa.ResourceManager(backend)  # '@ni' or '@py'
    inst = rm.open_resource(visa_addr)
    inst.write_termination = '\n'
    inst.read_termination = '\n'
    inst.timeout = timeout_ms
    return rm, inst


def scpi_query(inst, cmd: str) -> str:
    """Safe query (to avoid overwriting exception messages)"""
    return inst.query(cmd)


def scpi_write(inst, cmd: str):
    inst.write(cmd)


def ensure_dhcp_or_static(inst, static_ip=None, mask=None, gw=None):
    """
    IP configuration helper:
    - If static_ip is provided, set DHCP OFF + IP/MASK/GW configuration + LAN:UPDate + REStart
    - Otherwise, attempt to query current settings/address only
    """
    if static_ip:
        if not (mask and gw):
            raise ValueError("When setting a static IP, --mask and --gw must also be specified.")
        # Units/format are standard SI units according to the manual, LAN commands use string arguments
        scpi_write(inst, "SYST:COMM:LAN:DHCP OFF")
        scpi_write(inst, f"SYST:COMM:LAN:IPAD {static_ip}")
        scpi_write(inst, f"SYST:COMM:LAN:SMAS {mask}")
        scpi_write(inst, f"SYST:COMM:LAN:GATE {gw}")
        scpi_write(inst, "SYST:COMM:LAN:UPD")  # Save settings and restart LAN
        # Restart the instrument for network changes to take effect
        scpi_write(inst, "SYST:REStart")
        print("[INFO] Static IP configuration and restart command sent. Waiting briefly during reboot (approx. 20-40 seconds).")
        time.sleep(40)
        return

    # Query DHCP/current IP (not critical if it fails)
    try:
        dhcp = scpi_query(inst, "SYST:COMM:LAN:DHCP?")
        ipad = scpi_query(inst, "SYST:COMM:LAN:IPAD?")
        host = scpi_query(inst, "SYST:COMM:LAN:HOST?")
        print(f"[INFO] DHCP: {dhcp.strip()}, IP: {ipad.strip()}, HOST: {host.strip()}")
    except Exception as e:
        print(f"[WARN] Failed to query LAN settings: {e}")


def idn_and_errors(inst):
    """Check *IDN? and the error buffer."""
    idn = scpi_query(inst, "*IDN?")
    print(f"[OK] *IDN?: {idn.strip()}")
    try:
        errs = scpi_query(inst, "SYST:ERR:ALL?")
        print(f"[OK] SYST:ERR:ALL?: {errs.strip()}")
    except Exception as e:
        print(f"[WARN] Failed to query errors: {e}")


def minimal_waveform_demo(inst):
    """Smoke test with a short sine wave & DC output (safe range)."""
    print("[INFO] Starting simple waveform demo (sine wave ch1, DC ch2~ch5=0.2V).")
    # Sine wave: 20 kHz, 1 Vpp (span=1), continuous, immediate trigger
    scpi_write(inst, "SOUR1:SINE:FREQ 20000")
    scpi_write(inst, "SOUR1:SINE:SPAN 1")
    scpi_write(inst, "SOUR1:SINE:COUNT INF")
    scpi_write(inst, "SOUR1:SINE:TRIG:SOUR IMM")
    scpi_write(inst, "SOUR1:SINE:INIT")
    time.sleep(0.5)

    # DC configuration (safe 0.2 V example)
    scpi_write(inst, "SOUR:VOLT 0.2,(@2:5)")
    time.sleep(0.5)

    # Status check
    idn_and_errors(inst)

    # Stop and restore to 0V
    scpi_write(inst, "SOUR1:SINE:ABOR")
    scpi_write(inst, "SOUR:VOLT 0,(@1:24)")
    print("[OK] Demo complete. All channels restored to 0V.")


def connect_qcodes(ip: str, backend: str):
    """Verifies QCoDeS driver connection (+get_idn)."""
    if not QCODeS_AVAILABLE:
        raise RuntimeError("qcodes / qcodes_contrib_drivers are not installed. pip install qcodes qcodes_contrib_drivers")
    addr = f"TCPIP::{ip}::5025::SOCKET"
    qdac = QDAC2_driver.QDac2("QDAC2", visalib=backend, address=addr)
    print("[OK] QCoDeS connection complete:", qdac.get_idn())
    return qdac


def qcodes_demo(qdac):
    """Simple QCoDeS demo: ch1 sine wave / start_all -> stop and restore to 0V."""
    print("[INFO] Starting QCoDeS sine wave demo (ch1 10 kHz / 1 Vpp).")
    qdac.ch01.sine(frequency=10e3, amplitude=0.5)  # amplitude=Vpp/2
    qdac.start_all()
    time.sleep(1.0)
    # Status/error check
    print("[OK] IDN:", qdac.get_idn())
    print("[OK] ERR:", qdac.errors())
    # Stop and restore to 0V
    qdac.stop_all()
    for ch in range(1, 25):
        getattr(qdac, f"ch{ch:02d}").dc(0.0)
    print("[OK] QCoDeS demo complete. All channels restored to 0V.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ip", required=True, help="QDAC-II IP address (e.g., 192.168.8.17)")
    ap.add_argument("--backend", default="@py", choices=["@py", "@ni"], help="PyVISA backend ('@py' or '@ni'). Default: @py")
    ap.add_argument("--timeout", type=int, default=10000, help="VISA timeout in ms. Default: 10000")
    ap.add_argument("--idn-only", action="store_true", help="Run only IDN/error checks (skip waveform demos)")
    ap.add_argument("--qcodes", action="store_true", help="Also test QCoDeS driver after PyVISA")
    ap.add_argument("--static-ip", help="Set static IP (disables DHCP). Example: --static-ip 192.168.8.17")
    ap.add_argument("--mask", help="Subnet mask when --static-ip is used. Example: 255.255.255.0")
    ap.add_argument("--gw", help="Gateway when --static-ip is used. Example: 192.168.8.1")
    args = ap.parse_args()

    ip = args.ip
    backend = args.backend

    print(f"[INFO] Target IP: {ip}, VISA backend: {backend}")
    if not ping_host_quick(ip):
        print("[WARN] TCP:5025 port pre-check failed (reference warning). Check network policy/firewall/cable/power status.")

    # 1) PyVISA Connection
    rm, inst = connect_pyvisa(ip, backend, args.timeout)
    try:
        # 2) IDN/Error Check
        idn_and_errors(inst)

        # 3) DHCP/Static IP Handling (Optional)
        ensure_dhcp_or_static(inst, static_ip=args.static_ip, mask=args.mask, gw=args.gw)

        # 4) Smoke Test
        if not args.idn_only:
            minimal_waveform_demo(inst)

    finally:
        try:
            inst.close()
        except Exception:
            pass
        try:
            rm.close()
        except Exception:
            pass

    # 5) QCoDeS Driver Connection/Test (Optional)
    if args.qcodes:
        qdac = connect_qcodes(ip, backend)
        try:
            if not args.idn_only:
                qcodes_demo(qdac)
        finally:
            try:
                qdac.close()
            except Exception:
                pass

    print("[DONE] All procedures complete.")


if __name__ == "__main__":
    main()

"""
## Additional Operation Tips

* If you are in a **DHCP environment**: If the IP isn't obtained immediately after connecting the cable, send `SYST:REStart` once.
* The **LAN socket port** is 5025, and message delay can be up to several milliseconds (synchronization with a query immediately after the command is recommended).
* **Concurrent sessions** are possible, but global commands like `*RST` can affect other sessions, so separate your operation procedures.

If needed, I can also provide a version that extends this script to include **USB (ASRL) initialization/firmware updates/and `SYST:COMM:LAN:*` batch setup parts**.
"""