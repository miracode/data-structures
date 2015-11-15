from stack import Stack
import unittest


class StackTest(unittest.TestCase):
    def test_init(self):
        t_stack = Stack()
        assert t_stack.top_node is None

    def test_push(self):
        """Test that push adds value to top of stack"""
        t_stack = Stack()
        val = 8
        t_stack.push(val)
        assert t_stack.top_node.data == val
        val2 = 'a'
        t_stack.push(val2)
        assert t_stack.top_node.next.data == val
        assert t_stack.top_node.data == val2

    def test_pop(self):
        """Test that pop returns first value of stack and removes from stack"""
        t_stack = Stack()
        with self.assertRaises(IndexError) as context:
            t_stack.pop()
        self.assertEqual(context.exception.message,
                         'Stack is empty, cannot pop value.')
        t_stack.push(8)
        t_stack.push('a')
        x = t_stack.pop()
        assert x.data == 'a'
        assert t_stack.top_node.data == 8

    def test_peek(self):
        stack = Stack()
        with self.assertRaises(IndexError) as context:
            stack.peek()
        self.assertEqual(context.exception.message,
                         'Stack is empty, cannot peek value.')
        stack.push('a')
        stack.push('b')
        assert stack.peek() == 'b'

if __name__ == '__main__':
    unittest.main()
