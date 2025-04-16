#!/bin/bash

rename_files() {
    local from=$1
    local to=$2
    local increment=$3

    if [[ -z $from || -z $to || -z $increment ]]; then
        echo "Usage: $0 from=<start_range> to=<end_range> increment=<True|False>"
        exit 1
    fi

    # Determine direction based on increment
    if [[ $increment == "True" ]]; then
        step=1
        sequence=$(seq "$to" -1 "$from") # Reverse loop for incrementing
    elif [[ $increment == "False" ]]; then
        step=-1
        sequence=$(seq "$from" 1 "$to") # Forward loop for decrementing
    else
        echo "Invalid value for increment: $increment. Use True or False."
        exit 1
    fi

    # Process files in the specified range
    for i in $sequence; do
        current=$(printf "%02d" "$i")
        next=$(printf "%02d" "$((i + step))")
        
        for file in ${current}[a-c]_*.py; do
            if [[ -e $file ]]; then
                # Preserve the 'a', 'b', 'c' prefix after the number
                prefix=${file:2:1}  # Extract the letter after the number (a, b, or c)
                new_file="${next}${prefix}_${file:4}"  # Construct new filename

                echo "Renaming: $file -> $new_file"
                git mv "$file" "$new_file"
            else
                echo "No files found for pattern: ${current}[a-c]_*.py"
            fi
        done
    done
}

if [[ $# -ne 3 ]]; then
    echo "Usage: $0 from=<start_range> to=<end_range> increment=<True|False>"
    exit 1
fi

from=
to=
increment=

for arg in "$@"; do
    case $arg in
        from=*)
            from="${arg#*=}"
            ;;
        to=*)
            to="${arg#*=}"
            ;;
        increment=*)
            increment="${arg#*=}"
            ;;
        *)
            echo "Unknown argument: $arg"
            exit 1
            ;;
    esac
done

rename_files "$from" "$to" "$increment"
