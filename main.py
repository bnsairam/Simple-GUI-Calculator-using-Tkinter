# simple_calculator.py
# A simple GUI-based calculator using Tkinter that performs basic arithmetic operations.

from tkinter import *

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("270x200")  # Adjusted height to fit the decimal button properly
        self.root.configure(bg="light green")

        self.expr = ""  # Expression string
        self.display = StringVar()

        # Entry widget for display
        entry = Entry(self.root, textvariable=self.display, justify='right')
        entry.grid(row=0, column=0, columnspan=4, ipadx=70, pady=10)

        # Number buttons
        self._create_button('1', 1, 0, lambda: self.press('1'))
        self._create_button('2', 1, 1, lambda: self.press('2'))
        self._create_button('3', 1, 2, lambda: self.press('3'))
        self._create_button('4', 2, 0, lambda: self.press('4'))
        self._create_button('5', 2, 1, lambda: self.press('5'))
        self._create_button('6', 2, 2, lambda: self.press('6'))
        self._create_button('7', 3, 0, lambda: self.press('7'))
        self._create_button('8', 3, 1, lambda: self.press('8'))
        self._create_button('9', 3, 2, lambda: self.press('9'))
        self._create_button('0', 4, 0, lambda: self.press('0'))

        # Operator buttons
        self._create_button('+', 1, 3, lambda: self.press('+'))
        self._create_button('-', 2, 3, lambda: self.press('-'))
        self._create_button('*', 3, 3, lambda: self.press('*'))
        self._create_button('/', 4, 3, lambda: self.press('/'))

        # Other buttons
        self._create_button('=', 4, 2, self.equal)
        self._create_button('Clear', 4, 1, self.clear)
        self._create_button('.', 5, 0, lambda: self.press('.'))

    def _create_button(self, text, row, col, command):
        button = Button(self.root, text=text, fg='black', bg='red', command=command, height=1, width=7)
        button.grid(row=row+1, column=col, padx=2, pady=2)  # Adjusted row to account for entry at row 0

    def press(self, key):
        self.expr += str(key)
        self.display.set(self.expr)

    def equal(self):
        try:
            result = str(eval(self.expr))
            self.display.set(result)
            self.expr = result  # Allow chaining calculations
        except Exception as e:
            self.display.set("Error")
            self.expr = ""

    def clear(self):
        self.expr = ""
        self.display.set("")

if __name__ == "__main__":
    root = Tk()
    app = SimpleCalculator(root)
    root.mainloop()
