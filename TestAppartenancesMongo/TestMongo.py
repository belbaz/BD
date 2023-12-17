import json
from pymongo import MongoClient
import time

# Établir une connexion à MongoDB
client = MongoClient("localhost", 27017)

# Sélectionner la base de données
db = client['DBTestAppartenance']

# Sélectionner ou créer la collection sans index
collection_without_index = db['your_collection_name_without_index']

# Charger les données depuis le fichier JSON
with open('DEM-1_1.json', 'r') as json_file:
    words = json.load(json_file)

# Mesurer le temps d'exécution sans index
start_time_without_index = time.time()

# Insérer les données dans la collection sans index
result_without_index = collection_without_index.insert_many(words)

end_time_without_index = time.time()
elapsed_time_without_index = end_time_without_index - start_time_without_index

# Sélectionner ou créer la collection avec index
collection_with_index = db['your_collection_name_with_index']

# Créer un index sur le champ approprié (par exemple)
collection_with_index.create_index("bonjour")

# Mesurer le temps d'exécution avec index
start_time_with_index = time.time()

# Insérer les données dans la collection avec index
result_with_index = collection_with_index.insert_many(words)

end_time_with_index = time.time()
elapsed_time_with_index = end_time_with_index - start_time_with_index

print(f"Temps d'exécution sans index : {elapsed_time_without_index} secondes")
print(f"Temps d'exécution avec index : {elapsed_time_with_index} secondes")

client.close()