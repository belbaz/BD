from pymongo import MongoClient
import json

# Définition de la fonction de jointure
def jointure(collection1, collection2, champ_comm):
    result = []
    for doc1 in collection1:
        for doc2 in collection2:
            if champ_comm in doc1 and champ_comm in doc2 and doc1[champ_comm] == doc2[champ_comm]:
                jointed_doc = {**doc1, **doc2}
                result.append(jointed_doc)
    return result

# Établir une connexion à la base de données MongoDB
client = MongoClient("localhost", 27017)

# Sélectionner la base de données
db = client['ma_bdd']

# Sélectionnez la collection 'vols' et supprimez tous les documents
db['vols'].delete_many({})

# Sélectionnez la collection 'defclasses' et supprimez tous les documents
db['defclasses'].delete_many({})

# Sélectionnez la collection 'reservations' et supprimez tous les documents
db['reservations'].delete_many({})

# Insérer les données des fichiers JSON dans les collections correspondantes
with open("DEFCLASSES.json", "r") as f:
    defclasses_data = json.load(f)
db['defclasses'].insert_many(defclasses_data)

with open("RESERVATIONS.json", "r") as f:
    reservations_data = json.load(f)
db['reservations'].insert_many(reservations_data)

with open("VOLS.json", "r") as f:
    vols_data = json.load(f)
db['vols'].insert_many(vols_data)

# Récupérer les données insérées précédemment
vols_documents = db['vols'].find()
defclasses_documents = db['defclasses'].find()

# Convertir les curseurs MongoDB en listes de dictionnaires
vols_data = list(vols_documents)
defclasses_data = list(defclasses_documents)

# Appliquer la fonction de jointure
result = jointure(vols_data, defclasses_data, "NumVol")

# Récupérer les données de la collection 'reservations'
reservations_documents = db['reservations'].find()

# Convertir le curseur MongoDB en liste de dictionnaires
reservations_data = list(reservations_documents)

# Appliquer une deuxième jointure avec la collection 'reservations' basée sur 'NumVol'
result = jointure(result, reservations_data, "NumVol")

# Supprimer le champ "_id" qui est un ObjectId avant la sérialisation JSON
for doc in result:
    if "_id" in doc:
        del doc["_id"]

# Afficher les résultats de la jointure
#for document in result:
#    print(document)

# Enregistrer le résultat de la jointure dans un fichier JSON
with open("jointure.json", "w") as f:
    json.dump(result, f, indent=2)
