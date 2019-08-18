from algos.unordered_list import Node, UnOrderedList
from algos.ordered_list import OrderedList

def test_search():
    list1 = OrderedList()
    list1.add(1)
    list1.add(20)
    list1.add(14)
    list1.add(58)
    list1.add(30)
    assert list1.size() == 5     # [1, 14, 20, 30, 58]

    assert list1.search(14)
    assert list1.search(58)

    assert list1.search(0) is False
    assert list1.search(15) is False
    assert list1.search(100) is False


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


def test_add_old():
    list1 = OrderedList()
    list1.add_old(1)                  # [1]
    assert list1.head.value == 1

    list1.add_old(18)                 # [1, 18]
    assert list1.head.value == 1
    assert list1.head.next.value == 18

    list1.add_old(7)                  # [1, 7, 18]
    assert list1.head.value == 1
    assert list1.head.next.value == 7
    assert list1.size() == 3

    list1.add_old(34)                 # [1, 7, 18, 34]
    assert list1.size() == 4
