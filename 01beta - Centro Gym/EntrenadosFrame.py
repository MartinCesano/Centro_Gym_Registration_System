import tkinter as tk      
from tkinter import ttk, messagebox
from ContenidoFrame import ContenidoFrame
import sqlite3 


class EntrenadosFrame(ContenidoFrame):
    def __init__(self, master, navegacion_callback):
        super().__init__(master, "Entrenados", navegacion_callback)
        
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=15)
        self.master.columnconfigure(0, weight=1)
        self.frame_titulo.grid(row=0, column=0,  sticky="nsew")

        self.opciones_entrenados = ttk.Notebook(master)
        self.opciones_entrenados.grid(row=1,column=0,sticky="nsew")

        # Crear un estilo
        self.style = ttk.Style()
        # Configurar el estilo de las pestañas del Notebook
        self.style.configure('TNotebook.Tab', font=('Century Gothic', '18'), padding=[5, 5])
        
        # Crear los frames
        self.frame_registrar = tk.Frame(self.opciones_entrenados, bg="#DCD0CA")
        self.frame_modificar = tk.Frame(self.opciones_entrenados, bg="#DCD0CA")
        self.frame_buscar = tk.Frame(self.opciones_entrenados, bg="#DCD0CA")

        # Añadir los frames al notebook
        self.opciones_entrenados.add(self.frame_registrar, text='Registrar ')
        self.opciones_entrenados.add(self.frame_modificar, text='Modificar ')
        self.opciones_entrenados.add(self.frame_buscar, text='Buscar')
        
        # Configurar el frame de registrar

        self.frame_registrar.grid_propagate(False)

        self.frame_registrar.columnconfigure(0, weight=1)
        self.frame_registrar.columnconfigure(1, weight=2)
        self.frame_registrar.columnconfigure(2, weight=1)

        # Filas para las entradas y etiquetas
        self.frame_registrar.rowconfigure(0, weight=1)
        self.frame_registrar.rowconfigure(1, weight=1) 
        self.frame_registrar.rowconfigure(2, weight=1) 
        self.frame_registrar.rowconfigure(3, weight=1) 
        self.frame_registrar.rowconfigure(4, weight=1)
        self.frame_registrar.rowconfigure(5, weight=1)
        self.frame_registrar.rowconfigure(6, weight=1)
        self.frame_registrar.rowconfigure(7, weight=1)
        self.frame_registrar.rowconfigure(8, weight=1)
        self.frame_registrar.rowconfigure(9, weight=1)
        self.frame_registrar.rowconfigure(10, weight=1)


        # 
        self.etiqueta_nombre = tk.Label(self.frame_registrar, text="Nombre", font=("Arial", 15))
        self.etiqueta_nombre.grid(row=0, column=1, sticky="nsew")
        self.nombre = tk.Entry(self.frame_registrar, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=30, font=("Arial", 15))
        self.nombre.grid(row=1, column=1, sticky="nsew")

        self.etiqueta_apellido = tk.Label(self.frame_registrar, text="Apellido", font=("Arial", 15))
        self.etiqueta_apellido.grid(row=2, column=1, sticky="nsew")
        self.apellido = tk.Entry(self.frame_registrar, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=30, font=("Arial", 15))
        self.apellido.grid(row=3, column=1, sticky="nsew")

        self.etiqueta_documento = tk.Label(self.frame_registrar, text="Documento", font=("Arial", 15))
        self.etiqueta_documento.grid(row=4, column=1, sticky="nsew")
        self.documento = tk.Entry(self.frame_registrar, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=30, font=("Arial", 15))
        self.documento.grid(row=5, column=1, sticky="nsew")

        self.etiqueta_FechaNacimiento = tk.Label(self.frame_registrar, text="Fecha de Nacimiento", font=("Arial", 15))
        self.etiqueta_FechaNacimiento.grid(row=6, column=1, sticky="nsew")
        self.fechaDeNacimiento = tk.Entry(self.frame_registrar, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=30, font=("Arial", 15))
        self.fechaDeNacimiento.grid(row=7, column=1, sticky="nsew") 
        
        self.boton_guardar = tk.Button(self.frame_registrar, text="Guardar datos", font=("Arial", 15), command=self.guardar_datos)
        self.boton_guardar.grid(row=8, column=1, sticky="nsew")
  
    def guardar_datos(self):
        conexion = sqlite3.connect('Centro-Gym.db')
        cursor = conexion.cursor()
        
        dato1 = self.nombre.get()
        dato2 = self.apellido.get()
        dato3 = self.documento.get()
        dato4 = self.fechaDeNacimiento.get()

        if dato1 and dato2 and dato3:
            cursor.execute("INSERT INTO Entrenados (DNI, Nombre, Apellido, FechaDeNacimiento) VALUES (?, ?, ?, ?)", (dato3, dato1, dato2, dato4))
            conexion.commit()
            messagebox.showinfo("Registro Exitoso", "Se registró el usuario correctamente")
            self.nombre.delete(0, tk.END)
            self.apellido.delete(0, tk.END)
            self.documento.delete(0, tk.END)
            self.fechaDeNacimiento.delete(0, tk.END)
        else: 
            messagebox.showinfo("Error", "Faltan campos por completar")


        cursor.close()
        conexion.close()

    def editar_datos(self):
        self.nombre.delete(0, tk.END)
        self.apellido.delete(0, tk.END)
        self.documento.delete(0, tk.END)
        self.label_datos.config(text="")