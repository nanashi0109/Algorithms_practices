from __future__ import annotations


class PriorityQueue:

    __head: Node
    __tail: Node

    def __init__(self):

        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self, item: Node):
        if self.__tail is None:
            self.__tail = item
            self.__head = item

        elif self.__tail.get_priority() <= item.get_priority():
            self.__tail.set_next_node(item)
            self.__tail = item
        else:
            iterator = self.__head
            while iterator.get_next_node().get_priority() <= item.get_priority():
                iterator = iterator.get_next_node()

            item.set_next_node(iterator.get_next_node())
            iterator.set_next_node(item)

        self.__count += 1

    def dequeue(self):
        if self.__head is None:
            return None

        result = self.__head

        self.__head = self.__head.get_next_node()
        self.__count -= 1
        return result

    def peek(self) -> Node:
        return self.__head

    def is_empty(self) -> bool:
        return True if self.__head is None else False

    def __str__(self):
        result = "(head) -> "

        iterator = self.__head
        while not (iterator.get_next_node() is None):
            result += f"({iterator.get_data()} : {iterator.get_priority()}) -> "
            iterator = iterator.get_next_node()
        result += "None"
        return result


class Node:
    def __init__(self, data: any, priority: int):
        self.__data = data
        self.__next_node = None
        self.__priority = priority

    def set_next_node(self, new_node) -> None:
        self.__next_node = new_node

    def get_next_node(self) -> Node:
        return self.__next_node

    def get_priority(self) -> int:
        return self.__priority

    def get_data(self) -> any:
        return self.__data


# queue = PriorityQueue()
#
# n1 = Node(1, 1)
# n2 = Node(2, 2)
# n3 = Node(3, 3)
# n4 = Node(4, 4)
# n5 = Node(5, 5)
# n6 = Node(6, 2)
# n7 = Node(7, 3)
#
# queue.enqueue(n1)
# queue.enqueue(n4)
# queue.enqueue(n3)
# queue.enqueue(n2)
# queue.enqueue(n5)
# queue.enqueue(n6)
# queue.enqueue(n7)
#
# queue.dequeue()
# queue.dequeue()
#
# print(queue)
