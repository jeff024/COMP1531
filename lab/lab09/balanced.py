from permutations import permutations

def is_balanced(string):
    flag = 0
    for cha in string:
        if cha == '(':
            flag += 1
        elif cha == ')':
            flag -= 1
        if flag < 0:
            return False
    return True
def balanced(n):
    '''
    Given a positive number n, yield all strings of length n, in any order, that only contain balanced brackets. For example:
    >>> sorted(list(balanced(6)))
    ['((()))', '(()())', '(())()', '()(())', '()()()']
    '''
    if n % 2 != 0 or n < 0:
        raise ValueError('the input number should be a positive double integer to be balanced')
    string = ''
    for _ in range(n // 2):
        string += '('
    for _ in range(n // 2):
        string += ')'
    string = list(permutations(string))
    string = list(dict.fromkeys(string))    # remove duplicated string
    for bracket in string:
        if is_balanced(bracket):
            yield bracket
    
if __name__ == '__main__':
    print(sorted(list(balanced(1))))