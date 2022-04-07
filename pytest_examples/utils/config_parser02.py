

import configparser
from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent
# CONFIG_FILE = BASE_DIR.joinpath(cfgFileDir).joinpath(cfgfile)


class ConfigParser():

    cfgfile = "qa.ini" # default 
    cfgFileDir = "config"
    config = configparser.ConfigParser()

    def __init__(self, cfg=cfgfile):
        self.cfgfile = cfg 
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.CONFIG_FILE = self.BASE_DIR.joinpath(self.cfgFileDir).joinpath(self.cfgfile)
        self.config.read(self.CONFIG_FILE)

    def get_gmailUrl(self):
        return self.config["gmail"]["url"]

    def get_gmailuser(self):
        return self.config["gmail"]["user"]

    def get_gmailpass(self):
        return self.config["gmail"]["pass"]

    def get_outlookUrl(self):
        return self.config["outlook"]["url"]

if __name__ == "__main__":
    config = ConfigParser(cfg="prod.ini")
    print(config.get_gmailUrl())
    print(config.get_outlookUrl())




