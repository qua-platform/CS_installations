# N Fixed Transmon Qubits
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

## Installation
This folder contains an installable module called `quam_libs`, which provides a collection of tailored components for controlling flux-tunable qubits and experiment functionality. These components extend the functionality of QuAM, making it easier to design and execute calibration nodes.

### Requirements
To run the calibration nodes in this folder, you need to install `quam_libs`. First, ensure you have Python ≥ 3.8 installed on your system.
Then run the following command:

```sh
# Install quam
pip install git+https://github.com/qua-platform/quam.git
# Install quam_libs
pip install -e .  
# or, if you see a red underline, in PyCharm, you can simply try
# pip install .
```
> **_NOTE:_**  The `-e` flag means you *don't* have to reinstall if you make a local change to `quam_libs`! 
