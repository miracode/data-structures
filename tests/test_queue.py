# -*- coding: utf-8 -*-
import unittest
from queue import Queue


class QueueTest(unittest.TestCase):
    def test_enqueue(self):
        """test that enqueue works on one node"""
        q = Queue()
        val = 9
        q.enqueue(val)
        self.assertEqual(q.first_node.data, val)
        self.assertEqual(q.last_node.data, val)

    def test_large_enqueue(self):
        """test that enqueue works on multiple node queue"""
        q = Queue()
        q.enqueue(1)
        q.enqueue('a')
        q.enqueue('bob')
        q.enqueue(10)
        self.assertEqual(q.first_node.data, 1)
        self.assertEqual(q.last_node.data, 10)

    def test_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue('a')
        q.enqueue('bob')
        q.enqueue(1.0)
        actual = q.dequeue()
        self.assertEquals(actual, 1)
        self.assertEquals(q.first_node.data, 'a')
        self.assertEquals(q.last_node.data, 1.0)

    def test_null_dequeue(self):
        q = Queue()
        with self.assertRaises(IndexError) as context:
            q.dequeue()
        self.assertEqual(context.exception.message,
                         'Queue is empty, cannot dequeue.')

    def test_size(self):
        q = Queue()
        self.assertEquals(q.size(), 0)
        q.enqueue(1)
        q.enqueue('a')
        q.enqueue('bob')
        q.enqueue(1.0)
        self.assertEquals(q.size(), 4)

    def test_peek(self):
        q = Queue()
        with self.assertRaises(IndexError) as context:
            q.peek()
        self.assertEqual(context.exception.message,
                         'Queue is empty, cannot peek.')
        q.enqueue(1)
        q.enqueue('a')
        q.enqueue('bob')
        q.enqueue(1.0)
        self.assertEquals(q.peek(), 1)

    def test_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(1)
        self.assertFalse(q.is_empty())

if __name__ == '__main__':
    unittest.main()
