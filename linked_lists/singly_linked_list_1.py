""" Singly Linked List with head pointer only.

API naming is based on Coursera course Data Structures by
University of California, San Diego &
National Research University Higher School of Economics.
"""


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f"{__class__.__name__}({self.data})"

    def __str__(self):
        return f"{self.data}"


class SinglyLinkedList:
    """ Singly Linked List with head pointer.
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        """ Returns True if list is empty, False otherwise.
        """
        return self.head is None

    def push_front(self, new_data):
        """ Creates a new node with data = new_data and prepends it to the
        beginning of the list.
        Time complexity: O(1).
        """
        new_node = Node(new_data)  # allocate a new node
        new_node.next_node = self.head  # connect new node to the 1st node
        self.head = new_node  # change the head pointer

    def top_front(self):
        """ Returns the 1st node in the list.
        Time complexity: O(1).
        """
        return self.head

    def pop_front(self):
        """ Removes the 1st node from the list and returns it.
        Time complexity: O(1).
        """
        # raise exception if the list is empty
        if self.is_empty():
            raise Exception("Cannot pop a node from the empty list.")

        removed = self.head  # save the link to the to-be-removed node
        self.head = self.head.next_node  # remove node
        return removed

    def push_back(self, new_data):
        """ Creates a new node with data = new_data and appends it to the end
        of the list.
        Time complexity: O(n).
        """
        new_node = Node(new_data)  # allocate a new node
        if self.is_empty():  # special case, list is empty
            self.head = new_node  # change the head pointer
            return

        curr = self.head
        while curr.next_node:  # traverse the list till the last node
            curr = curr.next_node
        # set the next pointer of the last node to the new node
        curr.next_node = new_node

    def top_back(self):
        """ Returns the last node in the list.
        Time complexity: O(n).
        """
        # special case, the list is empty
        if self.is_empty():
            return

        # list has only 1 node
        if self.head.next_node is None:
            return self.head

        # traverse the list till the last node and return it
        curr = self.head
        while curr.next_node:
            curr = curr.next_node
        return curr

    def pop_back(self):
        """ Removes the last node from the list and returns it.
        Time complexity: O(n).
        """
        # raise exception if the list is empty
        if is_empty():
            raise Exception("Cannot pop a node from the empty list.")

        # list has only 1 node
        if self.head.next_node is None:
            removed = self.head
            self.head = None
            return removed

        # traverse the list till the last node, keep track of current node
        # and the previous node
        prev = None
        curr = self.head
        while curr.next_node:
            prev, curr = curr, curr.next_node
        # unlink the last node, i.e. link the previous node to None
        removed = curr
        prev.next_node = None
        return curr

    def find(self, key):
        """ Returns True if there's node on the list with data == key,
        False otherwise.
        Time complexity: O(n).
        """
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next_node
        return False

    def erase(self, key):
        """ Deletes the node with data = key.
        Raises an exception if node with such data doesn't exist.
        Time complexity: O(n).
        """
        prev = None
        curr = self.head
        while curr:
            if curr.data == key:  # found the node
                if prev is None:  # special case, list has only 1 node
                    self.head = None
                    return
                else:
                    prev.next_node = curr.next_node  # unlink the node
                    return
            # node with data == key wasn't found, check the next node
            prev, curr = curr, curr.next_node

        # node is not in the list, raise an exception
        raise Exception(f"Node with data = {key} is not in the list.")


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
