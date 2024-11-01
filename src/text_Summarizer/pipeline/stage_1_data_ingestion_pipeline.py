
# from src.text_Summarizer.entity import DataIngestionConfig

from src.text_Summarizer.config.configuration import ConfigurationManager

from src.text_Summarizer.components.data_ingestion import DataIngestion

from src.text_Summarizer.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()

        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.zip_extract()