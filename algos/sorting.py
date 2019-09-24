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
