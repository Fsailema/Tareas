
import tkinter as tk

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tareas")

        self.tasks = []

        # Frame para la entrada de tareas
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.input_frame, width=50)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(self.input_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # Lista de tareas
        self.task_list = tk.Listbox(root, width=50)
        self.task_list.pack(padx=10, pady=5)

        # Botones de acción
        self.action_frame = tk.Frame(root)
        self.action_frame.pack(pady=5)

        self.complete_button = tk.Button(self.action_frame, text="Marcar como Completada", command=self.mark_complete)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.action_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT)

        # Configuración de eventos
        self.task_entry.bind("<Return>", self.add_task_event)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def mark_complete(self):
        selection = self.task_list.curselection()
        if selection:
            index = selection[0]
            task = self.tasks[index]
            task = task + " (Completada)"
            self.task_list.delete(index)
            self.task_list.insert(index, task)

    def delete_task(self):
        selection = self.task_list.curselection()
        if selection:
            index = selection[0]
            self.task_list.delete(index)
            del self.tasks[index]

    def add_task_event(self, event):
        self.add_task()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()