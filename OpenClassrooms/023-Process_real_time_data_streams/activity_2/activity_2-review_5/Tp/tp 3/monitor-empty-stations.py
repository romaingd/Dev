#!/usr/bin/env python3
import json
from kafka import KafkaConsumer

stations_vides = {}
consumer = KafkaConsumer("empty-stations", bootstrap_servers='localhost:9092', group_id="monitor-empty-stations")
for message in consumer:
    station = json.loads(message.value.decode())
    station_number = station["number"]
    contract = station["contract_name"]
    available_bikes = station["available_bikes"]
    address=station["address"]

    # Pour connaitre le nombre de stations vides dans la ville, il faut les memoriser dans un dictionnaire.
    # Si le message reçu est celui d'une station vide, on l'ajoute à la liste de la ville.
    # Si le message reçu est celui d'une station non vide, on le retire de la liste de la ville.

    if contract not in stations_vides:
        # La ville n'est pas connue, on ajoute la liste vide correspondante dans le dictionnaire
        stations_vides[contract]=[]
        if available_bikes == 0:
            # Si le message reçu indique que la station vient de se vider,
            # on ajoute le nom de la station à la liste
            stations_vides[contract].append(station_number)
    else:
        # La ville est déjà dans le dictionnaire
        if available_bikes == 0: 
            # Si le message indique que la station vient de se vider,
            # on l'ajoute à la liste
            stations_vides[contract].append(station_number)
        else:
            if station_number in stations_vides[contract]:
                # Si le message indique que la station n'est plus vide
                # et si la station est dans la liste, on la supprime de la liste 
                stations_vides[contract].remove(station_number)
           
    if available_bikes==0:
        # Si la station vient de se vider, on affiche un message
        print("La ville de {} a {} station(s) vide(s), dont la station située '{}'.".format(
            contract,                      # ville de la station
            len(stations_vides[contract]), # nombre de stations vides dans la ville
            address                        # adresse de la station
        ))
