package asauve.pagerank;

import java.io.IOException;
import java.util.Iterator;
import java.util.List;
import java.util.ArrayList;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.conf.Configuration;

public class PageRankSumReducer extends Reducer<IntWritable, Text, IntWritable, Text> {
    
    private Text outValue = new Text();
    private int    iter   = 0;
    private int    paramN = -1;
    private double paramS = Double.NaN;
    
    
    @Override
    public void setup(final Reducer.Context context) throws IOException, InterruptedException {
        Configuration conf = context.getConfiguration();
        iter   = Integer.parseInt(conf.get("iter"));
        paramS = Double.parseDouble(conf.get("PARAM_S"));
        paramN = Integer.parseInt(conf.get("PARAM_N"));
        System.out.println("PageRankReducer.setup(): PARAM_S="+paramS+" PARAM_N="+paramN);
    }
    
    
    /* 
     * Stage 2 : Reduce
     * Sommation des produits partiels et output sous la forme
     *  <column index> \t "x"<value>
     */
    @Override
    public void reduce(final IntWritable key, final Iterable<Text> values,
            final Context context) throws IOException, InterruptedException {
        double       sum    = 0.0;
        
        /* l'input est un produit partiel */
        for (Text textValue: values) {
            sum  += Double.parseDouble(textValue.toString());
        }
        
        /* Nouvelle valeur du vecteur x
         *     x_i+1[k] = sum (x_i[k] * P[*,k]) 
         */
        outValue.set("x"+sum);
        if (key.get() == 218) System.out.println("KEYOUT="+key.get()+" value="+sum);
        context.write(key, outValue);
    }
}

