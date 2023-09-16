import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class FaceInPageFilter {

    public static class TokenizerMapper
            extends Mapper<Object, Text, Text, Text>{

//        private final static IntWritable one = new IntWritable(1);
//        private Text word = new Text();
        private Text name = new Text();
        private Text hobby = new Text();

        public void map(Object key, Text value, Context context
        ) throws IOException, InterruptedException {
            String[] fields = value.toString().split(",");
            if (fields.length == 5 && fields[2].equals("Ireland")){
                name.set(fields[1]); // set name
                hobby.set(fields[4]); // set hobby
                context.write(name, hobby);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        // for debugging
        for (String arg : args) {
            System.out.println("Argument: " + arg);
        }

        // No reducer is needed since this is just a simple filtering job

        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "face in page filter");
        job.setJarByClass(FaceInPageFilter.class);
        job.setMapperClass(TokenizerMapper.class);

        // set the number of reduce tasks to zero:
        job.setNumReduceTasks(0);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);
        /*
         * This sets the input directory for the MapReduce job. The method expects a Job and Path as args. The path is created from args[0]
         * */
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}