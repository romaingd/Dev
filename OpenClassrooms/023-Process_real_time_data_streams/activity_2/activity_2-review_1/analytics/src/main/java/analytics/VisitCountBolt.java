package analytics;

import java.util.Map;

import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseRichBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;

public class VisitCountBolt extends BaseRichBolt {
	private OutputCollector outputCollector;
	private int totalVisitCount;
	
	@Override
	public void execute(Tuple arg0) {
		// TODO Auto-generated method stub
		String url = arg0.getStringByField("url");
		Integer userId = arg0.getIntegerByField("userId");
		totalVisitCount += 1;
		
		outputCollector.emit(arg0, new Values(url,userId));
		
		System.out.printf("Received visit %d from user %d to page %s \n",totalVisitCount, userId, url);
		
		outputCollector.ack(arg0);

	}

	@Override
	public void prepare(Map arg0, TopologyContext arg1, OutputCollector arg2) {
		// TODO Auto-generated method stub
		outputCollector = arg2;
		totalVisitCount = 0;

	}

	@Override
	public void declareOutputFields(OutputFieldsDeclarer arg0) {
		// TODO Auto-generated method stub
		arg0.declare(new Fields("url","userId"));

	}

}
