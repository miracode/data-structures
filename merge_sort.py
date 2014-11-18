def merge_sort(array):
    """
    Return a sorted list using the merge sort algorithm

    Worst case: O(n log(n))
    For each element in list (n), split the problem in half to merge (log(n))

    Best case: O(n log(n))
    Algorithm still needs to go through the same process whether or not the
    list is already sorted.

    """
    if len(array) <= 1:
        return array
    else:
        middle = len(array) / 2
        left = array[:middle]
        right = array[middle:]

        left = merge_sort(left)
        right = merge_sort(right)
        return _merge(left, right)


def _merge(left_array, right_array):
    merged = []
    while len(left_array) > 0 or len(right_array) > 0:
        if len(left_array) > 0 and len(right_array) > 0:
            if left_array[0] <= right_array[0]:
                merged.append(left_array.pop(0))
            else:
                merged.append(right_array.pop(0))
        elif len(left_array) > 0:
            merged.append(left_array.pop(0))
        elif len(right_array) > 0:
            merged.append(right_array.pop(0))
    return merged


if __name__ == '__main__':
    print merge_sort.func_doc
    array1 = [3, 2, 1]
    assert merge_sort(array1) == [1, 2, 3]
    array2 = [1, 2, 3, 5, 4]
    assert merge_sort(array2) == [1, 2, 3, 4, 5]
    array3 = range(100, 0, -1)
    assert merge_sort(array3) == range(1, 101)
