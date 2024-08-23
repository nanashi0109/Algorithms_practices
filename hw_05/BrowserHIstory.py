from datetime import datetime
from enum import Enum


class BrowserHistory:
    class HistoryItem:
        def __init__(self, url: str, timestamp: datetime):
            self.url = url
            self.timestamp = timestamp
            self.next = None
            self.prev = None

    def __init__(self):
        self.current_history_item = None

    def visit(self, url: str):
        node = BrowserHistory.HistoryItem(url, datetime.now())
        if self.__is_empty():
            self.current_history_item = node
        else:
            self.current_history_item.next = node
            node.prev = self.current_history_item
            self.current_history_item = node

    def back(self):
        if (self.current_history_item is None) or (self.current_history_item.prev is None):
            return "Site not found"

        self.current_history_item = self.current_history_item.prev
        return self.current_history_item.url

    def forward(self):
        if (self.current_history_item is None) or (self.current_history_item.next is None):
            return "Site not found"

        self.current_history_item = self.current_history_item.next
        return self.current_history_item.url

    def clear(self):
        self.current_history_item = None

    def all(self) -> str:
        if self.__is_empty():
            return "History not found"

        result = ""

        iterator = self.current_history_item
        while not (iterator.next is None):
            iterator = iterator.next

        while not (iterator is None):
            result += f"{iterator.timestamp} : {iterator.url}\n"
            iterator = iterator.prev

        return result

    def __is_empty(self):
        return True if self.current_history_item is None else False


class Application:
    def run(self):
        history = BrowserHistory()

        print("Введите команду (visit <url>, back, forward, all, clear, exit): ")
        command = self.get_command()

        while command != Commands.Exit.value:
            match command[0]:
                case Commands.Visit.value:
                    history.visit(command[1])
                    print(f"Вы посетили {command[1]}")
                case Commands.Back.value:
                    print(f"Переход к {history.back()}")
                case Commands.Forward.value:
                    print(f"Переход к {history.forward()}")
                case Commands.All.value:
                    print(history.all())
                case Commands.Clear.value:
                    history.clear()
                    print("История очищена")
                case _:
                    print("Команда не найдена")

            print("Введите команду (visit <url>, back, forward, all, clear, exit): ")
            command = self.get_command()

    def get_command(self) -> list:
        command = input()
        return command.split()


class Commands(Enum):
    Visit = "visit"
    Back = "back"
    Forward = "forward"
    Exit = "exit"
    All = "all"
    Clear = "clear"


Application().run()
