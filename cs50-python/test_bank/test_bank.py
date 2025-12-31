from bank import value


def test_hello():
    assert value("hello") == 0

def test_HELLO():
    assert value("HELLO") == 0

def test_starts_with_h():
    assert value("hola") == 20


def test_not_hello_and_starts_with_h():
    assert value("ciao") == 100
