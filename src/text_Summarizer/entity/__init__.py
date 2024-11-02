from dataclasses import dataclass
from pathlib import Path

# @dataclass automatically creates an __init__ method, so you don’t have to manually define it. This method will take each of the fields (like root_dir, source_url, etc.) as an argument, making it easier to initialize the class with configuration values.


class DataIngestionConfig:
    def __init__(self, root_dir, source_url, local_data_file, unzip_dir):
        self.root_dir = root_dir
        self.source_url = source_url
        self.local_data_file = local_data_file
        self.unzip_dir = unzip_dir

class DataTransformationConfig:
    def __init__(self, root_dir, data_path,tokenizer_name):
        self.root_dir = root_dir
        self.data_path = data_path
        self.tokenizer_name = tokenizer_name

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int