import ipdb
import pprint


def insert(tree, item_to_insert, current_node):
    left_node, right_node = tree.get(current_node, (None, None))
    print("\n==============")
    print(f"current_node: {current_node}")
    print(f"left_node: {left_node}, right_node: {right_node}")

    # base case
    if tree.get(current_node) is None:
        if item_to_insert > current_node:
            tree[current_node] = (None, item_to_insert)
            return tree
        elif item_to_insert < current_node:
            tree[current_node] = (item_to_insert, None)
            return tree
    else:
        if item_to_insert > current_node and right_node is None:
            tree[current_node] = (left_node, item_to_insert)
            return tree
        elif item_to_insert < current_node and left_node is None:
            tree[current_node] = (item_to_insert, right_node)
            return tree

    # if new item bigger than current node, go right
    if item_to_insert > current_node:
        return insert(tree, item_to_insert, right_node)
    # if new item smaller than current node, go left
    if item_to_insert < current_node:
        return insert(tree, item_to_insert, left_node)


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
