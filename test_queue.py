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

    def test_dequeue(self):
        tqueue = queue.Queue()
        tqueue.enqueue(1)
        tqueue.enqueue('a')
        tqueue.enqueue('bob')
        tqueue.enqueue(1.0)
        actual = tqueue.dequeue()
        self.assertEquals(actual.val, 1)
        self.assertEquals(tqueue.first_n.val, 'a')

    def test_null_dequeue(self):
        tqueue = queue.Queue()
        with self.assertRaises(IndexError) as context:
            tqueue.dequeue()
        self.assertEqual(context.exception.message,
                         'Queue is empty, cannot dequeue.')


if __name__ == '__main__':
    unittest.main()
