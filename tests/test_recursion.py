import pytest
import algos.recursion as recursion


@pytest.mark.parametrize("number, base, expected_result", [
    pytest.param(
        769,
        10,
        "769",
        id="base10"
    ),
    pytest.param(
        1453,
        16,
        "5ad",
        id="base16"
    ),
    pytest.param(
        100,
        12,
        "84",
        id="base12"
    ),
    pytest.param(
        194678,
        15,
        "3ca38",
        id="base15"
    ),
])
def test_to_string(number, base, expected_result):
    actual_result = recursion.to_string(number, base)
    assert actual_result == expected_result
