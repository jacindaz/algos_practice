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
    ([1,2,3,4], 3, True)
])
def test_binary_search(list, item_to_find, expected):
    actual = search.binary_search(list, item_to_find)
    assert actual == expected
