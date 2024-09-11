from pathlib import Path
from iqcc_cloud_client import IQCC_Cloud
from .macros import generate_config, get_job_results


def execute_local(program, machine, close_other_machines=True):
    qmm = machine.connect()
    config = machine.generate_config()

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


def execute_IQCC(program, machine, token=None, debug=False):
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

    qc = IQCC_Cloud(token)

    config = generate_config(machine)
    results = qc.execute(program, config, True, debug=debug)
    return results["result"]
