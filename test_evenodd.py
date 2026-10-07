from evenodd import even_or_odd

def test_even():
    assert even_or_odd(4) == "Even number "

def test_odd():
    assert even_or_odd(5) == "Odd number"