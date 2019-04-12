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

public class App 
{
	public static void main( String[] args ) throws AlreadyAliveException, InvalidTopologyException, AuthorizationException
	{
		TopologyBuilder builder = new TopologyBuilder();
		builder.setSpout("page-visits", new PageVisitSpout());
    	builder.setBolt("user-page-visits-counts", new UserPageVisitCount()
            .withWindow( 
                BaseWindowedBolt.Duration.of(1000*60*60), // window length  (visite sur la dernière heure d'après l'énoncé, soit 1000*60*60 ms)
                BaseWindowedBolt.Duration.of(1000*30)     // sliding interval (toutes les 30 secondes, soit 30 000 ms)
            )        
        )
    		.fieldsGrouping("page-visits", new Fields("url","userId"));
        // N.B.: Le regroupement se fait par couple (url,userId) afin d'avoir des statistiques correctes si le bold est exécuté
        //       de manière distribuée sur plusieurs workers en même temps (demande de l'énoncé).
            
		StormTopology topology = builder.createTopology();
		
		Config config = new Config();
       	config.setMessageTimeoutSecs(3640); // on définit un time out supérieur à window length + time out (>3 630 000ms)
		String topologyName = "analytics-topology";
		if(args.length > 0 && args[0].equals("remote")) {
			StormSubmitter.submitTopology(topologyName, config, topology);
		}
		else {
			LocalCluster cluster = new LocalCluster();
			cluster.submitTopology(topologyName, config, topology);
		}
	}
}
