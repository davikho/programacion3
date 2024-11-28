#3.	Número par o impar:
#o	Crea una función que reciba un número y retorne True si es par y False si es impar.
#o	Ejemplo: Entrada: 4 → Salida: True.

def es_par(num):
    return num % 2 == 0  

# Solicitar un número al usuario
numero = int(input("Ingresa un número: "))

# Llamar a la función y mostrar el resultado
resultado = es_par(numero)
print(f"El número {numero} es par: {resultado}")