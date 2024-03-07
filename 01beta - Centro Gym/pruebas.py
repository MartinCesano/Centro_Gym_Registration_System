import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Notebook Demo")
        self.geometry("300x200")

        # Crear el notebook
        self.opciones_entrenados = ttk.Notebook(self)
        self.opciones_entrenados.pack(fill='both', expand=True)

        # Crear un estilo
        self.style = ttk.Style()

        # Configurar el estilo de las pestañas del Notebook
        self.style.configure('TNotebook.Tab', font=('Cooper Black', '18'), padding=[5, 5])


        # Crear los frames
        self.frame1 = tk.Frame(self.opciones_entrenados, bg='red')
        self.frame2 = tk.Frame(self.opciones_entrenados, bg='green')
        self.frame3 = tk.Frame(self.opciones_entrenados, bg='blue')

        # Añadir los frames al notebook
        self.opciones_entrenados.add(self.frame1, text='Frame 1')
        self.opciones_entrenados.add(self.frame2, text='Frame 2')
        self.opciones_entrenados.add(self.frame3, text='Frame 3')

if __name__ == "__main__":
    app = Application()
    app.mainloop()