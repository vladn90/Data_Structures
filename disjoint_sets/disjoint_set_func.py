""" Implementing Disjoint Set data structure using only dictionaries, no classes.
https://en.wikipedia.org/wiki/Disjoint-set_data_structure

Usage:
parent = dict()  # initialize dictionary of parents
rank = dict()  # initialize dictionary of ranks
make_set(parent, rank, x)  # creates an empty set x
find(parent, x)  # returns parent of a set x
union(parent, rank, x, y)  # creates a union of a set x and a set y

Time complexity for find and union operations is O(lg(n)), however for all
practical values we can consider it to be constant, i.e. O(1). See this video
for more insight: https://www.youtube.com/watch?v=1-RjRtDnfPQ&feature=youtu.be
"""


def make_set(parent_dict, rank_dict, data):
    """ Creates a new set containing data. Time complexity: O(1).
    """
    if data in parent_dict:  # such set already exist
        print(f"There's already a set with data = {data}.")
        return
    parent_dict[data] = data  # parent of a new set is itself
    rank_dict[data] = 0  # starting rank is 0


def find(parent_dict, data):
    """ Returns a parent of a set with data. Compresses the path on the way to
    the root. Time complexity: O(1).
    """
    if data != parent_dict[data]:
        parent_dict[data] = find(parent_dict, parent_dict[data])  # path compression
    return parent_dict[data]  # return a new parent, i.e. the root


# below is an implementation of a find without path compression
# def find(parent_dict, data):
#     """ Returns a parent of a set with data. Time complexity: O(lg(n)),
#     n is a total number of disjoint sets.
#     """
#     if data not in parent_dict:
#         raise Exception(f"Set with data = {data} doesn't exist.")
#
#     while parent_dict[data] != data:
#         data = parent_dict[data]
#     return data


def union(parent_dict, rank_dict, data1, data2):
    """ Merges sets containing data1 and data2. Time complexity: O(1).
    """
    parent1 = find(parent_dict, data1)
    parent2 = find(parent_dict, data2)
    if parent1 == parent2:  # data1 and data2 are already in the same set, do nothing
        return
    if rank_dict[parent1] > rank_dict[parent2]:
        parent_dict[parent2] = parent1
    elif rank_dict[parent2] > rank_dict[parent1]:
        parent_dict[parent1] = parent2
    else:  # ranks are equal
        rank_dict[parent1] += 1
        parent_dict[parent2] = parent1


if __name__ == "__main__":
    parent_dict = dict()  # dictionary containing parent of a set x
    rank_dict = dict()  # dictionary containing rank of a set x

    make_set(parent_dict, rank_dict, 1)
    make_set(parent_dict, rank_dict, 2)
    make_set(parent_dict, rank_dict, 3)
    print(f"disjoint sets: {parent_dict}")

    x = 1  # set x
    print(f"Parent of set {x} is {find(parent_dict, x)}")

    x, y = 1, 3
    print(f"Merging sets {x} and {y}...")
    union(parent_dict, rank_dict, x, y)

    print(f"Parent of set {x} is {find(parent_dict, x)}")
    print(f"Parent of set {y} is {find(parent_dict, y)}")

    print(f"disjoint sets: {parent_dict}")
