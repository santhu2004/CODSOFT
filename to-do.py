import tkinter as tk

def add_task():
    # Function to add a task to the list
    task = entry.get()  # Retrieve the task from the Entry widget
    if task:
        tasks.insert(tk.END, task)  # Insert the task into the Listbox
        entry.delete(0, tk.END)  # Clear the Entry widget after adding the task

def remove_task():
    # Function to remove a selected task from the list
    try:
        index = tasks.curselection()[0]  # Get the index of the selected task
        tasks.delete(index)  # Remove the task from the Listbox
    except IndexError:
        pass  # Ignore if no task is selected

def complete_task():
    # Function to mark a selected task as completed
    try:
        index = tasks.curselection()[0]  # Get the index of the selected task
        tasks.itemconfig(index, fg="gray")  # Change the color of the task to gray
    except IndexError:
        pass  # Ignore if no task is selected

# Create main window
root = tk.Tk()
root.title("To-Do List")

# Create task list
tasks = tk.Listbox(root, bg="lightyellow", width=50)
tasks.pack(padx=10, pady=10)

# Create entry for new tasks
entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=5)

# Create buttons
add_button = tk.Button(root, text="Add Task", width=10, command=add_task)
add_button.pack(padx=10, pady=5)

remove_button = tk.Button(root, text="Remove Task", width=10, command=remove_task)
remove_button.pack(padx=10, pady=5)

complete_button = tk.Button(root, text="Complete Task", width=12, command=complete_task)
complete_button.pack(padx=10, pady=5)

root.mainloop()
