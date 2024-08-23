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
@pytest.mark.parametrize("count_tasks, expected_result",
                         [
                             (3, "desc_3 -> desc_2 -> desc_1 -> None"),
                         ])
def test_pop_positive_1(count_tasks, expected_result, pre_condition):
    pre_condition.pop()

    assert str(pre_condition) == expected_result
    assert pre_condition.count() == count_tasks


@pytest.mark.hw_05
@pytest.mark.task_stack
@pytest.mark.parametrize("count_pops, count_tasks, expected_result",
                         [
                             (2, 2, "desc_2 -> desc_1 -> None"),
                             (3, 1, "desc_1 -> None"),
                             (4, 0, "None")
                         ])
def test_pop_positive_2(count_pops, count_tasks, expected_result, pre_condition):
    for i in range(0, count_pops, 1):
        pre_condition.pop()

    assert str(pre_condition) == expected_result
    assert pre_condition.count() == count_tasks


@pytest.mark.hw_05
@pytest.mark.task_stack
@pytest.mark.parametrize("count_pops, expected_result",
                         [
                             (2, "desc_2"),
                             (3, "desc_1")
                         ])
def test_pop_positive_3(count_pops, expected_result, pre_condition):
    for i in range(0, count_pops, 1):
        pre_condition.pop()

    assert pre_condition.pop().description == expected_result


@pytest.mark.hw_05
@pytest.mark.task_stack
@pytest.mark.parametrize("count_pops, expected_result",
                         [
                             (5, None),
                             (19, None)
                         ])
def test_pop_negative(count_pops, expected_result, pre_condition):
    for i in range(0, count_pops, 1):
        pre_condition.pop()

    assert pre_condition.pop() == expected_result
