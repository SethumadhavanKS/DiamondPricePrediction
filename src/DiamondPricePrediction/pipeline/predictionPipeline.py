import pandas as pd, os, sys

from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException
from src.DiamondPricePrediction.utils.utils import load_object

class PredictionPipeline():

    def predict(self, features):
        try:
            logging.info("Prediction pipeline")
            preprocessor_path = os.path.join("artifacts","preprocessor.pkl")
            model_path = os.path.join("artifacts","model.pkl")

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            scaled_data = preprocessor.transform(features)
            pred = model.predict(scaled_data)
            return pred
        
        except Exception as e:
            logging.info("Exception occured at prediction pipeline")
            raise CustomException(e, sys)
     


class CustmData:

    def __init__(self,
                carat:float,
                depth:float,
                table:float,
                x:float,
                y:float,
                z:float,
                cut:str,
                color:str,
                clarity:str):
        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data_as_frame(self):

        try:
            custom_data_imput_dict = {
                    "carat":[self.carat],
                    "depth":[self.depth],
                    "table":[self.table],
                    "x":[self.x],
                    "y":[self.y],
                    "z":[self.z],
                    "cut":[self.cut],
                    "color":[self.color],
                    "clarity":[self.clarity]
                }
            df= pd.DataFrame(custom_data_imput_dict)
            logging.info("Datafram created from custom data")
        except Exception as e:
            logging.info("Exception occured at creating DF from custom data")
            raise CustomException(e, sys)
     

    