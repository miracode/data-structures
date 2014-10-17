"""
Create a priority queue

Priority queue handles lower numbers as higher priority
Values with same priority will be returned in order of queueing
"""


class PriorityQ(object):

    def __init__(self):
        self.harray = []

    def insert(self, priority, value):
        # if priority already in heap, add value to end of priority's list
        found = False
        if self.harray != []:
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
                if self.harray[pindex][0]is None:
                    break
                else:
                    # swap when not in right order
                    self.harray[pindex], self.harray[vindex] = \
                        self.harray[vindex], self.harray[pindex]
                    vindex = pindex
                    pindex = vindex / 2
