#%%
# Example code to control the QDAC II in Manual
import pyvisa as visa

class QDAC_II():
    ADDRESS = 'ASRL3::INSTR'  # Example VISA address for serial communication
    def __init__(self, visa_addr=ADDRESS, lib=''):
        rm = visa.ResourceManager(lib) # To use pyvisa-py backend, use argument lib='@py'
        self._visa = rm.open_resource(visa_addr)
        self._visa.write_termination = '\n'
        self._visa.read_termination = '\n'
        # Set baudrate and stuff for serial communication only
        if (visa_addr.find("ASRL") != -1):
            self._visa.baud_rate = 921600
            self._visa.send_end = False
    def query(self, cmd):
        return self._visa.query(cmd)
    def write(self, cmd):
        self._visa.write(cmd)
    def write_binary_values(self, cmd, values):
        self._visa.write_binary_values(cmd, values)
    def __exit__(self):
        self.close()


#%%
rm = visa.ResourceManager('') # To use pyvisa-py backend, use argument '@py'
# List connected instruments. Instruments on LAN are often not shown.
rm.list_resources()


#%%
q = QDAC_II(visa_addr = "ASRL15::INSTR", lib = '') 
# To use the ethernet port please replace visaAddress by the appropriate 
# address in the form of: visaAddress = "TCPIP::192.168.8.197::5025::SOCKET")

#%%
print(q.query('*IDN?'))
print(q.query("syst:err:all?"))

#%%
# Start a 20kHz sine with 1V pp on ch1
q.write("sour1:sine:freq 20000")
q.write("sour1:sine:span 1")
q.write("sour1:sine:count inf")
q.write("sour1:sine:trig:sour IMM")
q.write("sour1:sine:init")

#%%
# Stop the sine generator
q.write("sour1:sine:abort")
# Set a DC voltage of 0.2 V on ch2 - ch5
q.write("sour:volt 0.2,(@2:5)")
