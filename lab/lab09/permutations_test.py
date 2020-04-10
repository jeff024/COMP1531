from permutations import permutations
from hypothesis import given, strategies, assume
import inspect

def test_generator():
    '''
    Ensure it is generator function
    '''
    assert inspect.isgeneratorfunction(permutations), "permutations does not appear to be a generator"

def test_empty_string():
    assert list(permutations('')) == ['']

def test_single():
    assert list(permutations('a')) == ['a']

def test_two():
    assert list(permutations('ab')) == ['ab', 'ba']

def test_ABC():
    assert list(permutations('ABC')) == ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']

def test_repeat():
    assert sorted(list(permutations('ABB'))) == ['ABB', 'ABB', 'BAB', 'BAB', 'BBA', 'BBA']

def test_all_same():
    assert list(permutations('AAA')) == ['AAA', 'AAA', 'AAA', 'AAA', 'AAA', 'AAA']