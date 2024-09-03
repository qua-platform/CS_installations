# %%
import json

def sort_key(key):
    """Helper function to sort keys numerically if possible, otherwise alphabetically."""
    try:
        # Try to convert the key to an integer for numeric sorting
        return int(key)
    except ValueError:
        # If conversion fails, keep it as a string for alphabetical sorting
        return key

def sort_dict_alphabetically_and_numerically(d):
    """Recursively sorts a dictionary alphabetically and numerically by its keys."""
    if isinstance(d, dict):
        # Sort keys using the helper function
        return {k: sort_dict_alphabetically_and_numerically(v) for k, v in sorted(d.items(), key=lambda item: sort_key(item[0]))}
    elif isinstance(d, list):
        # If a list contains dictionaries, sort each dictionary element recursively
        return [sort_dict_alphabetically_and_numerically(i) if isinstance(i, dict) else i for i in d]
    else:
        # Return non-dictionary types as is
        return d

def json_to_python_file(json_file_path, python_file_path):
    """Reads a JSON file, sorts it alphabetically and numerically by keys, and writes it to a Python file."""
    # Read the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    
    # Sort the JSON data
    sorted_data = sort_dict_alphabetically_and_numerically(data)

    # Prepare the content for the Python file with proper Python formatting
    python_content = "sorted_config = " + json.dumps(sorted_data, indent=4).replace("true", "True").replace("false", "False")

    # Write the sorted data to a Python file
    with open(python_file_path, 'w') as py_file:
        py_file.write(python_content)

    print(f"Python file '{python_file_path}' generated successfully.")


if __name__ == "__main__":
    # Usage example
    json_file_path = 'qua_config.json'  # Replace with your JSON file path
    python_file_path = 'qua_config.py'  # Replace with your desired output Python file path
    json_to_python_file(json_file_path, python_file_path)


# %%
