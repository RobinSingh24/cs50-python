from plates import is_valid

def test_valid_plate():
    assert is_valid('CS50') == True

def test_invalid_plate_len_more():
    assert is_valid('CSS5000') == False

def test_invalid_plate_len_less():
    assert is_valid('C') == False

def test_invalid_plate_alpa_after_digit():
    assert is_valid('CS50A') == False

def test_invalid_plate_first_digit_zero():
    assert is_valid('CS05') == False

def test_invalid_plate_begin_not_alpha():
    assert is_valid('50') == False

def test_invalid_plate_not_alnum():
    assert is_valid('CS-50') == False
