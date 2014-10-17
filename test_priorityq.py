import unittest
import priorityq


class MyTest(unittest.TestCase):

    def test_insert_one(self):
        pass
        val, pri = 'a', 2
        testq = priorityq.PriorityQ()
        testq.insert(val, pri)
        expected = testq.heap
        actual = [(val, pri)]
        self.assertEquals(expected, actual)


if __name__ == '__main__':
    unittest.main()
