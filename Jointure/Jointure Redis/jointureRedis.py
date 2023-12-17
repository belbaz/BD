import json
import redis

# Se connecter à Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

def charger_fichier_json(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        donnees = json.load(fichier)
    return donnees

def inserer_donnees_dans_redis(donnees, prefixe_cle):
    for item in donnees:
        cle = f"{prefixe_cle}:{item['NumVol']}"
        redis_client.hset(cle, mapping=item)

def effectuer_jointure():
    donnees_defclasses = charger_fichier_json("DEFCLASSES.json")
    donnees_reservations = charger_fichier_json("RESERVATIONS.json")
    donnees_vols = charger_fichier_json("VOLS.json")

    # Insérer les données dans Redis
    inserer_donnees_dans_redis(donnees_defclasses, "DEFCLASSES")
    inserer_donnees_dans_redis(donnees_reservations, "RESERVATIONS")
    inserer_donnees_dans_redis(donnees_vols, "VOLS")

    # Exemple : Jointure entre DEFCLASSES et RESERVATIONS basée sur NumVol
    donnees_jointes = []
    for reservation in donnees_reservations:
        num_vol = reservation["NumVol"]
        cle_defclasses = f"DEFCLASSES:{num_vol}"
        cle_vols = f"VOLS:{num_vol}"

        info_defclasses = redis_client.hgetall(cle_defclasses)
        info_vols = redis_client.hgetall(cle_vols)

        if info_defclasses and info_vols:
            item_joint = {**info_vols, **info_defclasses, **reservation}
            donnees_jointes.append(item_joint)

    # Enregistrer le résultat dans un fichier JSON
    with open("jointure.json", 'w') as fichier_jointure:
        json.dump(donnees_jointes, fichier_jointure, indent=2)

if __name__ == "__main__":
    effectuer_jointure()
