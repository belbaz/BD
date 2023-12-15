import csv
import json

def convert_csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    with open(json_file, 'w') as file:
        json.dump(rows, file)

convert_csv_to_json('AVIONS.csv', 'AVIONS.json')
convert_csv_to_json('CLIENTS.csv', 'CLIENTS.json')
convert_csv_to_json('DEFCLASSES.csv', 'DEFCLASSES.json')
convert_csv_to_json('PILOTES.csv', 'PILOTES.json')
convert_csv_to_json('RESERVATIONS.csv', 'RESERVATIONS.json')
convert_csv_to_json('VOLS.csv', 'VOLS.json')
