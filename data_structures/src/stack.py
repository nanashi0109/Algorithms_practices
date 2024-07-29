from __future__ import annotations


class Stack:

    __top: Node

    def __init__(self):
        self.__top = None
        self.__count = 0

    def push(self, item: Node):
        item.set_next_node(self.__top)
        self.__top = item

        self.__count += 1

    def pop(self) -> Node:
        if self.__top is None:
            return None

        result = self.__top

        self.__top = self.__top.get_next_node()

        self.__count -= 1

        return result

    def peek(self):
        return self.__top

    def is_empty(self) -> bool:
        return True if self.__top is None else False

    def __str__(self):
        result = ""

        iterator = self.__top
        while not (iterator is None):
            result += f"{iterator.get_data()} -> "
            iterator = iterator.get_next_node()

        result += "None"

        return result


class Node:
    def __init__(self, data: any, next_node: Node = None) -> None:
        self.__next_node = next_node
        self.__data = data

    def set_next_node(self, new_node: Node) -> None:
        self.__next_node = new_node

    def get_next_node(self) -> Node:
        return self.__next_node

    def get_data(self) -> any:
        return self.__data


# stack = Stack()
#
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
#
# stack.push(node1)
# stack.push(node2)
# stack.push(node3)
# stack.push(node4)
#
# stack.pop()
#
# print(stack)

