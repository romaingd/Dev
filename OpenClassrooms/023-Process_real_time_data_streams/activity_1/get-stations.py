import json
import time
import urllib.request

from kafka import KafkaProducer


API_KEY = "XXX"
url = "https://api.jcdecaux.com/vls/v1/stations?apiKey={}".format(API_KEY)

producer = KafkaProducer(bootstrap_server=["localhost:9092", "localhost:9093"])

# Store the status of stations, grouped by city
stations_empty = {}

while True:
    response = urllib.request.urlopen(url)
    stations = json.loads(response.read().decode())

    for station in stations:
        # Get info about the station
        station_number = station["number"]
        contract = station["contract_name"]
        available_bike_stands = station["available_bike_stands"]

        # Find past information about the station
        if contract not in stations:
            stations_empty[contract] = {}
        city_stations_empty = stations_empty[contract]

        if station_number not in city_stations_empty:
            city_stations_empty[station_number] = (available_bike_stands == 0)

        station_was_empty = city_stations_empty[station_number]
        station_is_empty = (available_bike_stands > 0)

        # Send a message if the station changed "emptiness status"
        if (station_is_empty ^ station_was_empty):
            producer.send(
                "empty-stations",
                json.dumps(station).encode(),
                key=str(station["number"].encode())  # same stat. -> same part.
            )
        
        city_stations_empty[station_number] = (available_bike_stands == 0)

    print("{} Produced {} station records".format(time.time(), len(stations)))
    time.sleep(1)