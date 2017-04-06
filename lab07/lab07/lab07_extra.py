## Extra Recursive Objects ##

from lab07 import *

# Linked List Practice


def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.

    >>> list_to_link([1, 2, 3])
    Link(1, Link(2, Link(3)))
    """
    "*** YOUR CODE HERE ***"
    #if lst == []:
        #return
    #elif len(lst) == 1:
        #return Link(lst[0])
    if lst == []:
        return Link.empty                          # This is great. Notice that you're calling list_to_link([])
                                                   # within the call list_to_link([last_elem])
    else:
        return Link(lst[0], list_to_link(lst[1:])) # remember: you don't have to specify the end index
                                                   # I want from index 1 until the end of the list


def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return []
    else:
        return [link.first] + link_to_list(link.rest)


def reverse(link):
    """Returns a Link that is the reverse of the original.

    >>> reverse(Link(1))
    Link(1)
    >>> link = Link(1, Link(2, Link(3)))
    >>> reverse(link)
    Link(3, Link(2, Link(1)))
    >>> link
    Link(1, Link(2, Link(3)))
    """
    "*** YOUR CODE HERE ***"
    lst = link_to_list(link)
    revlst = rev(lst)
    return list_to_link(revlst)


def rev(lst):
    """Returns a list that is the reverse of the original.

    >>> mylist = [1, 2, 3]
    >>> rev(mylist)
    [3, 2, 1]
    >>> mylist
    [1, 2, 3]
    """
    if lst == []:
        return lst
    return [lst[len(lst)-1]] + rev(lst[:len(lst)-1])


def mutate_reverse(link):
    """Mutates the Link so that its elements are reversed.

    >>> link = Link(1)
    >>> mutate_reverse(link)
    >>> link
    Link(1)

    >>> link = Link(1, Link(2, Link(3)))
    >>> mutate_reverse(link)
    >>> link
    Link(3, Link(2, Link(1)))
    >>> link2 = Link(1, Link(2, Link(3, Link(4))))
    >>> mutate_reverse(link2)
    >>> link2
    Link(4, Link(3, Link(2, Link(1))))
    """
    "*** YOUR CODE HERE ***"
    countfrom = 0
    countto = len(link) - 1
    while countfrom < countto:
        start = link
        end = link
        counter = 0
        # initialize start
        while counter < countfrom:
            start = start.rest
            counter += 1

        counter = 0
        # initialize end
        while counter < countto:
            end = end.rest
            counter += 1

        swap(start, end)

        countfrom += 1
        countto -= 1


def swap(link1, link2):
    """Swaps the 'first' values of two links.
       I am considering the 'first' values to be primitives.

    >>> link = Link(1, Link(2, Link(3)))
    >>> swap(link, link.rest)
    >>> link
    Link(2, Link(1, Link(3)))
    """
    temp = link1.first
    link1.first = link2.first
    link2.first = temp


# Tree Practice

def leaves(t):
    """Returns a list of all the entries of the leaf nodes of the Tree t.

    >>> leaves(Tree(1))
    [1]
    >>> leaves(Tree(1, [Tree(2, [Tree(3)]), Tree(4)]))
    [3, 4]
    """
    "*** YOUR CODE HERE ***"
    if t.branches == ():
        return [t.entry]
    else:
        final = []
        for branch in t.branches:
            final += leaves(branch)
        return final

def copy_tree(t):
    """Returns a copy of the tree.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> x = copy_tree(t)
    >>> x
    Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    """
    if t.branches == ():
        return Tree(t.entry)
    else:
        x = Tree(t.entry, [])
        for branch in t.branches:
            x.branches += [copy_tree(branch)]
        return x

def cumulative_sum(t):
    """Return a new Tree, where each entry is the sum of all entries in the
    corresponding subtree of t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative = cumulative_sum(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(Tree(1))
    Tree(1)
    """
    "*** YOUR CODE HERE ***"
    return cumulative_sum_mutate(copy_tree(t))


def cumulative_sum_mutate(t):
    """Return the same instance of a Tree, where each entry is thee sum of all entries
    in the corresponding subtree of t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative = cumulative_sum_mutate(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])

    """
    if t.branches == ():
        return t
    else:
        for branch in t.branches:
            cumulative_sum_mutate(branch)
            t.entry += branch.entry
        return t


def same_shape(t1, t2):
    """Returns whether two Trees t1, t2 have the same shape. Two trees have the
    same shape if they have the same number of branches and each of their
    children have the same shape.

    >>> t, s = Tree(1), Tree(3)
    >>> same_shape(t, t)
    True
    >>> same_shape(t, s)
    True
    >>> t = Tree(1, [Tree(2), Tree(3)])
    >>> same_shape(t, s)
    False
    >>> s = cumulative_sum(t)
    >>> same_shape(t, s)
    True
    """
    "*** YOUR CODE HERE ***"
    return list_num_branches(t1) == list_num_branches(t2)


def list_num_branches(t):
    """Returns a list of the number of branches in all nodes of a tree, beginning with the root.
    The tree is traversed in preorder.

    >>> t = Tree(1, [Tree(3, [Tree(5, [Tree(4), Tree(2)]), Tree(6)]), Tree(7)])
    >>> list_num_branches(t)
    [2, 2, 2, 0, 0, 0, 0]
    """
    if t.branches == ():
        return [0]
    else:
        final = [num_branches(t)]
        for branch in t.branches:
            final += list_num_branches(branch)
        return final


def num_branches(t):
    """Returns the number of branches a tree has

    >>> t = Tree(1, [Tree(2), Tree(3)])
    >>> num_branches(t)
    2
    """
    return len(t.branches)



# Folding Linked Lists

from operator import add, sub, mul

def foldl(link, fn, z):
    """ Left fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldl(lst, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl(lst, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl(lst, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    if link is Link.empty:
        return z
    "*** YOUR CODE HERE ***"
    return foldl(link.rest, fn, fn(z,link.first))

def foldr(link, fn, z):
    """ Right fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldr(lst, sub, 0) # (3 - (2 - (1 - 0)))
    2
    >>> foldr(lst, add, 0) # (3 + (2 + (1 + 0)))
    6
    >>> foldr(lst, mul, 1) # (3 * (2 * (1 * 1)))
    6
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return z
    return fn(link.first, foldr(link.rest, fn, z))


identity = lambda x: x

def foldl2(link, fn, z):
    """ Write foldl using foldr
    >>> list = Link(3, Link(2, Link(1)))
    >>> foldl2(list, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl2(list, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl2(list, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    def step(x, g):
        "*** YOUR CODE HERE ***"

    return foldr(link, step, identity)(z)

