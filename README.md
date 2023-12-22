# Base de Données 2023

# Prérequis

- Assurez-vous d'avoir installé Redis et de l'avoir lancé sur le port 6379. En cas de problème avec Redis, accédez aux services et démarrez le service Redis.
- Lien d'installation pour installé Redis sur windows : https://github.com/tporadowski/redis/releases/tag/v5.0.14.1
- Assurez-vous d'avoir installé MongoDB et de l'avoir lancé sur le port 27017.
- Lien d'installation pour installé MongoDBCompass : https://www.mongodb.com/products/tools/compass

# Avant de Commencer

1. Créez un environnement virtuel avec la commande suivante :
    ```bash
    python -m venv venv
    ```

2. Activez l'environnement virtuel :
    - Linux :
        ```bash
        . venv/bin/activate
        ```
    - Windows :
        ```bash
        venv\Scripts\activate.bat
        ```
  3. Mettre a jour PIP :
      ```bash
      python.exe -m pip install --upgrade pip
      ```      

5. Installez les dépendances nécessaires (pymongo, pandas, redis et pybloom_live) :
    ```bash
    pip install pymongo pandas redis pybloom_live
    ```

Ces étapes vont nous permettre de mettre en place l'environnement nécessaire pour travailler avec les bases de données, notamment MongoDB et Redis.
