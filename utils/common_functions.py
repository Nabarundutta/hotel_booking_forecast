import os 
import yaml
import pandas as pd
import numpy as np
from src.logger import getLogger
from src.custom_exception import CustomException

logger = getLogger(__name__)

def read_yaml(filepath:str):
    try:
        if not os.path.exists(filepath):
            raise CustomException(f"File not found: {filepath}")

        with open(filepath,"r") as f:
            config =  yaml.safe_load(f)
            logger.info("siccessfully read the yaml file ")
            return config
    except Exception as e:
        logger.error("Error reading while reading yaml file")
        raise CustomException("failed to read yaml file",e)

def load_data(path):
    try:
        logger.info("Loading data")
        return pd.read_csv(path)
    except Exception as e:
        logger.error(f"Error loading the data {e}")
        raise CustomException("Failed to load data" , e)
