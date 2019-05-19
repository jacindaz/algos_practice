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

min_heap1 = [0,5,9,11]
min_heap2 = [0,5,9,11,14,18,19,21,33,17,27]

# Insertion properties:
#   => p: index of parent
#   => left child: position 2p
#   => right child: 2p + 1
#   => find parent of node: n/2 (discard remainder)
# Insertion steps:
#   => insert the node from left -> right
#   => percolate up

def insert_node(new_item, existing_heap):
    max_index = len(existing_heap) - 1

    # start at root
    root_index = 1
    root = existing_heap[root_index]
    left_index = 2*(root_index)
    right_index = 2*(root_index) + 1
    print("\n=============\n")
    print(f"existing_heap: {existing_heap}")
    print(f"root_index: {root_index}, root: {root}")
    print(f"left_index: {left_index}, right_index: {right_index}")
    print("\n")

    # if new item is larger than the root
    # and the root doesn't have BOTH: a left and right child
    if new_item > root and (left_index > max_index or right_index > max_index):
        if left_index > max_index:
            print("no left child node")

        elif right_index > max_index:
            print("no right child node")

            # not sure if this always works?
            # maybe need to grow array to the size of right_index
            existing_heap.append(new_item)

    return existing_heap

# current tree:
#    5
#  /   \
# 9
# print(insert(12, [0,5,9,11]))
print(insert(11, [0,5,9]))
# expected tree
#    5
#  /   \
# 9    11
