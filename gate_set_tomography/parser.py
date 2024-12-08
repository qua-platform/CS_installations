import re

# Load sequences from file
sequences = []
with open("dataset.txt", mode="r") as f:
    for line in f:
        line = line.strip()
        if "@(0)" not in line:
            print(f"Oops! Invalid line: {line}")
        else:
            sequences.append(line)

# Regex for general sequence parsing
# Define the regex pattern
pattern_sequence = r"^([^(^]*)?(\(([^)]*)\))?(\^(\d+))?([^\@]*)@\(0\).*$"

# Define fiducials pattern
_X = "Gxpi2:0"
_Y = "Gypi2:0"
pattern_fiducials = (
    rf"^(\{{\}}|{_X}{_X}{_X}|{_Y}{_Y}{_Y}|{_X}{_X}|{_X}|{_Y})"
    rf"(\{{\}}|{_X}{_X}{_X}|{_Y}{_Y}{_Y}|{_X}{_X}|{_X}|{_Y})?$"
)

# Lists to store extracted components
As, Gs, ds, Bs, Ps, Ms = [], [], [], [], [], []

# Process each sequence
for input_string in sequences:
    # Match the sequence with the general regex pattern
    match_seq = re.match(pattern_sequence, input_string)

    if not match_seq:
        raise ValueError(f"Unexpected pattern: {input_string}")

    else:
        # Extract components from the match
        A = match_seq.group(1) or None  # Prefix (before parentheses)
        G = match_seq.group(3) or None  # Inside parentheses
        d = match_seq.group(5) or None  # Exponent (after "^")
        B = match_seq.group(6) or None  # Suffix (after parentheses and "^")

        d = 1 if G is not None and d is None else d

        # Match X against the fiducials pattern if B is None
        if G is None:
            fiducial_match = re.fullmatch(pattern_fiducials, A)
            if fiducial_match:
                P = fiducial_match.group(1) or None  # Match first group
                M = fiducial_match.group(2) or None  # Match second group
            else:
                raise ValueError(f"Unexpected pattern: {input_string}, extracted A: {A}")

        # Append extracted components to respective lists
        As.append(A)
        Gs.append(G)
        Bs.append(B)
        ds.append(d)
        Ps.append(P)
        Ms.append(M)

        print(f"Input: {input_string}")
        print(f"A: {A}, G: {G}, d: {d}, B: {B}, P: {P}, M: {M}")

# Debugging output
print("Extracted components:")
print("As:", As)
print("Gs:", Gs)
print("ds:", ds)
print("Bs:", Bs)
print("Ps:", Ps)
print("Ms:", Ms)