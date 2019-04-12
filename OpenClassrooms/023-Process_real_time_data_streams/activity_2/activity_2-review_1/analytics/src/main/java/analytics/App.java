package analytics;

import org.apache.storm.Config;
import org.apache.storm.LocalCluster;
import org.apache.storm.StormSubmitter;
import org.apache.storm.generated.AlreadyAliveException;
import org.apache.storm.generated.AuthorizationException;
import org.apache.storm.generated.InvalidTopologyException;
import org.apache.storm.generated.StormTopology;
import org.apache.storm.topology.TopologyBuilder;
import org.apache.storm.topology.base.BaseWindowedBolt;
import org.apache.storm.tuple.Fields;


/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args ) throws AlreadyAliveException, InvalidTopologyException, AuthorizationException
    {
        TopologyBuilder builder = new TopologyBuilder();
        builder.setSpout("page-visits", new PageVisitSpout());
        builder.setBolt("visit-counts", new VisitCountBolt(), 1).shuffleGrouping("page-visits");
        builder.setBolt("user-counts", new UserVisitCountBolt(), 2).fieldsGrouping("page-visits", new Fields("userId"));
        builder.setBolt("page-counts", new PageVisitCountBolt(), 2).fieldsGrouping("page-visits", new Fields("url"));
        builder.setBolt("user-page-visit-counts", new UserPageVisitCount().withWindow(BaseWindowedBolt.Duration.of(601000), BaseWindowedBolt.Duration.of(101000)), 3).fieldsGrouping("page-visits", new Fields("url","userId"));
        //builder.setBolt("user-page-visit-counts", new UserPageVisitCount().withTumblingWindow(BaseWindowedBolt.Duration.of(30000)),2).fieldsGrouping("page-visits", new Fields("userId"));
        
        StormTopology topology = builder.createTopology();
        
        Config config = new Config();
        config.setMessageTimeoutSecs(3600);
        String topologyName = "analytics-topology";
        
        if (args.length > 0 && args[0].equals("remote")) {
        	StormSubmitter.submitTopology(topologyName, config, topology);
        }
        else{
        	System.out.println("Start cluster");
        	LocalCluster cluster = new LocalCluster();
        	cluster.submitTopology(topologyName, config, topology);
        }
    }
}
