import os
import boto3
from dotenv import load_dotenv
import logging
from datetime import datetime

#Load environment variables
load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

#Configure logs
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
logDir = 'log'
os.makedirs(logDir, exist_ok = True)
logFilename = f'{logDir}/load_{timestamp}.log'

logging.basicConfig(
    filename = logFilename,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

#Create the logger and confirm that it's been successfully set up
logger = logging.getLogger()
logger.info('Logger successfully initialised.')

#Create s3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
)

#Define filenames
dataDir = 'data/'
filesToUpload = os.listdir(dataDir)

#Loop through and upload to s3
for filename in filesToUpload:
    localFilepath = f'{dataDir}{filename}'
    uploadFilename = filename
    try:
        # Upload file
        s3_client.upload_file(localFilepath, AWS_BUCKET_NAME, uploadFilename)
        print(f'{filename} uploaded successfully.')
        logging.info(f'{filename} uploaded successfully.')
        os.remove(localFilepath)
    except Exception as e:
        print(f'An error has occured: {e}')
        logging.error(f'{filename} failed to upload. Error: {e}')