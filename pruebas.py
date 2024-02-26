import tkinter as tk

def clic_en_boton(numero):
    etiqueta_resultado.config(text=f"Hiciste clic en el botón {numero}")

ventana_principal = tk.Tk()
ventana_principal.title("Cuadrícula que Ocupa Toda la Ventana")

# Configurar opciones de la cuadrícula para la ventana
ventana_principal.rowconfigure(0, weight=1)
ventana_principal.columnconfigure(0, weight=1)

# Crear un frame y colocarlo en la cuadrícula
frame_botones = tk.Frame(ventana_principal, padx=10, pady=10)
frame_botones.grid(row=0, column=0, sticky="nsew")

# Configurar opciones de la cuadrícula para el frame
for i in range(2):
    frame_botones.rowconfigure(i, weight=1)
    frame_botones.columnconfigure(i, weight=1)

# Crear 6 botones y colocarlos en el frame
for i in range(6):
    fila = i // 3
    columna = i % 3
    boton = tk.Button(frame_botones, text=f"Botón {i+1}", command=lambda i=i: clic_en_boton(i+1))
    boton.grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana_principal, text="Haz clic en un botón")
etiqueta_resultado.grid(row=1, column=0, sticky="nsew", pady=10)

ventana_principal.mainloop()