import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculate_result():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            messagebox.showerror("Error", "Invalid operation choice")
            return

        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Create the main application window
app = tk.Tk()
app.title("Simple Calculator")

# Create and place widgets in the window
label_num1 = tk.Label(app, text="Enter the 1st number:")
label_num1.pack()

entry_num1 = tk.Entry(app)
entry_num1.pack()

label_num2 = tk.Label(app, text="Enter the 2nd number:")
label_num2.pack()

entry_num2 = tk.Entry(app)
entry_num2.pack()

label_operation = tk.Label(app, text="Choose an operation:")
label_operation.pack()

operation_var = tk.StringVar()
operation_choices = ["+", "-", "*", "/"]
operation_var.set("+")  # Default operation is addition

for choice in operation_choices:
    radio_btn = tk.Radiobutton(app, text=choice, variable=operation_var, value=choice)
    radio_btn.pack()

calculate_btn = tk.Button(app, text="Calculate", command=calculate_result)
calculate_btn.pack()

result_label = tk.Label(app, text="Result:")
result_label.pack()

app.mainloop()
