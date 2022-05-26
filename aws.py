import boto3

# AWS_REGION = "ap-southeast-1"
# EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)

# security_groups = EC2_RESOURCE.security_groups.all()

# # print('Security Groups:')
# for security_group in security_groups:
#    # print(f'- Security Group {security_group.id}')
#     print(security_group)
    
    
#region = "a
# ap-southeast-1"
ec2 = boto3.resource('ec2')
security_groups = ec2.security_groups.all()

for security_group in security_groups:
    print(security_group)
    
    
    
import boto3

region = "ap-southeast-1"
ec2 = boto3.resource('ec2')

instances = ec2.instances.all()

for instance in instances:
 
    print(instance.instance_id,"=",instance.instance_type)


import boto3

region = "ap-southeast-1"
ec2 = boto3.resource('ec2')

key_pairs = ec2.key_pairs.all()
#key_pairs = ec2.describe_key_pairs()

for key_pair in key_pairs:
    print(key_pair)
    
    
import boto3

region = "ap-southeast-1"

ec2 = boto3.resource('ec2')

for volume in ec2.volumes.all():
    print(volume)