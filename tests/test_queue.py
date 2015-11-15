# -*- coding: utf-8 -*-
import unittest
import queue


class QueueTest(unittest.TestCase):
    def test_enqueue(self):
        """test that enqueue works on one node"""
        tqueue = queue.Queue()
        val = 9
        tqueue.enqueue(val)
        self.assertEqual(tqueue.first_node.data, val)
        self.assertEqual(tqueue.last_node.data, val)

    def test_large_enqueue(self):
        """test that enqueue works on multiple node queue"""
        tqueue = queue.Queue()
        tqueue.enqueue(1)
        tqueue.enqueue('a')
        tqueue.enqueue('bob')
        tqueue.enqueue(10)
        self.assertEqual(tqueue.first_node.data, 1)
        self.assertEqual(tqueue.last_node.data, 10)

    def test_dequeue(self):
        tqueue = queue.Queue()
        tqueue.enqueue(1)
        tqueue.enqueue('a')
        tqueue.enqueue('bob')
        tqueue.enqueue(1.0)
        actual = tqueue.dequeue()
        self.assertEquals(actual, 1)
        self.assertEquals(tqueue.first_node.data, 'a')
        self.assertEquals(tqueue.last_node.data, 1.0)

    def test_null_dequeue(self):
        tqueue = queue.Queue()
        with self.assertRaises(IndexError) as context:
            tqueue.dequeue()
        self.assertEqual(context.exception.message,
                         'Queue is empty, cannot dequeue.')

    def test_size(self):
        tqueue = queue.Queue()
        self.assertEquals(tqueue.size(), 0)
        tqueue.enqueue(1)
        tqueue.enqueue('a')
        tqueue.enqueue('bob')
        tqueue.enqueue(1.0)
        self.assertEquals(tqueue.size(), 4)

    def test_peek(self):
        tqueue = queue.Queue()
        with self.assertRaises(IndexError) as context:
            tqueue.peek()
        self.assertEqual(context.exception.message,
                         'Queue is empty, cannot peek.')
        tqueue.enqueue(1)
        tqueue.enqueue('a')
        tqueue.enqueue('bob')
        tqueue.enqueue(1.0)
        self.assertEquals(tqueue.peek(), 1)

    def test_is_empty(self):
        tqueue = queue.Queue()
        self.assertTrue(tqueue.is_empty())
        tqueue.enqueue(1)
        self.assertFalse(tqueue.is_empty())

if __name__ == '__main__':
    unittest.main()
