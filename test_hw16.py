import pytest


from hw16 import kilometers_to_miles, get_unique_letters


def test_miles_to_kilometers_positive():
    assert kilometers_to_miles(10) == 16.0934


def test_miles_to_kilometers_zero():
    assert kilometers_to_miles(0) == 0


def test_miles_to_kilometers_negative():
    with pytest.raises(ValueError):
        kilometers_to_miles(-5)


def test_miles_to_kilometers_float():
    assert kilometers_to_miles(3.5) == 5.63269


def test_miles_to_kilometers_large_value():
    assert kilometers_to_miles(100000) == 160934


# Тести для другої функції get_unique_sorted_elements:
def test_get_unique_sorted_elements_list():
    assert get_unique_letters([3, 2, 1, 2, 3, 4]) == (1, 2, 3, 4)


def test_get_unique_sorted_elements_set():
    assert get_unique_letters({3, 2, 1, 2, 3, 4}) == (1, 2, 3, 4)


def test_get_unique_sorted_elements_string():
    assert get_unique_letters("hello") == ('e', 'h', 'l', 'o')


def test_get_unique_sorted_elements_dict():
    assert get_unique_letters({'a': 1, 'b': 2, 'c': 3}) == ('a', 'b', 'c')


def test_get_unique_sorted_elements_empty():
    assert get_unique_letters([]) == ()
