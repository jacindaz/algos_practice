
my_list = [4,3,2,10,12,1,5,6]
expected = [1,2,3,4,5,6,10,12]
def insertion_sort(list):
    # Assume anything to the left of you is sorted
    # move pointer to left 1 item
    # keep moving item until it is in the right place
    for current_index, current_item in enumerate(list[1:], start=1):
        previous_index = current_index - 1

        print("\n===========\n")
        print(f"current_index: {current_index}, current_item: {current_item}")
        print(f"previous_index (outside while loop): {previous_index}")

        while previous_index >= 0:
            if current_item < list[previous_index]:
                # import ipdb; ipdb.set_trace()

                print("\nswapping.......")
                print(f"current_item: {current_item}, previous_item: {list[previous_index]}")
                print(f"current_index: {current_index}, previous_index: {previous_index}")
                # swap
                previous_item = list[previous_index]
                list[previous_index] = current_item
                list[current_index] = previous_item
                previous_index -= 1
                current_index -= 1

                print(f"list: {list}")
            else:
                break

    return list

print(insertion_sort(my_list))
