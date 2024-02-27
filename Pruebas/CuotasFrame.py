import tkinter as tk
from ContenidoFrame import ContenidoFrame

class CuotasFrame(ContenidoFrame):
    def __init__(self, master, navegacion_callback):
        super().__init__(master, "Cuotas", navegacion_callback)
