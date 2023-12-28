from src.DiamondPricePrediction.pipeline.trainingPipeline import TrainingPipeline
# from src.DiamondPricePrediction.pipeline.predictionPipeline import PredictionPipeline, CustmData
from src.DiamondPricePrediction.logger import logging

logging.info("Test logger")
trainObj = TrainingPipeline()
trainObj.initiate_training_pipeline()

# predObj = PredictionPipeline()

# customData = CustmData(1,52,62.2,58,7.27,7.33,4.55,"Premium","F","VS2")

# df = customData.get_data_as_frame()
# predVal = predObj.predict(df)
