from numb3rs import validate

def test_valid():
    assert validate("1.2.3.4") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_invalid():
    assert validate("275.1.0.3") == False
    assert validate("cat") == False
    assert validate("255.257.0.9") == False

