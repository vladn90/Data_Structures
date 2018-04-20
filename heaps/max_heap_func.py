""" Implementing Max Binary Heap without classes, inspiration is drawn from
Python builtin heapq module. All procedures take O(1) space and no more than
O(lg(n)) time, where n is a number of elements in heap.

Max Heap has the following funtionality:
h = []  # initialize an empty heap, just like initializing a list(array)
insert(h, x)  # add element x to the heap
pop_max(h)  # pop maximum element from the heap
build_heap(array)  # modify an array in-place so it becomes a heap
"""


def left(i):
    """ Returns index of a left child of element i.
    """
    return 2 * i + 1


def right(i):
    """ Returns index of a right child of element i.
    """
    return 2 * i + 2


def parent(i):
    """ Returns index of a parent of element i.
    """
    return (i - 1) // 2


def max_child(heap, end, i):
    """ Returns an index of a child with maximum value for element i.
    """
    if right(i) > end:  # right child doesn't exist
        return left(i)
    if heap[left(i)] > heap[right(i)]:  # choose max between left and right
        return left(i)
    return right(i)


def sift_up(heap, i):
    """ Sifts element at index i up the heap until heap order property is restored.
    Time complexity: O(lg(n)).
    """
    # while we haven't reached the root and parent > child
    while parent(i) > -1 and heap[parent(i)] < heap[i]:
        heap[parent(i)], heap[i] = heap[i], heap[parent(i)]
        i = parent(i)


def sift_down(heap, end, i):
    """ Sifts element at index i down the heap till index end until heap order
    property is restored. Time complexity: O(lg(n)).
    """
    while left(i) <= end:  # while we still have some children below
        max_index = max_child(heap, end, i)
        if heap[i] < heap[max_index]:
            heap[i], heap[max_index] = heap[max_index], heap[i]
        i = max_index


def insert(heap, x):
    """ Adds element x to the heap. Time complexity: O(lg(n)).
    """
    heap.append(x)  # add an element to the heap
    sift_up(heap, len(heap) - 1)  # restore heap order property


def pop_max(heap):
    """ Pops maximum element from the heap while keeping heap order property.
    Returns popped element. Time complexity: O(lg(n)).
    """
    if not heap:  # empty heap
        raise IndexError("Cannot pop from an empty heap.")
    removed = heap[0]  # save the removed element
    heap[0] = heap[-1]  # substitute root with the last element in heap
    heap.pop()  # remove the last element, since we already have a copy at the root
    sift_down(heap, len(heap) - 1, 0)  # sift down root element to restore heap order property
    return removed  # return popped element


def build_heap(array):
    """ Turns array into a max heap in-place. Time complexity: O(n).
    """
    mid = len(array) // 2
    for i in range(mid, -1, -1):
        sift_down(array, len(array) - 1, i)


if __name__ == "__main__":
    h = [1, 2, 3, -1, -2, -3, 2]
    print(f"original array: {h}")
    build_heap(h)
    print(f"modified to max heap: {h}")

    for i in range(len(h)):
        print(f"popping max element...{pop_max(h)}")
    print(f"max heap: {h}")

    for i in range(5):
        insert(h, i)
        print(f"inserting...{i}")
    print(f"max heap: {h}")
