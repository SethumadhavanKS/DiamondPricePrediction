import sys, pandas as pd, numpy as numpy, os
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

class DataIngestion:
     
     def __init__(self):
        self.ingestion_config = DataIngestionConfig()

     def initiateDataIngestion(self):
        logging.info("Data ingestion started")
        try:
            data = pd.read_csv(os.path.join("notebooks/data","gemstone.csv"))
            logging.info("Read dataset as DF")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw data saved in artifacts")
            logging.info("Perfrming Train test split")
            trainData, TestData = train_test_split(data, test_size=0.3, random_state=42)
            logging.info("Train test split completed")
            data.to_csv(self.ingestion_config.train_data_path, index=False)
            logging.info("Train data saved in artifacts")
            data.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Test data saved in artifacts")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path
        
        except Exception as e:
            raise CustomException(e, sys)

@dataclass        
class DataIngestionConfig:

    raw_data_path:str = os.path.join("artifacts", "raw.csv")
    train_data_path:str = os.path.join("artifacts", "train.csv")
    test_data_path:str = os.path.join("artifacts", "test.csv")
