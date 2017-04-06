# Q4
def get_seven_a(x):
    """
    >>> x = [1, 3, [5, 7], 9]
    >>> get_seven_a(x)
    7
    """
    "*** YOUR CODE HERE ***"
    return x[2][1]

def get_seven_b(x):
    """
    >>> x = [[7]]
    >>> get_seven_b(x)
    7
    """
    "*** YOUR CODE HERE ***"
    return x[0][0]

def get_seven_c(x):
    """
    >>> x = [1, [2, [3, [4, [5, [6, [7]]]]]]]
    >>> get_seven_c(x)
    7
    """
    "*** YOUR CODE HERE ***"
    return x[1][1][1][1][1][1][0]

# Q5
def reverse_recursive(lst):
    """Returns the reverse of the given list.

    >>> reverse_recursive([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverse_recursive([1, 2, 3, 4, 5, 6, 7])
    [7, 6, 5, 4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"
    
    if len(lst) == 1:
        return lst
    elif len(lst) == 2:
        return [lst[1],lst[0]]
    else:
        end = len(lst) - 1
        return [lst[end]] + reverse_recursive(lst[1:end]) + [lst[0]]
    """
    if not lst:
        return []
    return reverse_recursive(lst[1:]) + [lst[0]]
    """
    
  

# Q6
def merge(lst1, lst2):
    """Merges two sorted lists recursively.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"

    """
    if lst1 == []:   # len(lst1) == 0
        return lst2
    elif lst2 == []: # len(lst2) == 0
        return lst1
    else:
        if lst1[0] < lst2[0]:
            return [lst1.pop(0)] + merge(lst1, lst2)
        else:
            return [lst2.pop(0)] + merge(lst1, lst2)

    # code above isn't good because it ruins lst1 and lst2

    """
    if not lst1 or not lst2:
        return lst1 + lst2
    elif lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge(lst1, lst2[1:])
    
# Q8
from math import sqrt

def is_square(n):
    return float(sqrt(n)) == int(sqrt(n))

def squares(seq):
    """Returns a new list containing elements of the original list that are
    perfect squares.

    >>> seq = [49, 8, 2, 1, 102]
    >>> squares(seq)
    [49, 1]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    return [x for x in seq if is_square(x)]

