from lab05 import *

## Extra Trees, Dictionaries Questions ##

#########
# Trees #
#########

# Q5
def height(t):
    """Return the depth of the deepest node in the tree.

    >>> height(tree(1))
    0
    >>> height(tree(1, [tree(2), tree(3)]))
    1
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> height(numbers)
    2
    """
    "*** YOUR CODE HERE ***"

    if(branches(t) == []):
        return 0
    return 1 + max( height(branch) for branch in branches(t) )



# Q6
def acorn_finder(t):
    """Returns True if t contains a node with the value 'acorn' and
    False otherwise.

    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('acorn')]), tree('branch2')])
    >>> acorn_finder(sproul)
    True
    >>> acorn_finder(numbers)
    False
    """
    "*** YOUR CODE HERE ***"

    if(root(t) == 'acorn'):
        return True
    else:
        return any([acorn_finder(branch) for branch in branches(t)])

"""
    if root(t) == 'acorn':
      return True
    for branch in branches(t):
      if acorn_finder(branch) == True:
        return True
    return False
"""


# Q7a
def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"

    if branches(t) == []:
        return [root(t)]

    else:
        final = [root(t)]
        for branch in branches(t):
            final += preorder(branch)
        return final


#Q7b
def postorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a postorder traversal (see problem description).

    >>> postorder(numbers)
    [2, 4, 5, 3, 7, 6, 1]
    >>> postorder(tree(2, [tree(4, [tree(6)])]))
    [6, 4, 2]
    """
    "*** YOUR CODE HERE ***"

    if branches(t) == []:
        return [root(t)]

    else:
        final = []
        for branch in branches(t):
            final += postorder(branch)
        return final + [root(t)]


#Q7c
def leaves(t):
    """Returns a list of all the entries of the leaf nodes of the Tree t.

    >>> leaves(tree(1))
    [1]
    >>> leaves(tree(1, [tree(2, [tree(3)]), tree(4)]))
    [3, 4]
    """
    "*** YOUR CODE HERE ***"
    if branches(t) == []:
        return [root(t)]
    else:
        final = []
        for branch in branches(t):
            final += leaves(branch)
        return final


################
# Dictionaries #
################

# Q8
def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of
    successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            "*** YOUR CODE HERE ***"
            table[prev] = []

        "*** YOUR CODE HERE ***"
        table[prev] += [word]
        prev = word
    return table

# Q9
def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.
    """
    import random
    result = ' '
    while word not in ['.', '!', '?']:
        "*** YOUR CODE HERE ***"
    return result + word

# Warning: do NOT try to print the return result of this function
def shakespeare_tokens(path='shakespeare.txt', url='http://goo.gl/SztLfX'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

# Uncomment the following two lines
# tokens = shakespeare_tokens()
# table = build_successors_table(tokens)

def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)
