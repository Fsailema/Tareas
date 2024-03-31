
import tkinter as tk

class ToDoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tareas Pendientes")
        self.geometry("400x300")

        self.tasks = []

        self.entry = tk.Entry(self)
        self.entry.pack(fill=tk.X, padx=10, pady=10)
        self.entry.bind("<Return>", self.add_task)

        self.task_list = tk.Listbox(self)
        self.task_list.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        self.task_list.bind("<Delete>", self.delete_task)
        self.task_list.bind("c", self.complete_task)

        self.add_button = tk.Button(self, text="Añadir tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.complete_button = tk.Button(self, text="Completar tarea", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.delete_button = tk.Button(self, text="Eliminar tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.bind("<Escape>", self.close_app)

    def add_task(self, event=None):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.entry.delete(0, tk.END)

    def complete_task(self, event=None):
        selection = self.task_list.curselection()
        if selection:
            index = selection[0]
            task = self.task_list.get(index)
            if task not in self.tasks:
                self.tasks[index] = task + " (Completada)"
                self.task_list.delete(index)
                self.task_list.insert(index, self.tasks[index])

    def delete_task(self, event=None):
        selection = self.task_list.curselection()
        if selection:
            index = selection[0]
            self.tasks.pop(index)
            self.task_list.delete(index)

    def close_app(self, event=None):
        self.destroy()

if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()