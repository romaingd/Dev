package analytics;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ThreadLocalRandom;

import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseRichBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;

public class UserVisitCountBolt extends BaseRichBolt {

	private OutputCollector outputCollector;
	private HashMap<Integer, Integer> userVisitCount;
	
	@Override
	public void execute(Tuple arg0) {
		// TODO Auto-generated method stub
		Integer userId = arg0.getIntegerByField("userId");
		userVisitCount.put(userId, userVisitCount.getOrDefault(userId, 0) + 1);
		
		if (ThreadLocalRandom.current().nextInt(10) == 0) {
			outputCollector.fail(arg0);
		}
		else{
			outputCollector.ack(arg0);
		}
		
	}

	@Override
	public void prepare(Map arg0, TopologyContext arg1, OutputCollector arg2) {
		// TODO Auto-generated method stub
		outputCollector = arg2;
		userVisitCount = new HashMap<Integer,Integer>();

	}

	@Override
	public void declareOutputFields(OutputFieldsDeclarer arg0) {
		// TODO Auto-generated method stub
		//arg0.declare(new Fields("url","userId"));
	}

}
