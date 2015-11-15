"""Implement a queue data structure"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def enqueue(self, data):
        node = Node(data)
        if self.last_node:
            self.last_node.next = node
        self.last_node = node
        if not self.first_node:
            self.first_node = self.last_node

    def dequeue(self):
        if not self.first_node:
            raise IndexError('Queue is empty, cannot dequeue.')
        data = self.first_node.data
        self.first_node = self.first_node.next
        if not self.first_node:
            self.last_node = None
        return data

    def size(self):
        if not self.first_node:
            return 0
        else:
            size_count = 1
            current = self.first_node
            while current.next:
                size_count += 1
                current = current.next
            return size_count

    def peek(self):
        if not self.first_node:
            raise IndexError('Queue is empty, cannot peek.')
        return self.first_node.data

    def is_empty(self):
        return self.first_node is None
