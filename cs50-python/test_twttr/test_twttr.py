from twttr import shorten

def test_capital():
    assert shorten("BOOK") == "BK"

def test_nonAlpha():
    assert shorten("$99.99") == "$99.99"
    assert shorten(":)") == ":)"

def test_alpha_and_special():
    assert shorten("hello-world") == "hll-wrld"

def test_upper_and_lower_case():
    assert shorten("Oracle") == "rcl"
