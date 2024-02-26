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
ventana_principal.configure(bg='red')

# la ventana principal tendra una sola fila 
ventana_principal.rowconfigure(0, weight=1)

# columna 0 menu
ventana_principal.columnconfigure(0, minsize=150)
    
# columna 1 contenido 
ventana_principal.columnconfigure(1, weight=1)

# Crear un frame - MENU para la columna izquierda 
menu = tk.Frame(ventana_principal, bg="green", padx=10, pady=10)
menu.grid(row=0, column=0, sticky="nsew")

# Frame interior 1 dentro del frame exterior
frame_inicio = tk.Frame(menu, padx=5, pady=5, bg="lightgreen")
frame_inicio.grid(row=0, column=0)
menu.columnconfigure(0, weight=1)
menu.rowconfigure(0, weight=1)
boton_inicio = tk.Button(frame_inicio, text="INICIO", bg="lightgreen")
boton_inicio.pack()

# Boton de Asistencia
frame_asistencia = tk.Frame(menu, padx=5, pady=5, bg="lightcoral")
frame_asistencia.grid(row=1, column=0)
menu.columnconfigure(0, weight=1)
menu.rowconfigure(1, weight=1)
boton_asistencia = tk.Button(frame_asistencia, text="Asistencia", bg="lightcoral")
boton_asistencia.pack()


ventana_principal.mainloop()