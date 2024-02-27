import tkinter as tk

from Aplicacion import Aplicacion

ventana_principal = tk.Tk()
ventana_principal.iconbitmap(r'Pruebas\gym.ico')
app = Aplicacion(ventana_principal)
ventana_principal.mainloop()