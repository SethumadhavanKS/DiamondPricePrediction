import pandas as pd, os, sys
from src.DiamondPricePrediction.components.dataIngestion import DataIngestion
from src.DiamondPricePrediction.components.dataTransformation import DataTransformation
from src.DiamondPricePrediction.components.modelTrainer import ModelTrainer

from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException

class TrainingPipeline:

    def initiate_training_pipeline(self):

        logging.info("Initiating training pipeline")
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiateDataIngestion()

        data_transformation = DataTransformation()
        train_arr, test_arr = data_transformation.initiateDataTransformation(train_data_path=train_data_path, test_data_path=test_data_path)

        model_trainer = ModelTrainer()
        model_trainer.initiateModelTrainer(train_arr,test_arr)
