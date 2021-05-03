import pytest

from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_fibonacci():
    actual = fibonacci(5)
    expected = 5
    assert expected == actual
    actual2 = fibonacci(10)
    expected2 = 55
    assert expected2 == actual2
    actual3 = fibonacci(1)
    expected3 = 1
    assert actual3 == expected3

def test_lucas():
    actual = lucas(5)
    expected = 11
    assert expected == actual
    actual2 = lucas(10)
    expected2 = 123
    assert expected2 == actual2
    actual3 = lucas(1)
    expected3 = 1
    assert actual3 == expected3

def test_sum_series():
    actual = sum_series(5, 2, 1)
    expected = 11
    assert expected == actual
    actual2 = sum_series(10)
    expected2 = 55
    assert expected2 == actual2
    actual3 = sum_series(1)
    expected3 = 1
    assert actual3 == expected3
    actual4 = sum_series(10, 2, 3)
    expected4 = 233
    assert actual4 == expected4