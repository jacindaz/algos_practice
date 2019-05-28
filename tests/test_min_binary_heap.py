import algos.min_binary_heap as min_heap
import pytest


@pytest.mark.parametrize("existing_heap,new_item,expected", [
    pytest.param(
        [0,1],
        2,
        [0,1,2],
        id="one_level_insert_2"
    ),
    pytest.param(
        [0,5,9],
        11,
        [0,5,9,11],
        id="two_levels_insert_11"
    ),
    pytest.param(
        [0,6,7,12,10,15,17],
        5,
        [0,5,7,6,10,15,17,12],
        id="three_levels_insert_5"
    ),
    pytest.param(
        [0,5,9,11],
        12,
        [0,5,9,11,12],
        id="three_levels_insert_12"
    ),
    pytest.param(
        [0,9,14,18,33,17,27,7,40,41],
        20,
        [0,9,14,18,33,17,27,7,40,41,20],
        id="four_levels_insert_20"
    )
])
def test_insert(existing_heap, new_item, expected):
    actual_heap = min_heap.insert(existing_heap, new_item)
    assert actual_heap == expected


@pytest.mark.parametrize("existing_heap,expected", [
    pytest.param(
        [0,1,2],
        [0,2],
        id="one_level"
    ),
    pytest.param(
        [0,5,9,11,14,18,19,21,33,17,27],
        [0,9,14,11,17,18,19,21,33,27],
        id="four_levels"
    )
])
def test_delete_min(existing_heap, expected):
    actual_heap = min_heap.delete_min(existing_heap)
    assert actual_heap == expected
