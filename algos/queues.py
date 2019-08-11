class Queue(object):
    def __init__(self, items=[]):
        self._items = items

    def is_empty(self):
        return len(self._items) == 0

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        self._items.pop()

    def size(self):
        return len(self._items)

# blah = Queue([1,2,3])
# blah.enqueue(4)
# print(blah._items)

# blah.dequeue()
# print(blah._items)


# We will implement a general simulation of Hot Potato.
# Our program will input a list of names and a constant,
# call it “num,” to be used for counting. It will return
# the name of the last person remaining after repetitive counting by num.

# To simulate the circle, we will use a queue. Assume that
# the child holding the potato will be at the front of the queue.
# Upon passing the potato, the simulation will simply
# dequeue and then immediately enqueue that child, putting
# her at the end of the line. She will then wait until
# all the others have been at the front before it will be
# her turn again. After num dequeue/enqueue operations,
# the child at the front will be removed permanently and another cycle will begin. This process will continue until only one name remains (the size of the queue is 1).

def hot_potato(name_queue, constant_num=-1):
    # child holding potato at the front of the queue
    # front of the queue: index -1 of the list
    name_that_ends_game = name_queue[constant_num]
    hot_potato_queue = Queue(name_queue)
    print(f"\n=============\n")
    print(f"hot_potato_queue: {hot_potato_queue._items}")

    # passing the potato: dequeue + enqueue (end of the line) the same child
    hot_potato_queue.dequeue()
    print(f"\ndequeued, new hot_potato_queue: {hot_potato_queue._items}")

    # do another round where the same child is dequeued again
    hot_potato_queue.enqueue(name_that_ends_game)
    print(f"\nenqueued, new hot_potato_queue: {hot_potato_queue._items}\n")

    while hot_potato_queue.size() > 1:
        # another cycle begins
        # the game ends when only 1 name remains
        # (size of the queue is 1)
        hot_potato_queue.dequeue()
        print(hot_potato_queue._items)

    print(f"\nname_queue: {name_queue}")
    return name_queue


hot_potato(["kenrick", "krithin", "julia", "val", "jacinda"])


