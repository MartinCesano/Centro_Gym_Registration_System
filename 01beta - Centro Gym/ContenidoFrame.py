import tkinter as tk 
class ContenidoFrame(tk.Frame):
    def __init__(self, master, titulo, navegacion_callback):
        super().__init__(master)

        # Etiqueta en el frame de la aplicación
        etiqueta_contenido = tk.Label(self, text=titulo, font=("Arial", 14, "bold underline"))
        etiqueta_contenido.pack()
