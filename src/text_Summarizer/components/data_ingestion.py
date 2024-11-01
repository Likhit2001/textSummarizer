import os
import urllib.request as request
import zipfile
from src.text_Summarizer.logging import logger
from urllib.request import urlretrieve

from src.text_Summarizer.entity import DataIngestionConfig

class DataIngestion:

    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_file(self):

        local_data_dir = os.path.dirname(self.config.local_data_file)
        os.makedirs(local_data_dir, exist_ok=True)

        if not os.path.exists(self.config.local_data_file):

            filename , headers = urlretrieve(
                url=str(self.config.source_url),
                filename=str(self.config.local_data_file)
            )
            logger.info(f"The file has downloaded into {filename}")
        else :
            logger.info(f"File has already been downloaded")

    def zip_extract(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
