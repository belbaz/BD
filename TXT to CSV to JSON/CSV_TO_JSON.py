import csv
import json
import os

def convert_csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    # Créer le dossier "JSON" s'il n'existe pas
    output_folder = 'JSON'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Construire le chemin complet pour le fichier JSON dans le dossier "JSON"
    json_file_path = os.path.join(output_folder, json_file)

    with open(json_file_path, 'w') as file:
        json.dump(rows, file)

# Convertir chaque fichier CSV en JSON
convert_csv_to_json('CSV/AVIONS.csv', 'AVIONS.json')
convert_csv_to_json('CSV/CLIENTS.csv', 'CLIENTS.json')
convert_csv_to_json('CSV/DEFCLASSES.csv', 'DEFCLASSES.json')
convert_csv_to_json('CSV/PILOTES.csv', 'PILOTES.json')
convert_csv_to_json('CSV/RESERVATIONS.csv', 'RESERVATIONS.json')
convert_csv_to_json('CSV/VOLS.csv', 'VOLS.json')
