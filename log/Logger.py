import logging
import time
import os
from functools import wraps


# From https://www.geeksforgeeks.org/create-an-exception-logging-decorator-in-python/

def create_logger():
    path = "/logs"
    try:
     os.makedirs(path,exist_ok=True)
     logger = logging.getLogger(__name__)
     logger.setLevel(logging.INFO)
     logfile = logging.FileHandler(f'/logs/{time.strftime("%Y-%m-%d_%H-%M")}.log')
     fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
     formatter = logging.Formatter(fmt)

     logfile.setFormatter(formatter)
     logger.addHandler(logfile)
    except TypeError:
        try:
         os.makedirs(path)
        except OSError as e:
            logger.error("Failed to create Directory")

    return logger


def exception(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        logger = create_logger()
        try:
            return function(*args, **kwargs)
        except:
            err = "Exception in "
            err += function.__name__
            logger.exception(err)
            raise

    return wrapper
