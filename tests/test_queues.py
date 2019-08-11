import pytest
import algos.queues as queues


@pytest.mark.parametrize("queue_items, method_name, inputs, expected_results", [
    pytest.param(
        [],
        "enqueue",
        [1,2,3],
        [[1], [2,1], [3,2,1]],
        id="enqueue"
    ),
    pytest.param(
        [5,4,3,2,1],
        "dequeue",
        ["no_input", "no_input"],
        [[5,4,3,2], [5,4,3]],
        id="dequeue"
    ),
])
def test_queue_methods(queue_items, method_name, inputs, expected_results):
    queue = queues.Queue(queue_items)

    for index, input_value in enumerate(inputs):
        if method_name == "enqueue":
            queue.enqueue(input_value)
        elif method_name == "dequeue":
            queue.dequeue()

        assert queue._items == expected_results[index]


def test_queue_length():
    queue1 = queues.Queue(["c", "b", "a"])
    assert queue1.size() == 3
    assert queue1.is_empty() is False

    queue2 = queues.Queue([])
    assert queue2.size() == 0
    assert queue2.is_empty() is True
