import pytest
import sys

pytestmark = pytest.mark.skipif(sys.platform != "win32", reason="will run only on linux")

CONST = 9/5

def cent_to_fah(cent=0):
    return (cent * 9/5) + 32 

# @pytest.mark.skipif(pytest.__version__ == '7.1.1', reason="Not the right version")
@pytest.mark.skipif(sys.version_info > (3, 6), reason="dont run if version greater than 3.6")
def test_case01():
    assert type(CONST) == float 


# @pytest.mark.skip(reason="testing skipping")
@pytest.mark.skipif(cent_to_fah() == 32, reason="default setting")
def test_case02():
    assert cent_to_fah() == 32


def test_case03():
    assert cent_to_fah(38) == 101.4





