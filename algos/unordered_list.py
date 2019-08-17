class Node(object):
    def __init__(self, value):
        self.value = value

        # It is always a good idea to explicitly assign None
        # to your initial next reference values.
        # this is called "grounding the node"
        self.next = None


class UnOrderedList(object):
    def __init__(self):
        self.head = None

    def add(self, item):
        """
        add(item) adds a new item to the list. It needs
        the item and returns nothing. Assume the item
        is not already in the list.
        """

        # add always adds at the head of the list
        # because otherwise need to traverse the entire list

        if self.is_empty():
            self.head = Node(item)
        else:
            new_head = Node(item)
            new_head.next = self.head

            self.head = new_head

    def remove(self, item):
        """
        remove(item) removes the item from the list. It needs
        the item and modifies the list. Assume the item is
        present in the list.
        """

        # search for the node to remove
        current_node = self.head
        previous_node = None
        while current_node:
            print(f"\ncurrent_node: {current_node.value}")
            if current_node.value == item:
                # need to fix pointers after node is removed
                if previous_node:
                    previous_node.next = current_node.next
                    current_node.next = None
                    break
                else:
                    next_item = current_node.next
                    self.head = next_item
                    break
            else:
                # keep track of previous/current node
                previous_node = current_node
                current_node = current_node.next

                print(f"previous_node: {previous_node.value}")
                print(f"current_node: {current_node.value}")


    def search(self, item):
        """
        search(item) searches for the item in the list.
        It needs the item and returns a boolean value.
        """
        current_node = self.head
        while current_node:
            if current_node.value == item:
                return True
            current_node = current_node.next

        return False

    def is_empty(self):
        """
        is_empty() tests to see whether the list is empty.
        It needs no parameters and returns a boolean value.
        """
        return self.head is None

    def size(self):
            return counter

    def append(self, item):
        """
        append(item) adds a new item to the end of the list
        making it the last item in the collection. It needs
        the item and returns nothing. Assume the item is not
        already in the list.
        """
        pass

    def index(self, item):
        """
        index(item) returns the position of item in the list.
        It needs the item and returns the index. Assume the
        item is in the list.
        """
        pass

    def insert(self, pos, item):
        """
        insert(pos, item) adds a new item to the list at position pos.
        It needs the item and returns nothing. Assume the
        item is not already in the list and there are enough
        existing items to have position pos.

        """
        pass

    def pop(self):
        """
        pop() removes and returns the last item in the list.
        It needs nothing and returns an item. Assume the list
        has at least one item.
        """
        pass

    def pop(self, pos):
        """
        pop(pos) removes and returns the item at position pos.
        It needs the position and returns the item. Assume
        the item is in the list.

        """
        pass
