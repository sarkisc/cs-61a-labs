## Extra Linked Lists and Sets ##

from lab08 import *

# Set Practice

def add_up(n, lst):
    """Returns True if any two non-identical elements in lst add up to any n.

    >>> add_up(100, [1, 2, 3, 4, 5])
    False
    >>> add_up(7, [1, 2, 3, 4, 2])
    True
    >>> add_up(10, [5, 5])
    False
    """
    "*** YOUR CODE HERE ***"
    for x in lst:
        for y in lst:
            if x != y and x+y == n:
                return True
    return False

def pow(n,k):
    """Computes n^k.

    >>> pow(2, 3)
    8
    >>> pow(4, 2)
    16
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    else:
        return n * pow(n,k-1)


def missing_no(lst):
    """lst contains all the numbers from 1 to n for some n except some
    number k. Find k.

    >>> missing_no([1, 0, 4, 5, 7, 9, 2, 6, 3])
    8
    >>> missing_no(list(filter(lambda x: x != 293, list(range(2000)))))
    293
    """
    "*** YOUR CODE HERE ***"
    return list( set( range(max(lst)+1) ).symmetric_difference(lst) )[0]


def find_duplicates_k(k, lst):
    """Returns True if there are any duplicates in lst that are within k
    indices apart.

    >>> find_duplicates_k(3, [1, 2, 3, 4, 1])
    False
    >>> find_duplicates_k(4, [1, 2, 3, 4, 1])
    True
    >>> find_duplicates_k(3, [1, 2, 3, 4, 5, 6, 7, 7])
    True
    """
    "*** YOUR CODE HERE ***"
    s = []
    i = 0
    j = (len(lst)-1)-(k+1)+2
    while i < j:
        s.append(lst[i:i+k+1])
        i = i+1
    for x in s:
        if find_duplicates(x):
            return True
    return False




