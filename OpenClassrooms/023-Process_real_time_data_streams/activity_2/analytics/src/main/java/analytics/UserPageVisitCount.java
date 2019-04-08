package analytics;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseWindowedBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;
import org.apache.storm.windowing.TupleWindow;


public class UserPageVisitCount extends BaseRichBolt {
	private OutputCollector outputCollector;

	@Override
	public void prepare(Map stormConf, TopologyContext context, OutputCollector collector) {
		outputCollector = collector;
	}

	@Override
	public void execute(TupleWindow inputWindow) {
		HashMap<Integer, HashMap<String, Integer>> userPageVisitCounts = new HashMap<Integer, HashMap<String, Integer>>();
    
        // Collect stats for all tuples, city by city, station by station
		Integer tupleCount = 0;
		for(Tuple input : inputWindow.get()) {
            Integer userId = input.getIntegerByField("userId");
			String url = input.getStringByField("city");
			
			userPageVisitCounts.putIfAbsent(userId, new HashMap<String, Integer>());
			userPageVisitCounts.get(userId).putIfAbsent(url, 0);
			Integer currentCount = userPageVisitCounts.get(userId).get(url);
            userPageVisitCounts.get(userId).put(url, currentCount + 1);
			
			outputCollector.ack(input);
			tupleCount += 1;
		}
		// System.out.printf("====== UserPageVisitCounts: Received %d tuples\n", tupleCount);

		// Emit visit counts, user by user, url by url
		String now = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date());
		for(Entry<Integer, HashMap<String, Integer>> userStats: userPageVisitCounts.entrySet()) {
            Integer userId = userStats.getKey();
            for(Entry<String, Integer> urlStats: userStats.getValue().entrySet()) {
                String url = urlStats.getKey();
                Integer visitsCount = urlStats.getValue();
                System.out.printf("%s User %d visited page %s a total number of %d times during the last hour", now, userId, url, visitsCount);
            }
		}
	}

	@Override
	public void declareOutputFields(OutputFieldsDeclarer declarer) {
	}
}
