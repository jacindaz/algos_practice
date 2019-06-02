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
    actual_result1 = stack.balanced_parentheses(parens_string)
    actual_result2 = stack.balanced_parentheses2(parens_string)
    assert actual_result1 == expected
    assert actual_result2 == expected


@pytest.mark.parametrize("symbols_string,expected", [
    pytest.param(
        "{{([][])}()}",
        True,
        id="balanced1"
    ),
    pytest.param(
        "[[{{(())}}]]",
        True,
        id="balanced2"
    ),
    pytest.param(
        "[][][](){}",
        True,
        id="balanced3"
    ),
    pytest.param(
        "([)]",
        False,
        id="not_balanced1"
    ),
    pytest.param(
        "((()]))",
        False,
        id="not_balanced2"
    ),
    pytest.param(
        "[{()]",
        False,
        id="not_balanced3"
    )
])
def test_balanced_symbols(symbols_string, expected):
    actual_result1 = stack.balanced_symbols(symbols_string)
    actual_result2 = stack.balanced_symbols2(symbols_string)
    assert actual_result1 == expected
    assert actual_result2 == expected
