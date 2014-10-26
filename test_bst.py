import unittest
import bst


class BSTTest(unittest.TestCase):
    def test_insert_first(self):
        first_val = 9
        test_bst = bst.BinarySearchTree()
        test_bst.insert(first_val)
        expected = (9, None, None)
        actual = (test_bst.root, test_bst.left, test_bst.right)
        self.assertEquals(expected, actual)

    def test_insert_two(self):
        first_val = 9
        second_val = 7
        test_bst = bst.BinarySearchTree()
        test_bst.insert(first_val)
        test_bst.insert(second_val)
        expected = (9, None, 7, None, None)
        actual = (test_bst.root, test_bst.right,
                  test_bst.left.root, test_bst.left.left,
                  test_bst.left.right)
        self.assertEquals(expected, actual)
