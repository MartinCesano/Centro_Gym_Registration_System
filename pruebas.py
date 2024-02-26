import tkinter as tk
ventana_principal = tk.Tk()
ventana_principal.title("Centro Gym")
# Establecer las dimensiones de la ventana para que ocupe toda la pantalla
# Obtener las dimensiones de la pantalla
ancho_pantalla = int(ventana_principal.winfo_screenwidth()*0.8)
alto_pantalla = int(ventana_principal.winfo_screenheight()*0.8)
# Establecer las dimensiones de la ventana para que ocupe toda la pantalla
ventana_principal.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")
ventana_principal.state('zoomed')
ventana_principal.configure(bg='#DCD0CA')

# la ventana principal tendra una sola fila 
ventana_principal.rowconfigure(0, weight=1)
ventana_principal.rowconfigure(1, weight=6)
# columna 0 menu
ventana_principal.columnconfigure(0, minsize=150)
    
# columna 1 contenido 
ventana_principal.columnconfigure(1, weight=1)

# Crear un frame - Encabezado
encabezado = tk.Frame(ventana_principal, bg="#E02E27")
encabezado.grid(row=0, column=0, columnspan=2,sticky="nsew")

# Crear un frame - MENU para la columna izquierda 
menu = tk.Frame(ventana_principal, bg="#E02E27")
menu.grid(row=1, column=0,sticky="nsew")

# Frame interior 1 dentro del frame exterior
frame_inicio = tk.Frame(menu, bg="blue")
frame_inicio.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10,4.5))

menu.columnconfigure(0, minsize=150)
menu.rowconfigure(0, weight=1)

frame_inicio.columnconfigure(0, weight=1) 
frame_inicio.rowconfigure(0, weight=1)

boton_inicio = tk.Button(frame_inicio, text="INICIO", bg="#555857")
boton_inicio.grid(row=0, column=0, sticky="nsew")

# Boton de Asistencia
frame_asistencia = tk.Frame(menu, bg="white")
frame_asistencia.grid(row=1, column=0, sticky="nsew", padx=10, pady=(10,4.5))

menu.columnconfigure(0, minsize=150)
menu.rowconfigure(1, weight=1)

frame_asistencia.columnconfigure(0, weight=1) 
frame_asistencia.rowconfigure(0, weight=1)

boton_asistencia = tk.Button(frame_asistencia, text="ASISTENCIA", bg="#555857")
boton_asistencia.grid(row=0, column=0, sticky="nsew")

# Boton de Entrenados
frame_entrenados = tk.Frame(menu, bg="blue")
frame_entrenados.grid(row=2, column=0, sticky="nsew", padx=10, pady=(10,4.5))

menu.columnconfigure(0, minsize=150)
menu.rowconfigure(2, weight=1)

frame_entrenados.columnconfigure(0, weight=1) 
frame_entrenados.rowconfigure(0, weight=1)

boton_entrenados = tk.Button(frame_entrenados, text="Entrenados", bg="#555857")
boton_entrenados.grid(row=0, column=0, sticky="nsew")


# Boton de Cuotas
frame_cuotas = tk.Frame(menu, bg="white")
frame_cuotas.grid(row=3, column=0, sticky="nsew", padx=10, pady=(10,10))

menu.columnconfigure(0, minsize=150)
menu.rowconfigure(3, weight=1)

frame_cuotas.columnconfigure(0, weight=1) 
frame_cuotas.rowconfigure(0, weight=1)

boton_cuotas = tk.Button(frame_cuotas, text="CUOTAS", bg="#555857")
boton_cuotas.grid(row=0, column=0, sticky="nsew")



ventana_principal.mainloop()