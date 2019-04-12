package analytics;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.base.BaseWindowedBolt;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;
import org.apache.storm.windowing.TupleWindow;

public class UserPageVisitCount extends BaseWindowedBolt {
	private OutputCollector outputCollector;
	

	@Override
	public void prepare(Map stormConf, TopologyContext context, OutputCollector collector) {
		outputCollector = collector;
	}
	
	@Override
	public void execute(TupleWindow inputWindow) {
		// TODO Auto-generated method stub
		HashMap<Integer, HashMap<String, ArrayList<Long>>> userPageVisits = new HashMap<Integer, HashMap<String, ArrayList<Long>>>();
		Integer tupleCount = 0;
		for(Tuple input : inputWindow.get()) {
			Integer userId = input.getIntegerByField("userId");
			String url = input.getStringByField("url");
			long visitPageDateTime = input.getLongByField("visitPageDateTime");
			
			userPageVisits.putIfAbsent(userId, new HashMap<String, ArrayList<Long>>());
			userPageVisits.get(userId).putIfAbsent(url, new ArrayList<Long>());
			userPageVisits.get(userId).get(url).add(visitPageDateTime);
			
			outputCollector.ack(input);
			tupleCount += 1;
		}
		
		System.out.printf("====== UserPageVisitCount: Received %d tuples\n", tupleCount);
		
		// Emit average stats, city by city
		for(Entry<Integer, HashMap<String, ArrayList<Long>>> userPageVisitCounter: userPageVisits.entrySet()) {
			Integer userId = userPageVisitCounter.getKey();
			for(Entry<String, ArrayList<Long>> pageVisits: userPageVisitCounter.getValue().entrySet()) {
				String url = pageVisits.getKey();
				ArrayList<Long> timeVisits = new ArrayList<Long>();
				for(Long time: pageVisits.getValue()) {
					timeVisits.add(time);
				}
				
				pageVisits.setValue(timeVisits);
				System.out.printf("L'utilisateur %d a visité la page %s %d fois sur la dernière heure. \n", userId, url, timeVisits.size());
			}			
		}
	}

}
