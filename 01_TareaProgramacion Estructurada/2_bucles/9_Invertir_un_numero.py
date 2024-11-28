#9.	Invertir un número:
#o	Solicita un número entero y muestra su versión invertida.
#o	Ejemplo: Entrada: 1234 → Salida: 4321.

numero = input("Ingresa un número entero: ")

numero_invertido = numero[::-1]  

print(f"El número invertido es: {numero_invertido}")