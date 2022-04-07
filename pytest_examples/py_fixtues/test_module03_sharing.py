from calendar import weekday
import pytest 
import os

weekday1 = ['mon', 'tue', 'wed']
weekday2 = ['fri', 'sat', 'sun']
filename = "test.txt"

def test_full_name(fn_name, ln_name):
    assert fn_name + ln_name == "DahliaKannan"
    

def test_weekdays(weekdays):
    assert "mon" in weekdays
    
