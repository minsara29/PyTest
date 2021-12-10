import pytest
import sys

@pytest.mark.skip
def test_login():
    print("login")

@pytest.mark.skipif(sys.version_info <=(3,9), reason="python version not supported !!")
def test_process():
    print("process")



def test_logout():
    print("logout")


# only run smoke functions
# pytest test_withMarker.py -m "smoke"

# run which are matching
# pytest test_withMarker.py -m "smoke regression"


# with and conditions
# pytest test_withMarker.py -m "smoke and regression"