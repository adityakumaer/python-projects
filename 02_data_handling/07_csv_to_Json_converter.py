import csv
import json
import os

input_file = 'data.csv'
output_file = 'converted_data.json'

def load_csv_data(file_name):
    if not os.path.exists(file_name):
        print(f"File {file_name} does not exist.")
        return []
    
    with open(file_name, 'r') as file:
        try:
            reader = csv.DictReader(file)
            data = list(reader)
            return data
        except:
            print("Invalid CSV format.")

def convert_to_json(csv_data, output_file_name):
    if not csv_data:
        print("No data to convert.")
        return

    with open(output_file_name, 'w') as output_file:
        json.dump(csv_data, output_file)

    print(f"converted {len(csv_data)} records to {output_file_name}")


def preview_json_data(json_file_name):
    if not os.path.exists(json_file_name):
        print(f"File {json_file_name} does not exist.")
        return

    with open(json_file_name, 'r') as file:
        try:
            data = json.load(file)
            print("Preview of JSON data:")
            for record in data[:5]:
                print(record)
        except:
            print("Invalid JSON format.")

def main():
    print("converting CSV to JSON conversion...")
    csv_data = load_csv_data(input_file)
    convert_to_json(csv_data, output_file)
    preview_json_data(output_file)


if __name__ == "__main__":
    main()