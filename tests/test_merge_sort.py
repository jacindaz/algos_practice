import algos.merge_sort as sort
import pytest


@pytest.mark.parametrize("list_to_merge,expected", [
    (
        [38,27],
        [27,38]
    ),
    (
        [38,27,43,3],
        [3,27,38,43]
    ),
    (
        [1],
        [1]
    ),
    (
        [38,27,43,3,9,82,10,8],
        [3,8,9,10,27,38,43,82]
    ),
    (
        [38,27,43,3,9,82],
        [3,9,27,38,43,82]
    ),
    (
        [38,27,43,3,9,82,10],
        [3,9,10,27,38,43,82]
    ),
])
def test_merge_sort(list_to_merge, expected):
    actual = sort.merge_sort(list_to_merge)
    assert actual == expected
