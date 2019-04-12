package analytics;

import java.util.HashMap;
import java.util.Map;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseWindowedBolt;
import org.apache.storm.tuple.Tuple;

import org.apache.storm.windowing.TupleWindow;

public class UserPageVisitCount extends BaseWindowedBolt {

	private OutputCollector outputCollector;

    
	@Override
	public void prepare(Map stormConf, TopologyContext context, OutputCollector collector) {
		outputCollector = collector;
	}

	@Override
	public void execute(TupleWindow inputWindow) {

    // Les données statistiques (hashMap userPageVisitCounts) sont renouvelées à chaque appel de execute 
    // ( Consigne de l'énoncé: "Ce bolt ne devra pas conserver de données en mémoire entre deux appels à sa méthode execute(), 
    //   par exemple sous la forme d'attributs." )
    
		HashMap<Integer,HashMap<String,Integer>> userPageVisitCounts = new HashMap<Integer,HashMap<String,Integer>>();
        
        Integer tupleCount = 0;
		for(Tuple input : inputWindow.get()) {
            
            Integer userId = input.getIntegerByField("userId");
            String url = input.getStringByField("url");
			
            userPageVisitCounts.putIfAbsent(userId, new HashMap<String,Integer>());
			userPageVisitCounts.get(userId).putIfAbsent(url,0);			
            userPageVisitCounts.get(userId).put(url, userPageVisitCounts.get(userId).get(url)+1);
            
			outputCollector.ack(input);
			tupleCount += 1;
		}
		System.out.printf("====== UserPageVisitCount: %d tuples reçus\n", tupleCount);

        // Affichage des statistiques....
		String date=LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
        System.out.printf("\nStatistiques de fréquentation @ %s :\n", date);
        for (Integer userKey : userPageVisitCounts.keySet()) {
            System.out.printf("\n");
            for (String urlKey: userPageVisitCounts.get(userKey).keySet()){
                System.out.printf(" - L'utilisateur %d a visité %d fois la page %s.\n",
                    userKey, 
                    userPageVisitCounts.get(userKey).get(urlKey),
                    urlKey
                );
            }
        }
        System.out.printf("\n");
    }

	@Override
	public void declareOutputFields(OutputFieldsDeclarer declarer) {
	}

}
