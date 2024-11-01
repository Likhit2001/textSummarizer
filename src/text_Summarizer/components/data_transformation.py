import os
from transformers import AutoTokenizer
import zipfile
from src.text_Summarizer.logging import logger
from datasets import load_from_disk

from src.text_Summarizer.entity import DataTransformationConfig

class DataTransformation:
    def __init__ (self,config:DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_dataset_to_features_usageable(self,data):

        input_encoding = self.tokenizer(data['dialogue'] , max_length = 1024 , truncation = True)

        with self.tokenizer.as_target_tokenizer():
            target_encoding = self.tokenizer(data['summary'] , max_length = 1024 , truncation = True)
        
        return {
            'input_ids' : input_encoding['input_ids'],
            'attention_mask' : input_encoding['attention_mask'],
            'labels' : target_encoding['input_ids']
        }
    def convert(self):
        
        dataset_samsum = load_from_disk(self.config.data_path)

        dataset_samsum_pt = dataset_samsum.map(self.convert_dataset_to_features_usageable,batched = True)

        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))







