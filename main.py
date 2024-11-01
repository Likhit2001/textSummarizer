from src.text_Summarizer.logging import logger

from src.text_Summarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline



STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"{STAGE_NAME} initiated")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e
