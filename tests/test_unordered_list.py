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


def test_size():
    list = UnOrderedList()
    list.add(1)
    assert list.size() == 1

    list.add(10)    # [10, 1]
    list.add(54)    # [54, 10, 1]
    assert list.size() == 3

    list.add(8)     # [8, 54, 10, 1]
    list.add(99)    # [99, 8, 54, 10, 1]
    assert list.size() == 5

    list.remove(54) # [99, 8, 10, 1]
    assert list.size() == 4


def create_list_length_5():
    list = UnOrderedList()
    list.add(1)     # [1]
    list.add(10)    # [10, 1]
    list.add(54)    # [54, 10, 1]
    list.add(8)     # [8, 54, 10, 1]
    list.add(99)    # [99, 8, 54, 10, 1]

    return list


def test_search():
    list = create_list_length_5()  # [99, 8, 54, 10, 1]

    assert list.search(54) == True
    assert list.search(22) == False


def test_remove():
    list = create_list_length_5()  # [99, 8, 54, 10, 1]

    # remove tail
    list.remove(1)  # [99, 8, 54, 10]
    assert not list.search(1)
    assert list.head.value == 99
    assert list.search(8)
    assert list.search(54)
    assert list.search(10)

    # remove item in the middle of list
    list.remove(54) # [99, 8, 10]
    assert not list.search(54)
    assert list.head.value == 99
    assert list.search(10)

    # remove head
    list.remove(99) # [8, 10]
    assert not list.search(9)
    assert list.head.value == 8
    assert list.search(10)


def test_append():
    list = create_list_length_5()  # [99, 8, 54, 10, 1]
