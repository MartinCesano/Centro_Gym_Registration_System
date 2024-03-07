import tkinter as tk 
class ContenidoFrame(tk.Frame):
    def __init__(self, frame_contenido, titulo, navegacion_callback):
        super().__init__(frame_contenido)
        
        # Frame en primer fila donde se muestra el titulo
        self.frame_titulo = tk.Frame(frame_contenido, bg="#DCD0CA")
        self.frame_titulo.grid(row=0, column=0, sticky="nsew")

        self.frame_titulo.columnconfigure(0, weight=2)
        self.frame_titulo.columnconfigure(1, weight=1)
        self.frame_titulo.columnconfigure(2, weight=2)

        # Etiqueta del frame 
        self.etiqueta_contenido = tk.Label(self.frame_titulo, text=titulo, font=("Century Gothic", 30 , "underline"), bg="#DCD0CA")
        self.etiqueta_contenido.grid(row=0, column=1, sticky="nsew")
        
        
