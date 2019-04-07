def insert(tree, item_to_insert):
    print(tree)

    for index, item in enumerate(tree[1:], start=1):

        if item == tree[-1] and item_to_insert > item:
            tree.insert(len(tree), item_to_insert)
            return tree

        previous = tree[index-1]

        if item_to_insert > item and item_to_insert < previous:
            tree.insert(index, item_to_insert)
            return tree

        elif item_to_insert < item and item_to_insert > previous:
            tree.insert(index, item_to_insert)
            return tree


def find_max(tree):
    max = tree[0]
    for item in tree:
        if item > max:
            max = item

    return max

def find_min(tree):
    min = tree[0]
    for item in tree:
        if item < min:
            min = item

    return min
