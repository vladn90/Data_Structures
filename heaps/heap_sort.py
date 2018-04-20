""" Heap sort algorithm, sorts array in-place, i.e. using O(1) space,
and has O(n * lg(n)) running time in the worst case.
https://en.wikipedia.org/wiki/Heapsort
"""
import random
import max_heap_func as mh


def heapsort(array):
    """ Sorts array in-place using max binary heap.
    Time complexity: O(n * lg(n)). Space complexity: O(1).
    """
    mh.build_heap(array)  # transform array into max heap, in-place, O(n) time
    end = len(array) - 1  # index of current last element in the heap
    for i in range(len(array) - 1):  # O(n * lg(n)) time
        array[0], array[end] = array[end], array[0]  # put max element at the end
        end -= 1  # last element is already in its place, adjust the end index
        mh.sift_down(array, end, 0)  # restore heap order property


if __name__ == "__main__":
    array = [random.randrange(-10, 10) for i in range(20)]
    print(f"original array: {array}")
    heapsort(array)
    assert array == sorted(array)  # self-check
    print(f"sorted array: {array}")
