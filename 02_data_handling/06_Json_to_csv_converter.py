import csv
import json
import os

input_file = 'api_data.json'
output_file = 'converted_data.csv'


def load_json_data(file_name):

    if not os.path.exists(file_name):
        print(f"File {file_name} does not exist.")
        return []
    
    with open(file_name, 'r') as file:
        try:
            data = json.load(file)
            return data
        except:
            print("Invalid JSON format.")


def convert_to_csv(json_data, output_file_name):

    if not json_data:
        print("No data to convert.")
        return

    keys = json_data[0].keys()

    with open(output_file_name, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        for record in json_data:
            dict_writer.writerow(record)

    print(f"converted {len(json_data)} records to {output_file_name}")


def main():
    print("converting JSON to CSV conversion...")
    json_data = load_json_data(input_file)
    convert_to_csv(json_data, output_file)

if __name__ == "__main__":
    main()