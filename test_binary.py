import unittest
import binary_heap


class MyTest(unittest.TestCase):
    def test_init_max_heap(self):
        tmaxheap = binary_heap.MaxBinaryHeap()
        self.assertEquals(tmaxheap.harray, [None])

    def test_max_heap_insert1(self):
        tmaxheap = binary_heap.MaxBinaryHeap()
        val = 2
        tmaxheap.mh_insert(val)
        self.assertEquals(tmaxheap.harray, [None, val])

    def test_max_heap_insert_many(self):
        vals = [3, 7, 1, 4]
        tmaxheap = binary_heap.MaxBinaryHeap()
        print tmaxheap.harray
        for val in vals:
            print val
            tmaxheap.mh_insert(val)
        actual = tmaxheap.harray
        expected = [None, 7, 4, 1, 3]
        self.assertEquals(actual, expected)

    def test_init_max_heap_vals(self):
        tarray = (3, 7, 1, 4)
        tmaxheap = binary_heap.MaxBinaryHeap(tarray)
        actual = tmaxheap.harray
        expected = [None, 7, 4, 1, 3]
        self.assertEquals(actual, expected)

    def test_pop_max_heap_val(self):
        tarray = (3, 7, 1, 4)
        tmaxheap = binary_heap.MaxBinaryHeap(tarray)
        actual = tmaxheap.mh_pop()
        expected = 7
        self.assertEquals(actual, expected)

    def test_pop_max_heap_array(self):
        tarray = (3, 7, 1, 4, 5, 2, 9)
        tmaxheap = binary_heap.MaxBinaryHeap(tarray)
        tmaxheap.mh_pop()
        actual = tmaxheap.harray
        expected = [None, 7, 5, 2, 3, 4, 1]
        self.assertEquals(actual, expected)

if __name__ == '__main__':
    unittest.main()
