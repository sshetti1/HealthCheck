# UDEL Health Checker

This program fills out UDEL's daily health check for you automatically.

## Use
To use this program, you need to be a University of Delaware student or employee. It will also only fill out the form 
as if you do not have COVID-19 or do not have symptoms. If you do have COVID-19 or have symptoms of COVID-19, **DO NOT 
USE THIS PROGRAM**.

To use the program, all you need to do is run the python file [HealthCheck.py](HealthCheck.py), and it will 
automatically fill out the form for you.


## Using AWS Lambda
This program can also be used with AWS Lambda. The workflow file creates a zip and pushes 
the zip into a preconfigured AWS Lambda machine. This can be configured for anybody else if they create a Lambda 
themselves. To make it functional the following steps need to be followed:
 - Create an AWS Lambda
 - Create an IAM User that has the permissions to update a Lambda
   - Take note of the AWS Access Key and AWS Secret Access Key
 - Set up the following GitHub repository secrets with those keys:
   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
 - Change the function name in workflow file to the name of the Lambda that you created

After those steps have been followed, it is up to you on how you use the Lambda.