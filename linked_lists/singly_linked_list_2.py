""" Singly Linked List with head and tail pointers.

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
    """ Singly Linked List with head and tail pointers.
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        """ Returns True if list is empty, False otherwise.
        """
        return self.head is None

    def push_front(self, new_data):
        """ Creates a new node with data = new_data and adds it to the
        beginning of the list.
        Time complexity: O(1).
        """
        new_node = Node(new_data)  # allocate a new node
        new_node.next_node = self.head  # connect new node to the 1st node
        self.head = new_node  # change the head pointer
        if self.tail is None:  # update tail pointer if the list was empty
            self.tail = new_node

    def top_front(self):
        """ Returns the 1st node in the list.
        Time complexity: O(1).
        """
        return self.head

    def pop_front(self):
        """ Removes the 1st node from the list and returns it.
        Raises an exception if the list is empty.
        Time complexity: O(1).
        """
        # raise exception if the list is empty
        if self.is_empty():
            raise Exception("Cannot pop a node from the empty list.")

        removed = self.head  # save the link to the to-be-removed node
        self.head = self.head.next_node  # remove node
        if self.head is None:  # list had only 1 node, update the tail pointer
            self.tail = None
        return removed

    def push_back(self, new_data):
        """ Creates a new node with data = new_data and adds it to the end
        of the list.
        Time complexity: O(1).
        """
        new_node = Node(new_data)  # allocate a new node
        if self.is_empty():  # list was empty, update both pointers
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def top_back(self):
        """ Returns the last node in the list.
        Time complexity: O(1).
        """
        return self.tail

    def pop_back(self):
        """ Removes the last node from the list and returns it.
        Raises an exception if the list is empty.
        Time complexity: O(n).
        """
        # raise an exception if the list is empty
        if self.is_empty():
            raise Exception("Cannot pop a node from the empty list.")

        # list has only 1 node
        if self.head == self.tail:
            removed = self.head
            self.head = self.tail = None  # update both pointers
            return removed

        # traverse the list till the last node, keep track of current pointer
        # and the previous pointer
        prev, curr = None, self.head
        while curr.next_node:  # while the next node is not None
            prev, curr = curr, curr.next_node
        prev.next_node = None  # unlink the last node
        self.tail = prev  # update the tail pointer
        return curr  # return removed node

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
                if prev is None:  # special case, wanted node is the 1st one
                    self.head = curr.next_node
                else:
                    prev.next_node = curr.next_node  # unlink the node

                if self.tail is curr:  # removed node was the last one
                    self.tail = prev  # update the tail
                return

            # node with data = key wasn't found, check the next node
            prev, curr = curr, curr.next_node

        # node is not in the list, raise an exception
        raise Exception(f"Node with data = {key} is not in the list.")


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
