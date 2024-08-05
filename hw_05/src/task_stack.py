from __future__ import annotations
from datetime import datetime


class ProjectTask:
    def __init__(self, description: str, due_date: datetime):
        self.__description = description
        self.__due_date = due_date

    def __get_description(self) -> str:
        return self.__description

    def __get_due_date(self) -> datetime:
        return self.__due_date

    description = property(__get_description)
    due_date = property(__get_due_date)


class TaskStack:
    class Node:
        prev_node: TaskStack.Node or None

        def __init__(self, task: ProjectTask):
            self.task = task
            self.prev_node = None

    __top: Node or None

    def __init__(self):
        self.__count = 0
        self.__top = None

    def push(self, task: ProjectTask) -> None:
        node = TaskStack.Node(task)

        if not self.is_empty():
            node.prev_node = self.__top

        self.__top = node
        self.__count += 1

    def pop(self) -> ProjectTask or None:
        if self.is_empty():
            return None

        task = self.__top.task

        self.__top = self.__top.prev_node
        self.__count -= 1

        return task

    def peek(self) -> ProjectTask or None:
        if self.is_empty():
            return None

        return self.__top.task

    def is_empty(self) -> bool:
        return True if self.__count == 0 else False

    def count(self) -> int:
        return self.__count

    def __str__(self):
        result = ""

        iterator = self.__top
        while not (iterator is None):
            result += f"{iterator.task.description} -> "
            iterator = iterator.prev_node

        result += "None"

        return result


# stack = TaskStack()
#
# task_1 = ProjectTask("desc 1", datetime(1, 1, 1))
# task_2 = ProjectTask("desc 2", datetime(2, 2, 2))
# task_3 = ProjectTask("desc 3", datetime(3, 3, 3))
# task_4 = ProjectTask("desc 4", datetime(4, 4, 4))
#
# stack.push(task_1)
# stack.push(task_2)
# stack.push(task_3)
# stack.push(task_4)
#
# print(stack)
#
# print(stack.peek().description)
#
# stack.pop()
# stack.pop()
#
# print(stack.peek().description)
#
# print(stack)
