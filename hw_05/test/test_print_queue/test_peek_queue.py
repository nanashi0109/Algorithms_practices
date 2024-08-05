from hw_05.src.print_queue import *
from datetime import datetime
import pytest


@pytest.fixture(scope="function")
def pre_condition():
    queue = PrintQueue()

    documents = [
                PrintDocument("title_1", 5),
                PrintDocument("title_2", 10),
                PrintDocument("title_3", 15),
                PrintDocument("title_4", 20),
            ]

    for doc in documents:
        queue.enqueue(doc)

    return queue


@pytest.mark.hw_05
@pytest.mark.print_queue
@pytest.mark.parametrize("expected_result",
                         [
                             "title_1",
                         ])
def test_peek_positive_1(expected_result, pre_condition):
    assert pre_condition.peek().title == expected_result


@pytest.mark.hw_05
@pytest.mark.print_queue
@pytest.mark.parametrize("count_dequeues, expected_result",
                         [
                             (2, "title_3"),
                             (3, "title_4"),
                         ])
def test_peek_positive_2(count_dequeues, expected_result, pre_condition):
    for i in range(0, count_dequeues, 1):
        pre_condition.dequeue()

    assert pre_condition.peek().title == expected_result


@pytest.mark.hw_05
@pytest.mark.print_queue
@pytest.mark.parametrize("count_dequeues, expected_result",
                         [
                             (5, None),
                             (10, None)
                         ])
def test_peek_negative(count_dequeues, expected_result, pre_condition):
    for i in range(0, count_dequeues, 1):
        pre_condition.dequeue()

    assert pre_condition.peek() == expected_result
