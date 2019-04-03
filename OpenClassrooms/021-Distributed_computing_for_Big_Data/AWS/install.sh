# Install AWS Command Line Interface
pip3 install awscli
# Check that awscli is correctly installed
which aws
# Configure awscli and grant it your AWS access key (see website)
# Use JSON as default output format
aws configure

# Check that the following command shows no error
aws s3 ls
