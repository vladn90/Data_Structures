""" Implementing minimum binary heap, a.k.a. priority queue.
https://en.wikipedia.org/wiki/Priority_queue

All operations take at most lg(n) time, where n is number of nodes:
1) h = MinHeap()  # initializes an empty binary min heap
2) h.empty()  # checks if heap is empty
3) h.insert(x)  # inserts element x into the heap
4) h.get_min()  # returns current minimum element
5) h.pop_min()  # removes minimum element and returns it
6) h.build_heap()  # erases current heap and creates a new one from iterable

Very good and detailed explanation videos on heaps and priority queues:
https://www.coursera.org/learn/data-structures week 3

Following is based on this implementation:
https://runestone.academy/runestone/static/pythonds/Trees/BinaryHeapImplementation.html
"""


class MinHeap:
    def __init__(self):
        self.heaplist = [0]  # 0 is for convinience
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
        """ Sifts an item at index i up the heap until min heap order property
        is restored. Time complexity: O(lg(n)).
        """
        # while we haven't reached the root and parent > current node
        while i // 2 > 0 and self.heaplist[i // 2] > self.heaplist[i]:
            self.heaplist[i // 2], self.heaplist[i] = self.heaplist[i], self.heaplist[i // 2]
            i //= 2

    def min_child_index(self, i):
        """ Returns an index of a child with a minimum value for node i
        if there're both children, otherwise returns an index of a left child.
        Time complexity: O(1).
        """
        if 2 * i + 1 > self.size:  # only left child exists
            return 2 * i
        if self.heaplist[2 * i] < self.heaplist[2 * i + 1]:
            return 2 * i  # left child is the min
        return 2 * i + 1  # right child is the min

    def sift_down(self, i):
        """ Sifts an item at index i down the heap until min heap order property
        is restored. Time complexity: O(lg(n)).
        """
        while 2 * i <= self.size:  # while there're still some children below
            min_index = self.min_child_index(i)
            if self.heaplist[i] > self.heaplist[min_index]:
                self.heaplist[i], self.heaplist[min_index] = \
                    self.heaplist[min_index], self.heaplist[i]
            i = min_index  # update current index

    def insert(self, x):
        """ Adds an element x to the the heap. Time complexity: O(lg(n)).
        """
        self.heaplist.append(x)  # append it to the end of the heap
        self.size += 1  # adjust size of the heap
        self.sift_up(self.size)  # self.size is a current index of x

    def get_min(self):
        """ Returns minimum element from the heap. Time complexity: O(1).
        """
        if self.empty():
            return
        return self.heaplist[1]

    def pop_min(self):
        """ Pops(deletes) minimum element from the heap.
        Returns popped element. Time complexity: O(lg(n)).
        """
        if self.empty():
            raise Exception("Cannot pop an element from an empty heap.")

        removed = self.heaplist[1]  # save the minimum element
        self.heaplist[1] = self.heaplist[self.size]  # put the last element at the root
        self.size -= 1  # adjust size
        self.heaplist.pop()  # actually remove the last element from array
        self.sift_down(1)  # restore min heap order property by sifting down root element
        return removed

    def build_heap(self, seq):
        """ Builds min heap from an iterable. Erases current heap.
        Time complexity: O(n).
        """
        self.size = len(seq)
        self.heaplist = [0] + seq[:]
        i = len(seq) // 2
        while i > 0:
            self.sift_down(i)
            i -= 1


if __name__ == "__main__":
    minheap = MinHeap()

    print(f"Is heap empty? {minheap.empty()}")

    for num in range(1, 4):
        print(f"inserting...{num}")
        minheap.insert(num)
    for num in range(-3, 0):
        print(f"inserting...{num}")
        minheap.insert(num)
    print(f"Is heap empty? {minheap.empty()}")
    print(minheap)
    print(f"What's the current min? {minheap.get_min()}")

    print(f"popping min element...{minheap.pop_min()}")
    print(f"popping min element...{minheap.pop_min()}")
    print(f"popping min element...{minheap.pop_min()}")
    print(f"popping min element...{minheap.pop_min()}")
    print(f"popping min element...{minheap.pop_min()}")
    print(f"popping min element...{minheap.pop_min()}")

    print(f"Is heap empty? {minheap.empty()}")
