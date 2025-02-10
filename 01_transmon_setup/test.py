import pyvisa

rm = pyvisa.ResourceManager()

IP_address = "192.168.2.2"
port = "5025"

qdac = rm.open_resource(f"TCPIP::{IP_address}::{port}::SOCKET")
qdac.baud_rate = 921600


qdac.write_termination = "\n"
qdac.read_termination = "\n"
print(qdac.query("*IDN?"))
print(qdac.query("syst:err:all?"))
qdac.write("syst:comm:lan:dhcp off")
print(qdac.query("syst:comm:lan:dhcp?"))

qdac.query("syst:comm:lan:ipad?")