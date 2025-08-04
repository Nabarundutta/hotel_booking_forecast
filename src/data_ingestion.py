# /Users/nabarundutta/Downloads/decisive-circle-462313-s7-cc7f2e062172.json
import os 
import pandas as pd 
import numpy 
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.logger import getLogger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml

logger = getLogger(__name__)

class DataIngestion:
    def __init__(self,config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.bucket_file_name = self.config["bucket_file_name"]
        self.train_test_ratio = self.config["train_ratio"]

        os.makedirs(RAW_DIR,exist_ok=True)
        logger.info(f"Data Ingestion started with {self.bucket_name} and file is {self.bucket_file_name}")
    
    def download_csv_from_gcp(self):
        try:
            credentials_path = "/Users/nabarundutta/Downloads/decisive-circle-462313-s7-cc7f2e062172.json"
            client = storage.Client.from_service_account_json(credentials_path)
            bucket = client.bucket(self.bucket_name)
            blob = bucket.blob(self.bucket_file_name)

            blob.download_to_filename(RAW_FILE_PATH)

            logger.info(f"Raw file downloaded to {RAW_FILE_PATH}")

        except Exception as e:
            logger.error(f"Error downloading file from GCP")
            raise CustomException("failed to download file from GCP",e)

    def split_data(self):
        try:
            logger.info("Starting the splitting process")
            data = pd.read_csv(RAW_FILE_PATH)
            train_data, test_data = train_test_split(data,test_size=1-self.train_test_ratio,random_state=42)
            train_data.to_csv(TRAIN_FILE_PATH)
            test_data.to_csv(TEST_FILE_PATH)
            logger.info(f"Train data saved to {TRAIN_FILE_PATH}")
            logger.info(f"Test data saved to {TEST_FILE_PATH}")
        
        except Exception as e:
            logger.error(f"Error while splitting data")
            raise CustomException("failed to split data",e)

    
    def run(self):
        try:
            logger.info("Starting data ingestion process")
            self.download_csv_from_gcp()
            self.split_data()
            logger.info("Data ingestion completed successfully")
        
        except Exception as e:
            logger.error(f"Error while running data ingestion process")
            raise CustomException("failed to run data ingestion process",e)

        finally :
            logger.info("Data ingestion process finished")


if __name__ == "__main__":
    data_ingestion = DataIngestion(read_yaml(CONFIG_FILE_PATH))
    data_ingestion.run()