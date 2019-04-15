# Fixed after correction
import json
import fastavro


schema = {
    "type": "record",
    "namespace": "com.lefabuleuxmandarindor",
    "name": "Plat",
    "doc": "Plats du restaurant chinois",
    "fields": [
        {"name": "nom", "type": "string"},
        {"name": "origine", "type": ["string", "null"], "default": "null"},
        {"name": "prix", "type": "float"},
        {"name": "type", "type": {
            "type": "enum",
            "name": "Genre",
            "symbols": ["plat", "accompagnement"]
        }},
        {"name": "ingredients", "type": {
            "type": "array",
            "items": "string"
        }, "default": []}
    ]
}
