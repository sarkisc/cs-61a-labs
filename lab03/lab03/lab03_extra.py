# Q9
def cycle(f1, f2, f3):
    """ Returns a function that is itself a higher-order function
    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    
    def doit(n):

        def apply(x):
            num_times = n
            while num_times >= 3:
                x = f3(f2(f1(x)))
                num_times -= 3

            if num_times == 1:
                x = f1(x)
            elif num_times == 2:
                x = f2(f1(x))

            return x

        return apply

    return doit

    """
    def doit(n):
        def theCycler(x):
            if n == 0:
                return x
            elif n == 1:
                return f1(x)
            elif n == 2:
                return f2(f1(x))
            elif n == 3:
                return f3(f2(f1(x)))
            else:
                m, k = x, 0       
                while k < (n // 3):
                    m, k = doit(3)(m), k + 1
                
                m = doit(n % 3)(m)
                
                return m

        return theCycler

    return doit
    """

# Q10
def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function func.
    >>> from operator import add
    >>> x = lambda_curry2(add)
    >>> y = x(3)
    >>> y(5)
    8
    """
    "*** YOUR CODE HERE ***"

    def curriedFunc(x):
        def func2(y):
            return func(x,y)

        return func2

    return curriedFunc

# Q12
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"

    
    if m == 1 or n == 1:
        return 1
    else:
        return 
        


# Q13
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"

    if a < b:
        return gcd(b,a)
    elif a % b == 0:
        return b
    else:
        return gcd(b,a % b)
