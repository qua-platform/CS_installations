# %%
from time import sleep

import matplotlib.pyplot as plt
import numpy as np
import pyvisa as visa
from IPython.display import Image, display
from qcodes_contrib_drivers.drivers.QDevil import QDAC2

##########################
# Ethernet communication #
##########################
# insert IP
qdac_ipaddr = "192.168.8.36"
# open communication
qdac = QDAC2.QDac2("QDAC", visalib="@py", address=f"TCPIP::{qdac_ipaddr}::5025::SOCKET")
# check the communication with the QDAC
print(qdac.IDN())  # query the QDAC's identity
sleep(3)
print(qdac.errors())  # read and clear all errors from the QDAC's error queue

# %%
####################
# 2D voltage sweep #
####################

inner_steps = 21  # define the voltage steps
inner_V = np.linspace(-0.3, 0.4, inner_steps)
outer_steps = 21  # define the voltage steps
outer_V = np.linspace(-0.2, 0.5, outer_steps)
inner_step_time = 5e-3

# define the plunger gates
arrangement = qdac.arrange(
    contacts={"p1": 2, "p2": 4},
    # Internal trigger for measuring current
    internal_triggers={"inner"},
)
sleep(1)

# # Add virtual gates corrections
# arrangement.initiate_correction("p1", [0.9, 0.1])
# arrangement.initiate_correction("p2", [-0.2, 0.97])

sweep = arrangement.virtual_sweep2d(
    inner_contact="p1",
    inner_voltages=inner_V,
    outer_contact="p2",
    outer_voltages=outer_V,
    inner_step_time_s=inner_step_time,
    inner_step_trigger="inner",
)

# %%
# Set to starting voltage
arrangement.set_virtual_voltage("p1", inner_V[0])
arrangement.set_virtual_voltage("p2", outer_V[0])

# define the sensor parameters
sensor_channel = 5  # define sensing channel
sensor_integration_time = (
    1e-3  # define time [s] to integrate current over #NOTE: sensor integration time should be <= step_time
)
sensor_delay_time = 1e-3  # sensor_integration_time + sensor_delay_time should be <= inner_step_time
sensing_range = "low"  # low (max 150 nA, noise level ~10 pA) or high (max 10 mA, noise level ~1 uA) current range

# Set up the current sensor
sensor = qdac.channel(sensor_channel)  # choose the sensor channel
measurement = sensor.measurement(
    aperture_s=sensor_integration_time, delay_s=sensor_delay_time, current_range=sensing_range
)
sensor.clear_measurements()  # clear any remaining buffer of measurements
measurement = sensor.measurement()  # create a measurement instance for the sensor
measurement.start_on(arrangement.get_trigger_by_name("inner"))  # set the trigger that will start a measurement

# %%
# Start sweep
sweep.start()
# %%
sleep(inner_step_time * inner_steps * outer_steps + 1)
sleep(10)  # VPN delay
# qdac.ask("*stb?")


raw = measurement.available_A()
available = list(map(lambda x: float(x), raw[-(outer_steps * inner_steps) :]))
sensor.clear_measurements()
# Stop current flow
arrangement.set_virtual_voltage("p1", 0)
arrangement.set_virtual_voltage("p2", 0)

# plot
currents = np.reshape(available, (-1, inner_steps)) * 1000
fig, ax = plt.subplots()
plt.title("2D stability diagram")
extent = [inner_V[0], inner_V[-1], outer_V[0], outer_V[-1]]
img = ax.imshow(currents, cmap="plasma", interpolation="nearest", extent=extent)
ax.set_xlabel("Volt")
ax.set_ylabel("Volt")
colorbar = fig.colorbar(img)
colorbar.set_label("mA")

plt.show()

# free all internal triggers, 12 internal triggers are available
qdac.free_all_triggers()
# close to qdac instance so you can create it again.
# %%
qdac.close()


# %%
