import os
import boto3
import logging
from datetime import datetime

def load_files_to_s3(data_dir:str, aws_access_key:str, aws_secret_access_key:str, aws_bucket_name:str):
    """_summary_

    Args:
        data_dir (str): Filepath to where the data to be uploaded are stored locally.
        aws_access_key (str): Linked to IAM user.
        aws_secret_access_key (str): Linked to IAM user.
        aws_bucket_name (str): Name of bucket in AWS to upload files
    """

    #Create the logger and confirm that it's been successfully set up
    logger = logging.getLogger(__name__)

    #Create s3 client
    s3_client = boto3.client(
        's3',
        aws_access_key_id = aws_access_key,
        aws_secret_access_key = aws_secret_access_key
    )

    #Define filenames
    filesToUpload = os.listdir(data_dir)

    #Loop through and upload to s3
    for filename in filesToUpload:
        localFilepath = f'{data_dir}/{filename}'
        uploadFilename = filename
        try:
            # Upload file
            s3_client.upload_file(localFilepath, aws_bucket_name, uploadFilename)
            print(f'{filename} uploaded successfully.')
            logging.info(f'{filename} uploaded successfully.')
            os.remove(localFilepath)
        except Exception as e:
            print(f'An error has occured: {e}')
            logging.error(f'{filename} failed to upload. Error: {e}')