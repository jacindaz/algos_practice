from algos.lists import Node, UnOrderedList


def test_unordered_list_is_empty():
    list1 = UnOrderedList()
    assert list1.is_empty()

    n1 = Node(1)
    list1.head = n1
    assert not list1.is_empty()
