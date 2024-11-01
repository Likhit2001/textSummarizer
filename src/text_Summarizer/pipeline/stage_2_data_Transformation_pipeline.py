from src.text_Summarizer.components.data_transformation import DataTransformation
from src.text_Summarizer.config.configuration import ConfigurationManager_tranformation
# from src.text_Summarizer.logging import logger

class Data_Tranformation:
    def __init__(self):
        pass
    def initiate_data_transformation(self):
        config = ConfigurationManager_tranformation()
        data_transformation_config = config.get_data_transformation_config()

        data_tranformation = DataTransformation(data_transformation_config)
        data_tranformation.convert()



