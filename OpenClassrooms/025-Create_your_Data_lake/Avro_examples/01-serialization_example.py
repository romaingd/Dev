import fastavro

# Define characters
characters = [
    {
        "id": 1,
        "name": "Martin Riggs"
    },
    {
        "id": 2,
        "name": "John Wick"
    },
    {
        "id": 3,
        "name": "Ripley"
    }
]

# Define data schema
schema = {
    "type": "record",
    "namespace": "com.badassmoviecharacters",
    "name": "Character",
    "doc": "Seriously badass characters",
    "fields": [
        {"name": "name", "type": "string"},
        {"name": "id", "type": "int"}
    ]
}

# More complex schema
schema = {
    "type": "record",
    "namespace": "com.badassmoviecharacters",
    "name": "Character",
    "fields": [
        {"name": "name", "type": "string"},
        {"name": "id", "type": "int"},
        {"name": "genre", "type": {"type": "enum", "name": "Genre", "symbols": ["HORROR", "ACTION", "OTHER"]}, "default": "HORROR"}
        {"name": "movies", "type": {"type": "array", "items": {
            "type": "record",
            "namespace": "com.badassmoviecharacters",
            "name": "Movie",
            "fields": [
                {"name": "title", "type": "string"},
                {"name": "year", "type": ["int", "null"]},
                {"name": "actors", "type": {
                    "type": "array",
                    "items": "string"
                }}
            ]
        }}}
    ]
}






# Open a binary file in writing mode
with open("characters.avro", "wb") as avro_file:
    fastavro.writer(avro_file, schema, characters)

# # Using HDFS
# import hdfs
# hdfs_client = hdfs.InsecureClient("http://0.0.0.0:9870")

# with hdfs_client.write("/hdfs/path/data.avro") as avro_file:
#     fastavro.writer(avro_file, schema, characters)