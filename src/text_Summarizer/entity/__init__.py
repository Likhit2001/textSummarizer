from dataclasses import dataclass
from pathlib import Path

# @dataclass automatically creates an __init__ method, so you don’t have to manually define it. This method will take each of the fields (like root_dir, source_url, etc.) as an argument, making it easier to initialize the class with configuration values.


class DataIngestionConfig:
    def __init__(self, root_dir, source_url, local_data_file, unzip_dir):
        self.root_dir = root_dir
        self.source_url = source_url
        self.local_data_file = local_data_file
        self.unzip_dir = unzip_dir