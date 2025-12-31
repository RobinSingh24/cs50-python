from working import convert
import pytest

def test_valid():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'

def test_invalid():
    with pytest.raises(ValueError):
        assert convert('13 AM to 5 PM')
    with pytest.raises(ValueError):
        assert convert('12:60 AM to 5 PM')
    with pytest.raises(ValueError):
        assert convert('9 AM - 5 PM')
