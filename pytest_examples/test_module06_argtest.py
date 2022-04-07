import pytest 

def test_argtest01(CmdOpt):
    # print("read config file:"+ CmdOpt.readline())
    assert CmdOpt.readline().index("property")