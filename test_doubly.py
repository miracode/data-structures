import doubly_ll
import unittest


class MyTest(unittest.TestCase):

    def test_insert_one(self):
        """test that insert will insert val at head of list"""
        val = 5
        test_dll = doubly_ll.Doubly_LL()
        test_dll.insert(val)
        self.assertEquals(test_dll.first_n.data, val)
        self.assertEquals(test_dll.first_n.prev, None)
        self.assertEquals(test_dll.first_n.next, None)
