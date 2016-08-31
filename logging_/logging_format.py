# Example of how to confiure the logger format
import logging

fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level='DEBUG', format=fmt)

logger = logging.getLogger('formatted')
logger.error('error log formattedc')
