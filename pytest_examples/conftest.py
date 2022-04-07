from email.policy import default
import pytest 

prod_config = 'prod.prop'
QA_config = 'qa.prop'

def pytest_addoption(parser):
    parser.addoption("--cmdopt", default='QA')


@pytest.fixture()
def CmdOpt(pytestconfig):
    print("In CmdOpt fixure function")
    opt = pytestconfig.getoption("cmdopt")
    if opt == "Prod":
        f = open(prod_config, "r")
    else: 
        f = open(QA_config, "r")
    yield f