from linked_list import Node

"""Create a stack data structure with same node class as LinkedList"""


class Stack(object):

    def __init__(self):
        self.top_node = None

    def push(self, data):
        self.top_node = Node(data, self.top_node)

    def pop(self):
        if not self.top_node:
            raise IndexError('Stack is empty, cannot pop value.')
        node = self.top_node
        self.top_node = self.top_node.next
        return node

    def peek(self):
        if not self.top_node:
            raise IndexError('Stack is empty, cannot peek value.')
        return self.top_node.data
