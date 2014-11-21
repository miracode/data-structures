from Queue import Queue


def radix_sort(array):
    """
    Sorts an array of numbers using the least signficant digit radix algorithm.

    Best & Worst Case: O(kn)
    Sort each number into buckets k times.

    """
    # Initialize a dictionary of queues for number buckets
    queue_dict = {'0': Queue(),
                  '1': Queue(),
                  '2': Queue(),
                  '3': Queue(),
                  '4': Queue(),
                  '5': Queue(),
                  '6': Queue(),
                  '7': Queue(),
                  '8': Queue(),
                  '9': Queue()
                  }
    # determine k, the number of passes needed
    k = max([len(str(elem)) for elem in array])
    i = 1
    # run loop while is less than k
    while i <= k:
        for elem in array:
            # place elem in bucket current digit
            try:
                queue_dict[str(elem)[i * -1]].put(elem)
            except IndexError:
                queue_dict['0'].put(elem)
        # update array to be ordered array by dequeueing buckets
        array = []
        for key in range(10):
            while queue_dict[str(key)].qsize():
                array.append(queue_dict[str(key)].get())
        i += 1

    return array


if __name__ == '__main__':
    print radix_sort.func_doc
    array1 = [501, 422, 300, 389, 201]
    assert radix_sort(array1) == [201, 300, 389, 422, 501]
    array2 = [501, 42, 300, 389, 201]
    assert radix_sort(array2) == [42, 201, 300, 389, 501]
    array3 = [500, 40, 11, 2]
    assert radix_sort(array3) == [2, 11, 40, 500]
    print "tests pass"
