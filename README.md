# Base de Données 2023

# Prérequis

- Assurez-vous d'avoir installé Redis et de l'avoir lancé sur le port 6379. En cas de problème avec Redis, accédez aux services et démarrez le service Redis.
- Assurez-vous d'avoir installé MongoDB et de l'avoir lancé sur le port 27017.

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

3. Installez les dépendances nécessaires :
    ```bash
    pip install pymongo pandas redis pybloom_live
    ```

Ces étapes vous permettront de mettre en place l'environnement nécessaire pour travailler avec les bases de données, notamment MongoDB et Redis.
