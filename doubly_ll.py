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

    def init_node(self, val):
        new_n = Node()
        new_n.data = val
        return new_n

    def first_node(self, new_n):
        self.first_n = new_n
        self.last_n = new_n

    def insert(self, val):
        new_n = self.init_node(val)
        if self.first_n is None and self.last_n is None:
            self.first_node(new_n)
        else:
            new_n.next = self.first_n
            self.first_n.prev = new_n
            if self.first_n.next is None:
                self.last_n = self.first_n
            self.first_n = new_n

    def append(self, val):
        new_n = self.init_node(val)
        if self.first_n is None and self.last_n is None:
            self.first_node(new_n)
