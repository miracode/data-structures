"""Implementation of a Binary Heap"""


class MaxBinaryHeap:
    def __init__(self, h_array=[None]):
        self.h_array = h_array

    def insert(self, val):
        self.h_array = self.h_array + [val]
