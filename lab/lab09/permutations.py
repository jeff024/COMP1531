
def permutations(string):
    '''
    For the given string, yield all permutations of the characters of that string in any order. For example:
    >>> sorted(list(permutations('ABC')))
    ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']

    If a character occurs more than once in the input string, each occurrence is still considered distinct. For example:
    >>> sorted(list(permutations('ABB')))
    ['ABB', 'ABB', 'BAB', 'BAB', 'BBA', 'BBA']
    '''
    pool = tuple(string)
    n = len(pool)
    r = n
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield to_string(list(pool[i] for i in indices[:r]))
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield to_string(list(pool[i] for i in indices[:r]))
                break
        else:
            return

def to_string(cha):
    perm = ''
    for c in range(len(cha)):
        perm += cha[c]
    return perm


if __name__ == '__main__':
    print(list(permutations('A')))