#4.	Calcular el cuadrado:
#o	Escribe una función que reciba un número y retorne su cuadrado.
#o	Ejemplo: Entrada: 5 → Salida: 25.

def calcular_cuadrado(num):
    return num ** 2  

# Solicitar un número al usuario
numero = float(input("Ingresa un número: "))

# Llamar a la función y mostrar el resultado
resultado = calcular_cuadrado(numero)
print(f"El cuadrado de {numero} es: {resultado}")