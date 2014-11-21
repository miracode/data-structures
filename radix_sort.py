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
    # i = len(str(array[0])) - 1
    i = 1
    # run loop while is less than last element's length
    while i <= len(str(array[-1])):
        print array
        for elem in array:
            # place elem in bucket current digit
            try:
                queue_dict[str(elem)[i * -1]].put(elem)
            except IndexError:
                queue_dict['0'].put(elem)
                print i
        # update array to be ordered array
        array = []
        for key in range(10):
            while queue_dict[str(key)].qsize():
                array.append(queue_dict[str(key)].get())
        print array
        i += 1
        print i

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
    
