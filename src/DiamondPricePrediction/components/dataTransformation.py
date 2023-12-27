import pandas as pd, os, sys
from dataclasses import dataclass 
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException
from src.DiamondPricePrediction.utils.utils import save_object

class DataTransformation:
     
     def __init__(self):
        self.dataTransformation_config = DataTransformationConfig()

     def get_data_transformation(self):
        # Creating numerical and categorical pipelines
        try:


            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer()), #For handle missing values
                    ("scalar", StandardScaler()) # Standardisation
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                        ('imputer',SimpleImputer(strategy="most_frequent")),
                        ("encoder",OrdinalEncoder(categories=[cut_cat,color_cat, clarity_cat])) # For encoding categorical values
                    ]
                )
            
            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline', num_pipeline, num_features),
                    ('cat_pipeline', cat_pipeline, cat_features)
                ]
            )

            return preprocessor
        
        except Exception as e:
            # logging.info("Exception occured in preprocessing get_data_transformation")
            raise CustomException(e, sys)

     def initiateDataTransformation(self,train_data_path, test_data_path):
        try:
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)
            preprocessing_obj = self.get_data_transformation()
            target_col = "price"
            drop_cols = [target_col, "id"]

            input_feature_train_df = train_df.drop(columns=drop_cols, axis=1)
            input_feature_test_df = test_df.drop(columns=drop_cols, axis=1)

            target_feature_train_df = train_df[target_col]
            target_feature_test_df = test_df[target_col]

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)
            # logging.info("Train and test data preprocessed")
            save_object(file_path = self.dataTransformation_config.preprocessor_obj_file_path, obj=preprocessing_obj)
            # logging.info("Preprocessing pickle file saved")
            
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

        except Exception as e:
            # logging.info("Exception occured in preprocessing initiate_transformation")
            raise CustomException(e, sys)

     
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")