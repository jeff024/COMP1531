'''
NOTE: This exercise assumes you have completed divisors.py
'''

from divisors import divisors

# You may find this helpful
def is_prime(n):
    return list(divisors(n)) == [1, n]

def find_prime(n):
    if n == 1:
        return []
    prime = []
    multi = 1
    factor = list(divisors(n))
    factor.remove(1)
    for i in factor:
        if is_prime(i):
            prime.append(i)
            multi *= i
    return prime + find_prime(n // multi)

def factors(n):
    '''
    A generator that yields all the prime factors of n. The prime factors are in ascending order with factors repeated as necessary. For example:
    >>> list(factors(36))
    [2, 2, 3, 3]
    '''
    factor = find_prime(n)
    factor.sort()
    for i in factor:
        yield i
