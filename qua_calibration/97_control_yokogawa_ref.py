#ref: https://microsoft.github.io/Qcodes/examples/driver_examples/Qcodes%20example%20with%20Yokogawa%20GS2xx.html
#!/usr/bin/env python
# coding: utf-8

# # QCoDeS Example with Yokogawa GS200/GS210

# In[1]:


import time

from qcodes.instrument_drivers.yokogawa import YokogawaGS200


# In[2]:


gs = YokogawaGS200(
    "gs200", address="USB::0xB21::0x39::91RB18719::INSTR", terminator="\n"
)


# The instrument turns on in the 'VOLT' mode:

# In[3]:


gs.source_mode()


# The mode can be changed to 'CURR' via source_mode:

# In[4]:


gs.source_mode("CURR")
gs.source_mode()


# If the instrument is reconnected without turning it off and on, it will be connected with the previous session's mode:

# In[5]:


gs.close()
gs = YokogawaGS200(
    "gs200", address="USB::0xB21::0x39::91RB18719::INSTR", terminator="\n"
)
gs.source_mode()


# The source_mode can only be changed when the output is 'off'. By default the
# output is off and there is no actual current is flowing:

# In[6]:


gs.output()


# Setting/ getting attributes/ methods of a mode ('VOLT' or 'CURR') is only possible if the source_mode is in that mode (in this case, we are in the'CURR' mode and trying to access voltage attributes/ methods):

# In[7]:


try:
    gs.voltage(0.1)  # Set the voltage
    print("Something has gone wrong.")
except Exception:
    print("Exception correctly raised.")

try:
    gs.voltage()  # Get the voltage
    print("Something has gone wrong.")
except Exception:
    print("Exception correctly raised.")

try:
    gs.voltage_range(10)  # Set the voltage_range
    print("Something has gone wrong.")
except Exception:
    print("Exception correctly raised.")

try:
    gs.voltage_range()  # Get the voltage_range
    print("Something has gone wrong.")
except Exception:
    print("Exception correctly raised.")

try:
    gs.ramp_voltage(5, 1, 1)  # Get the voltage_range
    print("Something has gone wrong.")
except Exception:
    print("Exception correctly raised.")


# We can set/ get current attributes in the 'CURR' mode:

# In[8]:


gs.current_range()


# In[9]:


gs.current(0.001)


# Snapshotting interactively changes when the source_mode is changed (voltage and voltage_range are excluded from snapshot in the 'CURR' mode and vice versa):

# In[10]:


gs.snapshot()


# By default, auto_range is in False state. So, setting voltage or current is
# limitted to the present voltage_range or current_range:

# In[11]:


gs.auto_range()


# In[12]:


gs.current_range(0.01)
try:
    gs.current(0.009)
    print("The current value is withing the present current_range")
except Exception:
    print("Exception incorrectly raised.")

try:
    gs.current(0.1)
    print("Something has gone wrong.")
except Exception:
    print(
        f"Exception is correctly raised. The value is out of the present "
        f"range of {gs.current_range()} A."
    )


# auto_range can be used to set the value even if the value is out of the
# present range. If the value exceeds the present range, the range automatically switches to the higher range tier untill the maximum allowed limit is reached (0.2 A for current and 30 V for voltage).
# auto_range can be useful when one wants to ramp the value without worrying about the end value to be out of the present range. We ramp the current from 0.009 A to 0.02 A with the step of 0.001 A (delay between each step is set to 1 second) and time it. Our present range is 0.01 A, so we expect the range automatically switches to 0.1 A because of auto_range is True.

# In[13]:


gs.auto_range(True)
gs.current(0.009)
gs.current_range()


# In[14]:


t1 = time.time()
gs.ramp_current(0.02, 0.001, 1)
t2 = time.time()
print(f"Ramping took {t2 - t1:.4} seconds")


# In[15]:


gs.current()


# In[16]:


gs.current_range()


# Now, we turn off auto_range and set the current value out of the present range
# to test if we correctly get an error

# In[17]:


gs.auto_range(False)


# In[18]:


try:
    gs.current(0.15)
    print("Something has gone wrong")
except Exception:
    print(
        f"Exception is correctly raised. The value is out of the present "
        f"range of {gs.current_range()} A."
    )


# Now, we want to test the ramping in the False state of auto_range. We expect the ramping to stop when we exceed the range and we get out of range error:

# In[19]:


gs.auto_range(False)
gs.current(0.007)
gs.current_range(0.01)


# In[20]:


try:
    gs.ramp_current(0.02, 0.001, 1)
except Exception:
    print(
        f"Exception is correctly raised. Ramping is stopped at {gs.current()} A because the"
        " range is exceeded"
    )


# Now, we switch to the 'VOLT' mode and test a few things:
# 

# In[21]:


gs.source_mode("VOLT")


# In[22]:


gs.voltage()


# In[23]:


gs.voltage_range()


# In[24]:


gs.auto_range()


# We can look at the voltage_limit and current_limit limit in any source_mode:

# In[25]:


gs.current_limit()


# In[26]:


gs.voltage_limit()


# Now, we turn on the output to test if we see the correct output (in the 'CURR' and 'VOLT' mode, the voltage_limit and current_limit is active, respectively):

# In[27]:


gs.output("on")


# We can verify that our multileter is reading 0.2 A. Now, we change the current_limit and test again:

# In[28]:


gs.current_limit(0.1)


# As expected, the multimeter is reading 0.1 A.

# In[29]:


gs.output("off")


# In[30]:


gs.close()


# In[ ]:



