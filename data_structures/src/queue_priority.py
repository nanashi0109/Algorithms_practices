from __future__ import annotations


class PriorityQueue:
    class Node:

        next_node: PriorityQueue.Node or None

        def __init__(self, data: any, priority: int):
            self.data = data
            self.next_node = None
            self.priority = priority

    __head: Node
    __tail: Node

    def __init__(self):

        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self, item: any, priority: int) -> None:
        node = PriorityQueue.Node(item, priority)

        if self.is_empty():
            self.__tail = node
            self.__head = node

        elif self.__tail.priority <= node.priority:
            self.__tail.next_node = node
            self.__tail = node
        else:
            iterator = self.__head
            while iterator.next_node.priority <= node.priority:
                iterator = iterator.next_node

            node.next_node = iterator.next_node
            iterator.next_node = node

        self.__count += 1

    def dequeue(self) -> Node or None:
        if self.is_empty():
            return None

        result = self.__head.data

        self.__head = self.__head.next_node
        self.__count -= 1
        return result

    def peek(self) -> Node:
        return self.__head.data

    def is_empty(self) -> bool:
        return True if self.__count == 0 else False

    def __str__(self):
        result = "(head) -> "

        iterator = self.__head
        while not (iterator.next_node is None):
            result += f"({iterator.data} : {iterator.priority}) -> "
            iterator = iterator.next_node
        result += "None"
        return result


# queue = PriorityQueue()
#
# queue.enqueue(1, 1)
# queue.enqueue(4, 2)
# queue.enqueue(3, 3)
# queue.enqueue(2, 4)
# queue.enqueue(5, 5)
# queue.enqueue(6, 2)
# queue.enqueue(7, 3)
#
# queue.dequeue()
# queue.dequeue()
#
# print(queue)
