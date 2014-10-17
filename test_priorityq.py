import unittest
import priorityq


class MyTest(unittest.TestCase):

    def test_insert_one(self):
        pass
        pri, val = 2, 'a'
        testq = priorityq.PriorityQ()
        testq.insert(pri, val)
        expected = testq.harray
        actual = [[pri, val]]
        self.assertEquals(expected, actual)


if __name__ == '__main__':
    unittest.main()
