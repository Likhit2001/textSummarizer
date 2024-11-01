import os
from box.exceptions import BoxValueError
import yaml
from src.text_Summarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
# from typing import Any , List


## To read the yaml file

@ensure_annotations
def read_yaml(path_yaml : Path) -> ConfigBox:
    try :
        with open(path_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


## to create a directories

@ensure_annotations
def create_directories(path_to_dirs : list , verbose: bool = True):
    for path in path_to_dirs:
        path = Path(path)
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Create directory as {path}")