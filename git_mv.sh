#!/bin/bash

# Loop over the numeric prefixes from 21 to 17 (in reverse)
for i in $(seq 22 -1 18); do
  next=$((i - 1))
  # Use a pattern to find files that start with the current number and follow the specific format
  for file in ${i}[a-z]_*; do
    # Check if the file exists
    if [[ -e "$file" ]]; then
      # Generate the new file name by replacing the numeric prefix
      new_name="${next}${file:2}"
      echo "Renaming $file to $new_name"
      git mv "$file" "$new_name"
    fi
  done
done
