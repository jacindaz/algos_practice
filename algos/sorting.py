def bubble_sort(my_list):
    for item in my_list:
        index1 = 0
        index2 = 1
        max_index = len(my_list)-1

        while index2 <= max_index:
            item1 = my_list[index1]
            item2 = my_list[index2]
            print("\n==============")
            print(f"item1: {item1}, index1: {index1}")
            print(f"item2: {item2}, index2: {index2}")

            if item1 > item2:
                # swap
                print(f"\nswapping! old list: {my_list}")
                placeholder = item1
                my_list[index1] = item2
                my_list[index2] = placeholder
                print(f"new list: {my_list}")

            # increment by 1
            index1 += 1
            index2 += 1

    return my_list

list1 = [-1,8,11,22,9,-5,2]   # -> [-5,-1,2,8,9,11,22]
print(bubble_sort(list1))
