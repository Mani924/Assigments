import boto3
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'your-bucket-name'
    folder_prefix = 'your-folder-prefix/'  # Include the trailing slash (/) to specify a folder
    destination_directory = '/tmp/downloaded_files/'  # Specify the desired destination directory
    
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_prefix)
    
    for file in response['Contents']:
        file_key = file['Key']
        file_name = os.path.basename(file_key)  # Extract the file name from the key
        
        # Download file from S3 folder to destination directory in Lambda
        destination_path = os.path.join(destination_directory, file_name)
        s3.download_file(bucket_name, file_key, destination_path)
