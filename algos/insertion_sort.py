def insertion_sort(list):
    for current_index, current_item in enumerate(list[1:], start=1):
        previous_index = current_index - 1
        while previous_index >= 0:
            if current_item < list[previous_index]:
                previous_item = list[previous_index]
                list[previous_index] = current_item
                list[current_index] = previous_item

                previous_index -= 1
                current_index -= 1
            else:
                break

    return list
