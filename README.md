# Double-Quantum-Dot Measurements
## Requirements
Start by [installing Anaconda 3](https://www.anaconda.com/download) if you have not done so already.

Then, from an Anaconda terminal, run the following commands:
```shell
# Create a conda environment
conda create -n qm python==3.11
conda activate qm

# Install relevant packages
pip install qm-qua, qualang-tools, qcodes_contrib_drivers, pyvisa_py
```
These packages provide access to the following features:
 - **qm-qua**: The QUA SDK required for connecting to and programming the OPX.
 - **qualang-tools**: A library to help with writing QUA programs on the OPX.
 - **qcodes_contrib_drivers**: Contains an open-source driver for connecting to and controlling the QDAC-I.

## Folder Structure
```
.
Experimental scripts
├── 00_hello_qua.py  
├── 01_turn_on_measurements.py
├── ... 
Octave mixer-calibration database
├── calibration_db.json  
OPX/QDAC Configuration file
├── configuration.py
Experimental Data folder
├── data
│   ├── YYYY-MM-DD
│   └── waveform_report...
QUA program functions
├── macros.py
Octave mixer-calibration script
├── octave_calibration.py
Python package requirements document
├── pyproject.toml
QDAC-I driver with convenience methods
├── qdac.py
This file
└── README.md

```
## Experiments
