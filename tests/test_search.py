import pytest
import algos.search as search


@pytest.mark.parametrize("ordered_list, item_to_find, expected", [
    ([1,2,3,4,5,6], 6, True),
    ([1,2,3,40,50], 20, False),
    ([1,2,3,40,50], 40, True)
])
def test_sequential_search_ordered(ordered_list, item_to_find, expected):
    actual = search.sequential_search_ordered(ordered_list, item_to_find)
    assert actual == expected


@pytest.mark.parametrize("list, item_to_find, expected", [
    ([1,2,3,4,6,8], 6, True),
    ([1,2,3,4,10], 6, False),
    ([1,2,3], 3, True),
    ([1,2,3], 0, False),
    ([1,2,3,4], 3, True),
    ([0,1,2,8,13,17,19,32,42], 3, False),
    ([0,1,2,8,13,17,19,32,42], 1, True),
    ([0,1,2,8,13,17,19,32,42], 13, True),
    ([0,1,2,8,13,17,19,32,42], 42, True),
    ([0,1,2,8,13,17,19,32,42], 100, False),
    ([0,1,2,8,13,17,19,32,42], -8, False),
    ([0,1,2,8,13,13,13,17,19,32,42,42], 42, True),
    ([0,1,2,8,13,13,13,17,19,32,42,42], 14, False),
    ([0,1,2,8,13,13,13,17,19,32,42,42], 12, False),
])
def test_binary_search(list, item_to_find, expected):
    actual1 = search.binary_search_longest(list, item_to_find)
    actual2 = search.binary_search_long(list, item_to_find)
    actual3 = search.binary_search(list, item_to_find)

    assert actual1 == expected
    assert actual2 == expected
    assert actual3 == expected
