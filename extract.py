#Import packages
import requests
import os
import json
from datetime import datetime
import logging
import time

#Define variables
url = 'https://api.tfl.gov.uk/BikePoint/'
maxAttempts = 15
delay = 10 #seconds

#Create a save and log directories and filenames
saveDir = 'data'
os.makedirs(saveDir, exist_ok = True)

logDir = 'log'
os.makedirs(logDir, exist_ok = True)

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{saveDir}/bikepoint_data_{timestamp}.json'
logFilename = f'{logDir}/{timestamp}.json'

#Configure logs
logging.basicConfig(
    filename = logFilename,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

#Create the logger and confirm that it's been successfully set up
logger = logging.getLogger()
logger.info('Logger successfully initialised.')

#Set up retry settings in case the API fails


#Send API get request
for i in range(maxAttempts):
    response = requests.get(url)
    statusCode = response.status_code

    #Status code handling
    if 200 <= statusCode < 300:
        data = response.json() # save the json response to a variable
        if len(data) > 0:
            try:
                with open(filename, 'w') as file:
                    json.dump(data, file) #open the output file and write the API data to it as JSON
                print(f'Yayyyy it worked good job! {filename} has been saved to the data folder.')
                logger.info(f'File {filename} was successfully saved.')
            except Exception as e:
                print(f'A write error has occurred: {e}')
                logger.error(f'A write error has occurred: {e}')
        else:
            print(f'Response is empty.')
            logger.info(f'Response is empty.')
        break
    elif statusCode < 200 or statusCode >= 500:
        print(f'Attempt {i+1}: {statusCode}.\nRetrying in {delay} seconds.')
        time.sleep(delay) # pause the code for x seconds before continuing
        logger.info(f'Attempt {i+1}: {statusCode}.\nRetrying in {delay} seconds.')
    else:
        f'Fatal error: {statusCode}'
        logger.critical(f'Fatal error: {statusCode}')
        break