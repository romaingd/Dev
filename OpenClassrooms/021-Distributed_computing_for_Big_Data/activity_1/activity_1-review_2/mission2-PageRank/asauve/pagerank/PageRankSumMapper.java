package asauve.pagerank;

import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.conf.Configuration;


public class PageRankSumMapper extends Mapper<LongWritable, Text, IntWritable, Text > {

    private IntWritable outKey   = new IntWritable();
    private Text        outValue = new Text();

    private int    iter   = 0;
    private int    paramN = -1;
    private double paramS = Double.NaN;

    /*
     * Stage 2 : Mapper == Identity
     * Le mapping pour la sommation est effectué en sortie de Stage1.Reduce
     */
    @Override
    public void map(LongWritable lineNumber, Text lineRaw, Context context) throws IOException, InterruptedException {
        StringTokenizer lineTok = new StringTokenizer(lineRaw.toString(), "\t");
        int    key        = Integer.parseInt(lineTok.nextToken());
        String typedValue = lineTok.nextToken();

        /* In stage 2 the mapper is the Identity */
        outKey.set(key);
        outValue.set(typedValue);
        context.write(outKey, outValue);
    }

    
    public void run(Context context) throws IOException, InterruptedException {
        setup(context);
        while (context.nextKeyValue()) {
            map(context.getCurrentKey(), context.getCurrentValue(), context);
        }
        cleanup(context);
    }

}
