import json
from kafka import KafkaConsumer

stations_empty = {}
consumer = KafkaConsumer(
    "empty-stations",
    bootstrap_server=["localhost:9092", "localhost:9093"],
    group_id="monitor-empty-stations"
)

for message in consumer:
    station = json.loads(message.value.decode())

    # Get some info about the station
    station_number = station["number"]
    address = station["address"]
    contract = station["contract_name"]
    available_bike_stands = station["available_bike_stands"]

    # Find past information about the station
    if contract not in stations_empty:
        stations_empty[contract] = {}
    city_stations_empty = stations_empty[contract]

    if station_number not in city_stations_empty:
        city_stations_empty[station_number] = (available_bike_stands == 0)
    
    # Since a message was sent, the station is either:
    #   * empty now, but was not before
    #   * not empty now, but was before
    # A single boolean is enough to check which case it is.
    station_is_empty = (available_bike_stands == 0)
    city_stations_empty[station_number] = station_is_empty

    if station_is_empty:
        print('The station at address {} in city {} is now empty. {} empty stations in this city'.format(
            address,
            contract,
            sum(city_stations_empty.values())
        ))
