import os
import logging
from  datetime import datetime

#Configure logs

def setup_logging(timestamp:str, logDir:str, debug = False):
    """This will initialise the logger.
    
    Args:
        logDir (str): where you want your logs saved
        timestamp (str): the timestamp will be the log filename
    """
    os.makedirs(logDir, exist_ok = True)

    logFilename = f'{logDir}/{timestamp}.log'
    if debug == True:
        logging.basicConfig(
            filename = logFilename,
            format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level = logging.DEBUG
        )
    elif debug == False:
        logging.basicConfig(
            filename = logFilename,
            format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level = logging.INFO
        )
    else:
        print('Debug kwarg must be boolean.')
    print(logFilename)
    #Create the logger and confirm that it's been successfully set up
    return logging.getLogger()