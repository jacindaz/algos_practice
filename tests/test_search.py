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
