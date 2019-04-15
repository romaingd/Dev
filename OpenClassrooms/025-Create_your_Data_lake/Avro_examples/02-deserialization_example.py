import fastavro

# Open a binary file in reading mode
with open("characters.avro", "rb") as avro_file:
    reader = fastavro.reader(avro_file)
    print(reader.schema)
    for character in reader:
        print(character)

# # Using HDFS
# import hdfs
# hdfs_client = hdfs.InsecureClient("http://0.0.0.0:9870")

# with hdfs_client.read("/hdfs/path/data.avro") as avro_file:
#     reader = fastavro.reader(avro_file)