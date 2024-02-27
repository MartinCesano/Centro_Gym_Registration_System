import tkinter as tk

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
        self. ventana_principal.configure(bg='#8D837E')

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

        # Crear un frame - CONTENIDO para la columna derecha
        self.contenido = tk.Frame(ventana_principal, bg="#8D837E")
        self.contenido.grid(row=1, column=1,sticky="nsew")
        self.contenido.columnconfigure(0, weight=1)
        self.contenido.rowconfigure(0, weight=1)

       

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

class InicioFrame(tk.Frame):
    def __init__(self, master, navegacion_callback):
        super().__init__(master)

        # Etiqueta en el frame de inicio
        etiqueta_inicio = tk.Label(self, text="Inicio", font=("Arial", 14, "bold underline"))
        etiqueta_inicio.pack(pady=10)

        # Puedes agregar más contenido al frame de inicio según tus necesidades

class AsistenciaFrame(tk.Frame):
    def __init__(self, master, navegacion_callback):
        super().__init__(master)

        # Etiqueta en el frame de la aplicación
        etiqueta_asistencia = tk.Label(self, text="Asistencia", font=("Arial", 14, "bold underline"))
        etiqueta_asistencia.pack(pady=10)

        # Puedes agregar más contenido al frame de aplicación según tus necesidades
        
class EntrenadosFrame(tk.Frame):
    def __init__(self, master, navegacion_callback):
        super().__init__(master)

        # Etiqueta en el frame de la aplicación
        etiqueta_entrenados = tk.Label(self, text="Entrenados", font=("Arial", 14, "bold underline"))
        etiqueta_entrenados.pack(pady=10)

        # Puedes agregar más contenido al frame de aplicación según tus necesidades

class CuotasFrame(tk.Frame):
    def __init__(self, master, navegacion_callback):
        super().__init__(master)

        # Etiqueta en el frame de la aplicación
        etiqueta_cuotas = tk.Label(self, text="Cuotas", font=("Arial", 14, "bold underline"))
        etiqueta_cuotas.pack(pady=10)

        # Puedes agregar más contenido al frame de aplicación según tus necesidades

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
        frame = tk.Frame(self, bg="white")
        frame.grid(row=fila, column=0, sticky="nsew", padx=1, pady=(1, 0.5))

        self.columnconfigure(0, minsize=150)
        self.rowconfigure(fila, weight=1)

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(fila, weight=1)

        boton = tk.Button(frame, font=('Arial', 16), relief=tk.FLAT, fg='white', text=texto, bg="#555857",command=lambda: self.navegacion_callback(FrameActivo))
        boton.grid(row=fila, column=0, sticky="nsew")


ventana_principal = tk.Tk()
app = Aplicacion(ventana_principal)
ventana_principal.mainloop()