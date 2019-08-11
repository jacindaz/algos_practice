class Dequeue(object):
    def __init__(self, items=[]):
        self._items = items

    def add_front(self, item):
        """front is index -1 of a list"""
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        self._items.pop()

    def remove_rear(self):
        self._items.pop(0)

    def is_empty(self):
        return size._items == []

    def size(self):
        return len(self._items)
