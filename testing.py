from src.logger import getLogger
from src.custom_exception import customException
import sys 

logger = getLogger(__name__)
logger.info("Testing")

def divide(a,b):
    try:
        result = a/b
        logger.info("dividing two numbers")
        return result
    except Exception as e:
        logger.error("Error in dividing two numbers")
        raise customException("Error in dividing two numbers",sys)

if __name__ == "__main__":
    try : 
        logger.info("Starting the program")
        divide(1,2)
        logger.info("Program completed successfully")
    except customException as ce:
        logger.error(str(ce))
