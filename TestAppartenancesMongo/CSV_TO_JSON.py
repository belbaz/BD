import csv
import json

def convert_csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    with open(json_file, 'w') as file:
        json.dump(rows, file)

convert_csv_to_json('DEM-1_1.csv', 'DEM-1_1.json')