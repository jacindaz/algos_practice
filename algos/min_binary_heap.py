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


def percolate_down(existing_heap, item_index=1):
    item = existing_heap[item_index]

    print(f"\nexisting_heap: {existing_heap}, line 64")
    print(f"item: {item}, item_index: {item_index}")

    max_index = len(existing_heap) - 1

    # travel down the tree
    # continue down left node
    left_child_index = item_index*2
    left_child = None
    if left_child_index <= max_index:
        left_child = existing_heap[left_child_index]
        print(f"\nleft_child_index: {left_child_index}, left_child: {left_child}")

    right_child_index = (item_index * 2) + 1
    right_child = None
    if right_child_index <= max_index:
        right_child = existing_heap[right_child_index]

    # swap until the left child is not
    #   smaller than the item
    if left_child and left_child < item:
        existing_heap[left_child_index] = item
        existing_heap[item_index] = left_child
        print(f"\nexisting_heap: {existing_heap}, line 78")

        percolate_down(existing_heap, left_child_index)
    elif right_child and right_child < item:
        existing_heap[item_index] = right_child
        existing_heap[right_child_index] = item

    return existing_heap


def delete_min(existing_heap):
    print(f"\nexisting_heap before swap: {existing_heap}\n")
    min_to_del = existing_heap[1]

    # delete
    # readjust tree:
    #   -> swap last item in list and root
    #      (this maintains heap property)
    #   -> percolate down swapped item
    #      (this maintains order property)

    # swap
    last_item = existing_heap[-1]
    existing_heap[1] = last_item
    existing_heap[-1] = min_to_del
    print(f"last_item: {last_item}, min_to_del: {min_to_del}")
    print(f"existing_heap after swap: {existing_heap}")

    min_deleted = existing_heap[:-1]
    if len(existing_heap) == 3:
        return min_deleted
    else:
        return percolate_down(min_deleted)
