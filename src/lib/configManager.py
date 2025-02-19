import logging
import os
import uuid
import re

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
        self.ConfigData = {}
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
                        if self.RemoveSpaces:
                            Key = self.FormatString(Key)
                            Value = self.FormatString(Value)
                        logger.info(f"Reading Line: {i} K: {Key} V: {Value}")
                        self.ConfigData[Key] = Value
                    
            except Exception as Error:
                logger.warn(f"LoadConfig Error: {Error}")
        else:
            logger.warn(f"ConfigFile Missing: {self.ID}")
        return self.ConfigData
    def FileExists(self) -> bool:
        return os.path.isfile(self.ConfigFile)
    def FormatString(self,UnformattedString) -> str:
        FormattedString = re.sub(r'[^a-zA-Z.:/]|\n|\r','',UnformattedString)
        return FormattedString