from __future__ import annotations
from hw_04.src.main_4 import *
from tkinter import *
from tkinter import ttk


class App:
    def __init__(self, root: Tk):
        self.__root_window = root

        self.__main_window = MainWindow()

        self.__config_window()

    def run(self):
        self.__root_window.mainloop()

    def __config_window(self):
        self.__root_window.geometry("1000x700")
        self.__root_window.title("Homework №4")
        self.__root_window.resizable(False, False)

        main_menu = self.__main_window.get_menu()
        self.__root_window.config(menu=main_menu)


class MainWindow:
    def __init__(self):
        self.__menu = Menu()
        self.__current_frame = None

        self.__config_menu()
        self.__config_start_frame()

    def __config_start_frame(self):
        self.__current_frame = Frame()

        Label(master=self.__current_frame, text=" ↑\nclick", font=("Arial", 14)).pack(padx=20)

        self.__current_frame.pack(anchor="nw")

    def __config_menu(self):

        algorithm_menu = Menu()
        commands = {"bobble sort": BobbleSortWindow(),
                    "choice sort": ChoiceSortWindow(),
                    "recursive sum": RecursiveSumWindow(),
                    "recursive max": RecursiveMaxWindow(),
                    "recursive even sum": RecursiveEvenSumWindow(),
                    "reverse string": ReverseStringWindow(),
                    "is palindrome": IsPalindromeWindow(),
                    "fibonacci": FibonacciWindow(),
                    "sum of digits": SumOfDigitsWindow(),
                    "DList": DListWindow()}
        for i in commands:
            algorithm_menu.add_command(label=i, command=lambda window=commands[i]: self.__switch_current_frame(window))

        self.__menu.add_cascade(label="Algorithms", menu=algorithm_menu)

    def __switch_current_frame(self, window: BaseWindow):
        if not (self.__current_frame is None):
            self.__current_frame.pack_forget()

        self.__current_frame = window.get_frame()
        self.__current_frame.pack()

    def get_menu(self) -> Menu:
        return self.__menu


class UserInputField:
    def __init__(self, master_frame, width: int = 20, key_to_convert_data=lambda x: x,
                 key_to_convert_elem_array=None):
        self.__input_field = None

        self.__key_to_convert_data = key_to_convert_data
        self.__key_to_convert_elem_array = key_to_convert_elem_array
        self.__config_input_field(master_frame, width)

    def __config_input_field(self, master_frame, width: int = 20):
        self.__input_field = Entry(master=master_frame, width=width)

    def get_data(self, alternative_key=None) -> any:
        if alternative_key is None:
            data = self.__key_to_convert_data(self.__input_field.get())
        else:
            data = alternative_key(self.__input_field.get())

        if not (self.__key_to_convert_elem_array is None):
            for i in range(0, len(data), 1):
                data[i] = self.__key_to_convert_elem_array(data[i])

        return data

    def get_input_field(self) -> Entry:
        return self.__input_field


class OutputField:
    def __init__(self, master: Frame, key_to_convert_data=lambda x: str(x)):
        self.__text_result = None
        self.__key_to_convert_data = key_to_convert_data

        self.__config_text(master)

    def __config_text(self, master: Frame):
        self.__text_result = Label(master=master, font=("Arial", 12))

    def get_text_result(self) -> Label:
        return self.__text_result

    def set_text(self, text: any) -> None:
        self.__text_result.config(text=self.__key_to_convert_data(text))


class BaseSolveButton:
    def get_button(self) -> Button:
        pass


class SolveButton(BaseSolveButton):
    def __init__(self, input_field: UserInputField, output_field: OutputField,
                 master: Frame, solve_function, width: int = 20):

        self.__button = None

        self.__solve_function = solve_function

        self.__input__field = input_field
        self.__output_field = output_field

        self.__config_button(master, width)

    def __config_button(self, master: Frame, width: int = 20):
        self.__button = ttk.Button(master=master, width=width, command=self.solve, text=Constants.SOLVE_TEXT)

    def solve(self):
        data = self.__input__field.get_data()

        result = self.__solve_function(data)

        self.__output_field.set_text(result)

    def get_button(self) -> Button:
        return self.__button


class BaseWindow:
    _frame: Frame
    _user_input_field: UserInputField
    _output_field: OutputField
    _solve_button: BaseSolveButton

    def get_frame(self) -> Frame:
        pass

    def _build_frame(self):
        ttk.Label(master=self._frame, text="Input numbers ->", font=("Arial", 9)).grid(row=1, column=0, sticky=E)
        input_field = self._user_input_field.get_input_field()
        input_field.grid(row=1, column=1, columnspan=2, sticky=W)

        ttk.Label(master=self._frame, text="Click ->", font=("Arial", 9)).grid(row=2, column=0, sticky=E)
        button_to_solve = self._solve_button.get_button()
        button_to_solve.grid(row=2, column=1, columnspan=2)

        ttk.Label(master=self._frame, text="Look ->", font=("Arial", 9)).grid(row=3, column=0, sticky=E)
        Label(master=self._frame, text=Constants.RESULT_TEXT, font=("Arial", 12)).grid(row=3, column=1, sticky=W)
        output_label = self._output_field.get_text_result()
        output_label.grid(row=3, column=2)


class BobbleSortWindow(BaseWindow):
    _frame: Frame
    _user_input_field: UserInputField
    _output_field: OutputField
    _solve_button: SolveButton

    def __init__(self):
        self._frame = Frame()

        self._user_input_field = UserInputField(self._frame, 20, key_to_convert_data=lambda x: x.split(" "))
        self._output_field = OutputField(self._frame, key_to_convert_data=lambda x: ", ".join(x))
        self._solve_button = SolveButton(self._user_input_field, self._output_field,
                                         master=self._frame, width=35,
                                         solve_function=bubble_sort)

        self._build_frame()

    def _build_frame(self):
        Label(master=self._frame, text="Bubble Sort", font=("Arial", 24)).grid(row=0, column=1, columnspan=2)
        Label(master=self._frame, text=Constants.INPUT_ARRAY_LABEL, font=("Arial", 10)).grid(row=1, column=3)

        super()._build_frame()

    def get_frame(self) -> Frame:
        return self._frame


class ChoiceSortWindow(BaseWindow):
    def __init__(self):
        self._frame = Frame()

        self._user_input_field = UserInputField(self._frame, 20,
                                                key_to_convert_data=lambda x: x.split(" "),
                                                key_to_convert_elem_array=lambda x: int(x))

        self._output_field = OutputField(self._frame, key_to_convert_data=lambda x: f"Array: {x[0]}, "
                                                                                    f"count exchanges: x{x[1]}, "
                                                                                    f"count comparisons: x{2}")

        self._solve_button = SolveButton(self._user_input_field, self._output_field,
                                         master=self._frame, width=35,
                                         solve_function=choice_sort)

        self._build_frame()

    def _build_frame(self):
        Label(master=self._frame, text="Choice sort", font=("Arial", 24)).grid(row=0, column=1, columnspan=2)
        Label(master=self._frame, text=Constants.INPUT_ARRAY_LABEL, font=("Arial", 10)).grid(row=1, column=3)

        super()._build_frame()

    def get_frame(self) -> Frame:
        return self._frame


class RecursiveSumWindow(BaseWindow):
    def __init__(self):
        self._frame = Frame()

        self._user_input_field = UserInputField(self._frame, 20,
                                                key_to_convert_data=lambda x: x.split(" "),
                                                key_to_convert_elem_array=lambda x: int(x))

        self._output_field = OutputField(self._frame, key_to_convert_data=lambda x: str(x))

        self._solve_button = SolveButton(self._user_input_field, self._output_field,
                                         master=self._frame, width=35,
                                         solve_function=recursive_sum)

        self._build_frame()

    def _build_frame(self):
        Label(master=self._frame, text="Recursive Sum", font=("Arial", 24)).grid(row=0, column=1, columnspan=2)
        Label(master=self._frame, text=Constants.INPUT_ARRAY_LABEL, font=("Arial", 10)).grid(row=1, column=3)

        super()._build_frame()

    def get_frame(self) -> Frame:
        return self._frame


class RecursiveMaxWindow(BaseWindow):
    def __init__(self):
        self._frame = Frame()

        self._user_input_field = UserInputField(self._frame, 20,
                                                key_to_convert_data=lambda x: x.split(" "),
                                                key_to_convert_elem_array=lambda x: int(x))

        self._output_field = OutputField(self._frame, key_to_convert_data=lambda x: str(x))

        self._solve_button = SolveButton(self._user_input_field, self._output_field,
                                         master=self._frame, width=35,
                                         solve_function=recursive_max)

        self._build_frame()

    def _build_frame(self):
        Label(master=self._frame, text="Recursive Max", font=("Arial", 24)).grid(row=0, column=1, columnspan=2)
        Label(master=self._frame, text=Constants.INPUT_ARRAY_LABEL, font=("Arial", 10)).grid(row=1, column=3)

        super()._build_frame()

    def get_frame(self) -> Frame:
        return self._frame


class RecursiveEvenSumWindow(BaseWindow):
    def __init__(self):
        self._frame = Frame()

        self._user_input_field = UserInputField(self._frame, 20,
                                                key_to_convert_data=lambda x: x.split(" "),
                                                key_to_convert_elem_array=lambda x: int(x))

        self._output_field = OutputField(self._frame, key_to_convert_data=lambda x: str(x))

        self._solve_button = SolveButton(self._user_input_field, self._output_field,
                                         master=self._frame, width=35,
                                         solve_function=recursive_even_sum)

        self._build_frame()

    def _build_frame(self):
        Label(master=self._frame, text="Recursive Even Sum", font=("Arial", 24)).grid(row=0, column=1, columnspan=2)
        Label(master=self._frame, text=Constants.INPUT_ARRAY_LABEL, font=("Arial", 10)).grid(row=1, column=3)

        super()._build_frame()

    def get_frame(self) -> Frame:
        return self._frame


class ReverseStringWindow(BaseWindow):
    def __init__(self):
        self._frame = Frame()

        self._user_input_field = UserInputField(self._frame, 20,
                                                key_to_convert_data=lambda x: str(x))

        self._output_field = OutputField(self._frame, key_to_convert_data=lambda x: str(x))

        self._solve_button = SolveButton(self._user_input_field, self._output_field,
                                         master=self._frame, width=35,
                                         solve_function=reverse_string)

        self._build_frame()

    def _build_frame(self):
        Label(master=self._frame, text="Reverse String", font=("Arial", 24)).grid(row=0, column=1, columnspan=2)
        Label(master=self._frame, text=Constants.INPUT_STRING_LABEL, font=("Arial", 10)).grid(row=1, column=3)

        super()._build_frame()

    def get_frame(self) -> Frame:
        return self._frame


class IsPalindromeWindow(BaseWindow):
    def __init__(self):
        self._frame = Frame()

        self._user_input_field = UserInputField(self._frame, 20,
                                                key_to_convert_data=lambda x: str(x))

        self._output_field = OutputField(self._frame, key_to_convert_data=lambda x: str(x))

        self._solve_button = SolveButton(self._user_input_field, self._output_field,
                                         master=self._frame, width=35,
                                         solve_function=is_palindrome)

        self._build_frame()

    def _build_frame(self):
        Label(master=self._frame, text="Is Palindrome", font=("Arial", 24)).grid(row=0, column=1, columnspan=2)
        Label(master=self._frame, text=Constants.INPUT_STRING_LABEL, font=("Arial", 10)).grid(row=1, column=3)

        super()._build_frame()

    def get_frame(self) -> Frame:
        return self._frame


class FibonacciWindow(BaseWindow):
    def __init__(self):
        self._frame = Frame()

        self._user_input_field = UserInputField(self._frame, 20,
                                                key_to_convert_data=lambda x: int(x))

        self._output_field = OutputField(self._frame, key_to_convert_data=lambda x: str(x))

        self._solve_button = SolveButton(self._user_input_field, self._output_field,
                                         master=self._frame, width=35,
                                         solve_function=fibonacci)

        self._build_frame()

    def _build_frame(self):
        Label(master=self._frame, text="Fibonacci", font=("Arial", 24)).grid(row=0, column=1, columnspan=2)
        Label(master=self._frame, text=Constants.INPUT_INT_LABEL, font=("Arial", 10)).grid(row=1, column=3)

        super()._build_frame()

    def get_frame(self) -> Frame:
        return self._frame


class SumOfDigitsWindow(BaseWindow):
    def __init__(self):
        self._frame = Frame()

        self._user_input_field = UserInputField(self._frame, 20,
                                                key_to_convert_data=lambda x: int(x))

        self._output_field = OutputField(self._frame, key_to_convert_data=lambda x: str(x))

        self._solve_button = SolveButton(self._user_input_field, self._output_field,
                                         master=self._frame, width=35,
                                         solve_function=sum_of_digits)

        self._build_frame()

    def _build_frame(self):
        Label(master=self._frame, text="Sum Of Digits", font=("Arial", 24)).grid(row=0, column=1, columnspan=2)
        Label(master=self._frame, text=Constants.INPUT_INT_LABEL, font=("Arial", 10)).grid(row=1, column=3)

        super()._build_frame()

    def get_frame(self) -> Frame:
        return self._frame


class DListWindow(BaseWindow):
    def __init__(self):
        self._frame = Frame()
        self.__dlist = DList(6)

        self._user_input_field = UserInputField(self._frame, 20,
                                                key_to_convert_data=lambda x: int(x))
        self._output_field = OutputField(self._frame, key_to_convert_data=lambda x: str(x))
        self._dlist_operation = DListOperations(self._frame, self.__dlist)

        self.__current_list_label = None

        self._solve_button = DListSolveButton(self._user_input_field, self._output_field,
                                              self._dlist_operation, master=self._frame,
                                              button_callback=lambda:
                                              self.__current_list_label.config(text=str(self.__dlist)))

        self._build_frame()

    def _build_frame(self):
        super()._build_frame()

        Label(master=self._frame, text="DList", font=("Arial", 24)).grid(row=0, column=1, columnspan=2)

        operations_field = self._dlist_operation.get_operations_fild()
        operations_field.grid(row=1, column=3)

        Label(master=self._frame, text="Current list: ", font=("Arial", 14)).grid(row=4, column=1)

        self.__current_list_label = Label(master=self._frame, font=("Arial", 14))
        self.__current_list_label.grid(row=4, column=2, columnspan=2, sticky=W)

    def get_frame(self) -> Frame:
        return self._frame


class DListSolveButton(BaseSolveButton):
    def __init__(self, input_filed: UserInputField, output_field: OutputField, operation: DListOperations,
                 button_callback,
                 master: Frame):
        self.__input_field = input_filed
        self.__output_field = output_field
        self.__operations = operation

        self.__button = None
        self.__button_callback = button_callback

        self.__config_button(master)

    def __config_button(self, master: Frame):
        self.__button = ttk.Button(master=master, command=self.solve, text=Constants.SOLVE_TEXT)

    def solve(self):
        func = self.__operations.types_operations[self.__operations.get_operations_fild().get()]

        if func == self.__operations.types_operations["Is Empty"]:
            result = func()
        elif func == self.__operations.types_operations["Insert Of Index"]:
            data = self.__input_field.get_data(alternative_key=lambda x: x.split(" "))
            print(int(data[0]), int(data[1]))
            result = func(int(data[0]), int(data[1]))
        else:
            data = self.__input_field.get_data()
            result = func(data)

        self.__button_callback()
        self.__output_field.set_text(result)

    def get_button(self) -> Button:
        return self.__button


class DListOperations:
    def __init__(self, master: Frame, dlist: DList):
        self.__operations_field = None

        self.__dlist = dlist
        self.types_operations = \
            {
                "Add": self.__dlist.add,
                "Add Front": self.__dlist.add_front,
                "Remove": self.__dlist.remove,
                "Remove Of Index": self.__dlist.remove_of_index,
                "Find": self.__dlist.find,
                "Insert Of Index": self.__dlist.insert_of_index,
                "Is Empty": self.__dlist.is_empty
            }

        self.__config_operations_field(master)

    def __config_operations_field(self, frame):
        self.__operations_field = ttk.Combobox(master=frame, values=list(self.types_operations.keys()),
                                               state="readonly")

    def get_operations_fild(self) -> ttk.Combobox:
        return self.__operations_field


class Program:
    @staticmethod
    def main():
        tk = Tk()

        app = App(tk)
        app.run()


class Constants:
    INPUT_ARRAY_LABEL = "HINT! Enter numbers separated by a space."
    INPUT_STRING_LABEL = "HINT! Enter some string without space."
    INPUT_INT_LABEL = "HINT! Enter integer."
    RESULT_TEXT = "Result: "
    SOLVE_TEXT = "Perform calculations"


if __name__ == "__main__":
    Program.main()
