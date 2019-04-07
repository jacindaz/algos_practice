import pre_order_bst as bst
import pytest

@pytest.mark.parametrize("tree,item_to_insert,expected", [
    (
        [20, 10, 8, 25],
        30,
        [20, 10, 8, 25, 30],
    ),
    (
        [25, 0],
        30,
        [25, 0, 30]
    ),
])
def test_bst_insert(tree, item_to_insert, expected):
    new_tree = bst.insert(tree, item_to_insert)
    assert new_tree == expected
