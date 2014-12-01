import unittest
import bst


class BSTTest(unittest.TestCase):
    def test_insert_first(self):
        first_val = 9
        test_bst = bst.BinarySearchTree()
        test_bst.insert(first_val)
        expected = (9, None, None, None)
        actual = (test_bst.value, test_bst.left, test_bst.right,
                  test_bst.parent)
        self.assertEquals(expected, actual)

    def test_insert_two(self):
        first_val = 9
        second_val = 7
        test_bst = bst.BinarySearchTree()
        test_bst.insert(first_val)
        test_bst.insert(second_val)
        expected = (9, None, 7, None, None, 9)
        actual = (test_bst.value, test_bst.right,
                  test_bst.left.value, test_bst.left.left,
                  test_bst.left.right, test_bst.left.parent.value)
        self.assertEquals(expected, actual)

    def test_insert_three1(self):
        #  9
        # / \
        #7   12
        first_val = 9
        second_val = 7
        third_val = 12
        test_bst = bst.BinarySearchTree()
        test_bst.insert(first_val)
        test_bst.insert(second_val)
        test_bst.insert(third_val)
        expected = (9, 7, None, None, 12, None, None, 9, 9)
        actual = (test_bst.value, test_bst.left.value, test_bst.left.left,
                  test_bst.left.right, test_bst.right.value,
                  test_bst.right.left, test_bst.right.right,
                  test_bst.right.parent.value, test_bst.left.parent.value)
        self.assertEquals(expected, actual)

    def test_insert_three2_self_balance(self):
        #     12
        #      \
        #       13
        #        \
        #         14
        # SELF BALANCE =>
        #   13
        #  / \
        # 12  14
        first_val = 12
        second_val = 13
        third_val = 14
        test_bst = bst.BinarySearchTree()
        test_bst.insert(first_val)
        test_bst.insert(second_val)
        test_bst.insert(third_val)
        print test_bst.value, test_bst.left.value, test_bst.left.left
        expected = (13, 12, None, None, 14, None, None, 13, 13)
        actual = (test_bst.value, test_bst.left.value, test_bst.left.left,
                  test_bst.left.right, test_bst.right.value,
                  test_bst.right.left, test_bst.right.right,
                  test_bst.right.parent.value, test_bst.left.parent.value)
        self.assertEquals(actual, expected)

    def test_insert_three3_self_balance(self):
        #     12
        #     /
        #    11
        #    /
        #   10
        # SELF BALANCE =>
        #   11
        #  / \
        # 10  12
        first_val = 12
        second_val = 11
        third_val = 10
        test_bst = bst.BinarySearchTree()
        test_bst.insert(first_val)
        test_bst.insert(second_val)
        test_bst.insert(third_val)
        print test_bst.value, test_bst.left.value, test_bst.left.left
        expected = (11, 10, None, None, 12, None, None, 11, 11)
        actual = (test_bst.value, test_bst.left.value, test_bst.left.left,
                  test_bst.left.right, test_bst.right.value,
                  test_bst.right.left, test_bst.right.right,
                  test_bst.right.parent.value, test_bst.left.parent.value)
        self.assertEquals(actual, expected)

    def test_insert_many_self_balance(self):
        #     12
        #    / \
        #   10   13
        #   /\
        #  9 11
        # /
        # 8
        # SELF BALANCE =>
        #     10
        #    / \
        #   9   12
        #  /   / \
        # 8   11  13
        vals = (12, 13, 10, 11, 9, 8)
        test_bst = bst.BinarySearchTree()
        for val in vals:
            test_bst.insert(val)
        self.assertEquals(3, test_bst.depth())
        self.assertEquals(10, test_bst.value)
        self.assertEquals(8, test_bst.left.left.value)

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
        #    12             12
        #   /  \           /  \
        #  9    14        2    14
        #                / \   / \
        #               1   7 13  15
        #                  / \
        #                 6   9
        vals1 = [12, 9, 14]
        vals2 = [12, 2, 7, 14, 9, 6, 1, 13, 15]
        test_bst1 = bst.BinarySearchTree()
        test_bst2 = bst.BinarySearchTree()
        for val in vals1:
            test_bst1.insert(val)
        for val in vals2:
            test_bst2.insert(val)
        actual1 = test_bst1.size()
        actual2 = test_bst2.size()
        self.assertEquals(actual1, 3)
        self.assertEquals(actual2, 9)

    def test_depth(self):
        #    12             12
        #   /  \           /  \
        #  9    14        2    14
        #                / \   / \
        #               1   7 13  15
        #                  / \
        #                 6   9
        vals1 = [12, 9, 14]
        vals2 = [12, 2, 7, 14, 9, 6, 1, 13, 15]
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

    def test_balance_even(self):
        #    12
        #   /  \
        #  9    14
        vals1 = [12, 9, 14]
        test_bst1 = bst.BinarySearchTree()
        for val in vals1:
            test_bst1.insert(val)
        bal = test_bst1.balance()
        self.assertEquals(bal, 0)
        more_vals = [10, 2, 13, 17]
        for val in more_vals:
            test_bst1.insert(val)
        bal = test_bst1.balance()
        self.assertEquals(bal, 0)

    def test_unbalanced(self):
        #  12
        #  /
        # 9
        vals = [12, 9]
        test_bst = bst.BinarySearchTree()
        for val in vals:
            test_bst.insert(val)
        bal = test_bst.balance()
        self.assertEquals(bal, 1)

    # def test_delete_node_no_children(self):
    #     test_bst = bst.BinarySearchTree()
    #     val = 12
    #     test_bst.insert(val)
    #     test_bst.delete(val)
    #     assert test_bst.value is None
    #     test_bst2 = bst.BinarySearchTree()
    #     vals = [12, 9]
    #     for val in vals:
    #         test_bst2.insert(val)
    #     test_bst2.delete(9)
    #     assert test_bst2.left is None
    #     vals = [9, 14, 15]
    #     for val in vals:
    #         test_bst2.insert(val)
    #     test_bst2.delete(15)
    #     assert test_bst2.right.right is None
    #     assert test_bst2.contains(15) is False

    # def test_delete_node_one_child(self):
    #     test_bst = bst.BinarySearchTree()
    #     vals = [12, 9, 2]
    #     for val in vals:
    #         test_bst.insert(val)
    #     test_bst.delete(9)
    #     assert test_bst.contains(9) is False
    #     test_bst.delete(12)
    #     self.assertEquals(test_bst.value, 2)

    # def test_delete_node_two_children(self):
    #     test_bst = bst.BinarySearchTree()
    #     vals = [9, 12, 2]
    #     for val in vals:
    #         test_bst.insert(val)
    #     test_bst.delete(9)
    #     assert test_bst.contains(9) is False
    #     assert test_bst.value == 2
    #     assert test_bst.left is None
    #     assert test_bst.right.value == 12

    # def test_delete_node_two_children2(self):

    #     #        20
    #     #         \
    #     #          40
    #     #         /  \
    #     #            60
    #     # REBAL >
    #     #       40
    #     #      /  \
    #     #     20   60
    #     #      \    / \
    #     #      30  50  70
    #     #      / \
    #     #     25  35

    #     test_bst = bst.BinarySearchTree()
    #     vals = [20, 40, 60, 30, 50, 70, 25, 35]
    #     for val in vals:
    #         test_bst.insert(val)
    #     test_bst.delete(40)
    #     assert test_bst.contains(40) is False
    #     assert test_bst.value == 35

    def test_delete_rebalance_no_children(self):
        #          20
        #         /  \
        #        15   25
        #       /
        #      10
        vals = [20, 15, 25, 10]
        test_bst = bst.BinarySearchTree()
        for val in vals:
            test_bst.insert(val)
        test_bst.delete(25)
        self.assertEquals(15, test_bst.value)

    def test_delete_rebalance_one_child(self):
        #          20
        #         /  \
        #        15   25
        #       /     /\
        #      10    24 26
        #                \
        #                 27
        vals = [20, 15, 25, 10, 26, 24, 27]
        test_bst = bst.BinarySearchTree()
        for val in vals:
            print val
            test_bst.insert(val)
        self.assertTrue(test_bst.contains(25))
        test_bst.delete(15)
        #         25
        #        /  \
        #       20  26
        #       /     \
        #      10     27
        self.assertEquals(25, test_bst.value)
