import pre_order_bst as bst
import pytest

@pytest.mark.parametrize("tree,item_to_insert,expected", [

    pytest.param(
        [20, 10, 8, 25],
        22,
        [20, 10, 8, 22, 25],
        id="insert_middle_1"
    ),
    pytest.param(
        [20, 10, 8, 25],
        12,
        [20, 12, 10, 8, 25],
        id="insert_middle_2"
    ),
    pytest.param(
        [25, 0],
        30,
        [25, 0, 30],
        id="insert_end"
    ),
])
def test_bst_insert(tree, item_to_insert, expected):
    new_tree = bst.insert(tree, item_to_insert)
    assert new_tree == expected
