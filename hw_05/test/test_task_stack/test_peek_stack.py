from hw_05.src.task_stack import *
from datetime import datetime
import pytest


@pytest.fixture(scope="function")
def pre_condition():
    stack = TaskStack()

    tasks = [
                ProjectTask("desc_1", datetime(1, 1, 1)),
                ProjectTask("desc_2", datetime(1, 1, 1)),
                ProjectTask("desc_3", datetime(1, 1, 1)),
                ProjectTask("desc_4", datetime(1, 1, 1)),
            ]

    for task in tasks:
        stack.push(task)

    return stack


@pytest.mark.hw_05
@pytest.mark.task_stack
@pytest.mark.parametrize("expected_result",
                         [
                             "desc_4",
                         ])
def test_peek_positive_1(expected_result, pre_condition):
    assert pre_condition.peek().description == expected_result


@pytest.mark.hw_05
@pytest.mark.task_stack
@pytest.mark.parametrize("count_pops, expected_result",
                         [
                             (2, "desc_2"),
                             (3, "desc_1"),
                         ])
def test_peek_positive_2(count_pops, expected_result, pre_condition):
    for i in range(0, count_pops, 1):
        pre_condition.pop()

    assert pre_condition.peek().description == expected_result


@pytest.mark.hw_05
@pytest.mark.task_stack
@pytest.mark.parametrize("count_pops, expected_result",
                         [
                             (5, None),
                             (10, None)
                         ])
def test_peek_negative(count_pops, expected_result, pre_condition):
    for i in range(0, count_pops, 1):
        pre_condition.pop()

    assert pre_condition.peek() == expected_result
