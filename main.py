import os
from modules.log_initialise import setup_logging
from modules.extract_api import extract_json
from modules.load_data import load_files_to_s3
from datetime import datetime
from dotenv import load_dotenv

#Define variables
url = 'https://api.tfl.gov.uk/BikePoint/'
maxAttempts = 15
delay = 10 #seconds
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
saveDir = 'data'
log_dir = 'log'

#Load environment variables
load_dotenv()
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

#Initialise logger
logger = setup_logging(timestamp, log_dir, debug = False)
logger.info('Logger successfully initialised.')

#Extract data
extract_json(url, timestamp, saveDir, maxAttempts, delay)

#Load to s3
load_files_to_s3(saveDir, AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, AWS_BUCKET_NAME)