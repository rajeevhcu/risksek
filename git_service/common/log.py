"""
python file for logging for every one day
 """
import logging
import logging.handlers as handlers
import os
from . import constants


def folder_exists(logfile):
    """checks directory exists or not.
    if directory is not existed create a directory."""
    try:
        if not os.path.exists(os.path.dirname(logfile)):
            os.makedirs(os.path.dirname(logfile))
    except Exception as err:
        print("Error in giles_log : folder_exists" + str(err))


logger = logging.getLogger(constants.NODE_NAME)
logger.setLevel(logging.INFO)

# Here we define our formatter
FORMATTER = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


folder_exists('log/' + constants.NODE_NAME + '/' + constants.NODE_NAME + '.log')
LOG_HANDLER = handlers.TimedRotatingFileHandler(
   'log/' + constants.NODE_NAME + '/' + constants.NODE_NAME + '.log',
    when='midnight',
    backupCount=10
)
LOG_HANDLER.setLevel(logging.INFO)
# Here we set our logHandler's formatter
LOG_HANDLER.setFormatter(FORMATTER)

logger.addHandler(LOG_HANDLER)


def info(msg):
    """to log the information message."""
    logger.info(str(msg))


def error(msg):
    """to log the error message."""
    logger.error(str(msg))
