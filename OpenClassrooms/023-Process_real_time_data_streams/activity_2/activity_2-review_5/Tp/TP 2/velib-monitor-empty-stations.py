import json
import time
from kafka import KafkaConsumer

stations = {}
consumer = KafkaConsumer("velib-empty-stations", bootstrap_servers='localhost:9092', group_id="velib-monitor-stations")
for message in consumer:
    station = json.loads(message.value.decode())
    station_number = station["number"]
    contract = station["contract_name"]
    address = station["address"]
    print("{} , {}".format(station["address"], contract))