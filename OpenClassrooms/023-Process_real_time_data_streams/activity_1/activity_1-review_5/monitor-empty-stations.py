import json
from kafka import KafkaConsumer

stations = {}
# créons un consumer Kafka pour le topic velib-stations
consumer = KafkaConsumer("empty-stations", bootstrap_servers='localhost:9092', group_id="velib-monitor-stations")

for message in consumer:
    station = json.loads(message.value.decode())
    station_number = station["number"]
    contract = station["contract_name"]
    available_bike_stands = station["available_bike_stands"]

    if contract not in stations:
        stations[contract] = {}
    city_stations = stations[contract]

    if station_number not in city_stations:
        city_stations[station_number] = available_bike_stands

    if available_bike_stands == 0:
        print("{} {} ({})".format(
            "Empty: " , station["address"], contract
        ))