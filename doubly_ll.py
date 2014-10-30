"""Create a doubly linked list data stucture"""


class Node:
    def __init__(self):
        self.prev = None
        self.next = None
        self.data = None


class DoublyLinkedList:
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def init_node(self, val):
        """Initialize a node"""
        new_node = Node()
        new_node.data = val
        return new_node

    def _init_first_node(self, new_node):
        """Create the first node in list after initialized"""
        self.first_node = new_node
        self.last_node = new_node

    def insert(self, val):
        """Add node with value to beginning of the list"""
        new_node = self.init_node(val)
        if self.first_node is None and self.last_node is None:
            self._init_first_node(new_node)
        else:
            new_node.next = self.first_node
            self.first_node.prev = new_node
            if self.first_node.next is None:
                self.last_node = self.first_node
            self.first_node = new_node

    def append(self, val):
        """Add node with value to end of the list"""
        new_node = self.init_node(val)
        if self.first_node is None and self.last_node is None:
            self._init_first_node(new_node)
        else:
            new_node.prev = self.last_node
            self.last_node.next = new_node
            if self.last_node.prev is None:
                self.first_node = self.last_node
            self.last_node = new_node

    def pop(self):
        """Removes and returns first node in list"""
        if self.first_node is None:
            raise IndexError(u"List is emtpy, cannot pop value")
        else:
            x = self.first_node
            self.first_node = self.first_node.next
            return x

    def shift(self):
        """Removes and returns last node in list"""
        if self.first_node is None:
            raise IndexError(u"List is emtpy, cannot shift value")
        else:
            x = self.last_node
            self.last_node = self.last_node.prev
            return x

    def remove(self, val):
        """Removes first node from the list with value"""
        if self.first_node is None:
            raise IndexError(u"List is emtpy, cannot remove value")
        current = self.first_node
        while current.data != val:
            current = current.next
            if current is None:
                raise ValueError(u"Value not in list")
        if current.prev is None:
            self.first_node = self.first_node.next
        elif current.next is None:
            self.last_node = self.last_node.prev
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
