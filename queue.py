"""Implement a queue data structure"""


class Node:
    def __init__(self):
        self.data = None
        self.next = None


class Queue:
    def __init__(self):
        self.first_node = Node()

    def enqueue(self, val):
        if (self.first_node.data, self.first_node.next) == (None, None):
            self.first_node.data = val
        else:
            current = self.first_node
            while current.next is not None:
                current = current.next
            last_node = Node()
            last_node.data = val
            current.next = last_node

    def dequeue(self):
        if (self.first_node.data, self.first_node.next) == (None, None):
            raise IndexError('Queue is empty, cannot dequeue.')
        else:
            dequeue_node = self.first_node
            self.first_node = self.first_node.next
            return dequeue_node

    def size(self):
        if (self.first_node.data, self.first_node.next) == (None, None):
            return 0
        else:
            size_count = 1
            current = self.first_node
            while current.next is not None:
                size_count += 1
                current = current.next
            return size_count
