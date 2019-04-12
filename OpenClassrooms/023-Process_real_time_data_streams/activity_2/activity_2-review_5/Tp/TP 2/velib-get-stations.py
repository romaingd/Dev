import json
import time
import urllib.request

from kafka import KafkaProducer

API_KEY = "400b2a6eb0214d21c0ca4674721a40035834a480"
url = "https://api.jcdecaux.com/vls/v1/stations?apiKey={}".format(API_KEY)

producer = KafkaProducer(bootstrap_servers="localhost:9092")

while True:
    response = urllib.request.urlopen(url)
    stations = json.loads(response.read().decode())
    for station in stations:
        if station["available_bike_stands"] == 0:
            producer.send("velib-empty-stations", json.dumps(station).encode()) 
    print("{} Produced {} station records".format(time.time(), len(stations)))
    time.sleep(1)
