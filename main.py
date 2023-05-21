import Conexion as Conector

print("Para conectarse a la Base de Datos presione 1")
print("Para cerrar la Base de Datos presione 2")
variableAuxiliar = int(input())

if variableAuxiliar == 1:
    conn = Conector.Conectar()

    conn = Conector

elif variableAuxiliar == 2:
    conn = Conector.conexion.cerrar_conexion()
    print("Gracias por cerrar la Base de Datos.")
else:
    print("Opción inválida. Por favor, ingrese una opción válida (1 o 2).")