"""
The shortest calculator program can be done in a single line using the "eval()" function in python:
print(eval(input("Enter the expression as a string: ")))
"""


import tkinter as tk

# Function to evaluate the expression in the entry field
def calculate():
    try:
        expression = entry.get()  # Get the expression from the entry field
        result = eval(expression)  # Evaluate the expression
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(tk.END, str(result))  # Display the result in the entry field
    except Exception as e:
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(tk.END, "Error")  # Display 'Error' if there's an exception

# Function to add a value to the entry field
def add_to_display(value):
    entry.insert(tk.END, value)  # Insert the given value at the end of the entry field

# Function to clear the entry field
def clear_display():
    entry.delete(0, tk.END)  # Clear the entry field

# Create the main window
root = tk.Tk()
root.title("Colorful Calculator")

# Entry field for display
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+')
]

# Create and place buttons in a grid layout
row_num = 1
col_num = 0

for row in buttons:
    col_num = 0
    for button_text in row:
        if button_text == '=':
            # '=' button for calculation
            button = tk.Button(root, text=button_text, padx=40, pady=20, command=calculate, bg='orange')
        elif button_text == 'C':
            # 'C' button for clearing
            button = tk.Button(root, text=button_text, padx=40, pady=20, command=clear_display, bg='red')
        else:
            # Buttons for numbers and operators
            button = tk.Button(root, text=button_text, padx=40, pady=20, command=lambda value=button_text: add_to_display(value))
        button.grid(row=row_num, column=col_num, padx=5, pady=5)  # Place the button in the grid
        col_num += 1
    row_num += 1

root.mainloop()  # Start the main event loop
