import logging
import os
from datetime import datetime

# Create a datetime object
now = datetime.now()
log_file = f"{now.strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)
log_filepath = os.path.join(log_path, log_file)

import logging

# Configure the logger
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

# Create a logger instance
jogging = logging.getLogger(__name__)
