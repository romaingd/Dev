#! /usr/bin/env python3
import json
import time
import urllib.request

# Run `pip install kafka-python` to install this package
from kafka import KafkaProducer

API_KEY = "XXXX" # A METTRE A JOUR
url = "https://api.jcdecaux.com/vls/v1/stations?apiKey={}".format(API_KEY)

producer = KafkaProducer(bootstrap_servers="localhost:9092")

# Pour pouvoir savoir si la station devient vide ou ne l'est plus, il faut sauvegarder son état.
# Pour cela, on utilise un dictionnaire (historique), qui aura :
#  - comme clef la paire (contract,station_number) qui est unique.
#  - comme valeur 0 ou 1, selon que la station est vide (0) ou non vide (1)
historique={}

while True:
    response = urllib.request.urlopen(url)
    stations = json.loads(response.read().decode())
    for station in stations:
        station_number = station["number"]
        contract = station["contract_name"]
        available_bikes = station["available_bikes"]

        # Testons si la station est déjà dans notre historique
        if (contract,station_number) not in historique:
            # Elle n'y est pas. Nous allons donc l'ajouter.
            # cette valeur vaut 0 quand le nombre de vélos est nul et vaut 1 quand le nombre de vélos est supérieur ou égal à 1
            historique[(contract,station_number)] = 0 if available_bikes==0 else 1
            # Pas d'emission de message car on ne connais pas son état précédent
        else:
            # Cette station est dans notre historique
            # Calculons le nouvel état (0: vide, 1: non vide)
            nouvel_etat=0 if available_bikes==0 else 1
            # Testons si notre état a changé. S'il n'a pas changé, aucune action a accomplir.
            if nouvel_etat != historique[(contract,station_number)]:
                # L'état de la station a changé. Mettons à jour l'historique et envoyons un message.
                historique[(contract,station_number)]=nouvel_etat
                # !!! On utilise ci-dessous le nom de la ville ("contract") pour la répartition des données dans les partitions
                # Ainsi, toutes les stations d'une même ville seront affectées à une même partition
                producer.send("empty-stations", json.dumps(station).encode(),key=str(contract).encode())
                # Ajout d'un print pour la correction afin de vérifier la cohérence entre info émises et reçues
                print("Envoi d'un message, ville {} station {} : nombre de vélos = {}".format(contract,station["address"],available_bikes))
    print("Produced {} station records".format(len(stations)))
time.sleep(1)
