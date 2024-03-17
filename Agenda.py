
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class EventManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Eventos")

        self.event_list = []

        # Crear Frames para organizar la interfaz
        self.events_frame = ttk.Frame(self.root)
        self.events_frame.pack(pady=10)

        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack(pady=10)

        self.actions_frame = ttk.Frame(self.root)
        self.actions_frame.pack(pady=10)

        # Lista de eventos
        self.events_tree = ttk.Treeview(self.events_frame, columns=("Fecha", "Hora", "Descripción"), selectmode="extended")
        self.events_tree.heading("#0", text="ID")
        self.events_tree.heading("Fecha", text="Fecha")
        self.events_tree.heading("Hora", text="Hora")
        self.events_tree.heading("Descripción", text="Descripción")
        self.events_tree.pack()

        # Campos de entrada
        ttk.Label(self.input_frame, text="Fecha:").grid(row=0, column=0, sticky="w")
        self.date_entry = ttk.Entry(self.input_frame)
        self.date_entry.grid(row=0, column=1, padx=5)

        ttk.Label(self.input_frame, text="Hora:").grid(row=1, column=0, sticky="w")
        self.time_entry = ttk.Entry(self.input_frame)
        self.time_entry.grid(row=1, column=1, padx=5)

        ttk.Label(self.input_frame, text="Descripción:").grid(row=2, column=0, sticky="w")
        self.description_entry = ttk.Entry(self.input_frame)
        self.description_entry.grid(row=2, column=1, padx=5)

        # Botones
        ttk.Button(self.actions_frame, text="Agregar Evento", command=self.add_event).grid(row=0, column=0, padx=5)
        ttk.Button(self.actions_frame, text="Eliminar Evento Seleccionado", command=self.remove_event).grid(row=0, column=1, padx=5)
        ttk.Button(self.actions_frame, text="Salir", command=self.root.quit).grid(row=0, column=2, padx=5)

    def add_event(self):
        # Obtener datos de los campos de entrada
        date = self.date_entry.get()
        time = self.time_entry.get()
        description = self.description_entry.get()

        # Validar campos
        if not date or not time or not description:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        # Agregar evento a la lista
        event_id = len(self.event_list) + 1
        self.event_list.append((event_id, date, time, description))

        # Actualizar TreeView
        self.events_tree.insert("", "end", text=str(event_id), values=(date, time, description))

        # Limpiar campos de entrada
        self.date_entry.delete(0, "end")
        self.time_entry.delete(0, "end")
        self.description_entry.delete(0, "end")

    def remove_event(self):
        # Obtener eventos seleccionados
        selected_items = self.events_tree.selection()
        if not selected_items:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un evento.")
            return

        # Confirmar eliminación
        confirm = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar el evento seleccionado?")
        if confirm:
            for item in selected_items:
                event_id = int(self.events_tree.item(item, "text"))
                del self.event_list[event_id - 1]
                self.events_tree.delete(item)

def main():
    root = tk.Tk()
    app = EventManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()