import unittest
import binary_heap


class MyTest(unittest.TestCase):
    def test_init_max_heap(self):
        test_mh = binary_heap.MaxBinaryHeap()
        self.assertEquals(test_mh.h_array, [None])

    def test_mheap_insert1(self):
        test_mh = binary_heap.MaxBinaryHeap()
        val = 2
        test_mh.mh_insert(val)
        self.assertEquals(test_mh.h_array, [None, val])

    def test_mheap_insert_many(self):
        vals = [3, 7, 1, 4]
        test_mh2 = binary_heap.MaxBinaryHeap()
        print test_mh2.h_array
        for val in vals:
            print val
            test_mh2.mh_insert(val)
        actual = test_mh2.h_array
        expected = [None, 7, 4, 1, 3]
        self.assertEquals(actual, expected)

    def test_init_mheap_vals(self):
        tarray = (3, 7, 1, 4)
        test_mh = binary_heap.MaxBinaryHeap(tarray)
        actual = test_mh.h_array
        expected = [None, 7, 4, 1, 3]
        self.assertEquals(actual, expected)

    def test_pop_mheap_val(self):
        tarray = (3, 7, 1, 4)
        test_mh = binary_heap.MaxBinaryHeap(tarray)
        actual = test_mh.mh_pop()
        expected = 7
        self.assertEquals(actual, expected)

    #def test_pop_mheap_array(self):
    #    tarray = (3, 7, 1, 4, 5, 2, 9)
    #    test_mh = binary_heap.MaxBinaryHeap(tarray)
    #    test_mh.pop()
    #    actual = test_mh.h_array
    #    expected = [None, 7, 5, 2, 3, 4, 1]
    #    self.assertEquals(actual, expected)

if __name__ == '__main__':
    unittest.main()
