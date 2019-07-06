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


@pytest.mark.parametrize("decimal_number, base, expected_number",
[
    pytest.param(
        25,
        16,
        '19',
        id="base_16"
    ),
    pytest.param(
        50,
        14,
        '38',
        id="base_14"
    ),
    pytest.param(
        79,
        7,
        '142',
        id="base_7"
    )
])
def test_convert_to_base(decimal_number, base, expected_number):
    actual_number = stack.convert_to_base(decimal_number, base)
    assert actual_number == expected_number
