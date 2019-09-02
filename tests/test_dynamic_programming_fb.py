import pytest
import algos.dynamic_programming_fib as fib


@pytest.mark.parametrize("input, expected", [
    (0, 0),
    (2, 1),
    (6, 8),
    (8, 21)
])
def test_fib(input, expected):
    actual_recursive = fib.fib(input)
    assert expected == actual_recursive

    actual_dp = fib.fib_dynamic_programming(input)
    assert expected == actual_dp
