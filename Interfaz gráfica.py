import tkinter as tk
from tkinter import messagebox


class AplicacionGUI:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Aplicación de Interfaz Gráfica")

        # Etiqueta para descripción
        self.etiqueta = tk.Label(ventana, text="Ingrese la información:")
        self.etiqueta.pack()

        # Campo de texto
        self.campo_texto = tk.Entry(ventana)
        self.campo_texto.pack()

        # Botón para agregar
        self.boton_agregar = tk.Button(ventana, text="Agregar", command=self.agregar_info)
        self.boton_agregar.pack()

        # Lista para mostrar datos
        self.lista = tk.Listbox(ventana)
        self.lista.pack()

        # Botón para limpiar
        self.boton_limpiar = tk.Button(ventana, text="Limpiar", command=self.limpiar_lista)
        self.boton_limpiar.pack()

    def agregar_info(self):
        texto = self.campo_texto.get()
        if texto:
            self.lista.insert(tk.END, texto)
            self.campo_texto.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese información.")

    def limpiar_lista(self):
        self.lista.delete(0, tk.END)


if __name__ == "__main__":
    ventana_principal = tk.Tk()
    aplicacion = AplicacionGUI(ventana_principal)
    ventana_principal.mainloop()