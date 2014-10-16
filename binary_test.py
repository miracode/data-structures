import unittest
import binary_heap


class MyTest(unittest.TestCase):
    def test_init_max_heap(self):
        test_mh = binary_heap.MaxBinaryHeap()
        self.assertEquals(test_mh.h_array, [])
