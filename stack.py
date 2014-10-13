from linked_list import Node

"""Create a stack data structure"""


class Stack(object):

    def __init__(self):
        self.first_n = None

    def push(self, data):
        self.first_n = Node(data, self.first_n)
