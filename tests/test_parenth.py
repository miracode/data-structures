from parentheses import parentheses


def test_open():
    text = u'hello (world), (how are you?'
    assert parentheses(text) == 1


def test_closed():
    text = u'hello (world), (how are you?)'
    assert parentheses(text) == 0


def test_broken():
    text = u'hello world), (how are you?)'
    assert parentheses(text) == -1
