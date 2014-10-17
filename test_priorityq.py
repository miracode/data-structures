import unittest
from priorityq import PriorityQ


class MyTest(unittest.TestCase):

    def test_insert_one(self):
        pri, val = 2, 'a'
        testq = PriorityQ()
        testq.insert(pri, val)
        actual = testq.harray
        expected = [[None], [pri, val]]
        self.assertEquals(expected, actual)

    def test_insert_many(self):
        pri1, val1 = 2, 'a'
        pri2, val2 = 5, 'b'
        pri3, val3 = 1, 'c'
        pri4, val4 = 4, 'd'
        pri5, val5 = 3, 'e'
        testq = PriorityQ()
        testq.insert(pri1, val1)
        testq.insert(pri2, val2)
        testq.insert(pri3, val3)
        testq.insert(pri4, val4)
        testq.insert(pri5, val5)
        expected = [[None],
                    [pri3, val3],
                    [pri5, val5],
                    [pri1, val1],
                    [pri2, val2],
                    [pri4, val4]]
        actual = testq.harray
        self.assertEquals(expected, actual)

    def test_many_equal_priorities(self):
        pri1, val1 = 2, 'a'
        pri2, val2 = 5, 'b'
        pri3, val3 = 1, 'c'
        pri4, val4 = 2, 'f'
        pri5, val5 = 4, 'd'
        pri6, val6 = 3, 'e'
        testq = PriorityQ()
        testq.insert(pri1, val1)
        testq.insert(pri2, val2)
        testq.insert(pri3, val3)
        testq.insert(pri4, val4)
        testq.insert(pri5, val5)
        testq.insert(pri6, val6)
        expected = [[None],
                [pri3, val3],
                [pri5, val5],
                [pri1, val1, val4],
                [pri2, val2],
                [pri4, val4]]
        actual = testq.harray
        self.assertEquals(expected, actual)

    #def test_pop_with_1_elem(self):
    #    pri1, val1 = 2, 'a'
    #    pri2, val2 = 5, 'b'
    #    pri3, val3 = 1, 'c'
    #    pri4, val4 = 4, 'd'
    #    pri5, val5 = 3, 'e'
    #    testq = PriorityQ()
    #    testq.insert(pri1, val1)
    #    testq.insert(pri2, val2)
    #    testq.insert(pri3, val3)
    #    testq.insert(pri4, val4)
    #    testq.insert(pri5, val5)
    #    x = testq.pop()
    #    self.assertEquals(x, 57)
#


if __name__ == '__main__':
    unittest.main()
