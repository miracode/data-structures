def quick_sort(array):
    if array:
        print "before %s" % array
        array, pivot_index = _partition(array)
        pivot_value = array[pivot_index]
        print "after %s, index %s" % (array, pivot_index)
        left = quick_sort(array[:pivot_index])
        right = quick_sort(array[pivot_index + 1:])
        array = [pivot_value]
        if left:
            array = left + array
        if right:
            array = array + right
        return array


def _partition(array):
    left = []
    right = []
    pivot_index = -1
    pivot_value = array[pivot_index]

    for i in range(len(array) - 1):
        if array[i] > pivot_value:
            right.append(array[i])
        else:
            left.append(array[i])

    array = left + [pivot_value] + right
    pivot_index = len(left)

    return array, pivot_index


if __name__ == '__main__':
    # print quick_sort.func_doc
    # array1 = [3, 2, 1]
    # assert quick_sort(array1) == [1, 2, 3]
    # array2 = [1, 2, 3, 5, 4]
    # assert quick_sort(array2) == [1, 2, 3, 4, 5]
    # array3 = range(100, 0, -1)
    # assert quick_sort(array3) == range(1, 101)
    array1 = [7, 2, 6, 4, 5, 3]
    print quick_sort(array1)
