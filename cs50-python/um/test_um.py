from um import count

def test_valid():
    assert count('um') == 1
    assert count('UM') == 1
    assert count(' um ') == 1
    assert count('um...') == 1
    assert count('hello, um, world') == 1

def test_invalid():
    assert count('hello umbrella') == 0
    assert count('yummy') == 0
