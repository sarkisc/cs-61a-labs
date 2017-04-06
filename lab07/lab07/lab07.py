## Recursive Objects ##

# Linked Lists

class Link(object):
    """A linked list.

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> len(s)
    4
    >>> s[2]
    3
    >>> s
    Link(1, Link(2, Link(3, Link(4))))
    >>> t = Link(1, Link(2, Link(3, Link(4))))
    >>> t == s
    True
    """
    empty = ()


    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __eq__(self, other):
        if self.first != other.first:
            return False
        elif self.rest is Link.empty and not(other.rest is Link.empty) or not(self.rest is Link.empty) and other.rest is Link.empty:
            return False
        elif self.first == other.first and self.rest is Link.empty and other.rest is Link.empty:
            return True
        else:
            return self.rest == other.rest


def insert(link, value, index):
    """Insert a value into a Link at the given index.

    >>> link = Link(1, Link(2, Link(3)))
    >>> insert(link, 9001, 0)
    >>> link
    Link(9001, Link(1, Link(2, Link(3))))
    >>> insert(link, 100, 2)
    >>> link
    Link(9001, Link(1, Link(100, Link(2, Link(3)))))
    >>> insert(link, 4, 5)
    Index out of bounds!
    """
    "*** YOUR CODE HERE ***"
    if index == 0:
        link.rest = Link(link.first, link.rest)
        link.first = value
    elif link.rest is Link.empty:
        print('Index out of bounds!')
    else:
        insert(link.rest, value, index-1)

    """lame solution
    if index >= len(link):
        print('Index out of bounds!')
    elif index == 0:
        newlink = Link(value)
        insert(link, value, 1)
        link.rest.first = link.first
        link.first = value
    elif index == 1:
        newlink = Link(value)
        newlink.rest = link.rest
        link.rest = newlink
    else:
        insert(link.rest, value, index-1)
    """
# Trees

class Tree:
    def __init__(self, entry, branches=()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.entry, branches_str)

    def is_leaf(self):
        return not self.branches

def square_tree(t):
    """Mutates a Tree t by squaring all its elements.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> square_tree(t)
    >>> t
    Tree(1, [Tree(9, [Tree(25)]), Tree(49)])
    """
    "*** YOUR CODE HERE ***"
    t.entry = t.entry * t.entry
    for branch in t.branches:
        square_tree(branch)
