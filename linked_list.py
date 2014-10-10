#!/usr/bin/env python

"""Implement a linked list.

Should support the following methods:
insert(val)
pop()
size()
search(val)
remove(node)
print()

Do not use the Python list type to solve the problem."""


class Node(object):

    def __init__(self, val, ref, ref_to):
        self.val = val
        self.ref = ref
        self.ref_to = ref_to


class Linked_list(object):
    i = 0  # First ref

    def __init__(self, *args):
        self.size = 0
        self.llist = (self.insert(arg) for arg in args)
        #for arg in args:
        #   self.insert(arg)

    def pop(self):
        """Remove first node of linked list"""
        pass

    def insert(self, val):
        """Insert a value to the head of a linked list"""
        try:
            head_ref = self.llist[0].ref
        except TypeError:
            head_ref = None
        self.llist = (Node(val, self.i, head_ref), self.llist)
        self.i += 1
        self.size += 1

    def size(self):
        """Return the size of the linked list"""
        return self.size

    def search(self, val):
        """Return index of value in linked list"""
        i = 0
        for x in self.linked:
            if x == val:
                return i
            i += 1
            return "Value does not exist in linked list"

    def remove(self, node):
        """Remove specified node from linked list"""
        pass

    def lprint(self):
        """Print entire linked list as a tuple literal"""
        # hint use a __ function
        pass
