import tkinter as tk
from tkinter import messagebox

# Store users and tasks
users = {}

# Add User
def add_user():
    name = entry_user.get()
    if name:
        if name not in users:
            users[name] = []
            messagebox.showinfo("Success", "User added!")
        else:
            messagebox.showerror("Error", "User already exists!")
    else:
        messagebox.showerror("Error", "Enter username")

# Add Task
def add_task():
    name = entry_user.get()
    task = entry_task.get()

    if name in users:
        if task:
            users[name].append({"task": task, "status": "Pending"})
            messagebox.showinfo("Success", "Task added!")
            entry_task.delete(0, tk.END)
            view_tasks()   # refresh display
        else:
            messagebox.showerror("Error", "Enter task")
    else:
        messagebox.showerror("Error", "User not found")

# View Tasks
def view_tasks():
    name = entry_user.get()

    if name in users:
        text_output.delete("1.0", tk.END)

        if not users[name]:
            text_output.insert(tk.END, "No tasks found\n")
        else:
            for i, t in enumerate(users[name]):
                text_output.insert(
                    tk.END,
                    f"{i+1}. {t['task']} - {t['status']}\n"
                )
    else:
        messagebox.showerror("Error", "User not found")

# Complete Task (FIXED)
def complete_task():
    name = entry_user.get()
    index = entry_index.get()

    if name in users:
        try:
            idx = int(index) - 1
            users[name][idx]["status"] = "Completed"
            messagebox.showinfo("Success", "Task completed!")
            view_tasks()   # 🔥 auto refresh
        except:
            messagebox.showerror("Error", "Invalid task number")
    else:
        messagebox.showerror("Error", "User not found")

# GUI Window
root = tk.Tk()
root.title("Task Manager")
root.geometry("350x450")

# Labels & Inputs
tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Task").pack()
entry_task = tk.Entry(root)
entry_task.pack()

tk.Label(root, text="Task Number to Complete").pack()
entry_index = tk.Entry(root)
entry_index.pack()

# Buttons
tk.Button(root, text="Add User", command=add_user).pack(pady=5)
tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="View Tasks", command=view_tasks).pack(pady=5)
tk.Button(root, text="Complete Task", command=complete_task).pack(pady=5)

# Output Box
text_output = tk.Text(root, height=12, width=40)
text_output.pack(pady=10)

# Run App
root.mainloop()
