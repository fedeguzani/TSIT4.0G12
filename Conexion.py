import mysql.connector

class Conectar():
    def _init_(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='Hillairet92,',
                database='big_bread_s'
            )
            if self.conexion.is_connected():
                print("LA CONEXION FUE EXITOSA")

        except mysql.connector.Error as error:
            print("NO SE PUDO CONECTAR A LA BASE DE DATOS:", error)

    def cerrar_conexion(self):
        if self.conexion.is_connected():
            self.conexion.close()
            print("LA CONEXION FUE CERRADA")

# Ejemplo de uso:
conexion = Conectar()
# Realizar operaciones con la conexión...
conexion.cerrar_conexion()
