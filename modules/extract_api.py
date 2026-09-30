#Import packages
import requests
import os
import json
from datetime import datetime
import logging
import time

def extract_json(url, timestamp, saveDir, maxAttempts, delay):
    """_summary_

    Args:
        saveDir (str): Where to save the data
        timestamp (str): When the data were extracted
        url (str): The url you want to call data from
        maxAttempts (int): The number of times the API call can be retried
        delay (int): Time in seconds to wait before retrying
    """

    logger = logging.getLogger(__name__)
    
    os.makedirs(saveDir, exist_ok = True)
    filename = f'{saveDir}/bikepoint_data_{timestamp}.json'


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