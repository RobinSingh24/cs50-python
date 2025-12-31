from seasons import Season
import pytest

def test_valid():
    dob = Season('2024-12-25')
    assert dob.minutes_passed() == 'Five hundred twenty-five thousand, six hundred minutes'
    dob = Season('2023-12-25')
    assert dob.minutes_passed() == 'One million, fifty-two thousand, six hundred forty minutes'

def test_invalid():
    with pytest.raises(SystemExit):
        Season('January 1, 1999')
