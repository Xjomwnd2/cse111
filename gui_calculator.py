import tkinter as tk
from tkinter import ttk
import pytest

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        # Create entry field
        self.entry = ttk.Entry(root, width=30, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Create buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # Add buttons to grid
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            ttk.Button(root, text=button, command=cmd).grid(
                row=row, column=col, padx=2, pady=2
            )
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Add clear button
        ttk.Button(root, text='C', command=self.clear).grid(
            row=row, column=col, padx=2, pady=2
        )

    def click(self, key):
        """Handle button clicks."""
        if key == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, key)

    def clear(self):
        """Clear the entry field."""
        self.entry.delete(0, tk.END)

    def calculate(self, expression):
        """Calculate result of expression (for testing).
        
        Parameters:
            expression: str - Mathematical expression
        Returns:
            float - Result of calculation
        """
        try:
            return eval(expression)
        except:
            return None

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

# Test functions
def test_calculator():
    root = tk.Tk()
    calc = Calculator(root)
    assert calc.calculate("2+2") == 4
    assert calc.calculate("3*4") == 12
    assert calc.calculate("10/2") == 5
    assert calc.calculate("invalid") is None
    root.destroy()

if __name__ == "__main__":
    main()
#Last edited 4 hours ago