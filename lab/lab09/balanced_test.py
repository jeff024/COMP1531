from balanced import balanced
from hypothesis import given, strategies
import inspect

def test_generator():
    '''
    Ensure it is generator function
    '''
    assert inspect.isgeneratorfunction(balanced), "balanced does not appear to be a generator"

def test_empty():
    assert sorted(list(balanced(0))) == ['']
        
def test_2():
    assert sorted(list(balanced(2))) == ['()']
    
def test_6():
    assert sorted(list(balanced(6))) == ['((()))', '(()())', '(())()', '()(())', '()()()']
    
def test_4():
    assert sorted(list(balanced(4))) == ['(())', '()()']
