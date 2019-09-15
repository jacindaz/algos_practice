import pytest
from algos.trees import Node, insert_left


def test_node():
    root = Node(1)

    leaf_left = Node(2)
    root.left = leaf_left

    leaf_right = Node(3)
    root.right = leaf_right

    # insert when left child exists
    root.insert_left(Node(4))
    assert root.left.value == 4
    assert root.left.left.value == leaf_left.value

    # insert when no left child
    leaf_left.insert_left(Node(10))
    leaf_left.left.value == 10

    # insert when right child exists
    root.insert_right(Node(12))
    root.right.value == 12

    # insert when no right child
    leaf_right.insert_right(Node(20))
    leaf_right.right.value == 20


@pytest.mark.parametrize("root, child_value, expected_new_root", [
    pytest.param(
        [],
        "new_value",
        ["new_value"],
        id="no_left_subtree"
    ),
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
    actual = insert_left(root, child_value)
    assert actual == expected_new_root
