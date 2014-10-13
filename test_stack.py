from stack import Stack


def test_push():
    t_stack = Stack()
    val = 8
    t_stack.push(val)
    assert t_stack.first_n.val == val
