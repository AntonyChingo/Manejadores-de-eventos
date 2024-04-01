import tkinter as tk


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, width=50)
        self.task_listbox.pack(pady=10)

        self.root.bind("<Escape>", self.close_app)
        self.root.bind("<KeyPress-c>", self.mark_completed)
        self.root.bind("<KeyPress-d>", self.delete_task)

    def add_task(self, event=None):
        task_text = self.entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.task_listbox.insert(tk.END, task_text)
            self.entry.delete(0, tk.END)

    def mark_completed(self, event=None):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            self.task_listbox.itemconfig(index, {'bg': 'green'})

    def delete_task(self, event=None):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            self.task_listbox.delete(index)
            del self.tasks[index]

    def close_app(self, event=None):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
