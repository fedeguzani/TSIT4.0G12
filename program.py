import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="nombre_de_la_base_de_datos"
)

mycursor = mydb.cursor()

sql = "INSERT INTO tabla (campo1, campo2, campo3) VALUES (%s, %s, %s)"
val = ("valor1", "valor2", "valor3")
mycursor.execute(sql, val)

mydb.commit()