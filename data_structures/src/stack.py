from __future__ import annotations


class Stack:
    class Node:

        prev_node: Stack.Node

        def __init__(self, data: any, next_node: Stack.Node = None) -> None:
            self.prev_node = next_node
            self.data = data

    __top: Node

    def __init__(self):
        self.__top = None
        self.__count = 0

    def push(self, item: any):
        node = Stack.Node(item)

        node.prev_node = self.__top
        self.__top = node

        self.__count += 1

    def pop(self) -> Node or None:
        if self.is_empty():
            return None

        result = self.__top.data

        self.__top = self.__top.prev_node

        self.__count -= 1

        return result

    def peek(self):
        return self.__top.data

    def is_empty(self) -> bool:
        return True if self.__count == 0 else False

    def __str__(self):
        result = ""

        iterator = self.__top
        while not (iterator is None):
            result += f"{iterator.data} -> "
            iterator = iterator.prev_node

        result += "None"

        return result


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

stack.pop()

print(stack)

