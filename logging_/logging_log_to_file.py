# Example of how to configure a logger to log to a file
import logging

logging.basicConfig(level=logging.INFO, filename='responses.log')
logger = logging.getLogger('webber')

logger.debug("Request received...")
logger.info("Send a response now")
logger.warn("The response is not validated")
