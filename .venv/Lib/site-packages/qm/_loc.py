import traceback
from pathlib import Path

from qm.exceptions import QmQuaException

QM_PACKAGE_DIR = Path(__file__).resolve().parent


def _get_loc() -> str:
    tb = traceback.extract_stack()
    for trace in reversed(tb):
        if QM_PACKAGE_DIR not in Path(trace.filename).parents:
            return f'File "{trace.filename}", line {trace.lineno}: {trace.line} '
    raise QmQuaException("Could not find location")
