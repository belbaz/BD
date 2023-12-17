import csv
import redis
import time
from pybloom_live import BloomFilter

# Initialisation de la connexion Redis
redis_host = 'localhost'  # Remplacez par l'adresse de votre serveur Redis
redis_port = 6379
redis_db = 0
redis_connection = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

# Charger le fichier CSV dans un dictionnaire (mot, définition)
dictionary = {}
with open('DEM-1_1.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        word = row[0]  # Utiliser l'index de la colonne pour le mot
        definition = row[0]  # Utiliser l'index de la colonne pour la définition
        dictionary[word] = definition

# Convertir le dictionnaire en une liste de mots
word_list = list(dictionary.keys())

# Initialiser le filtre de Bloom
bloom_filter_capacity = 200000
bloom_filter_error_rate = 0.001
redis_bloom_key = 'my_redis_bloom'
redis_bloom = BloomFilter(capacity=bloom_filter_capacity, error_rate=bloom_filter_error_rate)

# Ajouter les mots au filtre de Bloom
for word in word_list:
    redis_bloom.add(word)

# Convertir le filtre de Bloom en une chaîne d'octets (bytes) pour le stocker dans Redis
serialized_bloom = redis_bloom.bitarray.tobytes()

# Stocker la chaîne d'octets dans Redis
redis_connection.set(redis_bloom_key, serialized_bloom)

# Tester l'appartenance pour 100 000 mots et mesurer le temps avec Redis Bloom Filter
test_words = word_list[:100000]

start_time_redis_bloom = time.time()
for word in test_words:
    _ = word.encode() in redis_bloom
end_time_redis_bloom = time.time()
elapsed_time_redis_bloom = end_time_redis_bloom - start_time_redis_bloom

# Tester l'appartenance pour 100 000 mots et mesurer le temps avec Redis Set
redis_set_key = 'my_redis_set'
redis_connection.sadd(redis_set_key, *word_list)

start_time_redis_set = time.time()
for word in test_words:
    _ = redis_connection.sismember(redis_set_key, word)
end_time_redis_set = time.time()
elapsed_time_redis_set = end_time_redis_set - start_time_redis_set

# Tester l'appartenance pour 100 000 mots et mesurer le temps avec Redis normalement
start_time_redis = time.time()
for word in test_words:
    _ = redis_connection.get(word)
end_time_redis = time.time()
elapsed_time_redis = end_time_redis - start_time_redis

print(f"Temps avec Redis Normal : {elapsed_time_redis} secondes")
print(f"Temps avec Redis Set : {elapsed_time_redis_set} secondes")
print(f"Temps avec Redis Bloom Filter : {elapsed_time_redis_bloom} secondes")
