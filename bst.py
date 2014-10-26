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
        pass