

import configparser
from pathlib import Path

cfgfile = "qa.ini"
cfgFileDir = "config"

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDir).joinpath(cfgfile)

config = configparser.ConfigParser()

config.read(CONFIG_FILE)

def get_gmailUrl():
    return config["gmail"]["url"]

def get_gmailuser():
    return config["gmail"]["user"]

def get_gmailpass():
    return config["gmail"]["pass"]


# print(get_gmailUrl())


