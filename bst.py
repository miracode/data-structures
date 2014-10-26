"""Binary Search Tree"""
class BinaryNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def insert(self, val):
        leaf = BinaryNode(val)
        if self.root == None:
            self.root = leaf
        elif val < self.root.value:
            self.left = leaf
        elif val > self.root.value:
            self.right = leaf


    def contains(self, val):
        pass

    def size(self):
        pass

    def depth(self):
        pass

    def balance(self):
        pass
