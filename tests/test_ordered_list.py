from algos.unordered_list import Node, UnOrderedList
from algos.ordered_list import OrderedList

def test_search():
    list1 = OrderedList()
    pass


def test_add():
    list1 = OrderedList()
    list1.add(1)                  # [1]
    assert list1.head.value == 1

    list1.add(18)                 # [1, 18]
    assert list1.head.value == 1
    assert list1.head.next.value == 18

    list1.add(7)                  # [1, 7, 18]
    assert list1.head.value == 1
    assert list1.head.next.value == 7
    assert list1.size() == 3

    list1.add(34)                 # [1, 7, 18, 34]
    assert list1.size() == 4
