import tkinter as tk
from PIL import Image, ImageTk

class Aplicacion:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Imagen Ajustada")

        # Crear un frame
        self.frame = tk.Frame(ventana_principal)
        self.frame.pack()

        # Cargar la imagen
        imagen_original = Image.open(r"Pruebas\gym-encabezado.png")

        # Obtener el tamaño del frame
        frame_ancho = 300
        frame_alto = 200

        # Redimensionar la imagen al tamaño del frame
        imagen_redimensionada = imagen_original.resize((frame_ancho, frame_alto), Image.ANTIALIAS)

        # Convertir la imagen a un formato compatible con Tkinter
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

        # Crear una label para mostrar la imagen
        self.label_imagen = tk.Label(self.frame, image=imagen_tk)
        self.label_imagen.image = imagen_tk  # Conservar una referencia para evitar que la imagen se elimine por el recolector de basura
        self.label_imagen.pack()

# Crear la ventana principal
ventana_principal = tk.Tk()

# Crear la aplicación
app = Aplicacion(ventana_principal)

# Iniciar el bucle de eventos
ventana_principal.mainloop()
