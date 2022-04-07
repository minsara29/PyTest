import pytest 
import sys

def test_strjoin():
    s1 = "Python,pytest and automation" 
    l1 = ["Python,pytest", "and", "automation"]
    l2 = ["Python", "pytest and automation"]
    assert " ".join(l1) == s1

@pytest.mark.xfail
def test_str01():
    letters = "abcdefghijklmnopqrstuvwxyz"
    assert letters[10] 

@pytest.mark.xfail(reason="known error")
def test_str02():
    letters = "abcd"
    num = 1234
    assert letters + num == "abcd1234"


@pytest.mark.xfail(sys.platform == 'win32', reason="fail in win32")
def test_str03():
    letters = "abcdefghijklmnopqrstuvwxyz"
    assert letters[100] 

@pytest.mark.xfail(raises=IndexError, reason="Index error is fine")
def test_str04():
    letters = "abcdefghijklmnopqrstuvwxyz"
    assert letters[100] 