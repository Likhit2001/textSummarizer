from src.text_Summarizer.constants import *
from src.text_Summarizer.utils.common import read_yaml, create_directories

from src.text_Summarizer.entity import DataIngestionConfig

class ConfigurationManager:

    def __init__(self,config_path = CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_filepath)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir = Path(config.root_dir),
            source_url = config.source_url,
            local_data_file = Path(config.local_data_file),
            unzip_dir = Path(config.unzip_dir)
        )

        return data_ingestion_config    
