import json
import time
import urllib.request
import hashlib

from kafka import KafkaProducer

API_KEY = "63a60617bf34e206f881ca4869902e3db5240ccf" # FIXME Set your own API key here
url = "https://api.jcdecaux.com/vls/v1/stations?apiKey={}".format(API_KEY)

producer = KafkaProducer(bootstrap_servers="localhost:9092")
station_inventory = {}

while True:
    response = urllib.request.urlopen(url)
    stations = json.loads(response.read().decode())
    for station in stations:
        #trouver un id unique par station
        text= station['contract_name']+"_"+str(station['number'])
        id_unique= int(hashlib.md5(text.encode('utf-8')).hexdigest()[:8], 16) 
        if id_unique in station_inventory : 
            if station['available_bikes'] == 0 and station_inventory[id_unique]['available_bikes'] > 0 :
            # si la station n'est pas vide et qu'elle le devient
                station['filling']="empty"
                print("Looks like station {} ({}) is {} again!".format(station['name'],station['contract_name'],station['filling']))
                producer.send("empty-stations", json.dumps(station).encode(),key=str(station["number"]).encode())
            elif station['available_bikes']>0 and station_inventory[id_unique]['available_bikes']==0 :
            # si la station est vide et qu'elle ne l'est plus
                station['filling']="filled"
                print("Looks like station {} ({}) is {} again!".format(station['name'],station['contract_name'],station['filling']))
                producer.send("empty-stations", json.dumps(station).encode(),key=str(station["number"]).encode())
        else :
            print("Did Not Found This Index...")
        station_inventory[id_unique]=station
        producer.send("velib-stations", json.dumps(station).encode())
 #   print("{} Produced {} station records".format(time.time(), len(stations)))
    time.sleep(1)