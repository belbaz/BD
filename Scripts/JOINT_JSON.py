import json
import os

# Créer un dossier pour les fichiers dénormalisés
os.makedirs("denormalized_files", exist_ok=True)

# Charger les fichiers JSON
with open("AVIONS.json") as f:
    avions_data = json.load(f)

with open("CLIENTS.json") as f:
    clients_data = json.load(f)

with open("DEFCLASSES.json") as f:
    defclasses_data = json.load(f)

with open("PILOTES.json") as f:
    pilotes_data = json.load(f)

with open("RESERVATIONS.json") as f:
    reservations_data = json.load(f)

with open("VOL.json") as f:
    vol_data = json.load(f)

# Effectuer la dénormalisation
nouveau_vol = []
for vol in vol_data:
    num_vol = vol['NumVol']
    num_pil = vol['NumPil']
    num_av = vol['NumAv']

    # Rechercher les informations correspondantes dans les autres fichiers
    pilote = next((pilote for pilote in pilotes_data if pilote['NumPil'] == num_pil), None)
    avion = next((avion for avion in avions_data if avion['NumAv'] == num_av), None)
    defclasses = [defclasse for defclasse in defclasses_data if defclasse['NumVol'] == num_vol]
    reservations = [reservation for reservation in reservations_data if reservation['NumVol'] == num_vol]

    # Créer un nouveau vol avec toutes les informations dénormalisées
    nouveau_vol.append({
        'NumVol': num_vol,
        'VilleD': vol['VilleD'],
        'VilleA': vol['VilleA'],
        'DateD': vol['DateD'],
        'HD': vol['HD'],
        'DateA': vol['DateA'],
        'HA': vol['HA'],
        'NumPil': num_pil,
        'NumAv': num_av,
        'Pilote': pilote,
        'Avion': avion,
        'DefClasses': defclasses,
        'Reservations': reservations
    })

# Enregistrer le nouveau vol dénormalisé dans un fichier JSON
with open("denormalized_files/nouveau_vol.json", "w") as f:
    json.dump(nouveau_vol, f, indent=4)

print("Dénormalisation terminée. Le fichier denormalized_files/nouveau_vol.json a été créé.")
