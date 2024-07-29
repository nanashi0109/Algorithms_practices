from __future__ import annotations


class Dec:
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

        item.set_prev_node(self.__tail)

        self.__tail = item
        self.__count += 1

    def dequeue(self) -> Node:
        if self.__head is None:
            return None

        result = self.__head

        self.__head = self.__head.get_next_node()
        self.__head.set_prev_node(None)

        self.__count -= 1
        return result

    def peek(self) -> Node:
        return self.__head

    def enqueue_head(self, item: Node) -> None:
        if self.__head is None:
            self.__tail = item
        else:
            self.__head.set_prev_node(item)

        item.set_next_node(self.__head)
        self.__head = item
        self.__count += 1

    def dequeue_tail(self) -> Node:
        if self.__tail is None:
            return None

        result = self.__tail

        self.__tail = self.__tail.get_prev_node()
        self.__tail.set_next_node(None)

        self.__count -= 1
        return result

    def peek_tail(self) -> Node:
        return self.__tail

    def is_empty(self) -> bool:
        return True if self.__head is None else False

    def get_count(self) -> int:
        return self.__count

    def __str__(self):
        result = "None <- (head) <- "

        iterator = self.__head
        while not (iterator is None):
            result += f"{iterator.get_data()} <- "
            iterator = iterator.get_next_node()

        result += "(tail) <- None\n"

        result += "None -> (tail) -> "

        iterator = self.__tail
        while not (iterator is None):
            result += f"{iterator.get_data()} -> "
            iterator = iterator.get_prev_node()

        result += "(head) -> None"

        return result


class Node:

    __next_node: Node
    __prev_node: Node

    def __init__(self, data: any):
        self.__data = data
        self.__next_node = None
        self.__prev_node = None

    def set_next_node(self, new_node) -> None:
        self.__next_node = new_node

    def set_prev_node(self, new_node) -> None:
        self.__prev_node = new_node

    def get_next_node(self) -> Node:
        return self.__next_node

    def get_prev_node(self) -> Node:
        return self.__prev_node

    def get_data(self) -> any:
        return self.__data


# dec = Dec()
#
# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)
#
# dec.enqueue_head(n1)
# dec.enqueue_head(n2)
# dec.enqueue_head(n3)
# dec.enqueue_head(n4)
# dec.enqueue_head(n5)
#
# dec.dequeue_tail()
# dec.dequeue_tail()
#
# print(dec.get_count())
# print(dec)
