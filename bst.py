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

    # def _rebalance(self, node):
    #     pass

    def _rotate_left(self, root_node):
        """Rotate left by changing values and pointers."""
        ## make root_node the left child of its right child
        # make a new node for new left child
        new_left = BinarySearchTree(root_node.value)
        # make the left child of the new node the same as what was left of root
        new_left.left = root_node.left
        if new_left.left:
            new_left.left.parent = new_left
        # if the new root node (aka the right child of root node) has a left
        # child it is now the right child of the new left node
        if root_node.right.left:
            new_left.right = root_node.right.left
            new_left.right.parent = new_left
        # the new parent should point back to root node
        new_left.parent = root_node
        new_left.balance_factor = root_node.balance_factor

        # the root node should now reflect the right child
        root_node.value = root_node.right.value
        # update new root's bal factor
        root_node.balance_factor = root_node.right.balance_factor
        # the new right child should be the old right child's right child
        root_node.right = root_node.right.right
        # point the right child at new parent
        if root_node.right:
            root_node.right.parent = root_node
        # this way the root_node's parent can remain untouched.
        # point new root to new left
        root_node.left = new_left

        # update left BF to be old root BF + 1 - min(old_root.right.BF, 0)
        root_node.left.balance_factor += (1 - min(root_node.balance_factor, 0))
        # the new root bal factor should be the new root's bal factor + 1 -
        # the max(old root current bal factor, 0)
        root_node.balance_factor += (1 + max(root_node.left.balance_factor, 0))

    def _rotate_right(self, root_node):
        """Rotate right by changing values and pointers."""
        ## make root_node the left child of its right child
        # make a new node for new right child
        new_right = BinarySearchTree(root_node.value)
        # make the right child of the new node the same as what was
        # right of root
        new_right.right = root_node.right
        if new_right.right:
            new_right.right.parent = new_right
        # if the new root node (aka the left child of root node) has a right
        # child it is now the left child of the new right node
        if root_node.left.right:
            new_right.left = root_node.left.right
            new_right.left.parent = new_right
        # the new parent should point back to root node
        new_right.parent = root_node
        new_right.balance_factor = root_node.balance_factor

        # the root node should now reflect the left child
        root_node.value = root_node.left.value
        # update new root's bal factor
        root_node.balance_factor = root_node.left.balance_factor
        # the new left child should be the old left child's left child
        root_node.left = root_node.left.left
        # point the left child at new parent
        if root_node.left:
            root_node.left.parent = root_node
        # this way the root_node's parent can remain untouched.
        # point new root to new left
        root_node.right = new_right

        # update right BF to be old root BF - 1 - min(old_root.right.BF, 0)
        root_node.right.balance_factor -= (1 - min(root_node.balance_factor, 0))
        # the new root bal factor should be the new root's bal factor - 1 +
        # the max(old root current bal factor, 0)
        root_node.balance_factor -= (1 + max(root_node.right.balance_factor, 0))

    def _rebalance(self, node):
        if node.balance_factor < 0:
            if node.right.balance_factor > 0:
                self._rotate_right(node.right)
            self._rotate_left(node)
        elif node.balance_factor > 0:
            if node.left.balance_factor < 0:
                self._rotate_left(node.left)
            self._rotate_right(node)

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
