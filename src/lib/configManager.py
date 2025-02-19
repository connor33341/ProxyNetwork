import logging
import os
import uuid

logger = logging.getLogger(__name__)
class ConfigManager():
    def __init__(self,ConfigFile: str):
        self.ID = str(uuid.uuid4())
        self.LineSeperator = ";"
        self.KVSeperator = "="
        self.RemoveSpaces = True
        self.ConfigFile = ConfigFile
        logger.info(f"Loading File: {self.ID}")

    def LoadConfig(self):
        logger.info(f"ConfigReading: {self.ID}")
        if self.FileExists():
            logger.info(f"ConfigFile Located: {self.ID}")
            try:
                with open(self.ConfigFile,"r") as File:
                    self.FileContents = File.read()
                    File.close()
                self.FileLines = str(self.FileContents).split(self.LineSeperator)
                i=-1
                for Line in self.FileLines:
                    i+=1
                    KV = Line.split(self.KVSeperator)
                    if (i) < len(self.FileLines) - 1:
                        #print(KV)
                        Key = KV[0]
                        Value = KV[1]
                        logger.info(f"Reading Line: {i} K: {Key} V: {Value}")
                    
            except Exception as Error:
                logger.warn(f"ConfigFile IOError: {Error}")
        else:
            logger.warn(f"ConfigFile Missing: {self.ID}")
    def FileExists(self) -> bool:
        return os.path.isfile(self.ConfigFile)