""" Testing binary_search_tree_class.py.
"""
import string
import random
from binary_search_tree_class import TreeNode, BinarySearchTree


def inorder_traversal(bst):
    """ Returns a string of inorder key traversal of a binary search tree.
    """
    result = []
    for k in bst:
        result.append(k)
    return " ".join(map(str, result))


def put_test(display=False):
    """ Tests put method of BinarySearchTree class. If display == True, prints
    out intermediate test results to the screen.
    """
    bst = BinarySearchTree()  # initialize empty tree
    keys = [5, 30, 2, 40, 25, 4]
    result = ["5", "5 30", "2 5 30", "2 5 30 40", "2 5 25 30 40", "2 4 5 25 30 40"]
    for i, k in enumerate(keys):  # fill the tree with nodes
        bst.put(k, "no value")
        if display:
            print(f"Adding TreeNode with key = {k}")
        curr = inorder_traversal(bst)  # current inorder traversal of a tree
        assert curr == result[i]
        if display:
            print(f"current result of inorder traversal: {curr}")
            print()
    print("<<< put test is good >>>")


def setitem_test():
    """ Tests __setitem__ and __getitem__ method of BinarySearchTree class.
    """
    bst = BinarySearchTree()
    letters = string.ascii_uppercase
    for i, char in enumerate(letters):
        bst[i] = char
        assert bst[i] == char
    assert inorder_traversal(bst) == \
        "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25"
    print("<<< setitem test is good >>>")


def contains_test():
    """ Tests __contains__ method of BinarySearchTree class.
    """
    bst = BinarySearchTree()
    keys = [random.randrange(1, 100) for i in range(10**3)]
    for i, k in enumerate(keys):
        bst[k] = i
    for k in keys:
        assert (k in bst) == True
    print("<<< contains test is good >>>")


def delete_test():
    """ Tests __delitem__ method of BinarySearchTree class.
    """
    bst = BinarySearchTree()
    keys = set()
    while len(keys) < 10**3:
        keys.add(random.randrange(1, 10**6))
    for i, k in enumerate(keys):
        bst[k] = i
    for k in keys:
        del bst[k]
        assert (k not in bst) == True
    print("<<< delete test is good >>>")


if __name__ == "__main__":
    put_test()
    setitem_test()
    contains_test()
    delete_test()
