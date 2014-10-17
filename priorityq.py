"""
Create a priority queue 

Priority queue handles lower numbers as higher priority
Values with same priority will be returned in order of queueing
"""

#from binary_heap import BinaryHeap

class PriorityQ(object):
    def __init__(self):
        self.harray = [None]
        self.length = 0
        