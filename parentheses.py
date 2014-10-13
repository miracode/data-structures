

def parentheses(text):
    """Check whether parentheses are open, balanced, or broken"""
    p_open = text.count(u'(')
    p_closed = text.count(u')')

    if p_open > p_closed:
        return 1
    if p_open == p_closed:
        return 0
    if p_open < p_closed:
        return -1
