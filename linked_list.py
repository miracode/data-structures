#!/usr/bin/env python

"""Creates a singly linked list"""


class Node(object):

    def __init__(self, val, ref_to):
        self.val = val
        self.ref_to = ref_to


class Linked_list(object):

    def __init__(self, *args):
        self.size = 0
        #self.llist = ()
        self.first_n = None
        # reverse args since they are inserted in reverse
        args = args[::-1]
        for arg in args:
            self.insert(arg)

    def pop(self):
        """Remove first node of linked list"""
        x = self.first_n
        self.first_n = self.first_n.ref_to
        return x

    def insert(self, val):
        """Insert a value to the head of a linked list"""
        new_n = Node(val, self.first_n)
        self.first_n = new_n
        self.size += 1

    def size(self):
        """Return the size of the linked list"""
        return self.size

    def search(self, val):
        """Return node containing value in linked list"""
        n = self.first_n
        while True:
            if n.val == val:
                return n
            n = n.ref_to
        return None

    def remove(self, node):
        """Remove specified node from linked list"""
        if self.first_n == node:
            self.first_n = self.first_n.ref_to
        else:
            c_node = self.first_n.ref_to
            prev = self.first_n

            while True:
                if c_node == node:
                    prev.ref_to = c_node.ref_to
                    break
                prev = c_node
                c_node = c_node.ref_to

    def lprint(self):
        """Print entire linked list as a tuple literal"""
        # hint use a __ function
        n = self.first_n
        ll_tuple = ()
        while n:
            ll_tuple = ll_tuple + (n.val, )
            n = n.ref_to
        print ll_tuple
