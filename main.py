# from src.text_Summarizer.logging import logger

# from src.text_Summarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline



# STAGE_NAME = "Data Ingestion Stage"

# try:
#     logger.info(f"{STAGE_NAME} initiated")
#     data_ingestion = DataIngestionTrainingPipeline()
#     data_ingestion.initiate_data_ingestion()
#     logger.info(f"{STAGE_NAME} completed")
# except Exception as e:
#     logger.exception(e)
#     raise e


from src.text_Summarizer.components.data_transformation import DataTransformation
from src.text_Summarizer.config.configuration import ConfigurationManager_tranformation
from src.text_Summarizer.logging import logger
from src.text_Summarizer.pipeline.stage_2_data_Transformation_pipeline import Data_Tranformation

STATE_NAME = "The Data Transformation Stage"

try:
    logger.info(f"{STATE_NAME} is intialted")
    data_transformed = Data_Tranformation()
    data_transformed.initiate_data_transformation()
    logger.info(f"{STATE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e    

