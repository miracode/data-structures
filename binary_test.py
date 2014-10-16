import unittest
import binary_heap


class MyTest(unittest.TestCase):
    def test_init_max_heap(self):
        test_mh = binary_heap.MaxBinaryHeap()
        self.assertEquals(test_mh.h_array, [None])

    def test_mheap_insert1(self):
        test_mh = binary_heap.MaxBinaryHeap()
        val = 2
        test_mh.insert(2)
        self.assertEquals(test_mh.h_array, [None, val])

    #def test_init_mheap_vals(self):
    #    tarray = (1,4,9)
    #    test_mh = binary_heap.MaxBinaryHeap()
