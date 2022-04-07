import pytest 
import os

def test_fix_param01(setup06a):
    assert type(setup06a) in [tuple, list]

def test_fix_param02(setup06a, setup06b):
    if setup06b == 'access':
        assert setup06a[0] 
    elif setup06b == 'slice':
        assert setup06a[::-1] 
    elif setup06b == 'assign':
        setup06a[0] = 99
        assert True 
    elif setup06b == 'len':
        assert len(setup06a)
        
        



