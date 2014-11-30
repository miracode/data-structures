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
        self.balance_factor = 0

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
                # and update balance factor of parent
                if not self.left:
                    self.left = leaf
                    self._update_balance(self.left)
                # otherwise, recursively use insert to place in left BST
                else:
                    self.left.insert(val)

            elif val > self.value:
                if not self.right:
                    self.right = leaf
                    self._update_balance(self.right)
                else:
                    self.right.insert(val)

    def _update_balance(self, node):
        # if node.balance_factor != 0:
        #     self._rebalance(node)
        if node.parent:
            # if new leaf is a left child, parent gets +1 bal factor
            if node == node.parent.left:
                node.parent.balance_factor += 1
            # if new leaf is right child, parent gets -1 bal factor
            elif node == node.parent.right:
                node.parent.balance_factor -= 1

            # if the parent is now unbalanced, update grandparent bal factor
            if node.parent.balance_factor != 0:
                self._update_balance(node.parent)

    # def _rebalance(self, node):
    #     pass

    # def _rotate_left(self, node):
    #     new_root = node.right
    #     node.right = new_root.left
    #     temp_parent = node.parent
    #     node.parent = temp_parent.parent
    #     node.right = temp_parent
    #     node.right.parent = node
    #     node.right.left = None

    # def _rotate_right(self, node):
    #     temp_parent = node.parent
    #     node.parent = temp_parent.parent
    #     node.left = temp_parent
    #     node.left.parent = node
    #     node.left.right = None


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
        """
        Return 0 for a balanced tree, otherwise a positive or negative
        integer indicating the imbalance to the left or right, respectively

        balance = height(left_subtree) - height(right_subtree)
        """
        left_depth = 0
        right_depth = 0

        if self.left:
            left_depth = self.left.depth()
        if self.right:
            right_depth = self.right.depth()

        return (left_depth - right_depth)

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
