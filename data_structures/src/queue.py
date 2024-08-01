from __future__ import annotations


class Queue:
    class Node:

        next_node: Queue.Node

        def __init__(self, data: any):
            self.data = data
            self.next_node = None

    __head: Node
    __tail: Node

    def __init__(self):
        self.__count = 0

        self.__head = None
        self.__tail = None

    def enqueue(self, item: any) -> None:
        node = Queue.Node(item)

        if self.is_empty():
            self.__head = node
        else:
            self.__tail.next_node = node

        self.__tail = node
        self.__count += 1

    def dequeue(self) -> Node:
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

    def get_count(self) -> int:
        return self.__count

    def __str__(self):
        result = "(head) <- "

        iterator = self.__head
        while not (iterator is None):
            result += f"{iterator.data} <- "
            iterator = iterator.next_node

        result += "(tail) <- None"

        return result


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print(queue.dequeue())
print(queue.dequeue())


print(queue.get_count())
print(queue)
