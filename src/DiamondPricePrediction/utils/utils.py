import os, sys, pickle, numpy as np, pandas as pd
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException

from sklearn.metrics import r2_score

def save_obj(filepath, obj):
    try:
        dir_path = os.path.dirname(filepath)
        os.makedirs(dir_path, exist_ok=True)
        with open(filepath,"wb") as fileObj:
            pickle.dump(obj, fileObj)
            logging.info("Object saved")

    except Exception as e:
            logging.info("Exception occured in utils save object")
            raise CustomException(e, sys)
    
def evaluate_model(x_train, y_train, x_test, y_test, models):
     try:
          report = dict()
          for i in range(len(models)):
               model = list(models.values())[i]
            #    Train model
               model.fit(x_train, y_train)

            #    Predict test data
               y_test_pred = model.predict(x_test)

               test_model_score = r2_score(y_test, y_test_pred)

               report[list(models.keys())[i]]= test_model_score

          return report

     except Exception as e:
            logging.info("Exception occured in utils model evaluation")
            raise CustomException(e, sys)
     
def load_object(file_path):
     try:
          with open(file_path, "rb") as file_obj:
               return pickle.load(file_obj)
     except Exception as e:
            logging.info("Exception occured in utils load object")
            raise CustomException(e, sys)
