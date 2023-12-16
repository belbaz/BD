## BD

# Requirement

Avoir installer Redis et l'avoir lancer sur le port 6379 (si redis ne marche pas allez dans les servies et allez démarrer le services Redis)
Avoir installer MongoDB et l'avoir lancer sur le port 27017

# avant de commencer
python -m venv venv
Linux : . venv/bin/activate 
Windows : venv\Scripts\activate.bat

pip install pymongo redis pybloom_live

# Arborécence

Le dossier Script contients les scripts suivants :
-) dans le Dossier TXT : les fichier de la BD en TXT
-) dans le Dossier CSV : les fichier convertis en CSV
-) dans le Dossier JSON : les fichier convertis en JSON

Le dossier TestAppartenancesMongo Contient les fichiers de test.

Le dossier TestAppartenancesRedis Contient les fichiers de test.
