import pandas as pd, os, sys
from src.DiamondPricePrediction.components.dataIngestion import DataIngestion
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException

obj = DataIngestion()
obj.initiateDataIngestion()
