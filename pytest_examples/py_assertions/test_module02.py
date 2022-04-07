import pytest 

def func():
    raise ValueError("Error from func")

def test_case01():
    with pytest.raises(ZeroDivisionError):
        assert (1/0)

def test_case02():
    with pytest.raises(Exception) as e:
        func()
    print(e)
    assert str(e.value) == "Error from func"