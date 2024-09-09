import logging
import os
from datetime import datetime
import numpy as np

log_file=f"{datetime.strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path=os.path.join(os.getcwd(),"logs")
os.makedirs(log_path,exist_ok=True)
log_filepath=os.path.join(log_path,log_file)

logging(
    level=logging.INFO,
    filename=log_filepath,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s"
)