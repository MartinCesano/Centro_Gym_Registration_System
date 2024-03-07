import tkinter as tk
from Menu import Menu   
from InicioFrame import InicioFrame 
from AsistenciaFrame import AsistenciaFrame 
from EntrenadosFrame import EntrenadosFrame 
from CuotasFrame import CuotasFrame 

class Aplicacion:
    
    def __init__(self,ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Centro Gym")
        # Establecer las dimensiones de la ventana para que ocupe toda la pantalla
        # Obtener las dimensiones de la pantalla
        self.ancho_pantalla = int(ventana_principal.winfo_screenwidth()*0.8)
        self.alto_pantalla = int(ventana_principal.winfo_screenheight()*0.8)
        # Establecer las dimensiones de la ventana para que ocupe toda la pantalla
        self.ventana_principal.geometry(f"{self.ancho_pantalla}x{self.alto_pantalla}+0+0")
        self.ventana_principal.state('zoomed')
        self.ventana_principal.configure(bg='#DCD0CA')

        # la ventana principal tendra una sola fila 
        self.ventana_principal.rowconfigure(0, weight=1)
        self.ventana_principal.rowconfigure(1, weight=6)
        # columna 0 menu
        self.ventana_principal.columnconfigure(0, minsize=150)
        
        # columna 1 contenido 
        self.ventana_principal.columnconfigure(1, weight=1)

        
        # Crear un frame - Encabezado
        self.encabezado = tk.Frame(ventana_principal, bg="#E02E27")
        self.encabezado.grid(row=0, column=0, columnspan=2,sticky="nsew")
        self.encabezado.grid_propagate(False)

        self.encabezado.columnconfigure(0, weight=2)
        self.encabezado.columnconfigure(1, weight=1)
        self.encabezado.columnconfigure(2, weight=2)

        self.encabezado.rowconfigure(0, weight=2)
        self.encabezado.rowconfigure(1, weight=1)
        self.encabezado.rowconfigure(2, weight=2)

        #Crear un label para el encabezado

        self.titulo = tk.Label(self.encabezado, text="Centro Gym", font=("Century Gothic", 45 , "underline"), bg="#E02E27", fg="white")
        self.titulo.grid(row=1, column=1)


        # Crear un frame - CONTENIDO para la columna derecha
        self.contenido = tk.Frame(ventana_principal, bg="#DCD0CA")
        self.contenido.grid(row=1, column=1,sticky="nsew")
        self.contenido.columnconfigure(0, weight=1)
        self.contenido.rowconfigure(0, weight=1)
        self.contenido.grid_propagate(False)


       # Crear un frame - MENU para la columna izquierda
        self.menu = Menu(self.ventana_principal, self.mostrar_activo)
        self.menu.grid(row=1, column=0, sticky="nsew")
        
        self.mostrar_activo(InicioFrame)


    def mostrar_activo(self,FrameActivo):
        # Limpia el frame central y muestra el frame de aplicación
        for widget in self.contenido.winfo_children():
            widget.destroy()
        
        self.activo_frame = FrameActivo(self.contenido, self.mostrar_activo)
        self.activo_frame.grid(row=0, column=0, sticky="nsew")

