#2.	Suma de dos números:
#o	Escribe una función que reciba dos números como parámetros y retorne su suma.
#o	Ejemplo: Entrada: 3, 7 → Salida: 10.


def suma_dos_numeros(num1, num2):
    return num1 + num2  

# Solicitar los dos números al usuario
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Llamar a la función y mostrar el resultado
resultado = suma_dos_numeros(numero1, numero2)
print(f"La suma de {numero1} y {numero2} es: {resultado}")