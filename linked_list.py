#!/usr/bin/env python

"""Creates a singly linked list"""


class Node(object):

    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList(object):

    def __init__(self, *args):
        self.size = 0
        self.first_node = None
        # reverse args since they are inserted in reverse
        args = args[::-1]
        for arg in args:
            self.insert(arg)

    def pop(self):
        """Remove first node of linked list"""
        x = self.first_node
        self.first_node = self.first_node.next
        return x

    def insert(self, data):
        """Insert a data to the head of a linked list"""
        new_node = Node(data, self.first_node)
        self.first_node = new_node
        self.size += 1

    def size(self):
        """Return the size of the linked list"""
        return self.size

    def search(self, data):
        """Return node containing data in linked list"""
        n = self.first_node
        while True:
            if n.data == data:
                return n
            n = n.next
        return None

    def remove(self, data):
        """Remove first node with matching data in linked list"""
        node = self.first_node
        if node.data == data:
            self.first_node = self.first_node.next
            return self
        while node.next:
            if node.next.data == data:
                node.next = node.next.next
                return self
            node = node.next

    def print_tuple(self):
        """Print entire linked list as a tuple literal"""
        # hint use a __ function
        n = self.first_node
        linked_list_tuple = ()
        while n:
            linked_list_tuple = linked_list_tuple + (n.data, )
            n = n.next
        print linked_list_tuple
