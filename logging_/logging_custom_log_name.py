# Shows how you can create a custom logger with a name
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('bunyan')
logger.debug('custom debug')