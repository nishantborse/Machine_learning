import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d-%H-%S')}.log" #creating a log file with the current date as the name
logs_path=os.path.join(os.getcwd(), "logs", LOG_FILE) #creating a path for the log file

os.makedirs(logs_path, exist_ok=True) #creating a directory for logs if it does not exist

LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE) #creating a path for the log file

logging.basicConfig(
    filename=LOG_FILE_PATH,  #specifying the file name for the log file
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s', #specifying the format of the log file
    level=logging.INFO, #specifying the level of logging
)

"""if __name__=="__main__":
    logging.info("Logging has started") #logging the information that logging has started
    print("Logging has started") #printing the information that logging has started
    """