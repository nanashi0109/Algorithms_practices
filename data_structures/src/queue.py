from __future__ import annotations


class Queue:
    __head: Node
    __tail: Node

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self, item: Node) -> None:
        if self.__tail is None:
            self.__head = item
        else:
            self.__tail.set_next_node(item)

        self.__tail = item
        self.__count += 1

    def dequeue(self) -> Node:
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

    def get_count(self) -> int:
        return self.__count

    def __str__(self):
        result = "(head) <- "

        iterator = self.__head
        while not (iterator is None):
            result += f"{iterator.get_data()} <- "
            iterator = iterator.get_next_node()

        result += "(tail) <- None"

        return result


class Node:
    def __init__(self, data: any, next_node: Node = None):
        self.__data = data
        self.__next_node = next_node

    def set_next_node(self, new_node: Node) -> None:
        self.__next_node = new_node

    def get_next_node(self) -> Node:
        return self.__next_node

    def get_data(self) -> any:
        return self.__data


# queue = Queue()
#
# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)
#
# queue.enqueue(n1)
# queue.enqueue(n2)
# queue.enqueue(n3)
# queue.enqueue(n4)
# queue.enqueue(n5)
#
# queue.dequeue()
# queue.dequeue()
#
#
# print(queue.get_count())
# print(queue)
