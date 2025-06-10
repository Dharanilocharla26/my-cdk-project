from aws_cdk import (
    Stack,
    aws_s3 as s3,
)
from constructs import Construct

class MyCdkProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        s3.Bucket(self, "myBucketId", bucket_name="mycdkprojectbucket0136",
                  versioned=True,
                  encryption=s3.BucketEncryption.S3_MANAGED)
