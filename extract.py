#Import packages
import requests
import os
import json
from datetime import datetime
import logging
import time

#Define variables
url = 'https://api.tfl.gov.uk/BikePoint/{ladida}'
maxAttempts = 15
delay = 10 #seconds

#Create a save directory and filenames
saveDir = 'data'
os.makedirs(saveDir, exist_ok = True)
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{saveDir}/bikepoint_data_{timestamp}.json'

#Send API get request
for i in range(maxAttempts):
    response = requests.get(url)
    statusCode = response.status_code

    #Status code handling
    if 200 <= statusCode < 300:
        data = response.json() # save the json response to a variable
        with open(filename, 'w') as file:
            json.dump(data, file) #open the output file and write the API data to it as JSON
        print(f'Yayyyy it worked good job! {filename} has been saved to the data folder.')
        break
    elif statusCode < 200 or statusCode >= 500:
        print(f'Attempt {i+1}: {statusCode}\nRetrying in {delay} seconds.')
        time.sleep(delay) # pause the code for x seconds before continuing
    else:
        f'Fatal error: {statusCode}'
        break