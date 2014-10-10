import unittest
import linked_list


""" For each method in a class, implement a test verifying that it works"""


class MyTest(unittest.TestCase):
    def test_node(self):
        """test that node is created"""
        test_vals = [1, 0, None]
        expected = (1, 0, None)
        anode = linked_list.Node(test_vals[0], test_vals[1], test_vals[2])
        actual = (anode.val, anode.ref, anode.ref_to)
        self.assertEqual(expected, actual)

    def test_llist_insert(self):
        """test linked_list.insert method"""
        test_val = 2
        expected = (2, 0)
        tlist = linked_list.Linked_list()
        tlist.insert(test_val)
        actual = (tlist.llist[0].val, tlist.llist[0].ref)
        self.assertEquals(expected, actual)

    def test_llist_init(self):
        """test linked_list initializes to a tuple of nodes"""
        tlist = linked_list.Linked_list(1, 'a')
        actual = (tlist.llist[0].val,
                  tlist.llist[0].ref,
                  tlist.llist[0].ref_to,
                  tlist.llist[1].val,
                  tlist.llist[1].ref,
                  tlist.llist[1].ref_to)
        expected = ('a', 1, 0, 1, 0, None)
        self.assertEquals(expected, actual)

    def test_size(self):
        tlist = linked_list.Linked_list(1, 'a', 100)
        expected = 3
        actual = tlist.size
        self.assertEquals(expected, actual)


if __name__ == '__main__':
    unittest.main()
