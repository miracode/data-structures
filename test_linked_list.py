import unittest
import linked_list
from StringIO import StringIO
import sys


""" For each method in a class, implement a test verifying that it works"""


class MyTest(unittest.TestCase):
    def test_node(self):
        """test that node is created"""
        anode = linked_list.Node(1, None)
        actual = (anode.val, anode.ref_to)
        expected = (1, None)
        self.assertEqual(expected, actual)

    def test_llist_insert(self):
        """test linked_list.insert method"""
        tlist = linked_list.Linked_list()
        tlist.insert(2)
        actual = (tlist.first_n.val, tlist.first_n.ref_to)
        expected = (2, None)
        self.assertEquals(expected, actual)

    def test_llist_init(self):
        """test linked_list initializes to a tuple of nodes"""
        tlist = linked_list.Linked_list(1, 'a')
        actual = (tlist.first_n.val, tlist.first_n.ref_to.val)
        expected = (1, 'a')
        self.assertEquals(expected, actual)

    def test_size(self):
        """test that size of linked list is correct"""
        tlist = linked_list.Linked_list(1, 'a', 100)
        expected = 3
        actual = tlist.size
        self.assertEquals(expected, actual)

    def test_search(self):
        """test that search returns correct node"""
        tlist = linked_list.Linked_list(1, 3, 'a')
        s_node = tlist.search(3)
        actual = (s_node.val)
        #expected = (3, 1, 0)
        self.assertEquals(3, actual)

    def test_pop(self):
        """test that pop returns and removes first node"""
        tlist = linked_list.Linked_list(1, 3, 5)
        r_pop = tlist.pop().val
        actual = (r_pop, tlist.first_n.val)
        expected = (1, 3)
        self.assertEquals(expected, actual)

    def setUp(self):
        """set up to capture print statement"""
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_print(self):
        """test that lprint prints nodes as tuple literal"""
        tlist = linked_list.Linked_list(1, 'b', 1.0)
        expected = "(1, 'b', 1.0)"
        tlist.lprint()
        actual = sys.stdout.getvalue().strip()  # gets printed val & strips /n
        self.assertEquals(expected, actual)

    def test_remove(self):
        """test that node is removed"""
        tlist = linked_list.Linked_list(1, 'node', 40, 1.0, 'apple')
        tlist.remove(tlist.first_n.ref_to)  # remove 'node' node
        tlist.remove(tlist.search('apple'))  # rmv last node
        tlist.remove(tlist.first_n)  # remove first node
        expected = "(40, 1.0)"
        tlist.lprint()
        actual = sys.stdout.getvalue().strip()
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()
