class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert_left(self, child):
        if self.left is None:
            self.left = child
        else:
            child.left = self.left
            self.left = child

    def insert_right(self, child):
        if self.right is None:
            self.right = child
        else:
            child.right = self.right
            self.right = child


def insert_left(root, child_value):
    left_subtree = root[1]
    if len(left_subtree) == 0:
        root[1] = [child_value, [], []]
    else:
        current_left_child = root[1]
        new_left_child = [child_value, current_left_child, []]
        root[1] = new_left_child
    return root
