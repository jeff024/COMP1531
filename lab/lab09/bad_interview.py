def bad_interview():
    '''
    A generator that yields all numbers from 1 onward, but with some exceptions:
    * For numbers divisible by 3 it instead yields "Fizz"
    * For numbers divisible by 5 it instead yields "Buzz"
    * For numbers divisible by both 3 and 5 it instead yields "FizzBuzz"
    '''
    i = 1
    while i > 0:
        div_3 = bool(i % 3 == 0)
        div_5 = bool(i % 5 == 0)
        if div_3 and div_5:
            yield 'FizzBuzz'
        elif div_3:
            yield 'Fizz'
        elif div_5:
            yield 'Buzz'
        else:
            yield i
        i += 1