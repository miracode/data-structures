
class Node:
    def __init__(self):
        self.val = None
        self.ref = None


class Queue:
    def __init__(self):
        self.first_n = Node()

    def enqueue(self, val):
        if (self.first_n.val, self.first_n.ref) == (None, None):
            self.first_n.val = val
        else:
            current = self.first_n
            while current.ref is not None:
                current = current.ref
            last_node = Node()
            last_node.val = val
            current.ref = last_node

    def dequeue(self):
        if (self.first_n.val, self.first_n.ref) == (None, None):
            raise IndexError('Queue is empty, cannot dequeue.')
        else:
            dequeue_node = self.first_n
            self.first_n = self.first_n.ref
            return dequeue_node

    def size(self):
        if (self.first_n.val, self.first_n.ref) == (None, None):
            return 0
        else:
            size_count = 1
            current = self.first_n
            while current.ref is not None:
                size_count += 1
                current = current.ref
            return size_count
