from calendar import weekday
import pytest 
import os

weekday1 = ['mon', 'tue', 'wed']
weekday2 = ['fri', 'sat', 'sun']
filename = "test.txt"

@pytest.fixture()
def setup01():
    print("\n in fixtures.... \n")
    weekday1.append("thur")
    yield weekday1
    print("\nafter yield in setup01 fixture\n")
    weekday1.pop()
    print(weekday1)

@pytest.fixture()
def setup02():
    print("\n in fixtures2.... \n")
    weekday2.insert(0, "thur")
    yield weekday2
    print("\nafter yield in setup02 fixture\n")
    weekday2.pop()
    print(weekday2.pop())


@pytest.fixture()
def setup03():
    f = open(filename, "w")
    f.write("pytest is good")
    f.close

@pytest.fixture()
def setup04():
    f =  open(filename, "r")
    yield f 
    f.close
    # os.remove(filename)

def test_extendList(setup01):
    setup01.extend(weekday2)
    assert setup01 == ['mon', 'tue', 'wed', "thur", 'fri', 'sat', 'sun']


def test_listLength(setup02):
    print(setup02)
    assert len(setup02) == 4


def test_fileContent(setup03, setup04):
    assert setup04.read() == "pytest is good"
