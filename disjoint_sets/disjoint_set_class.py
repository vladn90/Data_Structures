""" Implementing Disjoint Set data structure using Node and a dictionary.
https://en.wikipedia.org/wiki/Disjoint-set_data_structure
Nice explanation video:
https://www.youtube.com/watch?v=ID00PMy0-vE

Usage:
make_set(x)  # creates an empty set containing x
find(x)  # returns parent of a set x
union(x, y)  # creates a union of a set x and a set y
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.rank = 0
        self.parent = None

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data})"


class DisjointSet:
    def __init__(self):
        self.nodes = dict()  # data: link to the node containing data

    def __repr__(self):
        return f"{self.__class__.__name__}({self.nodes.keys()})"

    def make_set(self, data):
        """ Creates a new empty set.
        """
        if data in self.nodes:  # we already have a set containing this data
            print(f"There's already a set with data = {data}.")
            return
        node = Node(data)
        node.parent = node
        self.nodes[data] = node

    def find(self, data):
        """ Returns data of a parent of a node that contains data.
        """
        return self.find_parent(self.nodes[data]).data

    def find_parent(self, node):
        """ Finds a parent of a node, compresses path along the way.
        """
        parent = node.parent
        if node == parent:
            return parent  # reached the root
        node.parent = self.find_parent(parent)  # compress path
        return node.parent

    def union(self, data1, data2):
        """ Creates a union of two sets containing data1 and data2.
        """
        parent1 = self.find_parent(self.nodes[data1])
        parent2 = self.find_parent(self.nodes[data2])
        # check if nodes are already in the same set
        if parent1 == parent2:
            return
        # attach set with the lower rank to set with higher rank
        if parent1.rank > parent2.rank:
            parent2.parent = parent1
        elif parent2.rank > parent1.rank:
            parent1.parent = parent2
        else:  # parent2.rank == parent1.rank
            parent1.rank += 1
            parent2.parent = parent1
