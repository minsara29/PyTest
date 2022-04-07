from pytest_examples.utils.utils import get_data
import pytest 

@pytest.mark.parametrize("a,b,c,d", get_data())
def test_get_data(a,b,c,d):
    print(d)