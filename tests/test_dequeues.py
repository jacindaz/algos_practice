import pytest
import algos.dequeues as dequeues

@pytest.mark.parametrize("queue_items, inputs, method_name, expected_outputs", [
    pytest.param(
        [],
        [1,2,3],
        "add_front",
        [[1], [1,2], [1,2,3]],
        id="add_front",
    ),
    pytest.param(
        ["a"],
        ["b", "c"],
        "add_rear",
        [["b", "a"], ["c", "b", "a"]],
        id="add_rear"
    ),
    pytest.param(
        ["hi", "bye", "hello", "goodbye"],
        ["no_input1", "no_input2", "no_input3"],
        "remove_front",
        [["hi", "bye", "hello"], ["hi", "bye"], ["hi"]],
        id="remove_front"
    ),
    pytest.param(
        [5,6,7],
        ["no_input1", "no_input2"],
        "remove_rear",
        [[6,7], [7]],
        id="remove_rear"
    ),
])
def test_dequeue_methods(queue_items, inputs, method_name, expected_outputs):
    dequeue = dequeues.Dequeue(queue_items)

    for index, input_value in enumerate(inputs):
        if method_name == "add_front":
            dequeue.add_front(input_value)
        elif method_name == "add_rear":
            dequeue.add_rear(input_value)
        elif method_name == "remove_front":
            dequeue.remove_front()
        elif method_name == "remove_rear":
            dequeue.remove_rear()

        assert dequeue._items == expected_outputs[index]


@pytest.mark.parametrize("input, expected_output", [
    pytest.param(
        "radar",
        True,
        id="palindrome1"
    ),
    pytest.param(
        "toot",
        True,
        id="palindrome2"
    ),
    pytest.param(
        "aloha",
        False,
        id="not_palindrome1"
    ),
    pytest.param(
        "hello",
        False,
        id="not_palindrome2"
    ),
])
def test_is_palindrome(input, expected_output):
    result = dequeues.is_palindrome(input)
    assert result == expected_output
