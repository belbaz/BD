import pandas as pd

# Charger les données depuis les fichiers JSON
vols_data = pd.read_json("Vols.json")
defclasses_data = pd.read_json("Defclasses.json")
reservations_data = pd.read_json("Reservations.json")

# Effectuer la jointure entre Vols et Defclasses
merged_data = pd.merge(vols_data, defclasses_data, on="NumVol")

# Effectuer la jointure entre merged_data et Reservations
final_data = pd.merge(merged_data, reservations_data, left_on="NumVol", right_on="NumVol")

# Enregistrer le résultat dans un fichier JSON
final_data.to_json("jointure.json", orient="records", lines=True)
