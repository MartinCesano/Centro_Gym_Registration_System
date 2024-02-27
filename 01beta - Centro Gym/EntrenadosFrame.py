import tkinter as tk      
from ContenidoFrame import ContenidoFrame

class EntrenadosFrame(ContenidoFrame):
    def __init__(self, master, navegacion_callback):
        super().__init__(master, "Entrenados", navegacion_callback)

