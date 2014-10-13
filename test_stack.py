from stack import stack


def test_push():
    t_stack = stack()
    val = 8
    t_stack.push(val)
    assert t_stack.first.val == val
