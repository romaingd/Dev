import json
import fastavro

schema = json.load(open("plat.avsc"))
records = [
    {
        "nom": "饺子",
        "origine": "北京", 
        "ingredients": ["chou", "porc", "farine"],
        "prix": 4,
        "type": "plat"
    },
    {
        "nom": "方便面",
        "ingredients": ["piment", "nouilles"],
        "prix": 1.5,
        "type": "plat",
    },
    {
        "nom": "宫保鸡丁",
        "origine": "四川", 
        "ingredients": ["poulet", "cacahuetes"],
        "prix": 8,
        "type": "plat"
    },
    {
        "nom": "米饭",
        "ingredients": ["riz"],
        "prix": 1,
        "type": "accompagnement"
    },
    {
        "nom": "冰水",
        "prix": 0.5,
        "type": "accompagnement"
    }
]

fastavro.writer(open("plats.avro", "wb"), schema, records)