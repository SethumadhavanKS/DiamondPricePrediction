import pandas as pd, os, sys
from dataclasses import dataclass 
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet

from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException
from src.DiamondPricePrediction.utils.utils import save_obj, evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
     
     def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
     
     def initiateModelTrainer(self,train_arr,test_arr):
        try:
            x_train, y_train, x_test, y_test = (
                train_arr[:, :-1],
                train_arr[:, -1],
                test_arr[:, :-1],
                test_arr[:, -1],
               )

            models = {
               "LinearRegression":LinearRegression(),
               "Lasso":Lasso(),
               "Ridge": Ridge(),
               "ElasticNet":ElasticNet()
             }
            
            model_report:dict = evaluate_model(x_train, y_train, x_test, y_test, models)
            print(model_report)
            print("\n", "--"*20, "\n")
            logging.info(f"Model report : {model_report}")

            # Finding best model

            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            print(f"Best model is {best_model_name}, r2 score is {best_model_score}")
            print("\n", "--"*20, "\n")
            logging.info(f"Best model is {best_model_name}, r2 score is {best_model_score}")

            save_obj(filepath=self.model_trainer_config.trained_model_file_path, obj=best_model)

        except Exception as e:
            logging.info("Splitting dpendant and independant features from train and test data")
            raise CustomException(e, sys)
     
