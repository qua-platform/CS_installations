# N Flux-Tunable Transmon Qubits
## Installation
This folder contains an installable module called `quam_libs`, which provides a collection of tailored components for controlling flux-tunable qubits and experiment functionality. These components extend the functionality of QuAM, making it easier to design and execute calibration nodes.

### Requirements
To run the calibration nodes in this folder, you need to install `quam_libs`. First, ensure you have Python ≥ 3.8 installed on your system.
Then run the following command:

```sh
# Install quam_libs (locally, from this directory)
pip install .  
# The `-e` flag means you *don't* have to reinstall if you make a local change to `quam_libs`!
# pip install -e .

# Install qualibrate for Node structuring and front-end
pip install qualibrate-0.1.0.tar.gz

# Install pyqua-tools with wiring feature (if not in main yet)
pip install git+http://github.com/qua-platform/py-qua-tools.git@feature/auto_wiring

# Install qm-qua for the QUA SDK
pip install qm-qua==1.2.1a1
```
> **_NOTE:_**  The `-e` flag means you *don't* have to reinstall if you make a local change to `quam_libs`!

## Setup
The QuAM framework stores a database of calibration values in a collection of .json files. These files are generated when you run `make_quam.py`. In order to use them in experiment, you need to direct QuAM to the correct location. You can do this by creating an environment variable called `QUAM_STATE_PATH`, and setting its value to the directory of the `quam_state` folder created during `make_quam.py`.

### Setting Up the `QUAM_STATE_PATH` Environment Variable
#### Linux
1. Open a terminal.
2. Edit the `/etc/environment` file:
   ```sh
   sudo nano /etc/environment
   ```
3. Add the line:
   ```sh
   QUAM_STATE_PATH="/path/to/configuration/quam_state"
   ```
4. Save the file and log out, then log back in for changes to take effect.

#### Mac
1. Open a terminal.
2. Edit the `/etc/launchd.conf` file:
   ```sh
   sudo nano /etc/launchd.conf
   ```
3. Add the line:
   ```sh
   setenv QUAM_STATE_PATH "/path/to/configuration/quam_state"
   ```
4. Save the file and restart your system for changes to take effect.

#### Windows
1. Press `Win + X`, select **System**.
2. Click **Advanced system settings** > **Environment Variables**.
3. Click **New** under **System variables**.
4. Set **Variable name** to `QUAM_STATE_PATH`.
5. Set **Variable value** to `C:\path\to\configuration\quam_state`.
6. Click **OK** to close all windows.

The `QUAM_STATE_PATH` environment variable is now set up globally on your system.

### Connectivity
A class is provided to create a "default" wiring. The default wiring assigns ports in the following physical order:
1. All resonator I/Q channels are allocated to the first FEM/OPX+ for all qubits.
2. All qubit I/Q channels are allocated to the first FEM/OPX+ for all qubits.
3. All qubit flux channels are allocated to the first FEM/OPX+ for all qubits (if any).
4. All tunable coupler channels are allocated to the first FEM/OPX+ for all qubits (if any).

This extends over multiple LF-FEMs, OPX+ and Octaves when needed.
