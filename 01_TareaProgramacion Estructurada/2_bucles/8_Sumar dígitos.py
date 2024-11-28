#8.	Sumar dígitos:
#o	Solicita un número entero y calcula la suma de sus dígitos.
#o	Ejemplo: Entrada: 123 → Salida: 6 (1 + 2 + 3).

# Solicitar un número entero al usuario
numero = input("Ingresa un número entero: ")
suma = 0
for digito in numero:
    suma += int(digito)  

print(f"La suma de los dígitos es: {suma}")