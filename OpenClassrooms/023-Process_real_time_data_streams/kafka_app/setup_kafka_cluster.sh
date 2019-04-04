# Start the cluster manager
$KAFKA_HOME/bin/zookeeper-server-start.sh -daemon $KAFKA_HOME/config/zookeeper.properties
# Start the cluster itself
$KAFKA_HOME/bin/kafka-server-start.sh -daemon $KAFKA_HOME/config/server.properties


# Setup a distributed cluster
# First setup a second Kafka server
cp $KAFKA_HOME/config/server.properties $KAFKA_HOME/config/server1.properties

# WARNING: Make sure you change the following fields in server1.properties 
# to avoid conflicts with the running server:
#   - broker.id - Should be unique
#   - listeners - Should be unique if both servers are run on a single machine
#                 (here we chose localhost:9093 in the scripts)
#   - log.dirs - Should be unique if both servers are run on a single machine 

# Start the second Kafka server
$KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server1.properties


# It is also possible to setup multiple Zookeeper nodes (in a cluster),
# but is quite boring to describe here se we refer the reader to any tutorial.
# One thing to keep in mind is to set different ports for the different nodes.


# Create the topic
# Set the replication factor to 2 for better fault tolerance
$KAFKA_HOME/bin/kafka-topics.sh \
    --create \
    --zookeeper localhost:2181 \
    --replication-factor 2 \
    --partitions 1 \
    --topic velib-stations

# Add partitions to allow new consumers
$KAFKA_HOME/bin/kafka-topics.sh \
    --alter \
    --zookeeper localhost:2181 \
    --topic velib-stations \
    --partitions 10

# Since messages are obsolete after each API call, retention time can and
# should be reduced
$KAFKA_HOME/bin/kafka-configs.sh \
    --zookeeper localhost:2181 \
    --entity-type topics \
    --entity_name velib-stations \
    --alter \
    --add-config retention.ms=4000
# ... as well as segment duration
$KAFKA_HOME/bin/kafka-configs.sh \
    --zookeeper localhost:2181 \
    --entity-type topics \
    --entity_name velib-stations \
    --alter \
    --add-config segment.ms=4000

# Make sure partitions are well distributed among the servers
$KAFKA_HOME/bin/kafka-topics.sh \
    --describe \
    --zookeeper localhost:2181 \
    --topic velib-stations



# Launch the producer in another window/tab
# python ./velib-get-stations.py

# Launch consumer instances in another window/tab
# python ./velib-monitor-stations.py