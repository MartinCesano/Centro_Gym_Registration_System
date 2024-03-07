import tkinter as tk
from InicioFrame import InicioFrame
from AsistenciaFrame import AsistenciaFrame
from EntrenadosFrame import EntrenadosFrame
from CuotasFrame import CuotasFrame

class Menu(tk.Frame):
    def __init__(self, master, navegacion_callback):
        super().__init__(master, bg="#DCD0CA")
        self.navegacion_callback = navegacion_callback

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.crear_boton("INICIO", InicioFrame,0)
        self.crear_boton("ASISTENCIA", AsistenciaFrame,1)
        self.crear_boton("ENTRENADOS", EntrenadosFrame,2)
        self.crear_boton("CUOTAS", CuotasFrame,3)

    def crear_boton(self, texto, FrameActivo,fila):
        frame = tk.Frame(self, bg="#DCD0CA")
        frame.grid(row=fila, column=0, sticky="nsew", padx=1, pady=(1, 0.5))

        self.columnconfigure(0, minsize=150)
        self.rowconfigure(fila, weight=1)

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(fila, weight=1)

        boton = tk.Button(frame, font=('Century Gothic', 16, 'bold'), relief=tk.FLAT, fg='white', text=texto, bg="#555857",command=lambda: self.navegacion_callback(FrameActivo))
        boton.grid(row=fila, column=0, sticky="nsew")

