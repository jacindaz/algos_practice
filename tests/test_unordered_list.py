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
    assert list.size() == 5

    list.append(30)
    assert list.size() == 6
    assert list.search(30)

    list.append(2)
    assert list.size() == 7
    assert list.search(2)


def test_index():
    list = create_list_length_5()  # [99, 8, 54, 10, 1]

    assert list.index(99) == 0
    assert list.index(54) == 2
    assert list.index(1) == 4


def test_insert():
    list = UnOrderedList()
    list.add(1)         # [1]

    list.insert(1, 2)   # [1, 2]
    assert list.size() == 2
    assert list.head.next.value == 2

    list.insert(1, 3)   # [1, 3, 2]
    assert list.size() == 3
    assert list.head.next.value == 3

    list.insert(0, 4)   # [4, 1, 3, 2]
    assert list.size() == 4
    assert list.head.value == 4


def test_pop_last_item():
    list = create_list_length_5()       # [99, 8, 54, 10, 1]
    assert list.size() == 5

    last_item = list.pop_last_item()    # [99, 8, 54, 10]
    assert list.size() == 4
    assert last_item == 1

    last_item2 = list.pop_last_item()    # [99, 8, 54]
    assert list.size() == 3
    assert last_item2 == 10


def test_pop_with_pos():
    list = create_list_length_5()       # [99, 8, 54, 10, 1]

    # remove tail
    assert list.pop(4) == 1             # [99, 8, 54, 10]
    assert list.size() == 4

    # remove head
    assert list.pop(0) == 99            # [8, 54, 10]
    assert list.size() == 3

    # remove in the middle
    assert list.pop(1) ==54             # [8, 1]
    assert list.size() == 2
