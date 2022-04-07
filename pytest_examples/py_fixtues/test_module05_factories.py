from calendar import month, weekday
import pytest 
import os

def test_fact_factories(setup05):
    assert (setup05("list")) == [1,2,3]
    assert (setup05("tuple")) == (1,2,3)
