from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    aws_ecs_patterns as ecs_patterns,
    aws_ecs as ecs,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_ecr as ecr
    # aws_sqs as sqs,
)
from constructs import Construct

class DemoAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
         
        bucket =s3.Bucket(self, "Demo-api")
      
