def bubble_sort(my_list):
    for item in my_list:
        index1 = 0
        index2 = 1
        max_index = len(my_list)-1
        while index2 <= max_index:
            item1 = my_list[index1]
            item2 = my_list[index2]
            if item1 > item2:
                placeholder = item1
                my_list[index1] = item2
                my_list[index2] = placeholder
            index1 += 1
            index2 += 1
    return my_list


def selection_sort(my_list):
    current_index = 0
    max_index = len(my_list)-1
    while current_index <= max_index:
        # iterate over list, find smallest item
        smallest_item = min(my_list[current_index:])

        # once finds the smallest item, move to beginning of list
        my_list.remove(smallest_item)
        my_list.insert(current_index, smallest_item)

        print(my_list)

        # once finds 2nd smallest item, knows to put that in the 2nd spot of the list
        # so eventually scans less and less of the list
        current_index += 1
    return my_list


def insertion_sort(my_list):
    max_index = len(my_list)-1

    for current_index, current_item in enumerate(my_list):
        current_item_index = current_index
        previous_item_index = current_index-1

        print("\n========================")
        print(f"current_item_index: {current_item_index}, previous_item_index: {previous_item_index}")

        # if finds an item that is not in the right place
        # swaps with item before until it is in the right place
        current_item = my_list[current_item_index]
        previous_item = my_list[previous_item_index]

        while current_item < previous_item \
            and previous_item_index >= 0 \
            and current_item_index >= 1 \
            and current_item_index <= max_index:

            print(f"\ncurrent_item: {current_item}, current_item_index: {current_item_index}")
            print(f"previous_item: {previous_item}, previous_item_index: {previous_item_index}")

            # swap
            print(f"my_list before swap: {my_list}")
            my_list[current_item_index] = previous_item
            my_list[previous_item_index] = current_item
            print(f"my_list after swap: {my_list}")

            current_item_index = previous_item_index
            previous_item_index -= 1
            current_item = my_list[current_item_index]
            previous_item = my_list[previous_item_index]

        # then moves onto next item that is not in the right place

        # it remembers which two items it checked last
        # (so jumps to there after it puts previous item in the right place)
    return my_list
