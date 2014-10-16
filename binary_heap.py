"""Implementation of a Binary Heap"""


class MaxBinaryHeap:

    def __init__(self, in_array=None):
        self.h_array = [None]
        self.length = 0
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
        # increase length by 1
        self.length += 1

    def mh_pop(self):
        p_val = self.h_array[1]
        # replace root with last element
        self.h_array[1] = self.h_array.pop()
        #compare to children
        index = 1
        largest = index
        left = 2 * largest
        right = 2 * largest + 1
        if left <= self.length and self.h_array[left] > self.h_array[largest]:
            largest = left
        if right <= self.length and self.h_array[right] > \
                self.h_array[largest]:
            largest = right
        if largest != index:
            self.h_array[largest], self.h_array[index] = \
                self.h_array[index], self.h_array[largest]

        return p_val
