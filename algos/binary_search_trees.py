import ipdb
import pprint

def depth_first_search(tree, item_to_find, current_node):
    left_node, right_node = tree.get(current_node, (None, None))
    if current_node is None:
        return False
    elif item_to_find == current_node:
        return True

    if item_to_find > current_node:
        return depth_first_search(tree, item_to_find, right_node)
    elif item_to_find < current_node:
        return depth_first_search(tree, item_to_find, left_node)

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


def find_max_iterate(tree, current_node):
    max = current_node

    iterate_node = current_node
    while tree.get(iterate_node) != None:
        right_node = tree[iterate_node][1]
        if right_node is None:
            break
        elif max <= right_node:
            max = right_node
            iterate_node = right_node

    return max


def find_max_recurse(tree, current_node, max=None):
    _, right_node = tree.get(current_node, (None, None))

    if max is None:
        max = current_node

    if current_node and max <= current_node:
        max = current_node
        return find_max_recurse(tree, right_node, max)

    if right_node is None:
        return max


def find_min_recurse(tree, current_node, min_node = None):
    left_node, _ = tree.get(current_node, (None, None))

    if current_node is None:
        return min_node

    if min_node is None:
        min_node = current_node

    if current_node <= min_node:
        min_node = current_node
        return find_min_recurse(tree, left_node, min_node)
