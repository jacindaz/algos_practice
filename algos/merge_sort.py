import ipdb

my_list1 = [38, 27]
my_list2 = [38, 27, 43, 3]
my_list3 = [38, 27, 43, 3, 9, 82, 10, 8]

odd_list1 = [38, 27, 43, 3, 9, 82]
odd_list2 = [38, 27, 43, 3, 9, 82, 10]

def merge_sort(list_to_sort, new_list, split_index=None):
    print("\n============")
    print(f"new_list: {new_list}")
    print(f"split_index: {split_index}")

    if split_index is None:
        split_index = int(len(list_to_sort)/2)

    if split_index == 0:
        print(f"base case. new_list: {new_list}")
        return new_list

    if split_index >= 1:
        new_split_index = int(split_index/2)

        new_list_1 = new_list[0][:split_index]
        new_list_2 = new_list[0][split_index:]
        recursed_new_list = [new_list_1, new_list_2]
        new_list[0] = recursed_new_list
        print(f"recursed_new_list: {recursed_new_list}, new_list: {new_list}")
        merge_sort(list_to_sort, recursed_new_list, new_split_index)

        print(f"\ninside if statement, new_list: {new_list}")
        print(f"split_index: {split_index}")

        if split_index == int(len(list_to_sort)/2):
            return new_list

        new_list_1 = new_list[1][:split_index]
        new_list_2 = new_list[1][split_index:]
        recursed_new_list = [new_list_1, new_list_2]
        new_list[1] = recursed_new_list
        print(f"recursed_new_list: {recursed_new_list}, new_list: {new_list}")
        merge_sort(list_to_sort, recursed_new_list, new_split_index)


# print(merge_sort(my_list1, [my_list1]))
# print(merge_sort(my_list2, [my_list2]))
print(merge_sort(my_list3, [my_list3]))
