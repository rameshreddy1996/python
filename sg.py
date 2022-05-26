import boto3
region = "ap-southeast-1"
ec2 = boto3.resource('ec2')
security_groups = ec2.security_groups.all()

for security_group in security_groups:
    print(security_group)