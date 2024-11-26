from pathlib import Path
from typing import overload, Union, Optional
from iqcc_cloud_client import IQCC_Cloud
from quam_libs.components.quam_root import QuAM

from qualibrate_app.config import get_config_path, get_settings

from qualibrate import QualibrationNode
from qualibrate.storage.local_storage_manager import LocalStorageManager

config_path = get_config_path()
settings = get_settings(config_path)
QualibrationNode.storage_manager = LocalStorageManager(
    root_data_folder=settings.qualibrate.storage.location,
    active_machine_path=settings.active_machine.path,
)


def get_job_results(job):
    results = {}
    for key, value in job.result_handles.items():
        result = value.fetch_all()
        if isinstance(result, np.int64):
            result = int(result)
        results[key] = result
    return results


def strip_octaves_from_config(config):

    octaves_config = config.pop("octaves")
    for key, channel in config["elements"].items():
        if "RF_outputs" in channel:  # OPX input IQ channels
            RF_outputs_entry = channel.pop("RF_outputs")
            octave, idx = RF_outputs_entry["port"]
            if idx != 1:
                raise ValueError("Only RF output 1 is supported for Octave")

            IF_outputs = octaves_config[octave]["IF_outputs"]
            channel["outputs"] = {
                "out1": IF_outputs["IF_out1"]["port"],
                "out2": IF_outputs["IF_out2"]["port"],
            }
        if "RF_inputs" in channel:  # OPX output IQ channels
            RF_inputs_entry = channel.pop("RF_inputs")
            octave, idx = RF_inputs_entry["port"]
            RF_input = octaves_config[octave]["RF_outputs"][idx]

            channel["mixInputs"] = {
                "I": RF_input["I_connection"],
                "Q": RF_input["Q_connection"],
                "mixer": f"{key}.mixer",
                "lo_frequency": RF_input["LO_frequency"],
            }

            try:
                q_name, ch_name = key.split(".")
                qubit = machine.qubits[q_name]
                ch = getattr(qubit, ch_name)
                mixer_calibration = ch.mixer_calibration or [1, 0, 0, 1]
            except Exception:
                mixer_calibration = [1, 0, 0, 1]

            config["mixers"] = {
                f"{key}.mixer": [
                    {
                        "intermediate_frequency": channel["intermediate_frequency"],
                        "lo_frequency": RF_input["LO_frequency"],
                        "correction": mixer_calibration,
                    }
                ]
            }

    return config


def generate_config(machine: QuAM, strip_octaves: bool = True):
    # Generate the OPX and Octave configurations
    for label, qubit in machine.qubits.items():
        if label in machine.active_qubit_names:
            qubit.z.opx_output.offset = qubit.z.joint_offset
        else:
            qubit.z.opx_output.offset = qubit.z.min_offset
    config = machine.generate_config()
    if strip_octaves:
        config = strip_octaves_from_config(config)
    return config


@overload
def execute_program(
    program,
    machine,
    execution_mode: str = "IQCC",
    *,
    token: Optional[str] = None,
    debug: bool = False,
    strip_octaves: bool = True,
): ...


@overload
def execute_program(
    program,
    machine,
    execution_mode: str = "local",
    *,
    close_other_machines: bool = True,
    strip_octaves: bool = True,
): ...


def execute_program(
    program,
    machine,
    execution_mode: str = "IQCC",
    *,
    token: Optional[str] = None,
    debug: bool = False,
    close_other_machines: bool = True,
    strip_octaves: bool = True,
):
    if execution_mode.lower() == "iqcc":
        return execute_IQCC(program, machine, token=token, debug=debug)
    else:
        return execute_local(
            program, machine, close_other_machines=close_other_machines
        )


def execute_local(program, machine, close_other_machines=True, strip_octaves=True):
    qmm = machine.connect()
    config = generate_config(machine, strip_octaves=strip_octaves)

    # Open the quantum machine
    qm = qmm.open_qm(config, close_other_machines=close_other_machines)

    try:
        job = qm.execute(program)
        job.result_handles.wait_for_all_values()
    finally:
        qm.close()

    # Fetch results
    results = get_job_results(job)
    return results


def execute_IQCC(program, machine, token=None, debug=False, strip_octaves=True):
    if token is None:
        for path in [
            Path(".IQCC_token"),
            Path("/home/.IQCC_token"),
            Path("~/.IQCC_token"),
        ]:
            if not path.exists():
                continue

            token = path.read_text()
            break
        else:
            raise ValueError(
                "No token provided and no token file found at .IQCC_token or ~/.IQCC_token"
            )
    token = token.strip()

    qc = IQCC_Cloud(api_token=token)

    config = generate_config(machine, strip_octaves=strip_octaves)
    results = qc.execute(program, config, True, debug=debug)
    return results["result"]


def local_setup():
    import os
    from pathlib import Path

    user_home_dir = Path.home()
    base_dir = user_home_dir / "Repositories/IEEE-QCE24-docker-environment"
    os.chdir(base_dir)
    os.environ["QUAM_STATE_PATH"] = str(base_dir / "user_directory/quam_state")
