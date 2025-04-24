# %%
from pathlib import Path
import os
import glob
import subprocess
import shutil
from datetime import datetime


# Define paths
quam_state_dir = "quam_state"
backup_dir = "../backup_quam_states"
# List of scripts to run
make_scripts = [
    "make_wiring_opx1000_mwfem.py",
    # "make_wiring_opxplus_octave.py",
    "make_quam.py",
    "modify_quam.py",
]
cluster_type = make_scripts[0].replace("make_wiring_","")

# Create a timestamped backup directory
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
backup_path = os.path.join(backup_dir, f"quam_state_before_{cluster_type}_{timestamp}")

# Ensure backup directory exists
os.makedirs(backup_dir, exist_ok=True)

# Copy `quam_state` to the backup location
if os.path.exists(quam_state_dir):
    shutil.copytree(quam_state_dir, backup_path)
    print(f"Backup created at: {backup_path}")

# Remove JSON files under quam_state
json_files = glob.glob(os.path.join(quam_state_dir, "*.json"))
for file in json_files:
    os.remove(file)
    print(f"Removed: {file}")

path_config = Path("/workspaces/HI_20250428_EunseongKim/configuration")
for script in make_scripts:
    print(f"Running: {script}")
    subprocess.run(["python", path_config / script], check=True)


# Create a timestamped backup directory
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
backup_path = os.path.join(backup_dir, f"quam_state_after_{cluster_type}_{timestamp}")

# Copy `quam_state` to the backup location
if os.path.exists(quam_state_dir):
    shutil.copytree(quam_state_dir, backup_path)
    for sc in make_scripts:
        shutil.copy(path_config / sc, backup_path)
    print(f"Backup created at: {backup_path}")


print("All scripts executed successfully.")
# %%
