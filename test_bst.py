import unittest
import bst


class BSTTest(unittest.TestCase):
    def test_insert_first(self):
        first_val = 9
        test_bst = bst.BinarySearchTree()
        test_bst.insert(first_val)
        expected = (9, None, None)
        actual = (test_bst.root.value, test_bst.root.left, test_bst.root.right)
        self.assertEquals(expected, actual)
