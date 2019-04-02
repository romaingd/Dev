package asauve.pagerank;

import java.io.IOException;
import java.util.StringTokenizer;
import java.util.List;
import java.util.Hashtable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.conf.Configuration;
            
public class PageRankProductMapper extends Mapper<LongWritable, Text, IntWritable, Text> {

    private int         paramN = -1;
    private double      paramS = Double.NaN;
    private int         iter   = -1;
    private IntWritable key    = new IntWritable();
    private Text        value  = new Text();

    @Override
    public void setup(final Mapper.Context context) throws IOException, InterruptedException {
        Configuration conf = context.getConfiguration();
        paramN = Integer.parseInt(conf.get("PARAM_N"));
        paramS = Double.parseDouble(conf.get("PARAM_S"));
        iter   = Integer.parseInt(conf.get("iter"));
        System.out.println("PageRankProductMapper.setup(): PARAM_N="+paramN+" PARAM_S="+paramS);
    }
            
    
    /*
     * Stage 1 Map: preparation du produit x[i] * P[i,*]
     *  - <key> \t "x"[key]          // (initialise a 1/N sinon prends le vecteur precedent)
     *  - <key> \t "P"<column>:P[key, column]
     */
    @Override
    public void map(LongWritable lineNumber, Text line, Context context) throws IOException, InterruptedException 
    {
        int outLinks[] = new int[paramN];
        int nLink = 0;
        StringTokenizer   inputTok  = new StringTokenizer(line.toString());

        /* La ligne d'input proviens 
         *  - soit de la matrice d'adjacence contenue dans _movies/graph/adj_list 
         *      au format <pid>: <link1_pid> ... -1 
         *  - soit du vecteur precedent
         */
        if (inputTok.hasMoreTokens()) {
            
            /* Lit le  pid qui contient un caractere ':' */
            String pidStr = inputTok.nextToken();
            if (pidStr.endsWith(":")) {
                /* L'input proviens de la matrice d'adjacence: initialise key=pid */
                key.set(Integer.parseInt(pidStr.substring(0,pidStr.length()-1)));
    
                /* agregation des liens */
                while (inputTok.hasMoreTokens()) { 
                    String nextTok = inputTok.nextToken();
                     if (nextTok.equals("-1")) {
                         break;
                     } else {
                         outLinks[Integer.parseInt(nextTok)] = 1;
                         nLink += 1;
                     }
                }
          
                if (iter == 0) {
                    /* creation d'une valeur initiale du vecteur x de la forme:
                     *   <key> \t "x"1/N
                     */
                    value.set("x" + (1.0/(double)paramN));
                    context.write(key, value);
                }
                
                /* output des paires cles/valeur pour une ligne de P de la forme:
                 *   <key> \t "P"<column index>:P[key, column index]
                 *   
                 *   avec P[i,j] = (1-s) T[i,j] + s/N
                 *  
                 * Si il n'y a pas de liens sortant on ajoute une ligne de 1/n a T
                 * Ceci est une addition a la formule du cours pour introduire la propriete stochastique manquante
                 * En pratique on a P[i,*] = (1-s)T[i,*] + s/N = (1-s)/N + s/N = 1/N
                 * 
                 * Cette partie rends le traitement très lourd en remplissant la matrice qui est sparse au depart.
                 * On peut l'optimiser en ajoutant un mapping supplementaire. Mais cela alourdirait egalement
                 * le code de l'exercice.
                 */
                for (int i=0; i < paramN; i++) {
                    double d_i = 0;
                    if (nLink == 0) {
                        d_i = ((double)1.0) / paramN;
                    } else {
                        d_i = (1-paramS)*outLinks[i]/(double)nLink + paramS/paramN;
                    }
                    value.set("P"+i+":"+d_i);
                    context.write(key, value);
                }
            }
            else{
                /* Ici, l'input proviens du vecteur fourni par l'iteration precedente: 
                 * => on le transfere tel quel 
                 */
                key.set(Integer.parseInt(pidStr));
                value.set(inputTok.nextToken());
                context.write(key, value);
            }
        }
    }

    public void run(Context context) throws IOException, InterruptedException {
        setup(context);
        while (context.nextKeyValue()) {
            map(context.getCurrentKey(), context.getCurrentValue(), context);
        }
        cleanup(context);
    }

}
