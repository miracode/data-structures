"""
Create a priority queue 

Priority queue handles lower numbers as higher priority
Values with same priority will be returned in order of queueing
"""

class PriorityQ:
    def __init__(self):
        self.heap = []