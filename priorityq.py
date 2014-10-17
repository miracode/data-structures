"""
Create a priority queue

Priority queue handles lower numbers as higher priority
Values with same priority will be returned in order of queueing
"""


class PriorityQ(object):

    def __init__(self):
        self.harray = [[None]]

    def insert(self, priority, value):
        """Insert value to heap based on priority"""
        # if priority already in heap, add value to end of priority's list
        found = False
        for val in self.harray:
            if val[0] == priority:
                found = True
                val.append(value)
                break
        if not found:
            # insert to end of list
            self.harray.append([priority, value])
            # find value index and parent index
            vindex = len(self.harray) - 1
            pindex = vindex / 2
            # compare priority with parent priority
            while self.harray[pindex][0] > self.harray[vindex][0]:
                if self.harray[pindex][0] is None:
                    break
                else:
                    # swap when not in right order
                    self.harray[pindex], self.harray[vindex] = \
                        self.harray[vindex], self.harray[pindex]
                    vindex = pindex
                    pindex = vindex / 2

    def pop(self):
        popval = self.harray[1][1]
        # if there are multiple values with the same priority, 
        # pop from priority list
        if len(self.harray[1]) > 2:
            self.harray[1].remove(popval)
        # if only one value, replace root with last element
        elif len(self.harray[1]) == 2:
            self.harray[1] = self.harray.pop()
            index = 1
            while True:
                smallest = index
                left = 2 * smallest
                right = 2 * smallest + 1
                if left <= len(self.harray) - 1 and self.harray[left][0] < \
                        self.harray[smallest][0]:
                    smallest = left
                if right <= len(self.harray) - 1 and self.harray[right][0] < \
                        self.harray[smallest][0]:
                    smallest = right
                if smallest != index:
                    newindex = smallest
                    self.harray[smallest], self.harray[index] = \
                        self.harray[index], self.harray[smallest]
                    index = newindex
                else:
                    break
        return popval

