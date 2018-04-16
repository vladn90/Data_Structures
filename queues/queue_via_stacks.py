""" Implementing queue using two stacks.
One stack is used for the enqueue operation, another is used for dequeue.

Good explanations can be found here:
https://stackoverflow.com/questions/69192/how-to-implement-a-queue-using-two-stacks
https://leetcode.com/articles/implement-queue-using-stacks/
"""


class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return not self.items

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()


class Queue:
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def empty(self):
        """ Returns True if queue is empty, False otherwise.
        """
        return self.push_stack.empty() and self.pop_stack.empty()

    def enqueue(self, x):
        """ Adds element x to the queue. Time complexity: O(1).
        """
        self.push_stack.push(x)

    def dequeue(self):
        """ Removes an element from the queue.
        Amortized time complexity: O(1).
        """
        if queue.empty():
            raise Exception("Cannot dequeue from an empty queue.")

        if self.pop_stack.empty():
            while not self.push_stack.empty():
                self.pop_stack.push(self.push_stack.pop())
        return self.pop_stack.pop()


if __name__ == "__main__":
    queue = Queue()
    print(f"Is queue empty? {queue.empty()}")

    for n in range(1, 6):
        print(f"Enqueue...{n}")
        queue.enqueue(n)
    print(f"Is queue empty? {queue.empty()}")

    while not queue.empty():
        print(f"Dequeue... {queue.dequeue()}")
    print(f"Is queue empty? {queue.empty()}")
