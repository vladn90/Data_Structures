""" Naive implementation of heap sort algorithm using Min Heap data structure.
"""
import random
from min_heap_class import MinHeap


def heap_sort_naive(array):
    """ Sorts an array in non-descending order using heap. Doesn't return anything.
    Time complexity: O(n * lg(n)). Space complexity: O(n), n is len(array).
    """
    heap = MinHeap()
    for element in array:  # put all array elements into heap
        heap.insert(element)
    for i in range(len(array)):  # extract min element from the heap, update array
        array[i] = heap.pop_min()


if __name__ == "__main__":
    array = [random.randrange(-10, 10) for i in range(10)]

    print(f"original array: {array}")
    heap_sort_naive(array)
    assert array == sorted(array)  # self-check
    print(f"sorted array: {array}")
