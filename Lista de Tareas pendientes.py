
import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def complete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.itemconfig(selected_task, fg='gray')

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

def on_key_press(event):
    key = event.keysym
    if key == 'Return':
        add_task()
    elif key == 'c':
        complete_task()
    elif key == 'Delete' or key == 'd':
        delete_task()
    elif key == 'Escape':
        root.destroy()

root = tk.Tk()
root.title("Tareas Pendientes")

# Campo de entrada para añadir nuevas tareas
entry = tk.Entry(root)
entry.pack()

# Botón para añadir tareas
add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.pack()

# Botón para marcar tareas como completadas
complete_button = tk.Button(root, text="Marcar como Completada", command=complete_task)
complete_button.pack()

# Botón para eliminar tareas
delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.pack()

# Lista para mostrar las tareas
listbox = tk.Listbox(root)
listbox.pack()

# Asignar funciones a los eventos de clic
listbox.bind('<Double-Button-1>', lambda event: complete_task())
listbox.bind('<Delete>', lambda event: delete_task())
listbox.bind('<Escape>', lambda event: root.destroy())

# Asignar función al evento de pulsación de tecla
root.bind('<Key>', on_key_press)

root.mainloop()