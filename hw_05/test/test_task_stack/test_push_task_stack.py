from hw_05.src.task_stack import *
from datetime import datetime
import pytest


@pytest.fixture(scope="function")
def pre_condition():
    stack = TaskStack()

    return stack


@pytest.mark.hw_05
@pytest.mark.parametrize("task, count_tasks, expected_result",
                         [
                             (ProjectTask("desc_1", datetime(1, 1, 1)), 1, "desc_1 -> None"),
                             (ProjectTask("desc_2", datetime(2022, 11, 30)), 1, "desc_2 -> None")
                         ])
def test_push_positive_1(task, count_tasks, expected_result, pre_condition):
    pre_condition.push(task)

    assert str(pre_condition) == expected_result
    assert pre_condition.count() == count_tasks


@pytest.mark.hw_05
@pytest.mark.parametrize("tasks, count_tasks, expected_result",
                         [
                             ([
                                ProjectTask("desc_1", datetime(1, 1, 1)),
                                ProjectTask("desc_2", datetime(1, 1, 1)),
                                ProjectTask("desc_3", datetime(1, 1, 1)),
                                ProjectTask("desc_4", datetime(1, 1, 1)),
                                ], 4, "desc_4 -> desc_3 -> desc_2 -> desc_1 -> None")
                         ])
def test_push_positive_2(tasks, count_tasks, expected_result, pre_condition):
    for task in tasks:
        pre_condition.push(task)

    assert str(pre_condition) == expected_result
    assert pre_condition.count() == count_tasks
