# Deploying a cluster of distributed computing
# This requires running `s3.sh` first

# Concretely, our cluster will consist of EC2 (Elastic Cloud Compute) machines
# coordinated by EMR (Elastic MapReduce), that will launch a Spark cluster.


# Configure SSH keys, both locally and online, to access the EC2 machines
# In ~/.ssh/config, add the following (uncommented) lines:
# Host *.compute.amazonaws.com
#   IdentityFile ~/.ssh/name_of_your_private_key


# Create and configure the cluster on the EMR webpage

# Store the script and the data on S3
wget http://classics.mit.edu/Homer/iliad.mb.txt
aws s3 cp wordcount_aws.py s3://oc_calculsdistribues
aws s3 cp iliad.mb.txt s3://oc_calculsdistribues

# When the cluster is ready (green and "Waiting"), add a Step to your cluster:
# a Spark application located in s3://oc_calculsdistribues/wordcount_aws.py
# with s3://oc_calculsdistribues/iliad.mb.txt as argument.

# Note that this step was launched using the following command:
spark-submit --deploy-mode cluster s3://oc_calculsdistribues/wordcount_aws.py s3://oc_calculsdistribues/iliad.mb.txt

# Check the result once the step is done
aws s3 ls s3://oc_calculsdistribues
aws s3 cp s3://oc_calculsdistribues/words.txt .
head -10 words.txt


# Managing a cluster in this way can also easily be done using command lines.
# On the webpage of your cluster, you'll find a "Export AWS CLI" button, which 
# will give you the command line for creating an identical cluster, for example:
aws emr create-cluster \
    --name 'Cluster OC' \
    --instance-groups '[{"InstanceCount":1,"InstanceGroupType":"MASTER","InstanceType":"m3.xlarge","Name":"Master Instance Group"},{"InstanceCount":2,"InstanceGroupType":"CORE","InstanceType":"m3.xlarge","Name":"Core Instance Group"}]' \
    --release-label emr-5.3.1\
    --applications Name=Ganglia Name=Spark Name=Zeppelin \
    --ec2-attributes '{"KeyName":"regis-ec2-rsa","InstanceProfile":"EMR_EC2_DefaultRole","SubnetId":"subnet-0a6a3b52","EmrManagedSlaveSecurityGroup":"sg-8817f2f1","EmrManagedMasterSecurityGroup":"sg-9517f2ec"}' \
    --service-role EMR_DefaultRole \
    --enable-debugging \
    --log-uri 's3n://aws-logs-584596531731-eu-west-1/elasticmapreduce/' \
    --configurations '[{"Classification":"spark","Properties":{"maximizeResourceAllocation":"true"},"Configurations":[]}]' \
    --scale-down-behavior TERMINATE_AT_INSTANCE_HOUR \
    --region eu-west-1

# The previous command will give you a cluster ID.
# Use this ID to add steps to your cluster
aws emr add-steps \
    --cluster-id j-CLUSTERID \
    --steps Type=Spark,Name="YOUR APP NAME",Args=[--deploy-mode,cluster,s3://oc_calculsdistribues/wordcount_aws.py,s3://oc_calculsdistribues/iliad.mb.txt]

# The previous command will in turn give you a step ID.
# Use both IDs to monitor the evolution of a step (prefix by `watch` to repeat)
aws emr describe-step --cluster-id CLUSTERID --step-ID STEPID

# Terminate your clusters when you're done
aws emr terminate-clusters --cluster-ids CLUSTERID1 CLUSTERID2 ...


# It is also possible to create ephemeral clusters, i.e. clusters that will
# auto-terminate upon completion of the steps. On the web console, this
# requires advanced options, selecting "Add steps", configuring the step and
# selecting "Auto-terminate cluster after the last step is completed". This may 
# also require disabling "Termination protection".
# The corresponding command differs in the --steps and --auto-terminate options:
aws emr create-cluster \
    --name 'Cluster OC' \
    --instance-groups '[{"InstanceCount":1,"InstanceGroupType":"MASTER","InstanceType":"m3.xlarge","Name":"Master Instance Group"},{"InstanceCount":2,"InstanceGroupType":"CORE","InstanceType":"m3.xlarge","Name":"Core Instance Group"}]' \
    --release-label emr-5.3.1\
    --applications Name=Ganglia Name=Spark Name=Zeppelin \
    --ec2-attributes '{"KeyName":"regis-ec2-rsa","InstanceProfile":"EMR_EC2_DefaultRole","SubnetId":"subnet-0a6a3b52","EmrManagedSlaveSecurityGroup":"sg-8817f2f1","EmrManagedMasterSecurityGroup":"sg-9517f2ec"}' \
    --service-role EMR_DefaultRole \
    --enable-debugging \
    --log-uri 's3n://aws-logs-584596531731-eu-west-1/elasticmapreduce/' \
    --configurations '[{"Classification":"spark","Properties":{"maximizeResourceAllocation":"true"},"Configurations":[]}]' \
    --scale-down-behavior TERMINATE_AT_INSTANCE_HOUR \
    --region eu-west-1 \
    --steps '[{"Args":["spark-submit","--deploy-mode","cluster","s3://oc-calculsdistribues/wordcount.py","s3://oc-calculsdistribues/iliad.mb.txt"],"Type":"CUSTOM_JAR","ActionOnFailure":"CONTINUE","Jar":"command-runner.jar","Properties":"","Name":"Wordcount"}]' \
    --auto-terminate


# Sometimes you need to run initialization scripts on each worker, typically
# to install necessary dependencies. This is called bootstrapping.
# First create the bootstrap script
touch bootstrap-emr.sh
echo 'pip install --user nltk' >> bootstrap-emr.sh
echo $'python -c "import nltk; nltk.download(\'stopwords\')"' >> bootstrap-emr.sh
echo 'pip install --user nltk' >> bootstrap-emr.sh
echo 'sudo ln -s /home/hadoop/nltk_data /usr/share/nltk_data' >> bootstrap-emr.sh
aws s3 cp bootstrap-emr.sh s3://oc_calculsdistribues/
# Then add it as an option when creating the cluster
aws emr create-cluster \
    ...
    --bootstrap-action Path=s3://oc_calculsdistribues/bootstrap-emr.sh


# Using AWS' API is not mandatory, since we have control over the servers.
# We can indeed directly log in to the cluster driver to submit our aplications.
# This requires connecting via SSH to the driver, and modifying some security 
# parameters that are hard to describe here. We refer the reader to tutorials.


# Don't forget that the EMR cluster uses HDFS. This means that loading local
# files in a script requires moving them to HDFS first.
# This does not concern S3-stored files.


# Logs are stored on S3, and syncing them locally makes the analysis easier
mkdir logs
aws s3 sync s3://aws-logs-LOGBUCKET logs/
find logs/ -name '*.gz' -exec gunzip -k {} \;

# However, it is often much easier and more efficient to consult the Web UIs
# of Hadoop (port 8088) and Spark (port 18080), at http://MASTERNODEURL:PORT
# However, those ports are only accessible on the local network of the cluster.
# Acessing it requires building a SSH tunnel to the master node, which is
# out of the scope of those notes.


# To monitor the performance and resource consumption of your cluster, AWS
# provides several tools, most notably:
#   * Cloudwatch, for long-term supervision (refreshed every 5 minutes)
#   * Ganglia, for real-time monitoring


# Re-dimensioning your cluster can be done manually, but more interestingly,
# can be done automatically to fit sudden needs. During the configuration of
# the cluster, select "Auto Scaling rules", and define adequate "scale out"
# (load increase) and "scale in" (load decrease) behaviors.