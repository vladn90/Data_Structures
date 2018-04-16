""" Implementing queue using singly linked list with head and tail pointers.
All operations are O(1) time.
"""


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None

    def enqueue(self, element):
        """ Adds element to the queue, i.e. attaches it to the tail of the list.
        """
        new = Node(val=element)
        if self.empty():
            self.head = self.tail = new
            return
        self.tail.next = new  # connect tail with a new node
        self.tail = new  # update tail pointer

    def dequeue(self):
        """ Removes first element from the queue, i.e. removes the first node
        in the list. Returns removed element.
        """
        if self.empty():
            return  # nothing to dequeue, queue is empty
        removed = self.head
        self.head = self.head.next  # update head pointer
        if self.head is None:  # queue had only one element
            self.tail = None  # update tail pointer
        return removed.val


if __name__ == "__main__":
    q = Queue()
    print(f"Is queue empty? {q.empty()}")
    print(f"Enqueue a few integers...")
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(f"Is queue empty? {q.empty()}")
    print(f"dequeue {q.dequeue()}")
    print(f"dequeue {q.dequeue()}")
    print(f"dequeue {q.dequeue()}")
    print(f"dequeue {q.dequeue()}")
    print(f"dequeue {q.dequeue()}")
    print(f"Is queue empty? {q.empty()}")
