import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'your-bucket-name'
    key_prefix = 'your-folder-prefix'  # Optional: If you want to copy files from a specific folder within the bucket
    
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=key_prefix)
    
    for file in response['Contents']:
        file_key = file['Key']
        file_name = file_key.split('/')[-1]  # Extract the file name from the key
        
        # Copy file from S3 bucket to /tmp/ directory in Lambda
        s3.download_file(bucket_name, file_key, f'/tmp/{file_name}')

import boto3
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'your-bucket-name'
    key_prefix = 'your-folder-prefix'  # Optional: If you want to copy files from a specific folder within the bucket
    
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=key_prefix)
    
    for file in response['Contents']:
        file_key = file['Key']
        file_name = file_key.split('/')[-1]  # Extract the file name from the key
        
        # Download file from S3 bucket to /tmp/filename in Lambda
        with open('/tmp/' + file_name, 'wb') as f:
            s3.download_fileobj(bucket_name, file_key, f)
