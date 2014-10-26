import unittest
import bst


class BSTTest(unittest.TestCase):
    def test_insert_first(self):
        first_val = 9
        test_bst = bst.BinarySearchTree()
        test_bst.insert(first_val)
        expected = (9, None, None)
        actual = (test_bst.value, test_bst.left, test_bst.right)
        self.assertEquals(expected, actual)

    def test_insert_two(self):
        first_val = 9
        second_val = 7
        test_bst = bst.BinarySearchTree()
        test_bst.insert(first_val)
        test_bst.insert(second_val)
        expected = (9, None, 7, None, None)
        actual = (test_bst.value, test_bst.right,
                  test_bst.left.value, test_bst.left.left,
                  test_bst.left.right)
        self.assertEquals(expected, actual)

    def test_insert_three1(self):
        first_val = 9
        second_val = 7
        third_val = 12
        test_bst = bst.BinarySearchTree()
        test_bst.insert(first_val)
        test_bst.insert(second_val)
        test_bst.insert(third_val)
        expected = (9, 7, None, None, 12, None, None)
        actual = (test_bst.value, test_bst.left.value, test_bst.left.left,
                  test_bst.left.right, test_bst.right.value,
                  test_bst.right.left, test_bst.right.right)
        self.assertEquals(expected, actual)

    def test_insert_three2(self):
        first_val = 12
        second_val = 9
        third_val = 7
        test_bst = bst.BinarySearchTree()
        test_bst.insert(first_val)
        test_bst.insert(second_val)
        test_bst.insert(third_val)
        expected1 = (12, None)
        actual1 = (test_bst.value, test_bst.right)
        self.assertEquals(expected1, actual1)
        expected2 = (9, None)
        actual2 = (test_bst.left.value, test_bst.left.right)
        self.assertEquals(expected2, actual2)
        expected3 = (7, None, None)
        actual3 = (test_bst.left.left.value, test_bst.left.left.left,
                   test_bst.left.left.right)
        self.assertEquals(expected3, actual3)

    def test_insert_many(self):
        vals = [12, 2, 7, 14, 9]
        test_bst = bst.BinarySearchTree()
        for val in vals:
            test_bst.insert(val)
        expected = (12, 2, None, 7, 9, None, None, 14, None, None)
        actual = (test_bst.value, test_bst.left.value, test_bst.left.left,
                  test_bst.left.right.value, test_bst.left.right.right.value,
                  test_bst.left.right.right.left,
                  test_bst.left.right.right.right,
                  test_bst.right.value, test_bst.right.left,
                  test_bst.right.right)
        self.assertEquals(actual, expected)

    def test_contain_small_tree(self):
        vals = [12, 9, 14]
        test_bst = bst.BinarySearchTree()
        for val in vals:
            test_bst.insert(val)
        actual_true = test_bst.contains(9)
        actual_false = test_bst.contains(1)
        self.assertEquals(actual_true, True)
        self.assertEquals(actual_false, False)

    def test_contain_big_tree(self):
        vals = [12, 2, 7, 14, 9]
        test_bst = bst.BinarySearchTree()
        for val in vals:
            test_bst.insert(val)
        actual_true = test_bst.contains(9)
        actual_false = test_bst.contains(1)
        self.assertEquals(actual_true, True)
        self.assertEquals(actual_false, False)

    def test_size(self):
        vals1 = [12, 9, 14]
        vals2 = [12, 2, 7, 14, 9]
        test_bst1 = bst.BinarySearchTree()
        test_bst2 = bst.BinarySearchTree()
        for val in vals1:
            test_bst1.insert(val)
        for val in vals2:
            test_bst2.insert(val)
        actual1 = test_bst1.size()
        actual2 = test_bst2.size()
        self.assertEquals(actual1, 3)
        self.assertEquals(actual2, 5)

    def test_depth(self):
        vals1 = [12, 9, 14]
        vals2 = [12, 2, 7, 14, 9]
        test_bst1 = bst.BinarySearchTree()
        test_bst2 = bst.BinarySearchTree()
        for val in vals1:
            test_bst1.insert(val)
        for val in vals2:
            test_bst2.insert(val)
        expected1 = 2
        expected2 = 4
        actual1 = test_bst1.depth()
        actual2 = test_bst2.depth()
        self.assertEquals(actual1, expected1)
        self.assertEquals(actual2, expected2)


