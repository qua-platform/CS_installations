import numpy as np
import matplotlib.pyplot as plt
from quam_libs.macros import qua_declaration, active_reset
import sys

# print(matplotlib.get_backend())
t = np.linspace(0, 100, 100)
plt.figure()
plt.plot(t, np.cos(2*np.pi*t/10))
plt.show()
print(t)
# sys.exit(0)
def is_ipython():
    try:
        __IPYTHON__
        return True
    except NameError:
        return False


# Usage
if is_ipython():
    print("Running in IPython environment")
else:
    print("Running in a regular Python kernel")

import sys


def is_interactive():
    return bool(sys.flags.interactive)


# Usage
if is_interactive():
    print("Running in interactive mode")
else:
    print("Running in non-interactive mode")


def is_interactive():
    return bool(sys.flags.interactive)


# Usage
if is_interactive():
    print("Running in interactive mode")
    sys.exit(0)
else:
    raise Exception("Running in non-interactive mode")

# %%
if True:
    print(True)
else:
    t = np.linspace(0, 100, 100)*2
    plt.figure()
    plt.plot(t, np.cos(2 * np.pi * t / 10))
    plt.show()
    print(t)

# %%