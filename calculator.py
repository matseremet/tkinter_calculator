import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title('calculator')

        self.display = tk.Entry(master, width=30, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(master, text=text, width=7, height=2, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, value):
        current = self.display.get()
        if value == 'C':
            self.display.delete(0, tk.END)
        elif value == '=':
            try:
                result = eval(current)
                self.display.delete(0,tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, 'Error')
        else:
            self.display.insert(tk.END, value)

def main():
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()
