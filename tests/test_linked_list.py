import unittest
import linked_list
from StringIO import StringIO
import sys


""" For each method in a class, implement a test verifying that it works"""


class LinkedListTest(unittest.TestCase):
    def test_node(self):
        """test that node is created"""
        anode = linked_list.Node(1, None)
        actual = (anode.data, anode.next)
        expected = (1, None)
        self.assertEqual(expected, actual)

    def test_llist_insert(self):
        """test linked_list.insert method"""
        tlist = linked_list.LinkedList()
        tlist.insert(2)
        actual = (tlist.first_node.data, tlist.first_node.next)
        expected = (2, None)
        self.assertEquals(expected, actual)

    def test_llist_init(self):
        """test linked_list initializes to a tuple of nodes"""
        tlist = linked_list.LinkedList(1, 'a')
        actual = (tlist.first_node.data, tlist.first_node.next.data)
        expected = (1, 'a')
        self.assertEquals(expected, actual)

    def test_size(self):
        """test that size of linked list is correct"""
        tlist = linked_list.LinkedList(1, 'a', 100)
        expected = 3
        actual = tlist.size
        self.assertEquals(expected, actual)

    def test_search(self):
        """test that search returns correct node"""
        tlist = linked_list.LinkedList(1, 3, 'a')
        s_node = tlist.search(3)
        actual = (s_node.data)
        #expected = (3, 1, 0)
        self.assertEquals(3, actual)

    def test_pop(self):
        """test that pop returns and removes first node"""
        tlist = linked_list.LinkedList(1, 3, 5)
        r_pop = tlist.pop().data
        actual = (r_pop, tlist.first_node.data)
        expected = (1, 3)
        self.assertEquals(expected, actual)

    def setUp(self):
        """set up to capture print statement"""
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_print(self):
        """test that print_tuple prints nodes as tuple literal"""
        tlist = linked_list.LinkedList(1, 'b', 1.0)
        expected = "(1, 'b', 1.0)"
        tlist.print_tuple()
        actual = sys.stdout.getvalue().strip()  # gets printed val & strips /n
        self.assertEquals(expected, actual)

    def test_remove(self):
        """test that node is removed"""
        tlist = linked_list.LinkedList(1, 'node', 40, 1.0, 'apple')
        tlist.remove('node')  # remove 'node' node
        tlist.remove('apple')  # rmv last node
        tlist.remove(1)  # remove first node
        expected = "(40, 1.0)"
        tlist.print_tuple()
        actual = sys.stdout.getvalue().strip()
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()
