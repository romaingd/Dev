import json
import time
import urllib.request
from kafka import KafkaProducer

API_KEY = '0e70f90b01ed158d569bf684e3584e49a42f548f'
url = 'https://api.jcdecaux.com/vls/v1/stations?apiKey={}'.format('0e70f90b01ed158d569bf684e3584e49a42f548f')

producer = KafkaProducer(bootstrap_servers='localhost:9092')

empty_stations = []

while True:
    response = urllib.request.urlopen(url)
    stations = json.loads(response.read().decode())

    for station in stations:
        available_bike_stands = station["available_bike_stands"]
        if available_bike_stands == 0 and station not in empty_stations:
            empty_stations.append(station)
            producer.send('empty-stations', json.dumps(station).encode())
        elif available_bike_stands != 0 and station in empty_stations:
            empty_stations.remove(station)
            producer.send('empty-stations', json.dumps(station).encode())

    print('{} Produced {} station records'.format(time.time(), len(stations)))
    time.sleep(1)