# This example shows how you can change the default priority level
# Note the default priority level is: WARNING
import logging

# Set the prioorty level to DEBUG. Looks like this must be the first thing to be invoked before effect takes place.
logging.basicConfig(level=logging.DEBUG)

logging.debug("This is a DEBUG log")
logging.info("This is a INFO log")
logging.warning("This is a WARNING log")
logging.error("This is a ERROR log")
logging.critical("This is a CRITICAL log")
