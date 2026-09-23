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
interval = datetime.minute # Needs work

#Create a folder for our reponse to live
saveDir = 'data'
os.makedirs(saveDir, exist_ok = True)

#Create filename
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{saveDir}/bikepoint_data_{timestamp}.json'

#Send get request
for i in range(maxAttempts):
    response = requests.get(url)
    statusCode = response.status_code
    if response.status_code == 200:
        print(f'API call successful.')
        break
    elif response.status_code < 200:
        print('No data retrieved. The call will be attempted again in 15 seconds.')
        time.sleep(interval)
    else:
        f'Fatal error: {statusCode}'
        break

#Convert the JSON response into a python variable
data = response.json()

#Open the output file and write the API data to it as JSON
with open(filename, 'w') as file:
    json.dump(data, file)