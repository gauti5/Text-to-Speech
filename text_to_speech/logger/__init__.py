import logging
import os, sys

from datetime import datetime

LOG_DIR="pylogs"
LOG_DIR_PATH=os.path.join(os.getcwd(), LOG_DIR)  # Adding the log fir path to our working directory..

# Create a log directory..

os.makedirs(LOG_DIR, exist_ok=True)

# Create a log file name

Current_time_stamp=f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"

file_name=f"log_{Current_time_stamp}"
log_file_path=os.path.join(LOG_DIR, file_name)

# Configure logging

logging.basicConfig(filename=log_file_path, level=logging.INFO, format="%(asctime)s %(levelname)s %(module)s ==========> %(message)s",
                    datefmt="%d-%m-%Y %H:%M")

# Create a object for logging

logger=logging.getLogger()

