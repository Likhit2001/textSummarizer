import os 
import sys
import logging
from datetime import datetime

# log dir , name , 


LOG_DIR = "logs"
LOG_STR = "[%(asctime)s: %(levelname)s: %(module)s %(message)s]"
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

LOG_PATH = os.path.join(LOG_DIR,LOG_FILE)
os.makedirs(LOG_DIR,exist_ok= True)

logging.basicConfig(
    level=logging.INFO,
    format=LOG_STR,

    handlers=[
        logging.FileHandler(LOG_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("summarizerlogger")
