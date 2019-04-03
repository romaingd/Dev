# S3 is a balanced data storage solution, with several advantages:
#   * Low cost (opposed to EC2/EFS)
#   * Persistent (opposed to EC2, since computer clusters may be ephemere)
#   * Low data transfer time with computer servers (opposed to Glacier)
#
# The main disadvantage is that it does not support random reading of a file,
# i.e. reading a file from the middle on. 


# S3 is an object storage solution, each object being associated with:
#   * Data
#   * Metadata (permissions/path/version)
#   * Identifier

# Objects are stored in buckets that can be created using `mb` (make bucket)
# Buckets need to have a unique (in the world) name, because each is accessible
# using an URL defined by its name.
aws s3 mb s3://oc_calculsdistribues
# Confirm the creation of the bucket
aws s3 ls

# Create a file and send it to s3
echo 'hi openclassrooms!' > hello.txt
aws s3 cp hello.txt s3://oc_calculsdistribues
aws s3 ls s3://oc_calculsdistribues
# Fetch it
rm hello.txt
aws s3 cp s3://oc_calculsdistribues/hello.txt hello2.txt
cat hello2.txt
# Remove it
aws s3 rm s3://oc_calculsdistribues/hello.txt

# Declare a file as public, and fetch it using curl on its real URL
aws s3 cp --acl public-read hello.txt s3://oc_calculsdistribues/hello.txt
curl https://s3-eu-west-1.amazonaws.com/oc_calculsdistribues/hello.txt

# Remove a bucket by emptying it, then using `rb` (remove bucket)
aws s3 ls s3://oc_calculsdistribues
aws s3 rm s3://oc_calculsdistribues/hello.txt
aws s3 rb s3://oc_calculsdistribues