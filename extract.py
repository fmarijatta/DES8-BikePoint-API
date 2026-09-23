#Import packages
import requests
import os
import json
from datetime import datetime
import logging

#Define variables
url = 'https://api.tfl.gov.uk/BikePoint/'
maxAttempts = 15

#Create a folder for our reponse to live
saveDir = 'data'
os.makedirs(saveDir, exist_ok = True)

#Create a timestamp
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{saveDir}/bikepoint_data_{timestamp}.json'

#Send get request
for i in maxAttempts:
    response = requests.get(url)
    if response.status_code >

#Convert the JSON response into a python variable
data = response.json()

#Open the output file and write the API data to it as JSON
with open(filename, 'w') as file:
    json.dump(data, file)