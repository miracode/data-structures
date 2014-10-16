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
        # swap if not in right order
        while self.h_array[parent_index] < self.h_array[val_index]:
            if self.h_array[parent_index] is None:
                break
            else:
                self.h_array[parent_index], self.h_array[val_index] = \
                    self.h_array[val_index], self.h_array[parent_index]
                val_index = parent_index
                parent_index = val_index / 2


    def mh_pop(self):
        p_val = self.h_array[1]
        # replace root with last element
        self.h_array[1] = self.h_array.pop()
        #compare to children
        #largest = 1
        #left = 2 * largest
        #right = 2 * largest + 1

        return p_val
