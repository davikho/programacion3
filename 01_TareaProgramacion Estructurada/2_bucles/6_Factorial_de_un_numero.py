#6.	Factorial de un número:
#o	Calcula el factorial de un número ingresado por el usuario (n!).
#o	Ejemplo: Entrada: 5 → Salida: 120.

# Solicitar al usuario
numero = int(input("Ingresa un número para calcular su factorial: "))

# Inicializar la variable factorial en 1 (el factorial de 0 y 1 es 1)
factorial = 1

for i in range(1, numero + 1):
    factorial *= i  

# Imprimir el resultado
print(f"El factorial de {numero} es: {factorial}")