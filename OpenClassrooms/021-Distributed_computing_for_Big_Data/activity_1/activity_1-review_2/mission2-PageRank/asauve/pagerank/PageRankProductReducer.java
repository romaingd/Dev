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

public class PageRankProductReducer extends Reducer<IntWritable, Text, IntWritable, Text> {
    
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
     * Production des produits partiels avec en sortie
     * <column index> \t <product>
     */
    @Override
    public void reduce(final IntWritable key, final Iterable<Text> values,
            final Context context) throws IOException, InterruptedException {
        double  sum = 0.0;
        List<String> row = new ArrayList<String>();
        double       x   = Double.NaN;
        
        
        /* read input that can be of type vector(x) or matrix(P)  */
        for (Text textValue: values) {
            String typedValue = textValue.toString();
            char   vType      = typedValue.charAt(0);
            typedValue = typedValue.substring(1, typedValue.length());
            
            switch(vType) {
              case 'P':
                // aggregation de la chaine contenant "<column index>:P[*,k]"
                row.add(typedValue);
                // abandon de la matrice P qui sera reconstruite au prochain stage1.Mapper
                break;
              case 'x':
                // mise a jour de la valeur de x qui est unique pour chaque cle
                x = Double.parseDouble(typedValue);
                break;
              default:
                throw new IOException("Invalid text value for key="+key+" value="+textValue);
            }        
        }

        /* verifie que le vecteur x  est rempli correctement: 
         * un NaN va lever une exception ur ce test */
        if (x != x) {
            throw new IOException("x was not initialized at iter="+iter+" key="+key);
        } 

        /* multiplication de P[*,k] par x[k] */
        for (String typedValue: row) {
            /* la chaine en entree est de la forme:
             *   <column index>:<double>
             */

            String parts[] = typedValue.split(":");
            double partialProduct = Double.parseDouble(parts[1]) * x;

            /* la cle deviens <column index> pour la sommation au stage 2 */
            key.set(Integer.parseInt(parts[0]));
            outValue.set(""+partialProduct);
            context.write(key, outValue);
        }
    }
}

