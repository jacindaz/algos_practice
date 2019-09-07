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

def binary_search(list, item_to_find, current_index=None):

    if current_index is None:
        current_index = len(list) // 2

    if len(list) == 0:
        return False
    elif len(list) == 1:
        if list[0] == item_to_find:
            return True
        else:
            return False

    if list[current_index] == item_to_find:
        return True
    elif item_to_find > list[current_index]:
        return binary_search(list[current_index:], item_to_find, len(list[current_index:]) // 2)
    elif item_to_find < list[current_index]:
        return binary_search(list[:current_index], item_to_find, len(list[:current_index]) // 2)
