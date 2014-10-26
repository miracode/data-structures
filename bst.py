"""Binary Search Tree"""

class BinarySearchTree(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, val):
        leaf = BinarySearchTree(val)
        if self.value is None:
            self.value = val

        if val < self.value:
            if self.left is None:
                self.left = leaf
            else:
                self.left.insert(val)
        elif val > self.value:
            if self.right is None:
                self.right = leaf
            else:
                self.right.insert(val)

    def contains(self, val):
        print self.value, val
        if self.value is None:
            return False
        elif val == self.value:
            return True
        elif val < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(val)
        elif val > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(val)
        else:
            return False

    def size(self):
        pass

    def depth(self):
        pass

    def balance(self):
        pass
