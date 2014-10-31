"""
Binary Search Tree

This is a recursive binary search tree, each node is
also of class BinarySearchTree.
"""


class BinarySearchTree(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, val):
        """Insert a value into the BST"""
        leaf = BinarySearchTree(val)
        leaf.parent = self
        if not self.value:
            self.value = val

        if val < self.value:
            if not self.left:
                self.left = leaf
            else:
                self.left.insert(val)
        elif val > self.value:
            if not self.right:
                self.right = leaf
            else:
                self.right.insert(val)

    def contains(self, val):
        """Return True if BST contains value, otherwise False"""
        if not self.value:
            return False
        elif val == self.value:
            return True
        elif val < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(val)
        elif val > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(val)
        else:
            return False

    def size(self):
        """Return the number of nodes in the BST"""
        count = 0
        # count current value
        if self.value:
            count += 1
        # count left side
        if self.left:
            count += self.left.size()
        # count right side
        if self.right:
            count += self.right.size()

        return count

    def depth(self):
        """Return the depth of the BST"""
        count = 0
        count_left = 0
        count_right = 0
        # current value
        if self.value:
            count += 1
        # left node
        if self.left:
            count_left += self.left.depth()
        # right node
        if self.right:
            count_right += self.right.depth()

        count_max = max(count_left, count_right)
        count += count_max
        return count

    def balance(self):
        """Return 0 for a balanced tree, otherwise a positive or negative
        integer indicating the imbalance to the left or right, respectively"""
        count_left = 0
        count_right = 0
        # current value
        if self.value:
            if self.left:
                count_left += (1 - self.left.balance())
            # right node
            if self.right:
                count_right += 1 + self.right.balance()
        diff = count_right - count_left
        return diff

    def delete(self, val, side=None):
        if not self.value:
            return ValueError("%s not in emtpy BST" % (val, ))

        while val != self.value:
            if val < self.value:
                if not self.left:
                    return ValueError("%s not in BST" % (val, ))
                else:
                    # keep checking
                    self.left.delete(val)
            elif val > self.value:
                if not self.right:
                    return ValueError("%s not in BST" % (val, ))
                else:
                    self.right.delete(val)
            else:
                return ValueError("%s not in BST" % (val, ))

        # elif val == self.value:
        #     # delete node
        #     break
        # elif val < self.value:
        #     if not self.left:
        #         return ValueError("%s not in BST" % (val, ))
        #     else:
        #         # keep checking
        #         self.left.delete(val)
        # elif val > self.value:
        #     if not self.right:
        #         return ValueError("%s not in BST" % (val, ))
        #     else:
        #         self.right.delete(val)
        # else:
        #     return ValueError("%s not in BST" % (val, ))

        # # if no children, node's parent is now None

        # if not self.left and not self.right:
        #     self.parent.right = None
        # elif not self.left:
        #     self.parent.right = self
        if self.parent is None:
            print "no parent"
            self.value = None
        else:
            print "parent is %s" % self.parent
