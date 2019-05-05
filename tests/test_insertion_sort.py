import algos.insertion_sort as sort
import pytest


@pytest.mark.parametrize("list_to_sort,expected", [
    (
        [4,3,2,10,12,1,5,6],
        [1,2,3,4,5,6,10,12]
    ),
    (
        [12,11,13,5,6],
        [5,6,11,12,13]
    ),
    (
        [1],
        [1]
    ),
    (
        [5,4,3,2,1,-5],
        [-5,1,2,3,4,5]
    ),
    (
        [-1,-3,-5,-7,-9],
        [-9,-7,-5,-3,-1]
    )
])
def test_insertion_sort(list_to_sort, expected):
    actual = sort.insertion_sort(list_to_sort)
    assert actual == expected
