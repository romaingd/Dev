import json
from kafka import KafkaConsumer

city_empty_stations = {}
consumer = KafkaConsumer("empty-stations", bootstrap_servers='localhost:9092', group_id="velib-monitor-empty-stations")
for message in consumer:
    
    station = json.loads(message.value.decode())
    station_name = station["name"]
    station_status = station["filling"]
    station_address = station["address"]
    contract = station["contract_name"]

    if contract not in city_empty_stations:
        city_empty_stations[contract] = 0 #init le nombre de stations vides de la ville a 0
    
    if station_status == "empty" : #si le message est "empty" alors j'incrémente le nombre de stations vides de la ville et j'affiche le message
        #sinon, je décrémente le nombre de stations vides de la ville, avec un minimum de 0
        city_empty_stations[contract] += 1
        print("Une nouvelle station vide, {}. Cela en fait {} à {} !".format(station_address,str(city_empty_stations[contract]),contract))

    else : 
        if city_empty_stations[contract] > 1 :
            city_empty_stations[contract] -= 1
            print("Une station vide en moins ici : {}, {}. Plus que {} !".format(station_address,contract,str(city_empty_stations[contract])))
        else :
            city_empty_stations[contract]=0
            print("Bravo ! D'après nos données, plus aucune station vide à {}!".format(contract))
    