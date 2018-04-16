""" Implementing stack using array.
"""


class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        """ Returns True if stack is empty, False otherwise.
        Time complexity: O(1).
        """
        return len(self.items) == 0

    def push(self, element):
        """ Pushes element to the top of the stack.
        Time complexity: O(1).
        """
        self.items.append(element)

    def top(self):
        """ Returns the element from the top of the stack.
        Time complexity: O(1).
        """
        return self.items[-1]

    def pop(self):
        """ Pops an element from top of the stack and returns it.
        Time complexity: O(1).
        """
        if self.empty():
            raise Exception("Cannot pop an element from an empty stack.")

        return self.items.pop()


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
