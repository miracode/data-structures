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

    def test_max_heap_length(self):
        tarray = (3, 7, 1, 4, 5, 2, 9)
        tmaxheap = binary_heap.MaxBinaryHeap(tarray)
        actual = tmaxheap.length
        expected = 7
        self.assertEquals(actual, expected)

    def test_pop_max_heap_array2(self):
        tarray = (22, 7, 10, 45, 15, 27, 52, 12)
        tmaxheap = binary_heap.MaxBinaryHeap(tarray)
        tmaxheap.mh_pop()
        actual = tmaxheap.harray
        expected = [None, 45, 22, 27, 12, 15, 10, 7]
        self.assertEquals(actual, expected)

    def test_btype_init(self):
        theap = binary_heap.MaxBinaryHeap()
        actual = theap.btype
        expected = 'max'
        self.assertEquals(actual, expected)

    def test_min_max_error(self):
        theap = binary_heap.MaxBinaryHeap()
        actual = theap.btype
        expected = 'max'
        self.assertEquals(actual, expected)
        tarray = (3, 7, 1, 4, 5, 2, 9)
        theap2 = binary_heap.MaxBinaryHeap(tarray)
        actual = theap2.btype
        expected = 'max'
        self.assertEquals(actual, expected)
        theap3 = binary_heap.MaxBinaryHeap(btype='min')
        actual = (theap3.harray, theap3.btype)
        expected = ([None], 'min')
        self.assertEquals(actual, expected)
        with self.assertRaises(ValueError) as actual:
            binary_heap.MaxBinaryHeap(btype='foo')
        self.assertEquals(actual.exception.message,
                          u"Binary Heap type must be 'max' or 'min'")


if __name__ == '__main__':
    unittest.main()
