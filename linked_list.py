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

    def __init__(self, val, ref_to):
        self.val = val
        #self.ref = ref
        self.ref_to = ref_to


class Linked_list(object):
    i = 0  # First ref

    def __init__(self, *args):
        self.size = 0
        #self.llist = ()
        self.first_n = None
        # reverse args since they are added in reverse
        args = args[::-1]
        for arg in args:
            self.insert(arg)

    def pop(self):
        """Remove first node of linked list"""
        pass

    def insert(self, val):
        """Insert a value to the head of a linked list"""
        new_n = Node(val, self.first_n)
        self.first_n = new_n
        #try:
        #    #head_ref = self.llist[0].ref
        #    head_ref = self.first.ref
        #except IndexError:
        #    head_ref = None
        ##self.llist = (Node(val, self.i, head_ref), ) + self.llist
        #exec ()
        #self.i += 1
        self.size += 1

    def size(self):
        """Return the size of the linked list"""
        return self.size

    def search(self, val):
        """Return node containing value in linked list"""
        for n in self.llist:
            if n.val == val:
                return n
        return None

    def remove(self, node):
        """Remove specified node from linked list"""
        pass

    def lprint(self):
        """Print entire linked list as a tuple literal"""
        # hint use a __ function
        pass
