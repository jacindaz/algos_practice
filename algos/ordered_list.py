from algos.unordered_list import Node, UnOrderedList

class OrderedList(UnOrderedList):
    def __init__(self):
        UnOrderedList.__init__(self)

    def search(self, item):
        pass

    def add(self, item):
        """
        Add new items to list, ordered smallest to largest
        """
        if self.head is None:
            self.head = Node(item)
        else:
            current_node = self.head
            previous_node = None

            while True:
                if current_node is None:
                    previous_node.next = Node(item)
                    break
                elif item > current_node.value:
                    previous_node, current_node = current_node, current_node.next
                elif item <= current_node.value:
                    new_item = Node(item)
                    previous_node.next = new_item
                    new_item.next = current_node
                    break
