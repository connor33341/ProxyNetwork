# https://connor33341.dev
import logging
import uuid
from lib.proxyManager import ProxyManager
from lib.configManager import ConfigManager

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    print("[INFO]: Starting Logger")
    LogUUID = str(uuid.uuid4())
    LogFile = f"src/logs/{LogUUID}.log"
    logging.basicConfig(filename=LogFile,level=logging.INFO)
    logger.info(f"Starting Program: {LogUUID}")
    print(f"[INFO]: Created log file: {LogFile}")
    print("[INFO]: Resolving Config")
    logger.info(f"Resolving Config")
    Config = ConfigManager("src/config/default.cbcf")
    Config.LoadConfig()