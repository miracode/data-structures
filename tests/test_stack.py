from stack import Stack
import unittest


class StackTest(unittest.TestCase):
    def test_init(self):
        stack = Stack()
        self.assertIsNone(stack.top_node)

    def test_push(self):
        """Test that push adds value to top of stack"""
        stack = Stack()
        val = 8
        stack.push(val)
        self.assertEqual(stack.top_node.data, val)
        val2 = 'a'
        stack.push(val2)
        self.assertEqual(stack.top_node.next.data, val)
        self.assertEqual(stack.top_node.data, val2)

    def test_pop(self):
        """Test that pop returns first value of stack and removes from stack"""
        stack = Stack()
        with self.assertRaises(IndexError) as context:
            stack.pop()
        self.assertEqual(context.exception.message,
                         'Stack is empty, cannot pop value.')
        stack.push(8)
        stack.push('a')
        x = stack.pop()
        self.assertEqual(x.data, 'a')
        self.assertEqual(stack.top_node.data, 8)

    def test_peek(self):
        stack = Stack()
        with self.assertRaises(IndexError) as context:
            stack.peek()
        self.assertEqual(context.exception.message,
                         'Stack is empty, cannot peek value.')
        stack.push('a')
        stack.push('b')
        self.assertEqual(stack.peek(), 'b')

if __name__ == '__main__':
    unittest.main()
