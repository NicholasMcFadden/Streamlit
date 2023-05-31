# https://m-germanengineer.medium.com/tutorial-launch-saleable-streamlit-dashboards-aws-part-1-f7f5372e66e


import streamlit as st
import os

from botocore.exceptions import ClientError
import boto3
import requests

# S3 credentials
S3_KEY= os.environ.get("S3_KEY")
S3_SECRET=os.environ.get("S3_SECRET")
region_bucket=os.environ.get("REGION_BUCKET")




def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object
    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """
    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3',aws_access_key_id = S3_KEY, aws_secret_access_key = S3_SECRET,region_name = region_bucket)
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None
    # The response contains the presigned URL
    return response





def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=S3_KEY,
                      aws_secret_access_key=S3_SECRET)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False

