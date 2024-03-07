import tkinter as tk      
from tkinter import ttk

from ContenidoFrame import ContenidoFrame

class EntrenadosFrame(ContenidoFrame):
    def __init__(self, master, navegacion_callback):
        super().__init__(master, "Entrenados", navegacion_callback)
        

        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=20)
        self.master.columnconfigure(0, weight=1)
        self.frame_titulo.grid(row=0, column=0,  sticky="nsew")
        self.etiqueta_contenido.pack()

        self.opciones_entrenados = ttk.Notebook(master)
        self.opciones_entrenados.grid(row=1,column=0,sticky="nsew")

        # Crear un estilo
        self.style = ttk.Style()
        # Configurar el estilo de las pestañas del Notebook
        self.style.configure('TNotebook.Tab', font=('Century Gothic', '18'), padding=[5, 5])
        
        # Crear los frames
        self.frame_registrar = tk.Frame(self.opciones_entrenados, bg='red')
        self.frame_modificar = tk.Frame(self.opciones_entrenados, bg='green')
        self.frame_buscar = tk.Frame(self.opciones_entrenados, bg='blue')

        # Añadir los frames al notebook
        self.opciones_entrenados.add(self.frame_registrar, text='Registrar ')
        self.opciones_entrenados.add(self.frame_modificar, text='Modificar ')
        self.opciones_entrenados.add(self.frame_buscar, text='Buscar')
        '''
        self.nombre = tk.Entry(master.contenido, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=30, font=("Arial", 15))
        self.nombre.pack()

        self.apellido = tk.Entry(master.contenido, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=30, font=("Arial", 15))
        self.apellido.pack()

        self.documento = tk.Entry(master.contenido, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=30, font=("Arial", 15))
        self.documento.pack()

        self.boton_guardar = tk.Button(master.contenido, text="Guardar datos", command=self.guardar_datos)
        self.boton_guardar.pack()

        self.boton_editar = tk.Button(master.contenido, text="Editar datos", command=self.editar_datos)
        self.boton_editar.pack()

        self.label_datos = tk.Label(master.contenido, text="", wraplength=200)
        self.label_datos.pack()
        '''
    def guardar_datos(self):
        dato1 = self.nombre.get()
        dato2 = self.apellido.get()
        dato3 = self.documento.get()
        self.label_datos.config(text=f"Nombre: {dato1}\n Apellido: {dato2}\n DNI: {dato3}")

    def editar_datos(self):
        self.nombre.delete(0, tk.END)
        self.apellido.delete(0, tk.END)
        self.documento.delete(0, tk.END)
        self.label_datos.config(text="")