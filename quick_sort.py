def quick_sort(array, start=0, end=-1):
    """
    Sort array with quicksort algorithm

    Best Case: O(n log n)
    When the partition divides the problem into roughly two even sub-arrays
    the sort is broken up into sorting each half (log n) of the partition (n)

    Wors Case: O(n^2)
    If the array is already sorted, then each partition doesn't break the
    problem in half, we end up partitioning n times for each element n.

    """

    # -1 equivalent to last element in array
    if end == -1:
        end = len(array) - 1

    # partition and sort array if start < end index
    if start < end:
        # partition the sub array defined by start and end, return full array
        array, pivot = _partition(array, start, end)
        # quick sort left side
        array = quick_sort(array, start, pivot - 1)
        # quick sort right side
        array = quick_sort(array, pivot + 1, end)

    return array


def _partition(array, start, end):
    # use last element of sub-array as pivot index
    pivot_index = end
    pivot_value = array[pivot_index]
    # start comparing at beginning of sub-array
    store_index = start
    # compare each element in sub-array
    for i in range(start, end + 1):
        # if smaller than pvalue, swap to index of array
        # otherwise pass to next element
        if array[i] < pivot_value:
            array[i], array[store_index] = array[store_index], array[i]
            # after swap, move index to next element
            store_index += 1

    # swap the pivot value to index position
    array[store_index], array[end] = array[end], array[store_index]

    return array, store_index


if __name__ == '__main__':
    print quick_sort.func_doc
    array1 = [3, 2, 1]
    assert quick_sort(array1) == [1, 2, 3]
    array2 = [1, 2, 3, 5, 4]
    assert quick_sort(array2) == [1, 2, 3, 4, 5]
    array3 = range(100, 0, -1)
    assert quick_sort(array3) == range(1, 101)
    array4 = [4, 5, 7, 4, 3, 2]
    assert quick_sort(array4) == [2, 3, 4, 4, 5, 7]
    print "tests pass"
