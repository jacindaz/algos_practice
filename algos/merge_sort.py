def merge_sort(list_to_sort):
    if len(list_to_sort) <= 1:
        return list_to_sort

    left_list = []
    right_list = []
    for index, item in enumerate(list_to_sort):
        if index < (int(len(list_to_sort)/2)):
            left_list.append(item)
        else:
            right_list.append(item)

    left = merge_sort(left_list)
    right = merge_sort(right_list)

    return merge(left, right)


def merge(left_list, right_list):
    result = []
    while len(left_list) > 0 and len(right_list) > 0:
        if left_list[0] > right_list[0]:
            result.append(right_list[0])
            right_list.remove(right_list[0])

        elif left_list[0] < right_list[0]:
            result.append(left_list[0])
            left_list.remove(left_list[0])

    while len(left_list) > 0:
        result.append(left_list[0])
        left_list.remove(left_list[0])

    while len(right_list) > 0:
        result.append(right_list[0])
        right_list.remove(right_list[0])

    return result
