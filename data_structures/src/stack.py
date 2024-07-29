from __future__ import annotations


class Stack:

    __current_node: Node

    def __init__(self):
        self.__current_node = None

    def push(self, node: Node):
        node.set_next_node(self.__current_node)
        self.__current_node = node

    def pop(self) -> Node:
        if self.__current_node is None:
            return None

        result = self.__current_node

        self.__current_node = self.__current_node.get_next_node()

        return result

    def peek(self):
        return self.__current_node

    def is_empty(self) -> bool:
        return True if self.__current_node is None else False

    def __str__(self):
        result = ""

        iterator = self.__current_node
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


stack = Stack()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

stack.push(node1)
stack.push(node2)
stack.push(node3)
stack.push(node4)

stack.pop()

print(stack)

