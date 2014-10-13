from linked_list import Node

"""Create a stack data structure"""


class Stack(object):

    def __init__(self):
        self.first_n = None

    def push(self, data):
        self.first_n = Node(data, self.first_n)

    def pop(self):
        if self.first_n is None:
            raise IndexError('Stack is empty, cannot pop value.')
        else:
            x = self.first_n
            self.first_n = self.first_n.ref_to
            return x
