from collections.abc import Sequence
from typing import Any, List
import re


def broadcast_param_to_list(value: Any, n: int) -> List[Any]:
    """
    Normalize a parameter to a list of length n.

    - Scalar -> [value] * n
    - Sequence (not str/bytes):
        * len == n  -> list(value)
        * len == 1  -> [value[0]] * n
        * otherwise -> ValueError
    """
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        seq = list(value)
        if len(seq) == n:
            return seq
        if len(seq) == 1:
            return seq * n
        raise ValueError(f"Expected length 1 or {n}, got {len(seq)}.")
    return [value] * n


def pick_disjoint_qubit_pairs(pairs):
    _pat = re.compile(r"^q(\d+)-(\d+)$")

    edges = []
    seen = set()
    for s in pairs:
        m = _pat.match(s.strip())
        if not m:
            raise ValueError(f"Bad pair: {s!r}")
        a, b = map(int, m.groups())
        if a == b:
            continue  # skip self-pairs
        a, b = (a, b) if a < b else (b, a)  # normalize
        if (a, b) not in seen:              # dedupe q2-1 vs q1-2
            seen.add((a, b))
            edges.append((a, b))

    # Numeric sort: avoids 'q10-11' coming before 'q2-3'
    edges.sort(key=lambda ab: (ab[0], ab[1]))

    used = set()
    out = []
    for a, b in edges:
        if a not in used and b not in used:
            out.append(f"q{a}-{b}")  # always sorted form
            used.update((a, b))
    
    if len(pairs) != len(out):
        print(f"qubit_pairs passed: {pairs}")
        print(f"qubit_pairs chosen: {out}")

    return out