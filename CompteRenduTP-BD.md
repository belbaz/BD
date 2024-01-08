<div align="center" style="margin-bottom: 15px;">

# Compte Rendu
# Base de Données

</div>
<div align="center" style="paddingTop: 45px; paddingBottom: 45px;">

![Texte alternatif](https://www.supalia.fr/medias/photo/logo-uspn-2023_1677074893564-png)

</div>

<div align="center" style="margin-top: 15px; margin-bottom: 25px;">
  
![image](https://github.com/belbaz/BD/assets/76886674/5b3080d2-fc0f-461c-b03a-bd33e69635f1)

</div>

<div align="center" style="margin-top: 25px; margin-bottom: 25px;">

# Benjamin Elbaz

</div>

# Sommaire

I. [Introduction](#i-introduction)
  
II. [Base de données](#ii-base-de-données)  

III. [Jointure](#iii-jointure)  

IV. [Rédis](#iv-rédis)  

V. [Test d'appartenance pour Redis](#v-test-dappartenance-pour-redis)  

VI. [MongoDB](#vi-mongodb)  

VII. [Test d'appartenance pour MongoDB](#vii-test-dappartenance-pour-mongodb)  

VIII. [Graphique des tests d'appartenance](#viii-graphique-des-tests-dappartenance)

IX. [Conclusion](#ix-conclusion)


# I. Introduction

Ce compte rendu vise à résumer nos séances de travaux pratiques en bases de données, axées sur Redis et MongoDB. Nous avons abordé les notions fondamentales de ces systèmes, tout en mettant en œuvre des scripts Python pour effectuer des opérations pratiques, telles que des jointures entre des tables.

L'exploration de Redis s'est concentrée sur des concepts clés tels que les structures de données clé-valeur, les ensembles, et les filtres de Bloom. Les scripts Python que nous avons développés ont permis d'appréhender des opérations courantes dans Redis, tout en se familiarisant avec des fonctionnalités comme les filtres de Bloom.

MongoDB a été une autre dimension de notre apprentissage, avec son modèle de données orienté document. Les scripts Python ont illustré des jointures entre différentes collections MongoDB, démontrant la flexibilité de ce système.

Au-delà des opérations directes sur les bases de données, nous avons également consacré du temps à des configurations préliminaires. Avant chaque nouvelle base de données, nous avons pris le temps de nous familiariser avec l'environnement, en effectuant des tests basiques et en configurant notre espace de travail.

Le processus de transformation de données a été une composante cruciale, passant de formats tels que TXT à CSV, puis à JSON. Ces manipulations ont consolidé notre compréhension des différents formats et ont renforcé nos compétences pratiques.

Enfin, pour faciliter l'accès et le partage du code développé, l'ensemble des scripts Python, y compris ceux pour la conversion de formats, les opérations Redis et les requêtes MongoDB, ont été regroupés sur un dépôt GitHub. Ci joint le lien : [GitHub](https://github.com/belbaz/BD/)

**Ce compte rendu s'articulera autour de deux axes principaux : Redis et MongoDB. Après une présentation de la base de données, nous explorerons Redis en présentant ses concepts et en détaillant des script Python. Suivront des tests d'appartenance, puis nous aborderons MongoDB avec son installation, des jointures, et des tests spécifiques. En conclusion.
En somme ce compte ce compte rendu reflète notre expérience pratique en bases de données, soulignant les compétences acquises et les activités concrètes, tout en mettant en avant le processus exploratoire de configuration et de prise en main avant chaque nouvelle base de données.**

# II. Base de données

Voici la représentation graphique de notre Base de Données, illustrée dans la Figure 1, où chaque entité est clairement définie avec ses attributs respectifs :

**Figure 1 : Schéma de la Base de Données**

![Figure 1: Schéma de la Base de Données](/ImageRapport/Figure1.png)

- AVIONS (NumAv, NomAv, CapAv, VilleAv)
- PILOTES (NumPil, NomPil, NaisPil, VillePil)
- CLIENTS (NumCl, NomCl, NumRueCl, NomRueCl, CodePosteCl, VilleCl)
- VOLS (NumVol, VilleD, VilleA, DateD, HD, DateA, HA, NumPil, NumAv)
- DEFCLASSES (NumVol, Classe, CoeffPrix)
- RESERVATIONS (NumCl, NumVol, Classe, NbPlaces)

Voici un guide d’installation de l'environnement Python pour Redis et MongoDB : [Lien Github](https://github.com/belbaz/BD/blob/main/README.md)

# III. Jointure

Au cours d'une séance de TP en base de données, nous avons entrepris une démarche de dénormalisation au travers de la réalisation d'une jointure entre les tables Vols, Defclasses, et Reservations. Il est à noter que les tables Avions, Pilotes, et Clients sont demeurées inchangées, préservant ainsi leur structure normalisée.

L'implémentation de cette dénormalisation s'est matérialisée via un script Python utilisant la bibliothèque pandas, lequel a effectué une jointure entre les données des vols, les définitions de classes et les réservations. Le résultat de cette opération a pris la forme d'une vue consolidée nommée "jointure.json".

Concrètement, la jointure s'est opérée sur la clé primaire "NumVol" présente dans les tables Vols et Defclasses, ainsi que dans la table Reservations. Cette opération a permis de fusionner de manière cohérente les informations pertinentes relatives aux vols, aux classes de vol, et aux réservations en une seule structure.

Notre approche de dénormalisation, matérialisée par cette jointure, s'inscrit dans une démarche plus large de facilitation de l'analyse des données. La clé primaire "NumVol" a exercé une fonction pivot en tant que lien central, facilitant la clarté des relations entre les enregistrements des diverses tables.

Il est crucial de souligner que cette démarche ne s'éloigne pas des principes fondamentaux de la normalisation des bases de données. Elle vise plutôt à optimiser la structure des données pour des besoins d'analyse spécifiques tout en maintenant l'intégrité et la cohérence des informations stockées.

Voici le lien du script de la jointure : [Lien Github](https://github.com/belbaz/BD/blob/main/Jointure/Jointure%20Normal/Jointure.py)

La nouvelle table résultante, nommée "jointure", a intégré les données des vols avec les définitions de classes et les réservations associées. La clé primaire "NumVol" a servi de référence pour unifier ces informations, facilitant ainsi l'analyse et la compréhension des relations entre les différentes instances.

**Figure 2 : Schéma de la Table jointure**

![Figure 2: Schéma de la Table jointure](/ImageRapport/Figure2.png)

Dans la figure 2, chaque ligne représente un enregistrement de la table "jointure", avec les colonnes correspondant aux différents attributs fusionnés des tables Vols, Defclasses et Reservations. Les colonnes spécifiques à chaque table d'origine sont préfixées pour indiquer leur provenance, assurant ainsi une clarté dans la structure consolidée.

# IV. Rédis

## 1. Présentation

Redis acronyme de "REmote DIctionary Server" est une base de données open source NoSQL.
il est conçue pour offrir des performances élevées et une grande simplicité d'utilisation

Les données sont stockées principalement en mémoire (RAM), ce qui signifie que toutes les opérations de lecture et d'écriture se font directement dans la mémoire vive. Cette conception offre des performances extrêmement intéressantes pour les opérations de lecture et d'écriture, ce qui est l'une des principales raisons de la popularité de Redis.

Redis stocke des données sous forme de paires clé-valeur.

## 2. Script Python de conversion

Cette troisième figure met en lumière le processus de transition des données du modèle relationnel vers le format adapté à Redis. Les carrés représentent les fichiers texte initiaux, qui sont des composants clés du modèle relationnel de la base de données. La conversion de ces fichiers vers les formats CSV et JSON est clairement visualisée, symbolisant une étape nécessaire pour préparer les données à être intégrées dans Redis.

L'objectif de cette conversion est de rendre les données compatibles avec le modèle clé-valeur de Redis, qui requiert une structure {nomTable: [nomChamps, ...], ...}. Les fichiers CSV et JSON, résultant de cette conversion, représentent une mise en forme adéquate pour l'intégration ultérieure dans le système Redis.

**Figure 3 :  Processus de Conversion des Fichiers Texte en Fichiers CSV et JSON**

![Figure 3 : Processus de Conversion des Fichiers Texte en Fichiers CSV et JSON](/ImageRapport/Figure3.png)

Script python TXT to CSV : [Lien Github](https://github.com/belbaz/BD/blob/main/TXT%20to%20CSV%20to%20JSON/TXT_TO_CSV.py)

Script python CSV to JSON : [Lien Github](https://github.com/belbaz/BD/blob/main/TXT%20to%20CSV%20to%20JSON/CSV_TO_JSON.py)

Script python qui fait la jointure avec Redis : [Lien Github](https://github.com/belbaz/BD/blob/main/Jointure/Jointure%20Redis/jointureRedis.py)

## V. Test d'appartenance pour Redis

Ce code vise à évaluer le temps nécessaire pour tester l'appartenance de 100 000 mots à une structure de données particulière, en utilisant trois approches différentes : Redis Set, Redis BloomFilter, et Redis normalement.

Le dictionnaire utilisé pour les tests provient du fichier CSV DEM-1_1.csv accessible à l'adresse suivante : [Lien CSV](http://rali.iro.umontreal.ca/DEM//DEM-1_1.csv)

Voici le lien du script : [Lien Github](https://github.com/belbaz/BD/blob/main/TestAppartenancesRedis/TestRedis.py)

## 1. Redis Set :

Dans la première approche, nous utilisons un ensemble Redis (sadd et sismember). L'ensemble Redis est une structure de données non ordonnée qui n'accepte pas de doublons. Pour chaque mot dans le dictionnaire, nous l'ajoutons à l'ensemble Redis. Ensuite, nous mesurons le temps nécessaire pour vérifier si chaque mot dans le test fait partie de cet ensemble.

## 2. Redis BloomFilter :

La deuxième approche repose sur l'utilisation d'un filtre de Bloom Redis (implémenté avec la bibliothèque pybloom_live). Un filtre de Bloom est une structure de données probabiliste qui permet de tester rapidement l'appartenance d'un élément. Il répond à la question suivante: est-ce que cet élément fait partie de l'ensemble ? Pour chaque mot dans le dictionnaire, nous ajoutons le mot au filtre de Bloom. Ensuite, nous mesurons le temps nécessaire pour vérifier si chaque mot dans le test appartient au filtre de Bloom.

## 3. Redis normalement :

La troisième approche utilise Redis de manière plus conventionnelle. Dans cette configuration, nous considérons que les mots sont les clés dans Redis, et nous mesurons le temps nécessaire pour récupérer chaque mot à partir de Redis avec la méthode get.

## 4. Résultat des tests :

- Redis normal :
  Temps d'exécution : 6.213 secondes
  Performances similaires à l'utilisation d'un ensemble Redis.

- Redis Set :
  Temps d'exécution : 6.727 secondes
  Performances significativement plus lentes que le filtre de Bloom Redis.

- Redis Bloom Filter :
  Temps d'exécution : 0.301 secondes
  Efficacité exceptionnelle pour les tests d'appartenance rapide.

Ces résultats confirment que le filtre de Bloom Redis offre des performances nettement supérieures pour les tests d'appartenance par rapport aux méthodes Redis conventionnelles.

# VI. MongoDB

## 1. Présentation de MongoDB

MongoDB, une base de données NoSQL, offre une approche flexible avec son modèle de données orienté document. La dénormalisation des données est encouragée, éliminant le besoin de jointures coûteuses.

MongoDB utilise des indexes qui agissent comme des dictionnaires, pointant directement vers les documents. Cette approche accélère les opérations de recherche avec une complexité logarithmique O(log(n)), assurant des performances optimales même avec des volumes de données importants.

Concernant le stockage, MongoDB conserve les données sur le disque tout en optimisant les performances grâce à l'utilisation de la mémoire. Les données fréquemment consultées sont mises en cache en mémoire, réduisant la nécessité d'accéder fréquemment au disque et améliorant ainsi l'efficacité globale du système.

## 2. Installation de MongoDB dans une Alpine Linux

Sous Alpine Linux, plusieurs étapes sont nécessaires avant de pouvoir lancer MongoDB.

Lien pour la configuration de l’Alpine Linux pour installer MongoDB : [lien ici](https://linux.how2shout.com/how-to-install-mongodb-server-on-alpine-linux/)

```bash
echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/main' >> /etc/apk/repositories
echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/community' >> /etc/apk/repositories
apk update
apk add  mongodb mongodb-tools
mkdir -p /data/db/
rc-service mongodb start
mongo
```

Insérer un document (une entrée de données) dans une collection appelée "posts" dans MongoDB :
```javascript
db.posts.insert({ subject: "Blog Post 1", content: "Lorem Ipsum"})
```

Rechercher des documents dans la collection "posts" :
```javascript
db.posts.find({ subject: "Blog Post 1" })
```

Mettre à jour un seul document dans une collection :
```javascript
db.posts.updateOne(
  { subject: "Blog Post 1" }, // Critère de recherche
  { $set: { content: "New Post" } } // Nouvelles valeurs à mettre à jour
)
```

On crée d'abord les collections Employee et Dept :
```javascript
db.createCollection("Employee");
db.createCollection("Dept");
```

## 3. Jointure pour MongoDB (Python)

Voir le code ici : [Lien Github](https://github.com/belbaz/BD/blob/main/Jointure/Jointure%20MongoDB/joiuntureMongoDB.py)

La Figure 4 présente le résultat de la jointure locale effectuée à l'aide du code Python utilisant MongoClient, disponible sur GitHub. Cette opération de jointure a été réalisée entre les collections MongoDB "Vols", "Defclasses", et "Reservations". Chaque ligne de la figure représente un enregistrement résultant de cette jointure, combinant de manière cohérente les données des trois collections. L'objectif est de consolider les informations dispersées sur les vols, les classes de vol, et les réservations. La clé de jointure utilisée est "NumVol", assurant la cohérence des liens entre les enregistrements. La suppression du champ "_id" est effectuée pour garantir une sérialisation JSON adaptée, facilitant ainsi la lisibilité et l'utilisation ultérieure des données consolidées.

**Figure 4 : Résultat de la Jointure MongoDB**

![Figure 4: Résultat de la Jointure MongoDB](/ImageRapport/Figure4.png)



## 4. Jointure pour MongoDB

### Insertion de vols dans la collection "Vols" de MongoDB :

```javascript
db.Vols.insertMany([
  { "NumVol": 1, "VilleD": "Paris", "VilleA": "New York"},
  { "NumVol": 2, "VilleD": "London", "VilleA": "Tokyo"},
]);
```

Insertion de vols dans la collection "Defclasses" de MongoDB :
```javascript
db.Defclasses.insertMany([
  { "NumVol": 1, "Classe": "Economique", "CoeffPrix": 1.0 },
  { "NumVol": 2, "Classe": "Affaires", "CoeffPrix": 1.5 },
]);
```

Insertion de vols dans la collection "Reservations" de MongoDB :
```javascript
db.Reservations.insertMany([
  { "NumCl": 101, "NumVol": 1, "Classe": "Economique", "NbPlaces": 2 },
  { "NumCl": 102, "NumVol": 2, "Classe": "Affaires", "NbPlaces": 1 },
]);
```

Ce code réalise une jointure entre trois collections MongoDB : "Vols", "Defclasses", et "Reservations". Il utilise l'agrégation MongoDB pour combiner les documents des collections en fonction du champ "NumVol". La première étape ($lookup) associe les données de la collection "Defclasses" à celles de "Vols" en utilisant le champ "NumVol". Ensuite, le résultat est déplié ($unwind) pour obtenir une structure de document unique. Une deuxième jointure est effectuée avec la collection "Reservations", suivie d'un autre dépliement. Enfin, le projet ($project) sélectionne les champs pertinents des collections liées pour former un document résultant consolidé. Ce processus crée un ensemble de documents résultants représentant une vue consolidée des vols avec des détails sur les classes et les réservations associées.

Code de la Jointure : 
```javascript
var result = db.Vols.aggregate([
  {
    $lookup: {
      from: "Defclasses",
      localField: "NumVol",
      foreignField: "NumVol",
      as: "defclassesDetails"
    }
  },
  {
    $unwind: "$defclassesDetails"
  },
  {
    $lookup: {
      from: "Reservations",
      localField: "NumVol",
      foreignField: "NumVol",
      as: "reservationsDetails"
    }
  },
  {
    $unwind: "$reservationsDetails"
  },
  {
    $project: {
      "NumVol": 1,
      "VilleD": 1,
      "VilleA": 1,
      /* ... autres champs de la collection Vols ... */	
      "Classe": "$defclassesDetails.Classe",
      "CoeffPrix": "$defclassesDetails.CoeffPrix",
      "NumCl": "$reservationsDetails.NumCl",
      "NbPlaces": "$reservationsDetails.NbPlaces"
    }
  }
]);

result.forEach(doc => printjson(doc));
```

# VII. Test d'appartenance pour MongoDB

Dans ce script, nous évaluons le temps nécessaire pour tester l'appartenance d'un mot dans un dictionnaire contenant 100 000 mots dans une base de données MongoDB. Nous comparons deux scénarios : un avec un index et un sans index.

Un index MongoDB est une structure de données qui améliore la rapidité des opérations de recherche sur une collection. Il agit comme un tableau, établissant une correspondance entre les valeurs d'un champ particulier d'une collection et les documents associés. L'ajout d'un index sur un champ permet à MongoDB de parcourir ce champ plus efficacement lors de l'exécution de requêtes.

Voici le lien du script : [Lien Github](https://github.com/belbaz/BD/blob/main/TestAppartenancesMongo/TestMongo.py)

Dans ce script, nous utilisons PyMongo pour interagir avec MongoDB. Nous créons deux collections, l'une avec un index et l'autre sans, mesurant ainsi le temps d'exécution pour chaque scénario. L'indexation dans MongoDB peut améliorer les performances des requêtes de recherche, mais elle nécessite également des ressources supplémentaires lors de l'insertion ou de la mise à jour de données. Les résultats du test permettront de déterminer l'impact de l'index sur les opérations d'appartenance dans ce contexte particulier.

## MongoDB avec index :

Temps d'exécution : 1.23 secondes
L'utilisation d'un index améliore légèrement la performance, réduisant le temps d'exécution des opérations d'appartenance.

## MongoDB sans index :

Temps d'exécution : 1.31 secondes
L'absence d'index montre une légère augmentation du temps d'exécution, impactant la rapidité des requêtes d'appartenance.

## VIII. Graphique des tests d’appartenance

Voici un graphique comparant les temps d'exécution des différents tests d'appartenance sur le dictionnaire qui contient 100 000 mots. Il illustre la durée, en secondes, nécessaire pour chaque test d'appartenance dans les contextes suivants : MongoDB sans index, MongoDB avec index, Redis standard, Redis Set, et Redis BloomFilter.

**Figure 5 : Comparaison des tests d'Appartenance entre MongoDB et Redis**

![Figure 5: Comparaison des tests d'Appartenance entre MongoDB et Redis](/ImageRapport/Figure5.png)


## IX. Conclusion

En conclusion, nous avons mis en œuvre des opérations pratiques, notamment des jointures entre les tables Vols, Defclasses et Reservations dans le cadre de séances de travaux pratiques en bases de données. La dénormalisation a été démontrée par la création d'une vue consolidée baptisée "jointure.json", réalisée à l'aide d'un script Python avec la bibliothèque pandas.

Dans le contexte de Redis, nous avons effectué des opérations de conversion de fichiers texte vers les formats CSV et JSON, nécessaires pour intégrer les données dans le modèle clé-valeur de Redis. Les tests d'appartenance ont souligné l'efficacité du filtre de Bloom, notamment par rapport à l'utilisation d'un ensemble Redis de manière conventionnelle.

Quant à MongoDB, nous avons exploré son modèle de données orienté document en réalisant des jointures entre les collections Vols, Defclasses et Reservations. Des tests d'appartenance ont été conduits pour évaluer les performances avec et sans index, mettant en lumière l'impact significatif de cette optimisation.

Cette expérience pratique nous a permis d'approfondir nos compétences dans la gestion opérationnelle de bases de données, la réalisation de jointures, la dénormalisation, et l'évaluation comparative des performances entre Redis et MongoDB.

