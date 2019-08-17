from algos.unordered_list import Node, UnOrderedList


def test_is_empty():
    list = UnOrderedList()
    assert list.is_empty()

    n1 = Node(1)
    list.head = n1
    assert not list.is_empty()


def test_add():
    list = UnOrderedList()
    list.add(1) # [1]
    assert not list.is_empty()

    list.add(2) # [2, 1]
    assert list.head.value == 2
    assert list.head.next.value == 1

    list.add(3) # [3, 2, 1]
    assert list.head.value == 3
    assert list.head.next.value == 2
