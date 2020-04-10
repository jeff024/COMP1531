from factors import factors, is_prime
from hypothesis import given, strategies
import inspect

def test_generator():
    '''
    Ensure it is generator function.
    '''
    assert inspect.isgeneratorfunction(factors), "factors does not appear to be a generator"

def test_36():
    assert list(factors(36)) == [2, 2, 3, 3]

def test_4():
    assert list(factors(4)) == [2, 2]

def test_5():
    assert list(factors(5)) == [5]

def test_13():
    assert list(factors(13)) == [13]

def test_26():
    assert list(factors(26)) == [2, 13]


