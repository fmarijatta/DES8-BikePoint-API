import os
import boto3
from dotenv import load_dotenv


#Load environment variables
load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

s3_client = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
)

localFilename = f'data/bikepoint_data_2026-09-28 10-26-07.json'
uploadFilename = 'bikepoint_data_2026-09-28 10-26-07.json'

s3_client.upload_file(localFilename, AWS_BUCKET_NAME, uploadFilename)