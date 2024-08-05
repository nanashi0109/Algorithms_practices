from hw_05.src.print_queue import *
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
@pytest.mark.parametrize("count_documents, expected_result",
                         [
                             (3, "(head) <- title_2 <- title_3 <- title_4 <- (tail) <- None"),
                         ])
def test_dequeue_positive_1(count_documents, expected_result, pre_condition):
    pre_condition.dequeue()

    assert str(pre_condition) == expected_result
    assert pre_condition.count() == count_documents


@pytest.mark.hw_05
@pytest.mark.print_queue
@pytest.mark.parametrize("count_dequeue, count_documents, expected_result",
                         [
                             (1, 3, "(head) <- title_2 <- title_3 <- title_4 <- (tail) <- None"),
                             (2, 2, "(head) <- title_3 <- title_4 <- (tail) <- None"),
                             (3, 1, "(head) <- title_4 <- (tail) <- None"),
                             (4, 0, "(head) <- (tail) <- None"),
                         ])
def test_dequeue_positive_2(count_dequeue, count_documents, expected_result, pre_condition):
    for i in range(0, count_dequeue, 1):
        pre_condition.dequeue()

    assert str(pre_condition) == expected_result
    assert pre_condition.count() == count_documents
