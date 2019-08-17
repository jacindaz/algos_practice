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
        current_node = self.head
        previous_node = None
        while True:
            if current_node.value == item:
                break
            previous_node, current_node = current_node, current_node.next

        if previous_node:
            previous_node.next = current_node.next
        else:
            self.head = current_node.next

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
        """
        size() returns the number of items in the list. It
        needs no parameters and returns an integer.
        """
        if self.is_empty():
            return 0
        else:
            counter = 0
            current_node = self.head
            while current_node:
                counter += 1
                current_node = current_node.next

            return counter

    def append(self, item):
        """
        append(item) adds a new item to the end of the list
        making it the last item in the collection. It needs
        the item and returns nothing. Assume the item is not
        already in the list.
        """
        current_node = self.head
        previous_node = None
        while current_node:
            previous_node, current_node = current_node, current_node.next

        previous_node.next = Node(item)

    def index(self, item):
        """
        index(item) returns the position of item in the list.
        It needs the item and returns the index. Assume the
        item is in the list.
        """
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == item:
                return index
            index += 1
            current_node = current_node.next

    def insert(self, pos, item):
        """
        insert(pos, item) adds a new item to the list at position pos.
        It needs the item and returns nothing. Assume the
        item is not already in the list and there are enough
        existing items to have position pos.
        """
        current_node = self.head
        previous_node = None
        index = 0
        while True:
            if index == pos:
                new_item = Node(item)
                if previous_node:
                    previous_node.next = new_item
                else:
                    self.head = new_item

                new_item.next = current_node
                break
            else:
                previous_node, current_node = current_node, current_node.next
                index += 1

    def pop_last_item(self):
        """
        pop() removes and returns the last item in the list.
        It needs nothing and returns an item. Assume the list
        has at least one item.

        pop(pos) removes and returns the item at position pos.
        It needs the position and returns the item. Assume
        the item is in the list.
        """
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.next is None:
                break
            previous_node, current_node = current_node, current_node.next
        previous_node.next = None
        return current_node.value

    def pop(self, pos):
        """
        pop(pos) removes and returns the item at position pos.
        It needs the position and returns the item. Assume
        the item is in the list.
        """
        current_node = self.head
        previous_node = None
        index = 0
        while True:
            if index == pos:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    # at the head
                    self.head = current_node.next
                return current_node.value
            index += 1
            previous_node, current_node = current_node, current_node.next
