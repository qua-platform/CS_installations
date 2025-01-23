import pygsti
import numpy as np
import pandas as pd
import re

# Configure pandas display options
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)

# Import the single-qubit XY model pack
from pygsti.modelpacks import smq1Q_XY

# Print model pack details
print(smq1Q_XY.description)
print(smq1Q_XY.gates)
print(smq1Q_XY._prepfiducials)
print(smq1Q_XY._measfiducials)
print(smq1Q_XY.prep_fiducials())
print(smq1Q_XY.meas_fiducials())

# Fiducials and germ mappings
map_encode_prepfiducial = {
    "{}": 4,
    "Gxpi2:0": 5,
    "Gypi2:0": 6,
    "Gxpi2:0Gxpi2:0": 7,
    "Gxpi2:0Gxpi2:0Gxpi2:0": 9,
    "Gypi2:0Gypi2:0Gypi2:0": 10,
}
map_encode_germs = {
    "[]": 4,
    "Gxpi2:0": 5,
    "Gypi2:0": 6,
    "Gxpi2:0Gypi2:0": 8,
    "Gxpi2:0Gxpi2:0Gypi2:0": 11,
}
map_encode_measfiducial = {
    "{}": 4,
    "Gxpi2:0": 5,
    "Gypi2:0": 6,
    "Gxpi2:0Gxpi2:0": 7,
    "Gxpi2:0Gxpi2:0Gxpi2:0": 9,
    "Gypi2:0Gypi2:0Gypi2:0": 10,
}
# Gate counts for native gates
map_gate_count_prepfiducial = {
    "{}": 4,
    "Gxpi2:0": 1,
    "Gypi2:0": 1,
    "Gxpi2:0Gxpi2:0": 2,
    "Gxpi2:0Gxpi2:0Gxpi2:0": 3,
    "Gypi2:0Gypi2:0Gypi2:0": 3,
}
map_gate_count_germs = {
    "[]": 4,
    "Gxpi2:0": 1,
    "Gypi2:0": 1,
    "Gxpi2:0Gypi2:0": 2,
    "Gxpi2:0Gxpi2:0Gypi2:0": 3,
}
map_gate_count_measfiducial = {
    "{}": 4,
    "Gxpi2:0": 1,
    "Gypi2:0": 1,
    "Gxpi2:0Gxpi2:0": 2,
    "Gxpi2:0Gxpi2:0Gxpi2:0": 3,
    "Gypi2:0Gypi2:0Gypi2:0": 3,
}


# Path to the dataset
path = "./exp_dataset_240613200840.txt"

# Load sequences from file
sequences = []
with open(path, mode="r") as f:
    for line in f:
        line = line.strip()
        if "@(0)" not in line:
            print(f"Oops! Invalid line: {line}")
        else:
            sequences.append(line)

# Regex patterns for sequence parsing
pattern_sequence = r"^([^(^]*)?(\(([^)]*)\))?(\^(\d+))?([^\@]*)@\(0\).*$"
_X = "Gxpi2:0"
_Y = "Gypi2:0"
pattern_fiducials = (
    rf"^(\{{\}}|{_X}{_X}{_X}|{_Y}{_Y}{_Y}|{_X}{_X}|{_X}|{_Y})"
    rf"(\{{\}}|{_X}{_X}{_X}|{_Y}{_Y}{_Y}|{_X}{_X}|{_X}|{_Y})?$"
)

# Lists to store extracted components
Idx, As, Gs, ds, Bs, Ps, Ms = [], [], [], [], [], [], []

# Process each sequence
idx = 0
for input_string in sequences:
    match_seq = re.match(pattern_sequence, input_string)

    if not match_seq:
        raise ValueError(f"Unexpected pattern: {input_string}")

    idx += 1
    A = match_seq.group(1) or None
    G = match_seq.group(3) or None
    d = match_seq.group(5) or None
    B = match_seq.group(6) or None
    d = 1 if G is not None and d is None else d

    if G is None:
        fiducial_match = re.fullmatch(pattern_fiducials, A)
        if fiducial_match:
            P = fiducial_match.group(1) or None
            M = fiducial_match.group(2) or None
        else:
            raise ValueError(f"Unexpected pattern: {input_string}, extracted A: {A}")
    else:
        P = A
        M = B

    Idx.append(idx)
    As.append(A)
    Gs.append(G)
    Bs.append(B)
    ds.append(d)
    Ps.append(P)
    Ms.append(M)

    print(f"Input: {input_string}")
    print(f"A: {A}, G: {G}, d: {d}, B: {B}, P: {P}, M: {M}")

# Create a DataFrame from the extracted components
df = pd.DataFrame([Idx, sequences, As, Gs, ds, Bs, Ps, Ms]).T
df.columns = ["circ_idx", "seq", "A", "G", "d", "B", "P", "M"]
# Encode fiducials, germs, and counts
df["P_enc"] = df["P"].apply(lambda x: map_encode_prepfiducial.get(x, None) if x is not None else -1)
df["G_enc"] = df["G"].apply(lambda x: map_encode_germs.get(x, None) if x is not None else -1)
df["d_enc"] = df["d"].apply(lambda x: 0 if x is None else int(x))
df["M_enc"] = df["M"].apply(lambda x: map_encode_measfiducial.get(x, None) if x is not None else -1)
df["P_native_gate_count"] = df["P"].apply(lambda x: map_gate_count_prepfiducial.get(x, None) if x is not None else 0)
df["G_native_gate_count"] = df["G"].apply(lambda x: map_gate_count_germs.get(x, None) if x is not None else 0)
df["d_native_gate_count"] = df["d_enc"]
df["M_native_gate_count"] = df["M"].apply(lambda x: map_gate_count_measfiducial.get(x, None) if x is not None else 0)
df["full_native_gate_count"] = df["P_native_gate_count"] + df["d_native_gate_count"] * df["G_native_gate_count"] + df["M_native_gate_count"]

df["remaining_native_gate_count"] = df["full_native_gate_count"].max() - df["full_native_gate_count"]
df["remaining_wait_num_4-pihalf"] = df["remaining_native_gate_count"] // 4
df["remaining_wait_num_pihalf"] = df["remaining_native_gate_count"] % 4

df["full_sequence_length"] = (
    (df["P_native_gate_count"] > 0).astype(int) +
    df["d_native_gate_count"] +
    (df["M_native_gate_count"] > 0).astype(int) +
    df["remaining_wait_num_4-pihalf"] +
    df["remaining_wait_num_pihalf"].astype(int)
)

# Save the encoded DataFrame to a CSV file
output_path = "encoded_parsed_dataset.csv"
df.to_csv(output_path, encoding="utf8", header=True, index=False)

# Display the first few rows of the DataFrame
print(df.head())
