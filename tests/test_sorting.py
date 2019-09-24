import pytest
from algos.sorting import bubble_sort


@pytest.mark.parametrize("my_list, expected", [
    (
        [-1,8,11,22,9,-5,2],
        [-5,-1,2,8,9,11,22]
    ),
    (
        [100,-4,22,12,123,-38,12,50],
        [-38,-4,12,12,22,50,100,123]
    )
])
def test_bubble_sort(my_list, expected):
    actual = bubble_sort(my_list)
    assert actual == expected
