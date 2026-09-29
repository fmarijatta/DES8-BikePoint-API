from modules.log_initialise import setup_logging
from modules.extract_api import extract_json
from datetime import datetime

#Define variables
url = 'https://api.tfl.gov.uk/BikePoint/'
maxAttempts = 15
delay = 10 #seconds
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
saveDir = 'data'


logger = setup_logging('log', timestamp)
logger.info('Logger successfully initialised.')

extract_json(
        url = url,
        timestamp = timestamp,
        saveDir = saveDir,
        maxAttempts = maxAttempts,
        delay = delay
)