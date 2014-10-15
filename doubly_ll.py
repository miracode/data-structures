"""Create a doubly linked list data stucture"""


class Node:
    def __init__(self):
        self.prev = None
        self.next = None
        self.data = None


class Doubly_LL:
    def __init__(self):
        self.first_n = None
        self.last_n = None

    def insert(self, val):
        if self.first_n is None and self.last_n is None:
            new_n = Node()
            new_n.data = val
            self.first_n = new_n
            self.last_n = new_n
        #else:
        #    new_n = Node()
        #    new_n.data = val
        #    if self.first_n.next is None:
        #        self.first_n.
        #    self.first_n = new_n
