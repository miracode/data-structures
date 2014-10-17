"""Implementation of a Binary Heap"""


class MaxBinaryHeap:

    def __init__(self, iterable=None, btype='max'):
        self.harray = [None]
        self.length = 0
        if iterable is not None:
            for val in iterable:
                self.mh_insert(val)
        self.btype = btype
        if self.btype not in ['min', 'max']:
            raise ValueError(u"Binary Heap type must be 'max' or 'min'")

    def mh_insert(self, val):
        # insert val to end of list
        self.harray.append(val)
        # compare to parent
        vindex = self.harray.index(val)
        parent = vindex / 2
        # swap if not in right order
        while self.harray[parent] < self.harray[vindex]:
            if self.harray[parent] is None:
                break
            else:
                self.harray[parent], self.harray[vindex] = \
                    self.harray[vindex], self.harray[parent]
                vindex = parent
                parent = vindex / 2
        # increase length by 1
        self.length += 1

    def mh_pop(self):
        popval = self.harray[1]
        # replace root with last element
        self.harray[1] = self.harray.pop()
        # reduce length
        self.length -= 1
        #compare to children
        index = 1
        while True:
            largest = index
            left = 2 * largest
            right = 2 * largest + 1
            if left <= self.length and self.harray[left] > \
                    self.harray[largest]:
                largest = left
            if right <= self.length and self.harray[right] > \
                    self.harray[largest]:
                largest = right
            if largest != index:
                newindex = largest
                self.harray[largest], self.harray[index] = \
                    self.harray[index], self.harray[largest]
                index = newindex
            else:
                break

        return popval
