from hw_03.src.main_3 import increase_large_integer
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning


class App:
    def __init__(self, root: Tk) -> None:
        self.__root_window = root

        self.__input_field = UserInputField()
        self.__output_result_field = OutputResultField()
        self.__solveButton = SolveButton(self.__input_field, self.__output_result_field)

        self.__main_frame = None

        self.__config_window()

        self.__build_window()

    def run(self) -> None:
        self.__root_window.mainloop()

    def __config_window(self):
        self.__root_window.title("MAX_IN_RANGE")
        self.__root_window.geometry("700x400")
        self.__root_window.resizable(False, False)

    def __build_window(self) -> None:
        self.__main_frame = Frame()

        self.__create_widgets()

        ttk.Label(master=self.__main_frame,
                  text="Increase list of numbers",
                  font=("Arial", 16),
                  justify=LEFT).grid(row=0, column=0, columnspan=3, pady=30)

        (ttk.Label(master=self.__main_frame, text="Enter numbers separated by a space: ").
            grid(row=1, column=0, sticky=E, ipadx=5))
        self.__input_field.get_list_input_field().grid(row=1, column=1, sticky=W)

        self.__solveButton.get_button().grid(row=4, column=1, columnspan=2, pady=10, sticky=W)

        self.__output_result_field.get_text_result().grid(row=5, column=1, sticky=W)
        self.__output_result_field.get_output_result().grid(row=5, column=2, sticky=E)

        self.__main_frame.pack()

    def __create_widgets(self) -> None:
        self.__input_field.create_input_field(self.__main_frame)

        self.__solveButton.create_button(self.__main_frame)

        self.__output_result_field.create_output_result(self.__main_frame)

    @staticmethod
    def send_warning(massage: str) -> None:
        showwarning(title="Warning", message=massage)

    @staticmethod
    def send_info(massage: str) -> None:
        showinfo(title="Warning", message=massage)


class UserInputField:
    def __init__(self) -> None:
        self.__list_input_field = None

    def create_input_field(self, main_frame: Frame) -> None:
        self.__list_input_field = ttk.Entry(master=main_frame,  width=30)

    def get_list_input_field(self) -> Entry:
        return self.__list_input_field


class OutputResultField:
    def __init__(self) -> None:
        self.__text_result = None
        self.__output_result = None

    def create_output_result(self, master: Frame) -> None:
        self.__text_result = Label(master=master, text="Result: ", font=("Arial", 14))

        self.__output_result = Label(master=master, font=("Arial", 12))

    def get_text_result(self) -> Label:
        return self.__text_result

    def get_output_result(self) -> Label:
        return self.__output_result


class SolveButton:
    def __init__(self, input_field: UserInputField, output_field: OutputResultField) -> None:
        self.__solver_button = None

        self.__input_field = input_field
        self.__output_field = output_field

    def create_button(self, master: Frame) -> None:
        self.__solver_button = ttk.Button(
            master=master,
            text="SOLVE",
            command=self.__on_click_handler,
            width=40,
            padding=[10])

    def __on_click_handler(self):
        arr = self.__get_list_from_input()

        if not self.is_validate_input_data(arr):
            return

        result = increase_large_integer(arr)

        self.__output_field.get_output_result().config(text=result)

    def is_validate_input_data(self, input_list) -> bool:

        if input_list is None:
            return False

        for i in input_list:
            if i is None:
                App.send_warning("One of the items in the list is not a number")
                return False
            if i < 0 or i > 9:
                App.send_warning("Numbers should be less than 10 and greater than 0")
                return False

        return True

    def __get_list_from_input(self):
        input_data = self.__input_field.get_list_input_field().get()
        arr = input_data.split(" ")

        if not arr:
            App.send_warning("Input integer")
            return False

        for i in range(0, len(arr), 1):
            arr[i] = self.__convert_input_data(arr[i], lambda x: int(x))

        return arr

    def __convert_input_data(self, input_data: str, convert_to=lambda x: int(x)):
        if not input_data.isdigit():
            return None

        input_data = convert_to(input_data)

        return input_data

    def get_button(self) -> ttk.Button:
        return self.__solver_button


# --- #


class Program:
    @staticmethod
    def main():
        root = Tk()

        app = App(root)

        app.run()


if __name__ == "__main__":
    Program.main()
