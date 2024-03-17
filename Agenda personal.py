import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Función para agregar un nuevo evento
def agregar_evento():
    fecha = fecha_entry.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get()

    # Aquí se puede agregar la lógica para guardar el evento en una lista o base de datos

    # Actualizar la lista de eventos mostrada en la ventana principal
    eventos_treeview.insert("", "end", values=(fecha, hora, descripcion))

    # Limpiar los campos de entrada
    fecha_entry.delete(0, "end")
    hora_entry.delete(0, "end")
    descripcion_entry.delete(0, "end")


# Función para eliminar un evento seleccionado
def eliminar_evento():
    seleccionado = eventos_treeview.selection()
    if seleccionado:
        eventos_treeview.delete(seleccionado)
    else:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un evento para eliminar.")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Eventos")

# Crear un frame para la lista de eventos
eventos_frame = ttk.Frame(ventana)
eventos_frame.pack(pady=10)

# Crear el TreeView para mostrar la lista de eventos
eventos_treeview = ttk.Treeview(eventos_frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
eventos_treeview.heading("Fecha", text="Fecha")
eventos_treeview.heading("Hora", text="Hora")
eventos_treeview.heading("Descripción", text="Descripción")
eventos_treeview.pack()

# Crear un frame para los campos de entrada y botones
campos_frame = ttk.Frame(ventana)
campos_frame.pack(pady=10)

# Crear etiquetas y campos de entrada
fecha_label = ttk.Label(campos_frame, text="Fecha:")
fecha_label.grid(row=0, column=0, padx=5, pady=5)
fecha_entry = ttk.Entry(campos_frame)
fecha_entry.grid(row=0, column=1, padx=5, pady=5)

hora_label = ttk.Label(campos_frame, text="Hora:")
hora_label.grid(row=1, column=0, padx=5, pady=5)
hora_entry = ttk.Entry(campos_frame)
hora_entry.grid(row=1, column=1, padx=5, pady=5)

descripcion_label = ttk.Label(campos_frame, text="Descripción:")
descripcion_label.grid(row=2, column=0, padx=5, pady=5)
descripcion_entry = ttk.Entry(campos_frame)
descripcion_entry.grid(row=2, column=1, padx=5, pady=5)

# Crear botones
agregar_button = ttk.Button(campos_frame, text="Agregar Evento", command=agregar_evento)
agregar_button.grid(row=3, column=0, padx=5, pady=5)

eliminar_button = ttk.Button(campos_frame, text="Eliminar Evento Seleccionado", command=eliminar_evento)
eliminar_button.grid(row=3, column=1, padx=5, pady=5)

salir_button = ttk.Button(campos_frame, text="Salir", command=ventana.quit)
salir_button.grid(row=3, column=2, padx=5, pady=5)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()