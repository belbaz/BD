import csv

def convert_txt_to_csv_with_header(txt_file, csv_file, column_names):
    with open(txt_file, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        rows = list(reader)

    # Ajouter les noms de colonnes à la première ligne
    rows.insert(0, column_names)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Noms de colonnes pour chaque table
avions_columns = ["NumAv", "NomAv", "CapAv", "VilleAv"]
pilotes_columns = ["NumPil", "NomPil", "NaisPil", "VillePil"]
clients_columns = ["NumCl", "NomCl", "NumRueCl", "NomRueCl", "CodePosteCl", "VilleCl"]
vols_columns = ["NumVol", "VilleD", "VilleA", "DateD", "HD", "DateA", "HA", "NumPil", "NumAv"]
defclasses_columns = ["NumVol", "ClasseCoeffPrix"]
reservations_columns = ["NumCl", "NumVolClasse", "NbPlaces"]

# Convertir chaque fichier TXT en CSV avec les noms de colonnes
convert_txt_to_csv_with_header('AVIONS.txt', 'AVIONS.csv', avions_columns)
convert_txt_to_csv_with_header('PILOTES.txt', 'PILOTES.csv', pilotes_columns)
convert_txt_to_csv_with_header('CLIENTS.txt', 'CLIENTS.csv', clients_columns)
convert_txt_to_csv_with_header('VOLS.txt', 'VOLS.csv', vols_columns)
convert_txt_to_csv_with_header('DEFCLASSES.txt', 'DEFCLASSES.csv', defclasses_columns)
convert_txt_to_csv_with_header('RESERVATIONS.txt', 'RESERVATIONS.csv', reservations_columns)
