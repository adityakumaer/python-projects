import json
from logging import exception
import os

input_file = 'nested_data.json'
output_file = 'flattened_data.json'


def flatten_json(data,parent_key='', sep="."):
    items = {}
    if isinstance(data, dict):
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            items.update(flatten_json(v, parent_key=new_key, sep=sep))
    elif isinstance(data, list):
        for i, v in enumerate(data):
            new_key = f"{parent_key}{sep}{i}" if parent_key else i
            items.update(flatten_json(v, parent_key=new_key, sep=sep))
    else:
        items[parent_key] = data
    return items

def main():
    
    if not os.path.exists(input_file):
        print(f"File {input_file} does not exist.")
        return
    
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)
        sep = input("Enter the separator for flattening (default is '.'): ") or "."

        flattened_data = flatten_json(data)
        with open(output_file, 'w') as file:
            json.dump(flattened_data, file, indent=4)

        print(f"Flattened JSON data has been written to {output_file}")

    except exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()