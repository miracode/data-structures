# -*- coding: utf-8 -*-
import unittest
import queue


class MyTest(unittest.TestCase):
    def test_enqueue(self):
        """test that enqueue works on one node"""
        tqueue = queue.Queue()
        val = 9
        tqueue.enqueue(val)
        self.assertEquals(tqueue.first_n.val, val)

    def test_large_enqueue(self):
        """test that enqueue works on multiple node queue"""
        tqueue = queue.Queue()
        tqueue.enqueue(1)
        tqueue.enqueue('a')
        tqueue.enqueue('bob')
        tqueue.enqueue(1.0)
        tqueue_vals = (tqueue.first_n.val,
                       tqueue.first_n.ref.val,
                       tqueue.first_n.ref.ref.val,
                       tqueue.first_n.ref.ref.ref.val)
        expected = (1, 'a', 'bob', 1.0)
        self.assertEquals(tqueue_vals, expected)


    #def test_dequeue(self):


if __name__ == '__main__':
    unittest.main()
