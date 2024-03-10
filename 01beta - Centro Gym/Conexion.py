import sqlite3

class ComunicacionEntrenados:
    
    def guardar_datos(self,nombre, apellido, documento, fechaDeNacimiento):
        self.conexion = sqlite3.connect('Centro-Gym.db')
        self.cursor = self.conexion.cursor()
        self.cursor.execute('''INSERT INTO Entrenados (DNI, Nombre, Apellido, FechaDeNacimiento) 
                       VALUES (?, ?, ?, ?)''', (documento, nombre, apellido, fechaDeNacimiento))
        self.conexion.commit()
        self.cursor.close()
        self.conexion.close()

    def obtener_datos(self):
        self.conexion = sqlite3.connect('Centro-Gym.db')
        self.cursor = self.conexion.cursor()
        self.cursor.execute("SELECT * FROM Entrenados")
        filas = self.cursor.fetchall()
        self.cursor.close()
        self.conexion.close()
        return filas

