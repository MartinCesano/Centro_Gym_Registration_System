import tkinter as tk
from ContenidoFrame import ContenidoFrame
class InicioFrame(ContenidoFrame):
    def __init__(self, master, navegacion_callback):
        super().__init__(master, "Inicio", navegacion_callback)

