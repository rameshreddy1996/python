import boto3
session=boto3.Session(region_name='ap-southeast-1')
ec2_re=session.resource(service_name="ec2")

for each_instance in ec2_re.instances.all():
     print(each_instance.service_name)