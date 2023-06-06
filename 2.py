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
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def lambda_handler(event, context):
    # SMTP server configuration
    smtp_host = 'your-smtp-host'
    smtp_port = 587
    smtp_username = 'your-smtp-username'
    smtp_password = 'your-smtp-password'
    
    sender_email = 'sender@example.com'
    recipient_email = 'recipient@example.com'
    subject = 'Multiple HTML Files Email'
    
    # Retrieve the list of HTML files
    html_files = sorted([filename for filename in os.listdir('/path/to/html_files/') if filename.endswith('.html')])
    
    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    
    # Iterate through the HTML files and attach them to the email
    for file in html_files:
        file_path = '/path/to/html_files/' + file
        
        with open(file_path, 'r') as f:
            html_content = f.read()
        
        part = MIMEText(html_content, 'html')
        part.add_header('Content-Disposition', 'attachment', filename=file)
        message.attach(part)
    
    # Send the email
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
