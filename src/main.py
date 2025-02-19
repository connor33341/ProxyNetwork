# https://connor33341.dev
import logging
import uuid
from lib.proxyManager import ProxyManager
from lib.configManager import ConfigManager

logger = logging.getLogger(__name__)
VERSION = 1.0

def info(input_string):
    logger.info(input_string)
    input_string = "[INFO]: "+input_string
    print(input_string)

if __name__ == "__main__":
    info(f"Version: {VERSION}")
    print("[INFO]: Starting Logger")
    LogUUID = str(uuid.uuid4())
    LogFile = f"src/logs/{LogUUID}.log"
    logging.basicConfig(filename=LogFile,level=logging.INFO)
    info(f"Starting Program: {LogUUID}")
    print(f"[INFO]: Created log file: {LogFile}")
    info(f"Resolving Config")
    ConfigLoader = ConfigManager("src/config/default.cbcf")
    ConfigData = ConfigLoader.LoadConfig()
    #print(ConfigData)
    if ConfigData != {}:
        info("Config Loaded")
        ServerType = ConfigData["server"]
        ListConfigName = ConfigData["config"]
        info(f"Server Type: {ServerType}")
        info(f"Server ConfigFile: {ListConfigName}")
        info(f"Resolving ListConfig: {ListConfigName}")
        ListLoader = ConfigManager(f"src/config/{ListConfigName}")
        ListData = ListLoader.LoadConfig()
        if ListData != {}:
            info("Loadded ListConfig")
            ListUrl = ListData[ServerType]
            info(f"Loading List: {ListUrl}")
        else:
            print("[ERROR]: Failed to load ListConfig, please make sure 'config' in default.cbcf is set to a valid list")
            logger.error("ListData is empty, check previous logs for more information")

    else:
        logger.warn("Config NotFound")
        print("[WARN]: Failed to locate config")