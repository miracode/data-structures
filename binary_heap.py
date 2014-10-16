"""Implementation of a Binary Heap"""


class MaxBinaryHeap:

    def __init__(self, in_array=None):
        self.h_array = [None]
        if in_array is not None:
            for val in in_array:
                self.mh_insert(val)


    def mh_insert(self, val):
        # insert val to end of list
        self.h_array.append(val)
        # compare to parent
        val_index = self.h_array.index(val)
        parent_index = val_index / 2
        while self.h_array[parent_index] < self.h_array[val_index]:
            if self.h_array[parent_index] is None:
                break
            else:
                self.h_array[parent_index], self.h_array[val_index] = \
                    self.h_array[val_index], self.h_array[parent_index]
                val_index = parent_index
                parent_index = val_index / 2
