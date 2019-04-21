import algos.binary_search_trees as bst
import pytest


@pytest.mark.parametrize("tree,item_to_find,current_node,expected", [
    (
        {20: (10, None)},
        8,
        20,
        False
    ),
    (
        {20: (10, None)},
        10,
        20,
        True
    ),
    (
        {20: (10, 22), 10: (6, None), 6: (4, 9), 4: (1, 5)},
        5,
        20,
        True
    ),
    (
        {4: (1, 5), 10: (6, None), 6: (4, 9), 20: (10, 22)},
        5,
        30,
        False
    ),
    (
        {
            4: (1, 5), 10: (6, None), 6: (4, 9), 20: (10, 22),
            22: (21, 25)
        },
        30,
        20,
        False
    ),
    (
        {
            4: (1, 5), 10: (6, None), 6: (4, 9),
            20: (10, 22), 22: (21, 25)
        },
        4,
        20,
        True
    ),
])
def test_depth_first_search(tree, item_to_find, current_node, expected):
    result = bst.depth_first_search(tree, item_to_find, current_node)
    assert result == expected


@pytest.mark.parametrize("tree,root,item_to_insert,expected", [
    pytest.param(
        {20: (10, None)},
        20,
        22,
        {20: (10, 22)},
        id="insert_right_leaf"
    ),
    pytest.param(
        {20: (None, 22)},
        20,
        10,
        {20: (10, 22)},
        id="insert_left_leaf"
    ),
    pytest.param(
        {20: (10, 22)},
        20,
        21,
        {20: (10, 22), 22: (21, None)},
        id="insert_right_leaf_level2"
    ),
    pytest.param(
        {20: (10, 22)},
        20,
        23,
        {20: (10, 22), 22: (None, 23)},
        id="insert_right_leaf_level2"
    ),
    pytest.param(
        {20: (10, 22)},
        20,
        15,
        {20: (10, 22), 10: (None, 15)},
        id="insert_left_leaf_right_child_level2"
    ),
    pytest.param(
        {20: (10, 22)},
        20,
        6,
        {20: (10, 22), 10: (6, None)},
        id="insert_left_leaf_left_child_level2"
    ),
    pytest.param(
        {20: (10, 22), 10: (6, None)},
        20,
        3,
        {20: (10, 22), 10: (6, None), 6: (3, None)},
        id="insert_left_leaf_left_child_level3"
    ),
    pytest.param(
        {20: (10, 22), 10: (6, None), 6: (3, None)},
        20,
        1,
        {20: (10, 22), 10: (6, None), 6: (3, None), 3: (1, None)},
        id="insert_left_leaf_left_child_level4"
    ),
    pytest.param(
        {20: (10, 22), 10: (6, None), 6: (4, None)},
        20,
        9,
        {20: (10, 22), 10: (6, None), 6: (4, 9)},
        id="insert_left_leaf_right_level4"
    ),
    pytest.param(
        {20: (10, 22), 10: (6, None), 6: (4, 9), 4: (1, None)},
        20,
        5,
        {20: (10, 22), 10: (6, None), 6: (4, 9), 4: (1, 5)},
        id="insert_left_leaf_right_level5"
    )
])
def test_insert(tree, root, item_to_insert, expected):
    result = bst.insert(tree, item_to_insert, root)
    assert dict(sorted(result.items())) == dict(sorted(expected.items()))


@pytest.mark.parametrize("tree,current_node,expected", [
    (
        {20: (10, 30), 10: (8, None)},
        20,
        30
    ),
    (
        {25: (0, None)},
        25,
        25
    ),
    (
        {10: (8, None), 12: (10, None), 20: (12, None)},
        20,
        20
    ),
    (
        {1: (None, None)},
        1,
        1
    ),
    (
        {
            4: (1, 5), 10: (6, None), 6: (4, 9),
            20: (10, 22), 22: (21, 25)
        },
        20,
        25
    )
])
def test_bst_max(tree, current_node, expected):
    actual_max = bst.find_max(tree, current_node)
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
