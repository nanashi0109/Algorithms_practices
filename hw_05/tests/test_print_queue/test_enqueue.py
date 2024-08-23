from hw_05.src.print_queue import *
import pytest


@pytest.fixture(scope="function")
def pre_condition():
    queue = PrintQueue()

    return queue


@pytest.mark.hw_05
@pytest.mark.print_queue
@pytest.mark.parametrize("document, count_documents, expected_result",
                         [
                             (PrintDocument("title_1", 5), 1, "(head) <- title_1 <- (tail) <- None"),
                             (PrintDocument("title_2", 5), 1, "(head) <- title_2 <- (tail) <- None")
                         ])
def test_enqueue_positive_1(document, count_documents, expected_result, pre_condition):
    pre_condition.enqueue(document)

    assert str(pre_condition) == expected_result
    assert pre_condition.count() == count_documents


@pytest.mark.hw_05
@pytest.mark.print_queue
@pytest.mark.parametrize("documents, count_documents, expected_result",
                         [
                             ([
                                  PrintDocument("title_1", 5),
                                  PrintDocument("title_2", 5),
                                  PrintDocument("title_3", 5),
                                  PrintDocument("title_4", 5),
                              ], 4, "(head) <- title_1 <- title_2 <- title_3 <- title_4 <- (tail) <- None"),

                         ])
def test_enqueue_positive_2(documents, count_documents, expected_result, pre_condition):
    for document in documents:
        pre_condition.enqueue(document)

    assert str(pre_condition) == expected_result
    assert pre_condition.count() == count_documents
