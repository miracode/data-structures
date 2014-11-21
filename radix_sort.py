from Queue import Queue


def radix_sort(array):
    """
    Sorts an array of numbers of the same length using the least signficant
    digit radix algorithm.
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
    i = len(str(array[0]))
    while i >= 0:
        for elem in array:
            # place elem in bucket current digit
            try:
                queue_dict[str(elem)[-1 * i]].put(elem)
            except IndexError:
                print "%s is not long enough to sort" % str(elem)
        # update array to be ordered array
        array = []
        for key in range(10):
            while queue_dict[str(key)].qsize():
                array.append(queue_dict[str(key)].get())
        i -= 1

    return array


if __name__ == '__main__':
    print radix_sort.func_doc
    array1 = [501, 422, 300, 389, 201]
    assert radix_sort(array1) == [201, 300, 389, 422, 501]
    print "tests pass"
    array1 = [501, 42, 300, 389, 201]
    radix_sort(array1)
