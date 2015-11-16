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
        if node.balance_factor not in (-1, 0, 1):
            self._rebalance(node)
        elif node.parent:
            # if new leaf is a left child, parent gets +1 bal factor
            if node == node.parent.left:
                node.parent.balance_factor += 1
            # if new leaf is right child, parent gets -1 bal factor
            elif node == node.parent.right:
                node.parent.balance_factor -= 1

            # if the parent is now unbalanced, update grandparent bal factor
            if node.parent.balance_factor != 0:
                self._update_balance(node.parent)

    def _rotate(self, root, side='left'):
        """Rotate BST in the direction corresponding to the side"""
        if side == 'left':
            other_side = 'right'
        elif side == 'right':
            other_side = 'left'

        # Make the root node the child of the other side on the same side
        # (i.e.) for left rotation, root becomes left child of its right child.
        new = BinarySearchTree(root.value)

        # Give new new node values of root.
        setattr(new, side, getattr(root, side))
        if getattr(new, side):
            getattr(new, side).parent = new

        if getattr(getattr(root, other_side), side):
            setattr(new, other_side, getattr(getattr(root, other_side), side))
            getattr(new, other_side).parent = new

        new.parent = root
        new.balance_factor = root.balance_factor

        # Root should now be updated to become child
        root.value = getattr(root, other_side).value
        root.balance_factor = getattr(root, other_side).balance_factor

        setattr(root, other_side, getattr(getattr(root, other_side), other_side))
        if getattr(root, other_side):
            getattr(root, other_side).parent = root

        setattr(root, side, new)

        # Update the balance factor depending on side.
        sign = 1
        if side == 'right':
            sign = -1
        getattr(root, side).balance_factor += sign * (1 - min(root.balance_factor, 0))
        root.balance_factor += sign * (1 + max(getattr(root, side).balance_factor, 0))

    def _rebalance(self, node):
        if node.balance_factor < 0:
            if node.right.balance_factor > 0:
                self._rotate(node.right, side='right')
            self._rotate(node, side='left')
        elif node.balance_factor > 0:
            if node.left.balance_factor < 0:
                self._rotate(node.left, side='left')
            self._rotate(node, side='right')

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

    def delete(self, val, parent_side=None, rotate=True):
        if not self.value:
            return ValueError("%s not in emtpy BST" % (val, ))

        elif val == self.value:
            # delete node
            # if there are no children, change the parent's child to be None
            # (node will have no pointers and will be garbage collected)
            if not self.left and not self.right:
                if not self.parent:
                    self.value = None
                else:
                    if parent_side == 'left':
                        self.parent.left = None
                        self.parent.balance_factor -= 1
                    elif parent_side == 'right':
                        self.parent.right = None
                        self.parent.balance_factor += 1

                    if rotate:
                        self._update_balance(self.parent)

            # otherwise
            # if the child is the right one:
            elif not self.left:
                if not self.parent:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                    self.balance_factor = self.right.balance_factor
                    if self.left:
                        self.left.parent = self
                    if self.right:
                        self.right.parent = self
                    # no need to rebalance, subtree should be balanced
                else:
                    if parent_side == 'left':
                        self.parent.left = self.right
                        self.parent.balance_factor -= 1
                    elif parent_side == 'right':
                        self.parent.right = self.right
                        self.parent.balance_factor += 1
                    if rotate:
                        self._update_balance(self.parent)
            # otherwise, if child is the left one:
            elif not self.right:
                if not self.parent:
                    self.value = self.left.value
                    self.left = self.left.left
                    self.right = self.left.right
                    self.balance_factor = self.left.balance_factor
                    if self.left:
                        self.left.parent = self
                    if self.right:
                        self.right.parent = self
                else:
                    if parent_side == 'left':
                        self.parent.balance_factor
                        self.parent.left = self.left
                        self.parent.balance_factor -= 1
                    elif parent_side == 'right':
                        self.parent.right = self.left
                        self.parent.balance_factor += 1
                    self._update_balance(self.parent)
            # otherwise, node has two children
            else:
                # replace with largest of left node's children
                #### determine max left value
                repl_val = self._max_left_val(self.left)
                #### delete max left value (no children)
                self.delete(repl_val, rotate=False)
                #### replace current val with max val
                self.value = repl_val
                self._update_balance(self)


        # Otherwise, check subsequent BTs
        elif val < self.value:
            if not self.left:
                return ValueError("%s not in BST" % (val, ))
            else:
                # keep checking
                self.left.delete(val, parent_side='left', rotate=rotate)
        elif val > self.value:
            if not self.right:
                return ValueError("%s not in BST" % (val, ))
            else:
                self.right.delete(val, parent_side='right', rotate=rotate)
        else:
            return ValueError("%s not in BST" % (val, ))

    def _max_left_val(self, node):
        if node.right is None:
            return node.value
        else:
            return self._max_left_val(node.right)

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print node.value
            self.in_order_traversal(node.right)

    def pre_order_traversal(self, node):
        if node:
            print node.value
            self.in_order_traversal(node.left)
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            self.in_order_traversal(node.right)
            print node.value
