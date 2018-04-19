""" Implementing maximum binary heap, a.k.a. priority queue.
https://en.wikipedia.org/wiki/Priority_queue

All operations take at most lg(n) time, where n is number of nodes:
1) h = MaxHeap()  # initializes an empty binary max heap
2) h.empty()  # checks if heap is empty
3) h.insert(x)  # inserts element x into the heap
4) h.get_min()  # returns current maximum element
5) h.pop_min()  # removes maximum element and returns it
6) h.build_heap()  # erases current heap and creates a new one from iterable

Very good and detailed explanation videos on heaps and priority queues:
https://www.coursera.org/learn/data-structures week 3

Following is based on this implementation:
https://runestone.academy/runestone/static/pythonds/Trees/BinaryHeapImplementation.html
"""


class MaxHeap:
    def __init__(self):
        self.heaplist = [0]
        self.size = 0

    def __repr__(self):
        return f"{self.__class__.__name__}({self.heaplist})"

    def empty(self):
        """ Returns True if heap is empty, False otherwise. Time complexity: O(1).
        """
        if self.size == 0:
            return True
        return False

    def sift_up(self, i):
        """ Sifts up an element at index i until heap order property is restored.
        Time complexity: O(lg(n)).
        """
        while i // 2 > 0 and self.heaplist[i // 2] < self.heaplist[i]:
            self.heaplist[i // 2], self.heaplist[i] = self.heaplist[i], self.heaplist[i // 2]
            i //= 2

    def insert(self, x):
        """ Adds an item x to the heap. Time complexity: O(lg(n)).
        """
        self.heaplist.append(x)
        self.size += 1
        self.sift_up(self.size)

    def max_child_index(self, i):
        """ Returns an index of child with maximum value for element at index i.
        Time complexity: O(1).
        """
        if 2 * i + 1 > self.size:  # element i doesn't have a right child
            return 2 * i  # return index of a left child
        if self.heaplist[2 * i] > self.heaplist[2 * i + 1]:
            return 2 * i  # left child is max
        return 2 * i + 1  # right child is max

    def sift_down(self, i):
        """ Sifts down the heap an element at index i until max heap order
        property is restored. Time complexity: O(lg(n)).
        """
        while 2 * i <= self.size:  # while there're some children below
            max_index = self.max_child_index(i)
            if self.heaplist[i] < self.heaplist[max_index]:
                self.heaplist[i], self.heaplist[max_index] = \
                    self.heaplist[max_index], self.heaplist[i]
            i = max_index

    def get_max(self):
        """ Returns a maximum element from the heap without removing it.
        Time complexity: O(1).
        """
        if self.empty():
            return
        return self.heaplist[1]

    def pop_max(self):
        """ Pops(deletes) max element from the heap. Returns popped element.
        Time complexity: O(lg(n)).
        """
        if self.empty():
            raise Exception("Cannot pop an element from an empty heap.")

        removed = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.size]
        self.size -= 1
        self.heaplist.pop()
        self.sift_down(1)
        return removed

    def build_heap(self, seq):
        """ Builds max heap from an iterable. Erases current heap.
        Time complexity: O(n).
        """
        self.size = len(seq)
        self.heaplist = [0] + seq[:]
        i = len(seq) // 2
        while i > 0:
            self.sift_down(i)
            i -= 1


if __name__ == "__main__":
    maxheap = MaxHeap()

    print(f"Is heap empty? {maxheap.empty()}")

    for num in range(1, 6):
        print(f"inserting...{num}")
        maxheap.insert(num)
    print(f"Is heap empty? {maxheap.empty()}")
    print(maxheap)
    print(f"What's the current max? {maxheap.get_max()}")

    print(f"popping max element...{maxheap.pop_max()}")
    print(f"popping max element...{maxheap.pop_max()}")
    print(f"popping max element...{maxheap.pop_max()}")
    print(f"popping max element...{maxheap.pop_max()}")
    print(f"popping max element...{maxheap.pop_max()}")

    print(f"Is heap empty? {maxheap.empty()}")
