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



list1 = [-1,8,11,22,9,-5,2]
print(selection_sort(list1))
