import algos.stack as stack
import pytest

@pytest.mark.parametrize("parens_string,expected", [
    pytest.param(
        "(()()()())",
        True,
        id="balanced1"
    ),
    pytest.param(
        "(()()()())",
        True,
        id="balanced2"
    ),
    pytest.param(
        "(()((())()))",
        True,
        id="balanced3"
    ),
    pytest.param(
        "((((((())",
        False,
        id="not_balanced1"
    ),
    pytest.param(
        "()))",
        False,
        id="not_balanced2"
    ),
    pytest.param(
        "(()()(()",
        False,
        id="not_balanced3"
    )
])
def test_balanced_parantheses(parens_string, expected):
    actual_result = stack.balanced_parentheses(parens_string)
    actual_result = stack.balanced_parentheses2(parens_string)
    assert actual_result == expected
