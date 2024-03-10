import tkinter as tk      
from tkinter import ttk, messagebox
from ContenidoFrame import ContenidoFrame
from datetime import datetime
from Conexion import ComunicacionEntrenados

import sqlite3 

 
class EntrenadosFrame(ContenidoFrame):
    def __init__(self, master, navegacion_callback):
        super().__init__(master, "Entrenados", navegacion_callback)
        
        self.base_de_datos = ComunicacionEntrenados()


        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=15)
        self.master.columnconfigure(0, weight=1)
        self.frame_titulo.grid(row=0, column=0,  sticky="nsew")

        self.frame_registrar = tk.Frame(master, bg="#DCD0CA")
        self.frame_registrar.grid(row=1,column=0,sticky="nsew")

        # Configurar el frame de entrenados

        self.frame_registrar.grid_propagate(False)

        self.frame_registrar.columnconfigure(0, weight=3)
        self.frame_registrar.columnconfigure(1, weight=3)
        self.frame_registrar.columnconfigure(2, weight=1)
        self.frame_registrar.columnconfigure(3, weight=1)
        self.frame_registrar.columnconfigure(4, weight=1)

        # Filas para las entradas y etiquetas

        for i in range(4): 
            self.frame_registrar.rowconfigure(i, weight=10)
        
        self.frame_registrar.rowconfigure(4, weight=1)
        
        self.frame_registrar.rowconfigure(5, weight=50)
        # Creación de la etiqueta y campo de entrada para el nombre
        self.etiqueta_nombre = tk.Label(
            self.frame_registrar, 
            text="Nombre", 
            font=("Century Gothic", 18, 'bold'), 
            bg="#DCD0CA"
        )
        self.etiqueta_nombre.grid(row=0, column=0, sticky="nsew")

        self.nombre = tk.Entry(
            self.frame_registrar, 
            highlightbackground="black", 
            highlightcolor="#E02E27", 
            highlightthickness=3, 
            font=("Century Gothic", 15), 
            bg="white"
        )
        self.nombre.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # Creación de la etiqueta y campo de entrada para el apellido
        self.etiqueta_apellido = tk.Label(
            self.frame_registrar, 
            text="Apellido", 
            font=("Century Gothic", 18, 'bold'), 
            bg="#DCD0CA"
        )
        self.etiqueta_apellido.grid(row=1, column=0, sticky="nsew")

        self.apellido = tk.Entry(
            self.frame_registrar, 
            highlightbackground="black", 
            highlightcolor="#E02E27", 
            highlightthickness=3, 
            font=("Century Gothic", 15), 
            bg="white"
        )
        self.apellido.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        # Creación de la etiqueta y campo de entrada para el documento
        self.etiqueta_documento = tk.Label(
            self.frame_registrar, 
            text="Documento", 
            font=("Century Gothic", 18, 'bold'), 
            bg="#DCD0CA"
        )
        self.etiqueta_documento.grid(row=2, column=0, sticky="nsew")

        self.documento = tk.Entry(
            self.frame_registrar, 
            highlightbackground="black", 
            highlightcolor="#E02E27", 
            highlightthickness=3, 
            font=("Century Gothic", 15), 
            bg="white"
        )
        self.documento.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

        # Creación de la etiqueta y campos de entrada para la fecha de nacimiento
        self.etiqueta_FechaNacimiento = tk.Label(
            self.frame_registrar, 
            text="Nacimiento", 
            font=("Century Gothic", 18, 'bold'), 
            bg="#DCD0CA"
        )
        self.etiqueta_FechaNacimiento.grid(row=3, column=0, sticky="nsew")

        self.frame_fecha_de_nacimiento = tk.Frame(self.frame_registrar, bg="#DCD0CA")
        self.frame_fecha_de_nacimiento.grid_propagate(False)

        for i in range(6):
            weight = 1 if i % 2 == 0 else 100
            self.frame_fecha_de_nacimiento.columnconfigure(i, weight=weight)

        self.frame_fecha_de_nacimiento.grid(row=3, column=1, sticky="nsew")

        # Creación de la etiqueta y campo de entrada para el día
        self.etiqueta_dia = tk.Label(
            self.frame_fecha_de_nacimiento, 
            text="Día", 
            font=("Century Gothic", 15), 
            bg="#DCD0CA"
        ) 
        self.etiqueta_dia.grid(row=0, column=0, sticky="nsew", padx=10)

        self.dia = tk.Entry(
            self.frame_fecha_de_nacimiento, 
            highlightbackground="black", 
            highlightcolor="#E02E27", 
            highlightthickness=3, 
            font=("Century Gothic", 15), 
            bg="white"
        )
        self.dia.grid(row=0, column=1, padx=10)

        # Creación de la etiqueta y campo de entrada para el mes
        self.etiqueta_mes = tk.Label(
            self.frame_fecha_de_nacimiento, 
            text="Mes", 
            font=("Century Gothic", 15), 
            bg="#DCD0CA"
        ) 
        self.etiqueta_mes.grid(row=0, column=2, sticky="nsew", padx=10)

        self.mes = tk.Entry(
            self.frame_fecha_de_nacimiento, 
            highlightbackground="black", 
            highlightcolor="#E02E27", 
            highlightthickness=3, 
            font=("Century Gothic", 15), 
            bg="white"
        )
        self.mes.grid(row=0, column=3, padx=10)

        # Creación de la etiqueta y campo de entrada para el año
        self.etiqueta_año = tk.Label(
            self.frame_fecha_de_nacimiento, 
            text="Año", 
            font=("Century Gothic", 15), 
            bg="#DCD0CA"
        )
        self.etiqueta_año.grid(row=0, column=4, sticky="nsew", padx=10)

        self.año = tk.Entry(
            self.frame_fecha_de_nacimiento, 
            highlightbackground="black", 
            highlightcolor="#E02E27", 
            highlightthickness=3, 
            font=("Century Gothic", 15), 
            bg="white"
        )
        self.año.grid(row=0, column=5, padx=10)

        # Creación del botón para guardar los datos
        self.boton_guardar = tk.Button(
            self.frame_registrar, 
            text="Guardar datos", 
            font=("Century Gothic", 15), 
            bg="#E02E27",
            fg="white", 
            command=self.guardar_entrenado
        )
        self.boton_guardar.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)

        self.boton_eliminar = tk.Button(
            self.frame_registrar,
            text="Eliminar registro",
            font=("Century Gothic", 15),
            bg="#E02E27",
            fg="white",
            command=self.eliminar_entrenado
        )

        self.boton_eliminar.grid(row=1, column=3, sticky="nsew", padx=5, pady=5)


       # Crear y configurar el estilo de la tabla
        self.estilo_tabla = ttk.Style()
        self.estilo_tabla.configure('Treeview', font=("Century Gothic", 15, 'bold'), rowheight=25)
        self.estilo_tabla.configure('Treeview.Heading', font=("Century Gothic", 15, 'bold'), rowheight=25)

        # Agregar borde a las celdas
        self.estilo_tabla.configure('Treeview', borderwidth=1)
        self.estilo_tabla.configure('Treeview.Heading', borderwidth=1)   

        # Crear la tabla
        self.tabla = ttk.Treeview(
            self.frame_registrar, 
            columns=('id','DNI', 'Nombre', 'Apellido', 'Nacimiento'), 
            show='headings'
        )

        # Configurar el estilo de las filas
        self.tabla.tag_configure('fila_roja', background='#EB6B66')
        self.tabla.tag_configure('fila_blanca', background='white')

        # Posicionar la tabla en la grilla
        self.tabla.grid(row=5, column=0, sticky='nsew', columnspan=5)

        # Crear y posicionar la barra de desplazamiento
        self.scrollbar = ttk.Scrollbar(self.frame_registrar, orient='vertical', command=self.tabla.yview)
        self.scrollbar.grid(row=5, column=5, sticky='ns')

        # Conectar la barra de desplazamiento con la tabla
        self.tabla.configure(yscrollcommand=self.scrollbar.set)

        # Actualizar los datos de la tabla
        self.actualizar_tabla()

        # Configurar los encabezados de la tabla
        self.tabla.heading('id', text='N° Entrenado')
        self.tabla.heading('DNI', text='DNI')
        self.tabla.heading('Nombre', text='Nombre')
        self.tabla.heading('Apellido', text='Apellido')
        self.tabla.heading('Nacimiento', text='Nacimiento')       

                           

    def fecha_existe(self,dia, mes, año):
        try:
            datetime(int(año), int(mes), int(dia))
            return True
        except ValueError:
            return False

    def guardar_entrenado(self):
        # Inicializa una lista de errores vacía
        lista_de_errores = str()

        # Verifica que el nombre no esté vacío y que no contenga más de dos palabras
        nombre = self.nombre.get().strip()
        if nombre == "":
            lista_de_errores += "*El nombre no puede estar vacío\n"
        elif nombre.count(" ") > 1: 
            lista_de_errores += "*Se pueden guardar hasta dos nombres\n"

        # Verifica que el apellido no esté vacío y que no contenga más de dos palabras
        apellido = self.apellido.get().strip()
        if apellido == "":
            lista_de_errores += "*El apellido no puede estar vacío\n"
        elif apellido.count(" ") > 1:
            lista_de_errores += "*Se pueden guardar hasta dos apellidos\n"

        # Verifica que el DNI no esté vacío, que tenga entre 7 y 9 dígitos y que sea numérico
        documento = str(self.documento.get()).strip()
        if documento == "":
            lista_de_errores += "*El DNI no puede estar vacío\n"
        elif not(6 < len(documento) < 10) or not documento.isdigit():
            lista_de_errores += "*Revisa el DNI\n"
        
        # Verifica que la fecha de nacimiento exista y esté en el rango correcto
        dia, mes, año = self.dia.get(), self.mes.get(), self.año.get()
        if not(self.fecha_existe(dia, mes, año)) or not(1900 < int(año) < 2200):
            lista_de_errores += "*La fecha ingresada no es válida\n"
        else: 
            # Guarda la fecha en el formato correcto
            self.fechaDeNacimiento = f"{dia.zfill(2)}/{mes.zfill(2)}/{año}"

        # Si no hay errores, guarda los datos en la base de datos
        if lista_de_errores == "":
            try: 
                self.base_de_datos.guardar_datos(nombre, apellido, documento, self.fechaDeNacimiento)
                messagebox.showinfo("Registro Exitoso", "Se registró el usuario correctamente")
                # Limpia los campos de entrada
                self.nombre.delete(0, tk.END)
                self.apellido.delete(0, tk.END)
                self.documento.delete(0, tk.END)
                self.dia.delete(0, tk.END)
                self.mes.delete(0, tk.END)
                self.año.delete(0, tk.END)
                self.actualizar_tabla()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "El DNI ingresado ya existe o no es valido\n")
        else: 
            # Muestra los errores encontrados
            messagebox.showinfo("Error", lista_de_errores)

    def actualizar_tabla(self):
        # Elimina todos los elementos actuales de la tabla
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        
        contador = 0
        for fila in self.base_de_datos.obtener_datos():
            if contador % 2 == 0:
                estilo = 'fila_roja'
            else:
                estilo = 'fila_blanca'
            self.tabla.insert('', 'end', values=fila, tags=(estilo,))
            contador += 1

    def eliminar_entrenado(self):
        # Obtener el ID del registro a eliminar
        item_seleccionado = self.tabla.selection()[0]
        id_registro = self.tabla.item(item_seleccionado, "values")[0]

        # Conectar a la base de datos y eliminar el registro
        conexion = sqlite3.connect("Centro-Gym.db")
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Entrenados WHERE id = ?", (id_registro,))
        conexion.commit()
        conexion.close()

        # Actualizar la tabla
        self.actualizar_tabla()

