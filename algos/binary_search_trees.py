import ipdb
import pprint


def insert(tree, item_to_insert, current_node):

    # TODO: if tree has 0, 1, or 2 nodes

    child_nodes = tree[current_node]
    left_node = child_nodes[0]
    right_node = child_nodes[1]

    print("\n===================")
    print(f"current_node: {current_node}")
    pprint.pprint(tree)
    print(f"\nchild_nodes: {child_nodes}")
    print(f"left_node: {left_node}, right_node: {right_node}")


    if item_to_insert > current_node:
        right_node_children = tree.get(right_node)
        if item_to_insert > right_node:
            if right_node_children:
                print("figure out recursion or something L35")
            else:
                tree[right_node] = (None, item_to_insert)
                return tree

        elif item_to_insert < right_node:
            if right_node_children:
                print("figure out recursion or something L42")
            else:
                tree[right_node] = (item_to_insert, None)
                return tree
    else:
        left_node_children = tree.get(left_node)
        if item_to_insert > left_node:
            if left_node_children:
                print("figure out recursion or something L50")
            else:
                tree[left_node] = (None, item_to_insert)
                return tree
        elif item_to_insert < left_node:
            if left_node_children:
                print("figure out recursion or something L56")
            else:
                tree[left_node] = (item_to_insert, None)
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
