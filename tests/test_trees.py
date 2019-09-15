import pytest
import algos.trees as trees


@pytest.mark.parametrize("root, child_value, expected_new_root", [
    pytest.param(
        [3], "new_value", [3, ["new_value"]],
        id="no_left_child"
    ),
    pytest.param(
        [
            1,
            [2, [4]],
            [3]
        ],
        "new_value",
        [
            1,
            ["new_value", [2, [4]]],
            [3]
        ],
        id="existing_left_child"
    )
])
def test_insert_left(root, child_value, expected_new_root):
    actual = trees.insert_left(root, child_value)
    assert actual == expected_new_root
