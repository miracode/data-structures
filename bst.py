"""Binary Search Tree"""

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def insert(self, val):
        if self.root == None:
            self.root = val
        else:
            leaf = BinarySearchTree()
            leaf.root = val
            if val < self.root:
                self.left = leaf
            elif val > self.root:
                self.right = leaf


    def contains(self, val):
        pass

    def size(self):
        pass

    def depth(self):
        pass

    def balance(self):
        pass
