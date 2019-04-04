import json
import time
import urllib.request

from kafka import KafkaProducer


API_KEY = "XXX"
url = "https://api.jcdecaux.com/vls/v1/stations?apiKey={}".format(API_KEY)

producer = KafkaProducer(bootstrap_server=["localhost:9092", "localhost:9093"])

while True:
    response = urllib.request.urlopen(url)
    stations = json.loads(response.read().decode())
    for station in stations:
        producer.send(
            "velib-stations",
            json.dumps(station).encode(),
            key=str(station["number"].encode())     # same station -> same part.
        )
    print("{} Produced {} station records".format(time.time(), len(stations)))
    time.sleep(1)