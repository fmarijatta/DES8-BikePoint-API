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
    logDir = 'log'
    os.makedirs(logDir, exist_ok = True)

    # timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

    logFilename = f'{logDir}/{timestamp}.log'
    if debug == True:
        logging.basicConfig(
            filename = logFilename,
            format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level = logging.INFO
    elif:
        logging.basicConfig(
            filename = logFilename,
            format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level = logging.INFO
    else:
        print('Debug kwarg must be boolean.')
    )

    #Create the logger and confirm that it's been successfully set up
    return logging.get_logger()