## Requirements
QOP version: Please refer to this: https://docs.quantum-machines.co/1.2.2/docs/Releases/qop3_releases/.

Start by [installing Anaconda 3](https://www.anaconda.com/download) if you have not done so already.

Then, from an Anaconda terminal, run the following commands:
```shell
# Create a conda environment
conda create -n qm python==3.11
conda activate qm

# Install relevant packages
pip install qm-qua, qualang-tools
```
These packages provide access to the following features:
 - **qm-qua**: The QUA SDK required for connecting to and programming the OPX.
 - **qualang-tools**: A library to help with writing QUA programs on the OPX.