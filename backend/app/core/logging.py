import logging
import sys
from pythonjsonlogger import jsonlogger

def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logHandler = logging.StreamHandler(sys.stdout)
    formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(name)s %(message)s')
    logHandler.setFormatter(formatter)
    logger.handlers = [logHandler]
