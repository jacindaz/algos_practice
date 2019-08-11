class Dequeue(object):
    def __init__(self, items=[]):
        self._items = items

    def add_front(self, item):
        """front is index -1 of a list"""
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        return self._items.pop()

    def remove_rear(self):
        return self._items.pop(0)

    def is_empty(self):
        return self._items == []

    def size(self):
        return len(self._items)


def is_palindrome(string):
    dequeue = Dequeue([char for char in string])

    result = False
    while not dequeue.is_empty():
        if dequeue.size() == 1:
            return True
        else:
            front = dequeue.remove_front()
            rear = dequeue.remove_rear()

            if front == rear:
                result = True
            elif (front is None and rear is not None) or (front is not None and rear is None):
                result = True
            else:
                return False

    return result
