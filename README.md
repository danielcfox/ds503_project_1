# ds503_project_1
DS503 Project 1: Map-Reduce

## Contribution: Minh-Hang Redetsky:
  ```
  1) Wrote code in src/python_data_generation (`main.py`, `my_faker.py`)
  Generates large datasets for project input linked by IDs
  Used ChatGPT to generate lists of labels in my_faker.py:
    Prompts such as "generate a list of 50 different hobbies, each is a string from 20 to 50 characters"
    Visual inspection of the generated labels confirmed accuracy
  Documented assumptions in the writeup and provide screenshots of a few lines of each file
  2) Loaded the large datasets to HDFS and provided screenshots in the writeup
  3) Wrote and tested code for TaskA (`TaskA.java`) and created a writeup for the taskA.
  4) Wrote code for the basic implementation (`TaskB.java`) and the optimized implementation (`TaskB_opt.java`). Created a writeup for `TaskB.java` and `TaskB_opt.java`
      Used ChatGPT to provide some sample code on different types of joins. E.g. "what are the different types of joins, provide an example with code in Java".
      Used ChatGPT to help interpret some error messages, e.g. "Why does this error happens Caused by: java.util.concurrent.ExecutionException: java.io.IOException: Resource file:/home/minhhang/Documents/ds503_project_1/src/MapReduceTasks/input/FaceInPages.csv is not publicly accessable and as such cannot be part of the public cache.
  	at java.util.concurrent.FutureTask.report(FutureTask.java:122)
  	at java.util.concurrent.FutureTask.get(FutureTask.java:192)
  	at org.apache.hadoop.mapred.LocalDistributedCacheManager.setup(LocalDistributedCacheManager.java:145)"
  5) Wrote code for the basic implementation (`TaskH.java`) and the optimized implementation (`TaskH_comb.java`). Created a writeup for `TaskH.java` and TaskH_comb.java
  	Similar to TaskB, used ChatGPT to help with interpreting some error messages. Also after having completed a functional implementation of Task H, asked ChatGPT if we could use a combiner to further optimize TaskH, why or why not.
  6) Helped Rahul debug the implementation of TaskE.java
```
## Contribution: Daniel Fox

    Came up with preliminary implementation design/plans for each task.
    Final plans will be decided together as a team.
