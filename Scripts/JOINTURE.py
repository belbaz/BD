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

# Sélectionnez la collection 'avions' et supprimez tous les documents
db['avions'].delete_many({})

# Insérer les données de VOLS.json
with open("C:\\Users\\user\\Desktop\\BD\\BD\\Outputs\\VOLS.json", "r") as f:
    vols_data = json.load(f)
db['vols'].insert_many(vols_data)

# Insérer les données de AVIONS.json
with open("C:\\Users\\user\\Desktop\\BD\\BD\\Outputs\\AVIONS.json", "r") as f:
    avions_data = json.load(f)
db['avions'].insert_many(avions_data)

# Récupérer les données insérées précédemment
vols_documents = db['vols'].find()
avions_documents = db['avions'].find()

# Convertir les curseurs MongoDB en listes de dictionnaires
vols_data = list(vols_documents)
avions_data = list(avions_documents)

# Appliquer la fonction de jointure
result = jointure(vols_data, avions_data, "NumAv")

# Afficher les résultats de la jointure
for document in result:
    print(document) # Affiche tout lees documents ou NumAv est egal à 720
