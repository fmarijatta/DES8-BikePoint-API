import os
import boto3
from dotenv import load_dotenv


#Load environment variables
load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

#Create s3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
)

#Define filenames (test)
dataDir = 'data/'
filesToUpload = os.listdir(dataDir)

for filename in filesToUpload:
    localFilepath = f'{dataDir}{filename}'
    uploadFilename = filename
    try:
        # Upload file
        s3_client.upload_file(localFilepath, AWS_BUCKET_NAME, uploadFilename)
        print(f'{filename} uploaded successfully.')
        os.remove(localFilepath)
    except Exception as e:
        print(f'An error has occured: {e}')