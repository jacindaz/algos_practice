import algos.pre_order_bst as bst
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
    pytest.param(
        [],
        30,
        [30],
        id="insert_empty_tree"
    ),
    pytest.param(
        [2],
        3,
        [2, 3],
        id="insert_tree_length_1"
    ),
])
def test_bst_insert(tree, item_to_insert, expected):
    new_tree = bst.insert(tree, item_to_insert)
    assert new_tree == expected


@pytest.mark.parametrize("tree,expected", [
    ([20, 10, 8, 30], 30),
    ([25, 0], 25),
    ([20, 12, 10, 8], 20),
    ([1], 1)
])
def test_bst_max(tree, expected):
    actual_max = bst.find_max(tree)
    assert actual_max == expected


@pytest.mark.parametrize("tree,expected", [
    ([20, 10, 8, 30], 8),
    ([25, 0], 0),
    ([20, 12, 10, 8], 8),
    ([1], 1)
])
def test_bst_min(tree, expected):
    actual_min = bst.find_min(tree)
    assert actual_min == expected

@pytest.mark.xfail
@pytest.mark.parametrize("tree,item,expected", [
    ([20, 10, 8, 30], 8, True),
    ([0], 1, False),
])
def test_bst_search(tree, item, expected):
    assert bst.search(tree, item) == expected
