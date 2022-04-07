import pytest 
pytestmark = [pytest.mark.smoke, pytest.mark.strtest]
             #pytest -vm  strtest -> run from this modules 
             #pytest -vm  smoke -> run from this modules 

@pytest.mark.sanity
def test_str01():
    num = 9/4
    s1 = "I like " + "pytest"
    assert str(num) == "2.25"
    assert s1 == "I like pytest"
    assert s1 + str(num) == "I like pytest2.25"

@pytest.mark.sanity #you can group of test for sanity, integration or smoke test 
def test_str02():
    letters = "abcdefghijklmnopqrstuvwxyz"
    assert len(letters) == 26


def test_str03():
    letters = "abcdefghijklmnopqrstuvwxyz"
    assert letters[0] == "a"
    assert letters[25] == "z"

@pytest.mark.sanity # can be part of more than one group 
@pytest.mark.str #if want to skip then pytest -m "sanity and not str" ;
                 # only run this group pytest -m "sanity and str" 
def test_strslice():
    letters = "abcdefghijklmnopqrstuvwxyz"
    assert letters[:] == letters
    assert letters[10:] == "klmnopqrstuvwxyz"
    assert letters[-3:] == "xyz"
    assert letters[:25:5] == "afkpu"

@pytest.mark.str
def test_strsplit():
    s = "Python,pytest and automation" 
    assert s.split() == ["Python,pytest", "and", "automation"]
    assert s.split(",") == ["Python", "pytest and automation"]
    

def test_strjoin():
    s1 = "Python,pytest and automation" 
    l1 = ["Python,pytest", "and", "automation"]
    l2 = ["Python", "pytest and automation"]
    assert True