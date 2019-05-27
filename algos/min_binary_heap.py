import ipdb

# Min binary heap
#   => children nodes must be larger than parent node
#   => binary: only 2 nodes per parent

# Complete binary tree
#   => in this implementation, we are assuming our tree
#      is a complete binary tree
#   => a complete binary tree is a tree in which each level
#      (except the last level), has all of its nodes
#   => you fill in a complete binary tree w/ nodes from
#      left to right

# Insertion properties:
#   => p: index of parent
#   => left child: position 2p
#   => right child: 2p + 1
#   => find parent of node: n/2 (discard remainder)
# Insertion steps:
#   => insert the node from left -> right
#   => percolate up

def percolate_node_up(existing_tree, new_item, new_item_index=None):
    if new_item_index is None:
        new_item_index = len(existing_tree)-1

    parent_index = int(new_item_index/2)
    parent = existing_tree[parent_index]

    print(f"tree: {existing_tree}")
    print(f"new_item: {new_item}, new_item_index: {new_item_index}")
    print(f"parent: {parent}, parent_index: {parent_index}")

    if parent > new_item:
        parent_to_swap = parent
        existing_tree[parent_index] = new_item
        existing_tree[new_item_index] = parent_to_swap

        print("\n-------------swapped-------------")
        print(f"tree: {existing_tree}")
        print(f"new_item: {new_item}, new_item_index: {new_item_index}")
        print(f"parent: {parent}, parent_index: {parent_index}")

        percolate_node_up(existing_tree, new_item, parent_index)

    print("\n-------------recursion ends-------------")
    print(f"existing_tree: {existing_tree}")
    return existing_tree


def insert(existing_heap, new_item):
    existing_heap.append(new_item)
    final_tree = percolate_node_up(existing_heap, new_item)

    print("\n-------------final tree-------------")
    print(f"final_tree: {final_tree}")
    return final_tree
