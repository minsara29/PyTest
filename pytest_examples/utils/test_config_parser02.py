from pytest_examples.utils.config_parser02 import *

config = ConfigParser("prod.ini")

def test_get_gmailurl():
    print(config.get_gmailUrl())

def test_get_outlookurl():
    print(config.get_gmailUrl())