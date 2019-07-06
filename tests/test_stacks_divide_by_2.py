import algos.stacks_divide_by_2 as stack
import pytest

@pytest.mark.parametrize("decimal_number, expected_binary",
[
    pytest.param(
        10,
        '1010',
        id="10"
    ),
    pytest.param(
        42,
        '101010',
        id="42"
    ),
    pytest.param(
        100,
        '1100100',
        id="100"
    )
])
def test_decimal_number_to_binary(decimal_number, expected_binary):
    actual_binary = stack.decimal_number_to_binary(decimal_number)
    assert actual_binary == expected_binary
