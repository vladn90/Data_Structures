""" Implementation of an ADT map using Binary Search Tree data structure using classes:
https://en.wikipedia.org/wiki/Binary_search_tree

Based on the book "Problem Solving with Algorithms and Data Structures using Python":
https://runestone.academy/runestone/static/pythonds/Trees/SearchTreeImplementation.html


Usage:
bst = BinarySearchTree()  # initializes an empty tree
bst["a"] = 97  # sets key("a") in tree equal to value(97)
"a" in bst  # checks if key is in the tree
bst["a"]  # returns value of a key if it's present, None otherwise
del bst["a"]  # deletes key from the tree if it's present, raises an error if it doesn't

Following code implements unbalanced binary search tree so operations might take
O(n) time in the worst case, where n is a total number of nodes.
"""


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"{self.__class__.__name__}({self.key}, {self.val})"

    def __iter__(self):
        """ Implements inorder traversal of binary tree.
        """
        if self:
            if self.left:
                for node in self.left:
                    yield node
            yield self.key
            if self.right:
                for node in self.right:
                    yield node

    def is_left(self):
        """ Returns True if node is a left child of another node,
        False otherwise.
        """
        return self.parent is not None and self.parent.left == self

    def is_right(self):
        """ Returns True if node is a right child of another node,
        False otherwise.
        """
        return self.parent is not None and self.parent.right == self

    def is_root(self):
        """ Returns True if node is a root node, False otherwise.
        """
        return not self.parent

    def is_leaf(self):
        """ Returns True if node is a leaf node, False otherwise.
        """
        return not self.left and not self.right

    def replace_data(self, key, val, left, right):
        """ Replaces all node data with provided data.
        """
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def find_successor(self):
        """ Returns link to the node with the next largest key. Returns None
        if node with such key doesn't exist.
        """
        succ = None
        if self.right:
            succ = self.right.find_min()
        elif self.parent:
            if self.is_left():
                succ = self.parent
            else:
                self.parent.right = None
                succ = self.parent.find_successor()
                self.parent.right = self  # backtracking
        return succ

    def find_min(self):
        """ Returns a node with minimum key for current tree.
        """
        curr = self
        while curr.left:
            curr = curr.left
        return curr

    def remove_node(self):
        """ Removes node from the tree. Raises an exception if it's a root node.
        Method shouldn't be used directly.
        """
        if self.is_root():
            raise Exception("Node cannot be a root node.")

        if self.is_leaf():
            if self.is_left():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.left:
            if self.is_left():
                self.parent.left = self.left
            else:
                self.parent.right = self.left
            self.left.parent = self.parent
        else:
            if self.is_left():
                self.parent.left = self.right
            else:
                self.parent.right = self.right
            self.right.parent = self.parent


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        return f"{self.__class__.__name__}(root={self.root})"

    def __iter__(self):
        if not self.root:
            raise Exception("Cannot iterate over an empty tree.")
        return self.root.__iter__()

    def put(self, key, val):
        """ Inserts a new node in the tree with key=key and value=val. If node
        with such key is already present in the tree, updates its value.
        """
        if self.root:  # tree already has a root
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, curr):
        """ Helper function for put.
        """
        if key == curr.key:  # update node's value
            curr.val = val
        elif key < curr.key:
            if curr.left:  # search left subtree
                self._put(key, val, curr.left)
            else:  # doesn't have a left subtree, so insert node as a left subtree
                curr.left = TreeNode(key=key, val=val, parent=curr)
        else:
            if curr.right:  # search right subtree
                self._put(key, val, curr.right)
            else:  # doesn't have a right subtree, so insert node as a right subtree
                curr.right = TreeNode(key=key, val=val, parent=curr)

    def __setitem__(self, key, val):
        """ Allows usage like Python list or dictionary: tree[key]=val.
        """
        return self.put(key, val)

    def get(self, key):
        """ Returns a value of a node with key=key if there's one,
        returns None if there's no such node.
        """
        node = self._get(key, self.root)
        if node:
            return node.val
        return None

    def _get(self, key, curr):
        """ Helper function for get. Returns link to the node with key=key if
        there's one, return None otherwise.
        """
        if not curr:
            return None
        elif key == curr.key:
            return curr
        elif key > curr.key:  # search right subtree
            return self._get(key, curr.right)
        else:  # search left subtree
            return self._get(key, curr.left)

    def __getitem__(self, key):
        """ Allows usage like Python list or dictionary: x = tree[key].
        """
        return self.get(key)

    def __contains__(self, key):
        """ Allows membership check like: key in tree / key not in tree.
        """
        if self.get(key):
            return True
        else:
            return False

    def delete(self, key):
        """ Removes node with key=key from the tree, raises an error if there's
        no such node.
        """
        if self.size > 1:
            node = self._get(key, self.root)
            if node:  # node with key=key was found
                self.remove(node)
                self.size -= 1
            else:
                raise KeyError(f"Tree doesn't have a node with key={key}.")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError(f"Tree doesn't have a node with key={key}.")

    def remove(self, node):
        """ Helper function for delete. Removes node from the tree.
        """
        if node.is_leaf():  # node doesn't have any children
            if node.is_left():
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.left and node.right:  # node has both children
            succ = node.find_successor()
            succ.remove_node()
            node.key, node.val = succ.key, succ.val
        else:  # node has only one child
            if node.left:  # node has only left child
                if node.is_left():  # node itself is a left child
                    node.left.parent = node.parent
                    node.parent.left = node.left
                elif node.is_right():
                    node.left.parent = node.parent
                    node.parent.right = node.left
                else:  # node is a root node
                    node.replace_data(node.left.key, node.left.val,
                                      node.left.left, node.left.right)
            else:  # node has only right child
                if node.is_left():
                    node.right.parent = node.parent
                    node.parent.left = node.right
                elif node.is_right():
                    node.right.parent = node.parent
                    node.parent.right = node.right
                else:
                    node.replace_data(node.right.key, node.right.val,
                                      node.right.left, node.right.right)

    def __delitem__(self, key):
        """ Allows usage: del tree[key].
        """
        return self.delete(key)


if __name__ == "__main__":
    bst = BinarySearchTree()
