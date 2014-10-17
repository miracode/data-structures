import unittest
import binary_heap


class MyTest(unittest.TestCase):
    def test_init_max_heap(self):
        tmaxheap = binary_heap.BinaryHeap()
        self.assertEquals(tmaxheap.harray, [None])

    def test_max_heap_insert1(self):
        tmaxheap = binary_heap.BinaryHeap()
        val = 2
        tmaxheap.insert(val)
        self.assertEquals(tmaxheap.harray, [None, val])

    def test_max_heap_insert_many(self):
        vals = [3, 7, 1, 4]
        tmaxheap = binary_heap.BinaryHeap()
        print tmaxheap.harray
        for val in vals:
            print val
            tmaxheap.insert(val)
        actual = tmaxheap.harray
        expected = [None, 7, 4, 1, 3]
        self.assertEquals(actual, expected)

    def test_init_max_heap_vals(self):
        tarray = (3, 7, 1, 4)
        tmaxheap = binary_heap.BinaryHeap(tarray)
        actual = tmaxheap.harray
        expected = [None, 7, 4, 1, 3]
        self.assertEquals(actual, expected)

    def test_pop_max_heap_val(self):
        tarray = (3, 7, 1, 4)
        tmaxheap = binary_heap.BinaryHeap(tarray)
        actual = tmaxheap.pop()
        expected = 7
        self.assertEquals(actual, expected)

    def test_pop_max_heap_array(self):
        tarray = (3, 7, 1, 4, 5, 2, 9)
        tmaxheap = binary_heap.BinaryHeap(tarray)
        tmaxheap.pop()
        actual = tmaxheap.harray
        expected = [None, 7, 5, 2, 3, 4, 1]
        self.assertEquals(actual, expected)

    def test_max_heap_length(self):
        tarray = (3, 7, 1, 4, 5, 2, 9)
        tmaxheap = binary_heap.BinaryHeap(tarray)
        actual = tmaxheap.length
        expected = 7
        self.assertEquals(actual, expected)

    def test_pop_max_heap_array2(self):
        tarray = (22, 7, 10, 45, 15, 27, 52, 12)
        tmaxheap = binary_heap.BinaryHeap(tarray)
        tmaxheap.pop()
        actual = tmaxheap.harray
        expected = [None, 45, 22, 27, 12, 15, 10, 7]
        self.assertEquals(actual, expected)

    def test_btype_init(self):
        theap = binary_heap.BinaryHeap()
        actual = theap.btype
        expected = 'max'
        self.assertEquals(actual, expected)

    def test_min_max_error(self):
        theap = binary_heap.BinaryHeap()
        actual = theap.btype
        expected = 'max'
        self.assertEquals(actual, expected)
        tarray = (3, 7, 1, 4, 5, 2, 9)
        theap2 = binary_heap.BinaryHeap(tarray)
        actual = theap2.btype
        expected = 'max'
        self.assertEquals(actual, expected)
        theap3 = binary_heap.BinaryHeap(btype='min')
        actual = (theap3.harray, theap3.btype)
        expected = ([None], 'min')
        self.assertEquals(actual, expected)
        with self.assertRaises(ValueError) as actual:
            binary_heap.BinaryHeap(btype='foo')
        self.assertEquals(actual.exception.message,
                          u"Binary Heap type must be 'max' or 'min'")

    def test_min_insert(self):
        theap = binary_heap.BinaryHeap(btype='min')
        vals = [3, 7, 1, 4]
        for val in vals:
            print val
            theap.insert(val)
        actual = theap.harray
        expected = [None, 1, 4, 3, 7]
        self.assertEquals(actual, expected)

    def test_val_list(self):
        vals = [3, 7, 1, 4]
        theap = binary_heap.BinaryHeap(vals, 'min')
        actual = theap.harray
        expected = [None, 1, 4, 3, 7]
        self.assertEquals(actual, expected)

    def test_min_pop(self):
        vals = [3, 7, 1, 4]
        theap = binary_heap.BinaryHeap(vals, 'min')
        actual_pval = theap.pop()
        actual_array = theap.harray
        expected_pval = 1
        expectd_array = [None, 3, 4, 7]
        self.assertEquals(actual_pval, expected_pval)
        self.assertEquals(actual_array, expectd_array)


if __name__ == '__main__':
    unittest.main()
