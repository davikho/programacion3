#1.	Saludo personalizado:
#o	Crea una función que reciba un nombre como parámetro y retorne un saludo.
#o	Ejemplo: Entrada: María → Salida: "Hola, María!".

def saludo_personalizado(nombre):
    return f"Hola, {nombre}!"

# Solicitar el nombre al usuario
nombre_usuario = input("Ingresa tu nombre: ")

# Llamar a la función y mostrar el saludo
saludo = saludo_personalizado(nombre_usuario)
print(saludo)