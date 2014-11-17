
def insertion_sort(array):
    """
    Sort an input array with insertion sort algorithm

    The insertion sort algorithm compares an element with the preceeding
    ordered element to determine whether the two should be swapped.  This will
    continue until the preceeding element is no longer greater than the
    current element.

    Best case scenario: O(n)
    - Best case, if an array is already sorted, this algorithm will inspect
    every element of the list once to verify it is sorted, no swaps required.

    Worst case scenario: O(n^2)
    - Worst case, if an array is reversely sorted, each element must be
    compared and swapped with every element preceeding it until it reaches
    the beginning.
    """
    for elem in range(len(array)):
        curr = elem
        while curr > 0 and array[curr - 1] > array[curr]:
            # swap values
            array[curr - 1], array[curr] = array[curr], array[curr - 1]
            curr -= 1
    return array

if __name__ == '__main__':
    print insertion_sort.func_doc
    array1 = [3, 2, 1]
    assert insertion_sort(array1) == [1, 2, 3]
    array2 = [1, 2, 3, 5, 4]
    assert insertion_sort(array2) == [1, 2, 3, 4, 5]
    array3 = range(100, 0, -1)
    assert insertion_sort(array3) == range(1, 101)
