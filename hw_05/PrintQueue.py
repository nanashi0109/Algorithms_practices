from __future__ import annotations


class PrintDocument:
    def __init__(self, title: str, number_of_pages: int):
        self.__title = title
        self.__number_of_pages = number_of_pages

    def __get_title(self) -> str:
        return self.__title

    def __get_number_of_pages(self) -> int:
        return self.__number_of_pages

    title = property(__get_title)
    number_of_pages = property(__get_number_of_pages)


class PrintQueue:
    class Node:
        next_node: PrintQueue.Node or None

        def __init__(self, document: PrintDocument):
            self.document = document
            self.next_node = None

    __head: PrintQueue.Node or None
    __tail: PrintQueue.Node or None

    def __init__(self):
        self.__count = 0
        self.__head = None
        self.__tail = None

    def enqueue(self, document: PrintDocument) -> None:
        node = PrintQueue.Node(document)

        if self.is_empty():
            self.__head = node
        else:
            self.__tail.next_node = node

        self.__tail = node
        self.__count += 1

    def dequeue(self) -> PrintDocument or None:
        if self.is_empty():
            return None

        document = self.__head.document

        if self.__count == 1:
            self.__tail = None

        self.__head = self.__head.next_node

        self.__count -= 1

        return document

    def peek(self) -> PrintDocument or None:
        if self.is_empty():
            return None

        return self.__head.document

    def is_empty(self) -> bool:
        return True if self.__count == 0 else False

    def count(self) -> int:
        return self.__count

    def __str__(self):
        result = "(head) <- "

        iterator = self.__head
        while not (iterator is None):
            result += f"{iterator.document.title} <- "
            iterator = iterator.next_node

        result += "(tail) <- None"

        return result


# queue = PrintQueue()
#
# doc_1 = PrintDocument("one", 5)
# doc_2 = PrintDocument("two", 10)
# doc_3 = PrintDocument("three", 15)
# doc_4 = PrintDocument("four", 20)
#
# queue.enqueue(doc_1)
# queue.enqueue(doc_2)
# queue.enqueue(doc_3)
# queue.enqueue(doc_4)
#
# print(queue)
#
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
#
# print(queue.peek())
#
# print(queue)
