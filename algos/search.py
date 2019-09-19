def sequential_search_ordered(ord_list, item_to_find):
    """
    Find if an element exists in a sorted list
    """
    for value in ord_list:
        if item_to_find == value:
            return True
        elif value > item_to_find:
            return False
        previous = value

    return False

def binary_search_longest(list, item_to_find, current_index=None):

    if current_index is None:
        current_index = len(list) // 2

    if len(list) == 0:
        return False
    elif len(list) == 1:
        if list[0] == item_to_find:
            return True
        else:
            return False

    print(f"\nlist: {list}")
    print(f"item_to_find: {item_to_find}, current_index: {current_index}")
    print(f"item_to_find {item_to_find} == {list[current_index]}")

    if list[current_index] == item_to_find:
        return True
    elif item_to_find > list[current_index]:
        return binary_search(list[current_index:], item_to_find, len(list[current_index:]) // 2)
    elif item_to_find < list[current_index]:
        return binary_search(list[:current_index], item_to_find, len(list[:current_index]) // 2)


def binary_search_long(list_to_search, item_to_find, current_index=None):
    current_index = (len(list_to_search)-1) // 2

    if len(list_to_search) <= 2:
        if item_to_find in list_to_search:
            return True
        else:
            return False

    print(f"\nlist to search: {list_to_search}")
    print(f"item_to_find: {item_to_find}, current_index: {current_index}")
    print(f"comparing {item_to_find} == {list_to_search[current_index]}")

    if item_to_find == list_to_search[current_index]:
        return True
    elif item_to_find > list_to_search[current_index]:
        return binary_search(list_to_search[current_index:], item_to_find)
    elif item_to_find < list_to_search[current_index]:
        return binary_search(list_to_search[:current_index], item_to_find)


def binary_search(list_to_search, item_to_find, current_index=None):
    current_index = len(list_to_search) // 2
    if len(list_to_search) == 0:
        return False

    print(f"\nlist to search: {list_to_search}")
    print(f"item_to_find: {item_to_find}, current_index: {current_index}")
    print(f"comparing {item_to_find} == {list_to_search[current_index]}")

    if item_to_find == list_to_search[current_index]:
        return True
    elif item_to_find > list_to_search[current_index]:
        return binary_search(list_to_search[current_index+1:], item_to_find)
    return binary_search(list_to_search[:current_index], item_to_find)
