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

        # if the BST is empty, place value at top.
        if not self.value:
            self.value = val

        else:
            leaf = BinarySearchTree(val)
            leaf.parent = self

            if val < self.value:
                # if the leaf is None, place new leaf there
                if not self.left:
                    self.left = leaf
                # otherwise, recursively use insert to place in left BST
                else:
                    self.left.insert(val)

            elif val > self.value:
                if not self.right:
                    self.right = leaf
                else:
                    self.right.insert(val)

            # balance bst around leaf
            # while leaf.parent:
            #     if leaf == leaf.parent.left:
            #         if


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

    def balance(self, top=None):
        """Return 0 for a balanced tree, otherwise a positive or negative
        integer indicating the imbalance to the left or right, respectively"""
        if not top:
            top = self
        count_left = 0
        count_right = 0
        # current value
        if top.value:
            if top.left:
                count_left += (1 - top.left.balance())
            # right node
            if top.right:
                count_right += 1 + top.right.balance()
        diff = count_right - count_left
        return diff

    def delete(self, val, parent_side=None):
        if not self.value:
            return ValueError("%s not in emtpy BST" % (val, ))

        elif val == self.value:
            # delete node
            if self.parent is None:
                self.value = None
            elif not self.left and not self.right:
                if parent_side == 'left':
                    self.parent.left = None
                elif parent_side == 'right':
                    self.parent.right = None
            elif not self.left:
                if parent_side == 'left':
                    self.parent.left = self.right
                elif parent_side == 'right':
                    self.parent.right = self.right
            elif not self.right:
                if parent_side == 'left':
                    self.parent.left = self.left
                elif parent_side == 'right':
                    self.parent.right = self.left
            else:
                # replace with largest of left node's children
                #### determine max left value
                repl_val = self._max_left_val(self.left)
                #### delete max left value (no children)
                self.delete(repl_val)
                #### replace current val with max val
                self.value = repl_val

        # Otherwise, check subsequent BTs
        elif val < self.value:
            if not self.left:
                return ValueError("%s not in BST" % (val, ))
            else:
                # keep checking
                self.left.delete(val, parent_side='left')
        elif val > self.value:
            if not self.right:
                return ValueError("%s not in BST" % (val, ))
            else:
                self.right.delete(val, parent_side='right')
        else:
            return ValueError("%s not in BST" % (val, ))

    def _max_left_val(self, node):
        if node.right is None:
            return node.value
        else:
            return self._max_left_val(node.right)
