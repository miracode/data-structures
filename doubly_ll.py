"""Create a doubly linked list data stucture"""


class Node:
    def __init__(self):
        self.prev = None
        self.next = None
        self.data = None


class Doubly_LL:
    def __init__(self):
        self.first_n = Node()
        self.last_n = Node()

    def insert(self, val):
        if (self.first_n.prev, self.first_n.next, self.first_n.data) == (
                None, None, None):
            self.first_n.data = val
            self.last_n = self.first_n
        #else:
        #    self.first_n = Node(None, val, self.first_n)
