from __future__ import annotations


class LinkedList:

    class Node:
        next_node: LinkedList.Node

        def __init__(self, data: any):
            self.data = data
            self.next_node = None

    def __init__(self):
        self.__top = None

    def push(self):
        pass

    def pop(self):
        pass

    def peek(self):
        pass



