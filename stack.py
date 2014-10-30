from linked_list import Node

"""Create a stack data structure with same node class as LinkedList"""


class Stack(object):

    def __init__(self):
        self.first_node = None

    def push(self, data):
        self.first_node = Node(data, self.first_node)

    def pop(self):
        if self.first_node is None:
            raise IndexError('Stack is empty, cannot pop value.')
        else:
            x = self.first_node
            self.first_node = self.first_node.next
            return x
