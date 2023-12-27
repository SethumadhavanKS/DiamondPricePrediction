import logging, os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logPath = os.path.join(os.getcwd(),"logs")
os.makedirs(logPath,exist_ok=True)
LOG_FILE_PATH = os.path.join(logPath,LOG_FILE)
logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILE_PATH,
                    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s"
                    )
