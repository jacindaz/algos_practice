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
