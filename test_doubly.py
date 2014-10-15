import doubly_ll
import unittest


class MyTest(unittest.TestCase):

    def test_insert_one(self):
        """test that insert will insert val at head of list"""
        val = 5
        test_dll = doubly_ll.Doubly_LL()
        test_dll.insert(val)
        act_first_n = (test_dll.first_n.data, test_dll.first_n.prev,
                       test_dll.first_n.next)
        act_last_n = (test_dll.last_n.data, test_dll.last_n.prev,
                      test_dll.last_n.next)
        expected_n = (5, None, None)
        self.assertEquals(act_first_n, expected_n)
        self.assertEquals(act_last_n, expected_n)

    #def def_insert_two(self):
    #    val1, val2 = 2, 'a'
    #    test_dll = doubly_ll.Doubly_LL()
    #    test_dll.insert(val1)
    #    test_dll.insert(val2)
