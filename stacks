""" Implementing stack using singly linked list with head pointer only.
"""


class Stack:

    class Node:
        def __init__(self, val=None, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None  # top element of the stack

    def empty(self):
        """ Returns True if stack is empty, False otherwise.
        Time complexity: O(1).
        """
        return self.head == None

    def push(self, element):
        """ Pushed element to the top of the stack.
        Time complexity: O(1).
        """
        new = self.Node(val=element)
        new.next = self.head
        self.head = new

    def top(self):
        """ Returns the element from the top of the stack.
        Time complexity: O(1).
        """
        return self.head.val

    def pop(self):
        """ Pops an element from top of the stack and returns it.
        Time complexity: O(1).
        """
        if self.empty():
            raise Exception("Cannot pop an element from an empty stack.")

        rem = self.head.val
        self.head = self.head.next
        return rem


if __name__ == "__main__":
    stack = Stack()

    print(f"Is stack empty? {stack.empty()}")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Is stack empty? {stack.empty()}")
    print(f"top element: {stack.top()}")
    stack.pop()
    stack.pop()
    stack.pop()
    print(f"Is stack empty? {stack.empty()}")
    # stack.pop()  # gonna trigger an exception since stack is already empty
