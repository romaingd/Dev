    package asauve.pagerank;
    
    import org.apache.hadoop.conf.Configuration;
    import org.apache.hadoop.conf.Configured;
    import org.apache.hadoop.fs.FileSystem;
    import org.apache.hadoop.fs.Path;
    import org.apache.hadoop.io.IntWritable;
    import org.apache.hadoop.io.DoubleWritable;
    import org.apache.hadoop.io.Text;
    import org.apache.hadoop.mapreduce.Job;
    import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
    import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
    import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
    import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
    import org.apache.hadoop.util.GenericOptionsParser;
    import org.apache.hadoop.util.Tool;
    import org.apache.hadoop.util.ToolRunner;
    
    public class PageRankDriver extends Configured implements Tool {
        @Override
        public int run(String[] args) throws Exception {
            if (args.length != 5) {
                System.out.println("Usage: <adjMatrix> <prankFmt> <N> <S> <niter>");
                System.out.println("  <adjMatrix> is the _movies adjacency matrix HDFS input");
                System.out.println("  <prankFmt> is the printf-like format for HDFS Page rank vector");
                System.out.println("  <N>=nb of links  <S>=retention param  <niter>=nb of iterations");
                System.exit(-1);
            }
    
            
            // Command line
            String adjMatrix = args[0];
            String prankFmt  = args[1];
            String PARAM_N   = args[2];
            String PARAM_S   = args[3];
            int niter = Integer.parseInt(args[4]);
            
            // set parameters
            Configuration conf = getConf();
            conf.set("PARAM_N", PARAM_N);
            conf.set("PARAM_S", PARAM_S);

            FileSystem fs = FileSystem.newInstance(conf);

            int jobStatus = 1;
            for (int iter=0; iter < niter; iter++) {
                conf.set("iter", ""+iter);
                
                System.out.println("##############################################");
                System.out.println("############  ITER "+(iter+1)+" STAGE 1  ########");
                System.out.println("##############################################");
                
                {
                    // Creation d'un job en lui fournissant la configuration et une description textuelle de la tache
                    Job job = Job.getInstance(conf);
                    job.setJobName("PageRankGIM-V-Stage1-Product");
            
                    // On precise les classes MyProgram, Map et Reduce
                    job.setJarByClass(PageRankDriver.class);
                    job.setMapperClass(PageRankProductMapper.class);
                    job.setReducerClass(PageRankProductReducer.class);
            
                    // Definition des types clé/valeur de notre problème
                    job.setOutputKeyClass(IntWritable.class);
                    job.setOutputValueClass(Text.class);
            
                    // Gestion des entrees du stage 1
                    job.setInputFormatClass(TextInputFormat.class);
                    FileInputFormat.setInputDirRecursive(job, true); // Accepte entree recursive
                    Path adjMatrixInputPath = new Path(adjMatrix);
                    Path vectorInputPath    = new Path(String.format(prankFmt,  iter));
                    FileInputFormat.addInputPath(job, adjMatrixInputPath);
                    if (iter > 0) {
                        FileInputFormat.addInputPath(job, vectorInputPath);
                    }
                    
                    // Gestion de la sortie du stage 1
                    job.setOutputFormatClass(TextOutputFormat.class);
                    Path outputFilePath = new Path(String.format(prankFmt+"-stage1", iter));
                    FileOutputFormat.setOutputPath(job, outputFilePath);
                    
                    if (fs.exists(outputFilePath)) {
                        fs.delete(outputFilePath, true);
                    }
                    
                    jobStatus = job.waitForCompletion(true) ? 0: 1;
                    if (jobStatus != 0) {
                        return jobStatus;
                    }

                    if (iter > 0) {
                        //fs.delete(vectorInputPath, true);
                    }
                }
            
                {
                    System.out.println("##############################################");
                    System.out.println("############  ITER "+(iter+1)+" STAGE 2  ########");
                    System.out.println("##############################################");
            
            
                    // Creation d'un job en lui fournissant la configuration et une description textuelle de la tache
                    Job job = Job.getInstance(conf);
                    job.setJobName("PageRankGIM-V-Stage2-Sum");

                    // On precise les classes MyProgram, Map et Reduce
                    job.setJarByClass(PageRankDriver.class);
                    job.setMapperClass(PageRankSumMapper.class);
                    job.setReducerClass(PageRankSumReducer.class);
            
                    // Definition des types clé/valeur de notre problème
                    job.setOutputKeyClass(IntWritable.class);
                    job.setOutputValueClass(Text.class);
            
                    job.setInputFormatClass(TextInputFormat.class);
                    job.setOutputFormatClass(TextOutputFormat.class);
            
                    Path inputFilePath = new Path(String.format(prankFmt+"-stage1",  iter));
                    Path outputFilePath = new Path(String.format(prankFmt, iter+1));
            
                    // On accepte une entree recursive
                    FileInputFormat.setInputDirRecursive(job, true);
            
                    FileInputFormat.addInputPath(job, inputFilePath);
                    FileOutputFormat.setOutputPath(job, outputFilePath);

                    if (fs.exists(outputFilePath)) {
                        fs.delete(outputFilePath, true);
                    }
                    
                    jobStatus = job.waitForCompletion(true) ? 0: 1;
                    if (jobStatus != 0) {
                        return jobStatus;
                    }

                    // delete stage-1 interemediate data
                    //fs.delete(inputFilePath, true);
                }
            
            
        }
        
        return 0;
    }

    public static void main(String[] args) throws Exception {
        PageRankDriver driver = new PageRankDriver();
        int res = ToolRunner.run(driver, args);
        System.exit(res);
    }
}

