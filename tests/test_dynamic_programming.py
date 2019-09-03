import pytest
import algos.dynamic_programming as dp


@pytest.mark.parametrize("input, expected", [
    (0, 0),
    (2, 1),
    (6, 8),
    (8, 21)
])
def test_fib(input, expected):
    actual_recursive = dp.fib(input)
    assert expected == actual_recursive

    actual_dp = dp.fib_dynamic_programming(input)
    assert expected == actual_dp


@pytest.mark.parametrize("height, width, expected", [
    (0, 1, 1),
    (2, 2, 6),
    (2, 4, 15),
    (3, 7, 120),
    (7, 3, 120),
    (8, 5, 1287),
    (9, 10, 92378),
    (10, 10, 184756)
])
def test_num_paths(height, width, expected):
    actual_recursive = dp.num_paths(height, width)
    actual_dp = dp.num_paths(height, width)
    assert actual_recursive == expected
    assert actual_dp == expected
