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

    def test_insert_two(self):
        val1, val2 = 2, 'a'
        test_dll = doubly_ll.Doubly_LL()
        test_dll.insert(val1)
        test_dll.insert(val2)
        act_first_n = (test_dll.first_n.data, test_dll.first_n.prev,
                       test_dll.first_n.next)
        exp_first_n = ('a', None, test_dll.last_n)
        self.assertEquals(act_first_n, exp_first_n)
        act_last_n = (test_dll.last_n.data, test_dll.last_n.prev,
                      test_dll.last_n.next)
        exp_last_n = (2, test_dll.first_n, None)
        self.assertEquals(act_last_n, exp_last_n)

    def test_insert_three(self):
        val1, val2, val3 = 2, 'a', 1.0
        test_dll = doubly_ll.Doubly_LL()
        test_dll.insert(val1)
        test_dll.insert(val2)
        test_dll.insert(val3)
        act_first_n = (test_dll.first_n.data, test_dll.first_n.prev,
                       test_dll.first_n.next)
        act_last_n = (test_dll.last_n.data, test_dll.last_n.prev,
                      test_dll.last_n.next)
        act_second_n = (test_dll.first_n.next.data, test_dll.first_n.next.prev,
                        test_dll.first_n.next.next)
        exp_first_n = (1.0, None, test_dll.last_n.prev)
        exp_last_n = (2, test_dll.first_n.next, None)
        exp_second_n = ('a', test_dll.first_n, test_dll.last_n)
        self.assertEquals(act_first_n, exp_first_n)
        self.assertEquals(act_last_n, exp_last_n)
        self.assertEquals(act_second_n, exp_second_n)

    def test_append_one(self):
        test_dll = doubly_ll.Doubly_LL()
        val = 'p'
        test_dll.append(val)
        act_first_n = (test_dll.first_n.data, test_dll.first_n.prev,
                       test_dll.first_n.next)
        act_last_n = (test_dll.last_n.data, test_dll.last_n.prev,
                      test_dll.last_n.next)
        expected_n = ('p', None, None)
        self.assertEquals(act_first_n, expected_n)
        self.assertEquals(act_last_n, expected_n)

    def test_append_two(self):
        val1, val2 = 'a', 2
        test_dll = doubly_ll.Doubly_LL()
        test_dll.append(val1)
        test_dll.append(val2)
        act_first_n = (test_dll.first_n.data, test_dll.first_n.prev,
                       test_dll.first_n.next)
        exp_first_n = ('a', None, test_dll.last_n)
        self.assertEquals(act_first_n, exp_first_n)
        act_last_n = (test_dll.last_n.data, test_dll.last_n.prev,
                      test_dll.last_n.next)
        exp_last_n = (2, test_dll.first_n, None)
        self.assertEquals(act_last_n, exp_last_n)

    def test_append_three(self):
        val1, val2, val3 = 1.0, 'a', 2
        test_dll = doubly_ll.Doubly_LL()
        test_dll.append(val1)
        test_dll.append(val2)
        test_dll.append(val3)
        act_first_n = (test_dll.first_n.data, test_dll.first_n.prev,
                       test_dll.first_n.next)
        act_last_n = (test_dll.last_n.data, test_dll.last_n.prev,
                      test_dll.last_n.next)
        act_second_n = (test_dll.first_n.next.data, test_dll.first_n.next.prev,
                        test_dll.first_n.next.next)
        exp_first_n = (1.0, None, test_dll.last_n.prev)
        exp_last_n = (2, test_dll.first_n.next, None)
        exp_second_n = ('a', test_dll.first_n, test_dll.last_n)
        self.assertEquals(act_first_n, exp_first_n)
        self.assertEquals(act_last_n, exp_last_n)
        self.assertEquals(act_second_n, exp_second_n)
