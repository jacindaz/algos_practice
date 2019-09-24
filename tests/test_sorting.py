import pytest
from algos.sorting import bubble_sort, selection_sort, insertion_sort


@pytest.mark.parametrize("my_list, expected", [
    (
        [-1,8,11,22,9,-5,2],
        [-5,-1,2,8,9,11,22]
    ),
    (
        [100,-4,22,12,123,-38,12,50],
        [-38,-4,12,12,22,50,100,123]
    ),
    (
        [10,9,8,7,6,5,4,3,2,1],
        [1,2,3,4,5,6,7,8,9,10]
    ),
    (
        [1,2,3,0,4,5,6,-1,8,9,10],
        [-1,0,1,2,3,4,5,6,8,9,10]
    ),
    (
        [8,8,8,8,-8,2,2,2,2,10,0],
        [-8,0,2,2,2,2,8,8,8,8,10]
    )
])
def test_sorting(my_list, expected):
    actual_bubble = bubble_sort(my_list)
    assert actual_bubble == expected

    actual_selection = selection_sort(my_list)
    assert actual_selection == expected

    actual_insertion = insertion_sort(my_list)
    assert actual_insertion == expected
