import logging
import time
import random


logger = logging.getLogger("test-logger")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler() 
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

levels = [logging.INFO, logging.WARNING, logging.ERROR, logging.DEBUG]

while True:
    level = random.choice(levels)
    if level == logging.INFO:
        logger.info("This is an info message.")
    elif level == logging.WARNING:
        logger.warning("Warning! Something might be wrong.")
    elif level == logging.ERROR:
        logger.error("Error occurred!")
    elif level == logging.DEBUG:
        logger.debug("Debugging details here.")
    time.sleep(5)
