package velos;

import org.apache.storm.Config;
import org.apache.storm.LocalCluster;
import org.apache.storm.StormSubmitter;
import org.apache.storm.generated.AlreadyAliveException;
import org.apache.storm.generated.AuthorizationException;
import org.apache.storm.generated.InvalidTopologyException;
import org.apache.storm.generated.StormTopology;
import org.apache.storm.kafka.spout.KafkaSpout;
import org.apache.storm.kafka.spout.KafkaSpoutConfig;
import org.apache.storm.topology.TopologyBuilder;
import org.apache.storm.topology.base.BaseWindowedBolt;
import org.apache.storm.tuple.Fields;

public class App 
{
    public static void main( String[] args ) throws AlreadyAliveException, InvalidTopologyException, AuthorizationException {
    	TopologyBuilder builder = new TopologyBuilder();
    	
        // Create a KafkaSpoutConfigBuilder by passing as input parameters
        // a Kafka broker address, and a Kafka topic name
    	KafkaSpoutConfig.Builder<String, String> spoutConfigBuilder = KafkaSpoutConfig.builder("localhost:9092", "velib-stations");
        // Set the Kafka group of the spout
    	spoutConfigBuilder.setGroupId("city-stats");
        // Build the config
    	KafkaSpoutConfig<String, String> spoutConfig = spoutConfigBuilder.build();
        // And finally create the KafkaSpout itself
    	builder.setSpout("stations", new KafkaSpout<String, String>(spoutConfig));
    	
        // Create the bolds that will complete the topology
    	builder.setBolt("station-parsing", new StationParsingBolt())
    		.shuffleGrouping("stations");
    	
    	builder.setBolt("city-stats", new CityStatsBolt().withTumblingWindow(BaseWindowedBolt.Duration.of(1000*60*5)))
    		.fieldsGrouping("station-parsing", new Fields("city"));
    	
    	builder.setBolt("save-results",  new SaveResultsBolt())
    		.fieldsGrouping("city-stats", new Fields("city"));
    	
        // Build the topology itself
    	StormTopology topology = builder.createTopology();

    	Config config = new Config();
    	config.setMessageTimeoutSecs(60*30);
    	String topologyName = "velos";

        // If we passed the "remote" argument, submit to a Storm cluster
        // Otherwise, submit to a new local cluster
    	if(args.length > 0 && args[0].equals("remote")) {
    		StormSubmitter.submitTopology(topologyName, config, topology);
    	}
    	else {
    		LocalCluster cluster = new LocalCluster();
        	cluster.submitTopology(topologyName, config, topology);
    	}
    }
}
